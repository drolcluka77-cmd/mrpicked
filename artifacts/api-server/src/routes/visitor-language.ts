import { Router } from "express";
import { rateLimit } from "express-rate-limit";
import { detectVisitorLanguage, unavailableLanguage } from "../lib/visitor-language";

export function createVisitorLanguageRouter(detect = detectVisitorLanguage) {
  const router = Router();
  router.get("/visitor-language", (_req, res, next) => {
    // Never let a shared proxy/CDN cache one visitor's language for another.
    res.set("Cache-Control", "private, no-store");
    next();
  }, rateLimit({
    windowMs: 60_000,
    limit: 30,
    standardHeaders: "draft-8",
    legacyHeaders: false,
    message: unavailableLanguage(),
  }), async (req, res): Promise<void> => {
    // Express resolves only the immediate trusted proxy's forwarded client IP.
    // Do not accept an arbitrary address in a query parameter or body.
    const result = await detect(req.ip);
    if (result.reason === "unavailable") {
      req.log.warn("Visitor language detection unavailable; using English");
      res.status(503).json(result);
      return;
    }
    res.json(result);
  });
  return router;
}

export default createVisitorLanguageRouter();
