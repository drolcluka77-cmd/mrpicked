import assert from "node:assert/strict";
import test from "node:test";
import express from "express";
import { createLanguageDetector, interpretIpLookup, normalizePublicIp } from "../src/lib/visitor-language";
import { createVisitorLanguageRouter } from "../src/routes/visitor-language";

const lookup = (country: string, flags = {}) => ({
  is_vpn: false, is_proxy: false, is_tor: false, location: { country_code: country }, ...flags,
});

test("maps supported countries, and defaults other countries to English", () => {
  for (const [country, language] of Object.entries({
    SI: "SL", HR: "HR", IT: "IT", DE: "DE", AT: "DE", CH: "DE", HU: "HU", US: "EN", FR: "EN",
  })) {
    assert.equal(interpretIpLookup(lookup(country)).language, language);
  }
});

test("VPN, proxy and Tor override the IP country with English", () => {
  for (const flag of ["is_vpn", "is_proxy", "is_tor"]) {
    assert.deepEqual(interpretIpLookup(lookup("SI", { [flag]: true })), {
      language: "EN", country: "SI", vpn: true, reason: "vpn",
    });
  }
});

test("missing security data or provider errors are not treated as no VPN", () => {
  for (const value of [null, {}, { country: "Slovenia" }, { error: "quota" }, lookup("")]) {
    assert.throws(() => interpretIpLookup(value));
  }
});

test("does not send local or invalid IP addresses to the provider", async () => {
  const detect = createLanguageDetector(async () => { throw new Error("Must not be called"); });
  for (const ip of ["127.0.0.1", "10.0.0.2", "172.16.0.1", "192.168.1.1", "::1", "fc00::1", "fe80::1", "bad", undefined]) {
    assert.equal(normalizePublicIp(ip), null);
    assert.equal((await detect(ip)).reason, "unavailable");
  }
  assert.equal(normalizePublicIp("::ffff:8.8.8.8"), "8.8.8.8");
  assert.equal(normalizePublicIp("2001:4860:4860::8888"), "2001:4860:4860::8888");
});

test("deduplicates concurrent lookups and expires successful cache entries", async () => {
  let calls = 0;
  let time = 0;
  const detect = createLanguageDetector(async () => { calls++; return lookup("SI"); }, () => time);
  const results = await Promise.all([detect("8.8.8.8"), detect("8.8.8.8")]);
  assert.equal(calls, 1);
  assert.equal(results[0].language, "SL");
  time += 3_600_001;
  await detect("8.8.8.8");
  assert.equal(calls, 2);
});

test("uses English during outages and caches failures only briefly", async () => {
  let calls = 0;
  let time = 0;
  const detect = createLanguageDetector(async () => {
    if (++calls === 1) throw new Error("Unavailable");
    return lookup("IT");
  }, () => time);
  assert.equal((await detect("8.8.8.8")).reason, "unavailable");
  assert.equal((await detect("8.8.8.8")).language, "EN");
  assert.equal(calls, 1);
  time += 60_001;
  assert.equal((await detect("8.8.8.8")).language, "IT");
});

test("endpoint uses the trusted proxy IP, ignores query overrides and disables shared caching", async () => {
  let seen;
  const app = express();
  app.set("trust proxy", 1);
  app.use("/api", createVisitorLanguageRouter(async (ip) => {
    seen = ip;
    return { language: "SL", country: "SI", vpn: false, reason: "country" };
  }));
  const server = app.listen(0);
  await new Promise<void>((resolve) => server.once("listening", resolve));
  try {
    const { port } = server.address() as { port: number };
    const response = await fetch(`http://127.0.0.1:${port}/api/visitor-language?ip=1.1.1.1`, {
      headers: { "X-Forwarded-For": "8.8.8.8" },
    });
    assert.equal(seen, "8.8.8.8");
    assert.equal(response.headers.get("cache-control"), "private, no-store");
    assert.equal((await response.json()).language, "SL");
  } finally {
    server.closeAllConnections();
    await new Promise<void>((resolve) => server.close(() => resolve()));
  }
});
