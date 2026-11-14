import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync(new URL("../index.html", import.meta.url), "utf8");
const source = html.match(/<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/)[1];

function setup(fetch) {
  class Logic {
    props = {};
    state = { mail: "visitor@example.test", biz: "Restaurant", lang: "SL" };
    setState(update) { Object.assign(this.state, update); }
  }
  const document = {
    baseURI: "https://example.test/",
    createElement: () => ({
      value: "",
      checkValidity() { return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(this.value); },
    }),
  };
  const Component = new Function("DCLogic", "fetch", "document", `${source}; return Component;`)(Logic, fetch, document);
  return new Component();
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
