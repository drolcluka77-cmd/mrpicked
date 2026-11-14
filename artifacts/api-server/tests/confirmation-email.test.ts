import assert from "node:assert/strict";
import test from "node:test";
import { buildConfirmationEmail } from "../src/lib/confirmation-email";

const subjects = {
  EN: "Your AI report for Café & Hotel is being prepared",
  SL: "Vaše AI-poročilo za Café & Hotel je v pripravi",
  HR: "Vaše AI izvješće za Café & Hotel je u pripremi",
  IT: "Il tuo report AI per Café & Hotel è in preparazione",
  DE: "Ihr KI-Bericht für Café & Hotel wird vorbereitet",
  HU: "Készül a(z) Café & Hotel AI-jelentése",
};
const notices = {
  EN: "You're receiving this email because",
  SL: "To e-poštno sporočilo ste prejeli",
  HR: "Ovu poruku primate",
  IT: "Ricevi questa email",
  DE: "Sie erhalten diese E-Mail",
  HU: "Azért kapja ezt az e-mailt",
};

for (const language of Object.keys(subjects) as (keyof typeof subjects)[]) {
  test(`personalizes the complete ${language} confirmation`, () => {
    const message = buildConfirmationEmail({ language, business: "Café & Hotel" });
    assert.equal(message.subject, subjects[language]);
    assert.ok(message.text.includes("Café & Hotel"));
    assert.ok(message.text.includes(notices[language]));
    assert.match(message.text, /ChatGPT.*Gemini.*Perplexity/);
    assert.match(message.text, /48/);
    assert.match(message.text, /15/);
    assert.ok(message.text.includes("👉 https://calendly.com/drolcluka77/30min"));
    assert.ok(message.text.includes("Luka Drolc\nPicked"));
    assert.ok(message.text.includes("Cyberfinance, računalniško programiranje d.o.o."));
    assert.ok(message.text.includes("Celovška cesta 136, 1000 Ljubljana, Slovenia"));
    assert.ok(message.text.includes("+386 40 290 963 · info@mrpicked.eu"));
    assert.ok(!message.text.includes("{company_name}"));
    if (language !== "EN") assert.ok(!message.text.includes("You're receiving this email because"));
  });
}

test("preserves the exact supplied English copy", () => {
  const message = buildConfirmationEmail({ language: "EN", business: "Example" });
  assert.equal(message.text, `Hi,

Thanks for signing up. We're now checking what ChatGPT, Gemini and Perplexity tell potential customers about Example: whether they recommend you, who shows up instead, and whether your details are correct.

You'll get your report within 48 hours.

If you'd like, we'll walk you through it personally. Book a free 15-minute call and we'll show you where you're losing customers and what to fix first:
👉 https://calendly.com/drolcluka77/30min

Best regards,
Luka Drolc
Picked

Cyberfinance, računalniško programiranje d.o.o.
Celovška cesta 136, 1000 Ljubljana, Slovenia
+386 40 290 963 · info@mrpicked.eu

You're receiving this email because you requested a free AI check on mrpicked.eu.`);
});

test("does not interpret dollar signs or newlines in company names as template syntax", () => {
  const message = buildConfirmationEmail({ language: "EN", business: "Hotel $&\r\nExample" });
  assert.equal(message.subject, "Your AI report for Hotel $& Example is being prepared");
  assert.ok(message.text.includes("about Hotel $& Example:"));
});
