import { createHash } from "node:crypto";
import { Router } from "express";
import { rateLimit } from "express-rate-limit";
import { RequestReportBody } from "@workspace/api-zod";
import { deliverReport } from "../lib/report-mail";

export function createReportRouter(deliver = deliverReport) {
  const router = Router();
  const recent = new Map<string, {
    fingerprint: string;
    expires: number;
    result: ReturnType<typeof deliverReport>;
  }>();
  const limit = rateLimit({
    windowMs: 15 * 60_000,
    limit: 5,
    standardHeaders: "draft-8",
    legacyHeaders: false,
    message: { error: "RATE_LIMITED" },
  });
  const globalLimit = rateLimit({
    windowMs: 15 * 60_000,
    limit: 100,
    keyGenerator: () => "report-requests",
    message: { error: "RATE_LIMITED" },
  });
  router.post("/report-requests", globalLimit, limit, async (req, res): Promise<void> => {
    const parsed = RequestReportBody.strict().safeParse(req.body);
    if (!parsed.success || /[\r\n]/.test(parsed.data?.email ?? "") ||
        !parsed.data?.business.trim()) {
      res.status(400).json({ error: "INVALID_INPUT" });
      return;
    }
    const input = { ...parsed.data, business: parsed.data.business.trim() };
    const fingerprint = createHash("sha256").update(JSON.stringify(input)).digest("hex");
    for (const [key, entry] of recent) {
      if (entry.expires < Date.now()) recent.delete(key);
    }
    const cached = recent.get(input.requestId);
    if (cached && cached.fingerprint !== fingerprint) {
      res.status(409).json({ error: "REQUEST_ID_CONFLICT" });
      return;
    }
    try {
      const result = cached?.result ?? deliver(input);
      if (!cached) recent.set(input.requestId, {
        fingerprint, expires: Date.now() + 60 * 60_000, result,
      });
      const delivery = await result;
      if (!delivery.confirmationSent) req.log.warn("Report accepted; confirmation delivery failed");
      res.json(delivery);
    } catch {
      recent.delete(input.requestId);
      // SMTP errors can contain addresses or server details; do not log the raw error.
      req.log.error("Report email delivery failed");
      res.status(503).json({ error: "DELIVERY_FAILED" });
    }
  });
  return router;
}

export default createReportRouter();
