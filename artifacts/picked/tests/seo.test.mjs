import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync(new URL("../index.html", import.meta.url), "utf8");
const robots = fs.readFileSync(new URL("../public/robots.txt", import.meta.url), "utf8");
const sitemap = fs.readFileSync(new URL("../public/sitemap.xml", import.meta.url), "utf8");

test("includes a branded favicon and canonical social metadata", () => {
  assert.match(html, /<link rel="icon" type="image\/svg\+xml" href="\/favicon\.svg">/);
  assert.match(html, /<link rel="canonical" href="https:\/\/mrpicked\.eu\/">/);
  assert.match(html, /<meta property="og:url" content="https:\/\/mrpicked\.eu\/">/);
  assert.match(html, /<meta name="twitter:card" content="summary">/);

  const title = html.match(/<title>([^<]+)<\/title>/)?.[1] ?? "";
  const description = html.match(/<meta name="description" content="([^"]+)">/)?.[1] ?? "";
  assert.ok(title.length >= 50 && title.length <= 60, `Unexpected SEO title length: ${title.length}`);
  assert.ok(description.length >= 150 && description.length <= 160,
    `Unexpected SEO description length: ${description.length}`);
});

test("publishes valid organization and website structured data", () => {
  const jsonLd = html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1];
  assert.ok(jsonLd, "JSON-LD block should be present in the HTML shell");
  const structuredData = JSON.parse(jsonLd);
  assert.equal(structuredData["@context"], "https://schema.org");
  assert.deepEqual(structuredData["@graph"].map((item) => item["@type"]), ["Organization", "WebSite"]);
  assert.equal(structuredData["@graph"][0].url, "https://mrpicked.eu/");
});

test("allows crawlers and advertises the canonical sitemap", () => {
  assert.match(robots, /^User-agent: \*\s+Allow: \/\s+Sitemap: https:\/\/mrpicked\.eu\/sitemap\.xml/m);
  assert.match(sitemap, /^<\?xml version="1\.0" encoding="UTF-8"\?>/);
  assert.match(sitemap, /<loc>https:\/\/mrpicked\.eu\/<\/loc>/);
});
