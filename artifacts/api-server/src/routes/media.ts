import { Router } from "express";
import { GetPublicMediaParams } from "@workspace/api-zod";
import { getPublicMediaFile } from "../lib/media-storage";

export function parseByteRange(header: string | undefined, size: number) {
  if (!header) return null;
  const match = /^bytes=(\d*)-(\d*)$/.exec(header);
  if (!match || (!match[1] && !match[2])) return false;
  const first = match[1] ? Number(match[1]) : null;
  const last = match[2] ? Number(match[2]) : null;
  if ((first !== null && !Number.isSafeInteger(first)) ||
      (last !== null && !Number.isSafeInteger(last)) || size <= 0) return false;
  if (first === null) {
    if (!last) return false;
    return { start: Math.max(0, size - last), end: size - 1 };
  }
  const end = Math.min(last ?? size - 1, size - 1);
  if (first >= size || end < first) return false;
  return { start: first, end };
}

const router = Router();
router.get("/media/:filename", async (req, res): Promise<void> => {
  const parsed = GetPublicMediaParams.safeParse(req.params);
  if (!parsed.success) { res.sendStatus(404); return; }
  try {
    const file = getPublicMediaFile(parsed.data.filename);
    const [metadata] = await file.getMetadata();
    const size = Number(metadata.size);
    if (!Number.isSafeInteger(size) || size <= 0) throw new Error("Invalid media size");
    const range = parseByteRange(req.get("Range"), size);
    res.set({
      "Content-Type": parsed.data.filename.endsWith(".mp4") ? "video/mp4" : "image/jpeg",
      "Accept-Ranges": "bytes",
      "Cache-Control": "public, max-age=3600",
      "X-Content-Type-Options": "nosniff",
    });
    if (range === false) {
      res.status(416).set("Content-Range", `bytes */${size}`).end();
      return;
    }
    if (range) {
      res.status(206).set({
        "Content-Range": `bytes ${range.start}-${range.end}/${size}`,
        "Content-Length": String(range.end - range.start + 1),
      });
    } else res.set("Content-Length", String(size));
    if (req.method === "HEAD") { res.end(); return; }
    const stream = file.createReadStream(range ? { start: range.start, end: range.end } : {});
    stream.on("error", () => {
      req.log.warn("Public media stream failed");
      if (res.headersSent) res.destroy();
      else {
        res.removeHeader("Content-Length");
        res.removeHeader("Content-Range");
        res.status(503).set("Cache-Control", "no-store").end();
      }
    });
    res.on("close", () => stream.destroy());
    stream.pipe(res);
  } catch (error) {
    const notFound = (error as { code?: number }).code === 404;
    if (!notFound) req.log.warn("Public media storage unavailable");
    res.sendStatus(notFound ? 404 : 503);
  }
});

export default router;
