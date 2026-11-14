import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync(new URL("../index.html", import.meta.url), "utf8");
const source = html.match(/<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/)[1];

function setup(fetch, storedLanguage) {
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
  const Component = new Function("DCLogic", "fetch", "document", "window", `${source}; return Component;`)(Logic, fetch, document, window);
  return new Component();
}

test("automatically uses the detected language and English on lookup failure", async () => {
  const detected = setup(async () => ({ ok: true, json: async () => ({ language: "IT" }) }));
  await detected.detectLanguage();
  assert.equal(detected.state.lang, "IT");
  for (const fetch of [
    async () => ({ ok: false, status: 503 }),
    async () => { throw new Error("Timeout"); },
    async () => ({ ok: true, json: async () => ({ language: "XX" }) }),
  ]) {
    const component = setup(fetch);
    await component.detectLanguage();
    assert.equal(component.state.lang, "EN");
  }
});

test("honors saved manual language and ignores stale automatic results", async () => {
  const saved = setup(() => { throw new Error("Should skip lookup"); }, "HR");
  await saved.detectLanguage();
  assert.equal(saved.state.lang, "HR");
  let resolve;
  const component = setup(() => new Promise((done) => { resolve = done; }));
  const pending = component.detectLanguage();
  component.renderVals().langs.find((item) => item.label === "DE").pick();
  resolve({ ok: true, json: async () => ({ language: "IT" }) });
  await pending;
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
