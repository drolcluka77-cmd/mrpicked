import assert from "node:assert/strict";
import { randomUUID } from "node:crypto";
import test from "node:test";
import express from "express";
import type { Transporter } from "nodemailer";
import { createReportDelivery } from "../src/lib/report-mail";
import { createReportRouter } from "../src/routes/report-requests";

const input = () => ({
  email: "visitor@example.test", business: "Test restaurant", language: "SL" as const,
  consent: false, requestId: randomUUID(),
});

test("sends the owner notification and a localized visitor confirmation", async () => {
  const messages: any[] = [];
  const send = createReportDelivery({
    sendMail: async (message: any) => {
      messages.push(message);
      return { accepted: [message.to] };
    },
  } as unknown as Transporter, "sender@example.test");
  assert.deepEqual(await send(input()), { accepted: true, confirmationSent: true });
  assert.equal(messages.length, 2);
  assert.equal(messages[0].to, "info@mrpicked.eu");
  assert.equal(messages[0].replyTo, "visitor@example.test");
  assert.match(messages[0].text, /sporočila: NE/);
  assert.equal(messages[1].to, "visitor@example.test");
  assert.match(messages[1].subject, /Prejeli smo/);
});

test("does not send a confirmation when the owner notification fails", async () => {
  let calls = 0;
  const send = createReportDelivery({
    sendMail: async () => { calls++; throw new Error("mock failure"); },
  } as unknown as Transporter, "sender@example.test");
  await assert.rejects(send(input()));
  assert.equal(calls, 1);
});

test("preserves owner success when visitor confirmation fails", async () => {
  let calls = 0;
  const send = createReportDelivery({
    sendMail: async () => {
      if (++calls === 2) throw new Error("mock failure");
      return { accepted: ["owner"] };
    },
  } as unknown as Transporter, "sender@example.test");
  assert.deepEqual(await send(input()), { accepted: true, confirmationSent: false });
});

test("validates, deduplicates, detects conflicts and rate-limits without sending email", async () => {
  let deliveries = 0;
  const app = express();
  app.use(express.json());
  app.use((req, _res, next) => {
    req.log = { warn() {}, error() {} } as any;
    next();
  });
  app.use("/api", createReportRouter(async () => {
    deliveries++;
    return { accepted: true, confirmationSent: true };
  }));
  const server = app.listen(0);
  await new Promise<void>((resolve) => server.once("listening", resolve));
  const address = server.address() as { port: number };
  const post = (data: unknown) => fetch(`http://127.0.0.1:${address.port}/api/report-requests`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data),
  });
  try {
    assert.equal((await post({ ...input(), email: "invalid" })).status, 400);
    assert.equal(deliveries, 0);
    const body = input();
    assert.equal((await post(body)).status, 200);
    assert.equal((await post(body)).status, 200);
    assert.equal(deliveries, 1);
    assert.equal((await post({ ...body, business: "Different" })).status, 409);
    assert.equal((await post(input())).status, 200);
    assert.equal((await post(input())).status, 429);
    assert.equal(deliveries, 2);
  } finally {
    server.closeAllConnections();
    await new Promise<void>((resolve) => server.close(() => resolve()));
  }
});

test("returns a retryable error when delivery fails", async () => {
  const app = express();
  app.use(express.json());
  app.use((req, _res, next) => {
    req.log = { warn() {}, error() {} } as any;
    next();
  });
  app.use("/api", createReportRouter(async () => { throw new Error("mock failure"); }));
  const server = app.listen(0);
  await new Promise<void>((resolve) => server.once("listening", resolve));
  try {
    const address = server.address() as { port: number };
    const response = await fetch(`http://127.0.0.1:${address.port}/api/report-requests`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(input()),
    });
    assert.equal(response.status, 503);
    assert.deepEqual(await response.json(), { error: "DELIVERY_FAILED" });
  } finally {
    server.closeAllConnections();
    await new Promise<void>((resolve) => server.close(() => resolve()));
  }
});
