import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync(new URL("../index.html", import.meta.url), "utf8");
const source = html.match(/<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/)[1];

function setup(fetch, storedLanguage, browserLanguage = "en-US") {
  class Logic {
    props = {};
    state = { mail: "visitor@example.test", biz: "Restaurant", lang: "SL" };
    setState(update) { Object.assign(this.state, update); }
  }
  const document = {
    documentElement: { lang: "en" },
    baseURI: "https://example.test/",
    createElement: () => ({
      value: "",
      checkValidity() { return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(this.value); },
    }),
  };
  const window = { localStorage: {
    getItem: () => storedLanguage,
    setItem: (_key, value) => { storedLanguage = value; },
  } };
  const Component = new Function("DCLogic", "fetch", "document", "window", "navigator", `${source}; return Component;`)(Logic, fetch, document, window, { language: browserLanguage });
  return new Component();
}

test("uses navigator.language without any network request and falls back to English", () => {
  for (const [browserLanguage, expected] of [
    ["sl-SI", "SL"], ["hr-HR", "HR"], ["it-IT", "IT"], ["de-AT", "DE"],
    ["hu-HU", "HU"], ["EN-gb", "EN"], ["it", "IT"], ["fr-FR", "EN"],
    ["", "EN"], [null, "EN"], [42, "EN"],
  ]) {
    const component = setup(() => { throw new Error("No language lookup allowed"); }, undefined, browserLanguage);
    component.detectLanguage();
    assert.equal(component.state.lang, expected);
  }
  assert.ok(!html.includes("api/visitor-language"));
  assert.ok(!html.includes("ipapi.is"));
});

test("honors saved manual language and keeps the manual switch working", () => {
  const saved = setup(() => { throw new Error("No network expected"); }, "HR", "it-IT");
  saved.detectLanguage();
  assert.equal(saved.state.lang, "HR");
  const component = setup(() => { throw new Error("No network expected"); }, "invalid", "it-IT");
  component.detectLanguage();
  assert.equal(component.state.lang, "IT");
  component.renderVals().langs.find((item) => item.label === "DE").pick();
  assert.equal(component.state.lang, "DE");
  component.detectLanguage();
  assert.equal(component.state.lang, "DE");
});

const businessLabels = {
  EN: "Your business", SL: "Vaše podjetje", HR: "Vaša tvrtka",
  IT: "La tua azienda", DE: "Ihr Unternehmen", HU: "Az Ön vállalkozása",
};
const textValues = (value) => typeof value === "string" ? [value]
  : value && typeof value === "object" ? Object.values(value).flatMap(textValues) : [];
for (const [lang, label] of Object.entries(businessLabels)) {
  test(`${lang} addresses businesses throughout the page`, () => {
    const component = setup(() => { throw new Error("No network expected"); });
    component.state.lang = lang;
    const { t, d, roi, cal } = component.renderVals();
    assert.equal(t.dYour, label);
    assert.equal(t.fBiz, t.dName);
    // Preserve the founder's true restaurant background, not restaurant-only sales copy.
    const { fdP, ...salesCopy } = t;
    assert.doesNotMatch(textValues(salesCopy).join("\n"),
      /restaurant|restavr|restoran|ristoran|étter|guest|\bgost|ospit|Gäst|vendég|dinner|allergen|alergen|Speisekarte|étlap|TheFork|TripAdvisor/i);
    assert.ok(!d.qShown.includes("{city}"));
    assert.equal(roi.guests, 10);
    assert.equal(cal, "https://calendly.com/drolcluka77/30min");
  });
}

test("validates before sending and preserves form values on failure", async () => {
  let calls = 0;
  const component = setup(async () => { calls++; return { ok: false, status: 503 }; });
  component.state.mail = "invalid";
  await component.renderVals().form.submit();
  assert.equal(calls, 0);
  assert.equal(component.state.mailError, 1);
  component.state.mail = "visitor@example.test";
  await component.renderVals().form.submit();
  assert.equal(calls, 1);
  assert.equal(component.state.mailError, 2);
  assert.equal(component.state.sent, undefined);
  assert.equal(component.state.biz, "Restaurant");
  assert.equal(component.state.sending, false);
});

test("sends real input, blocks double-clicks, and displays confirmation only after success", async () => {
  let resolve;
  let body;
  let calls = 0;
  const component = setup(async (url, options) => {
    calls++;
    assert.equal(url, "/api/report-requests");
    body = JSON.parse(options.body);
    return new Promise((done) => { resolve = done; });
  });
  const submission = component.renderVals().form.submit();
  assert.equal(component.state.sent, undefined);
  assert.equal(component.state.sending, true);
  await component.renderVals().form.submit();
  assert.equal(calls, 1);
  resolve({ ok: true, json: async () => ({ accepted: true, confirmationSent: false }) });
  await submission;
  assert.equal(body.business, "Restaurant");
  assert.equal(body.language, "SL");
  assert.equal(body.consent, false);
  assert.equal(component.state.sent, true);
  assert.equal(component.state.confirmationFailed, true);
  assert.ok(component.renderVals().form.warning);
});
