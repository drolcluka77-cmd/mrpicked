import { createHash } from "node:crypto";
import { BlockList, isIP } from "node:net";
import type { VisitorLanguageResult } from "@workspace/api-zod";

type Language = VisitorLanguageResult["language"];
const countryLanguages: Record<string, Language> = {
  SI: "SL", HR: "HR", IT: "IT", DE: "DE", AT: "DE", CH: "DE", HU: "HU",
};
const privateRanges = new BlockList();
for (const [ip, prefix] of [
  ["0.0.0.0", 8], ["10.0.0.0", 8], ["100.64.0.0", 10], ["127.0.0.0", 8],
  ["169.254.0.0", 16], ["172.16.0.0", 12], ["192.0.0.0", 24],
  ["192.0.2.0", 24], ["192.168.0.0", 16], ["198.18.0.0", 15],
  ["198.51.100.0", 24], ["203.0.113.0", 24], ["224.0.0.0", 3],
] as const) privateRanges.addSubnet(ip, prefix, "ipv4");
for (const [ip, prefix] of [
  ["::", 128], ["::1", 128], ["fc00::", 7], ["fe80::", 10],
  ["ff00::", 8], ["2001:db8::", 32],
] as const) privateRanges.addSubnet(ip, prefix, "ipv6");

export function normalizePublicIp(value: string | undefined): string | null {
  if (!value) return null;
  const ip = value.replace(/^::ffff:/i, "");
  const version = isIP(ip);
  if (!version || privateRanges.check(ip, version === 4 ? "ipv4" : "ipv6")) return null;
  return ip;
}

export const unavailableLanguage = (): VisitorLanguageResult => ({
  language: "EN", country: null, vpn: null, reason: "unavailable",
});

export function interpretIpLookup(value: unknown): VisitorLanguageResult {
  if (!value || typeof value !== "object") throw new Error("INVALID_LOOKUP");
  const data = value as Record<string, unknown>;
  // A missing flag is not evidence of no VPN (e.g. keyless or limited API output).
  if (data.error || typeof data.is_vpn !== "boolean" ||
      typeof data.is_proxy !== "boolean" || typeof data.is_tor !== "boolean") {
    throw new Error("INCOMPLETE_LOOKUP");
  }
  const location = data.location as Record<string, unknown> | null;
  const country = typeof location?.country_code === "string" &&
    /^[a-z]{2}$/i.test(location.country_code) ? location.country_code.toUpperCase() : null;
  const vpn = data.is_vpn || data.is_proxy || data.is_tor;
  if (vpn) return { language: "EN", country, vpn: true, reason: "vpn" };
  if (!country) throw new Error("COUNTRY_UNAVAILABLE");
  const language = countryLanguages[country];
  return { language: language ?? "EN", country, vpn: false, reason: language ? "country" : "default" };
}

export async function lookupIp(ip: string): Promise<unknown> {
  const key = process.env.IPAPI_IS_KEY;
  if (!key) throw new Error("LOOKUP_NOT_CONFIGURED");
  const response = await fetch("https://api.ipapi.is", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ q: ip, key }),
    signal: AbortSignal.timeout(3000),
  });
  if (!response.ok) throw new Error("LOOKUP_FAILED");
  return response.json();
}

// Short-lived, bounded process-local cache; raw visitor IPs are not retained.
export function createLanguageDetector(lookup = lookupIp, now = Date.now) {
  const cache = new Map<string, { expires: number; result: Promise<VisitorLanguageResult> }>();
  return async (value: string | undefined): Promise<VisitorLanguageResult> => {
    const ip = normalizePublicIp(value);
    if (!ip) return unavailableLanguage();
    const key = createHash("sha256").update(ip).digest("hex");
    const cached = cache.get(key);
    if (cached && cached.expires > now()) return cached.result;
    cache.delete(key);
    if (cache.size >= 5000) cache.delete(cache.keys().next().value!);
    const entry = {
      expires: now() + 60 * 60_000,
      result: Promise.resolve().then(() => lookup(ip)).then(interpretIpLookup).catch(() => {
        // Cache failures briefly to avoid repeated calls during an outage or quota exhaustion.
        entry.expires = now() + 60_000;
        return unavailableLanguage();
      }),
    };
    cache.set(key, entry);
    return entry.result;
  };
}

export const detectVisitorLanguage = createLanguageDetector();
