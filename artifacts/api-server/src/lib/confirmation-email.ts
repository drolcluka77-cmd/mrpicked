import type { ReportRequestInput } from "@workspace/api-zod";

const bookingUrl = "https://calendly.com/drolcluka77/30min";
const signature = `Luka Drolc
Picked

Cyberfinance, računalniško programiranje d.o.o.
Celovška cesta 136, 1000 Ljubljana, Slovenia
+386 40 290 963 · info@mrpicked.eu`;

type Copy = { subject: string; body: string; notice: string };
const translations: Record<ReportRequestInput["language"], Copy> = {
  EN: {
    subject: "Your AI report for {company_name} is being prepared",
    body: `Hi,

Thanks for signing up. We're now checking what ChatGPT, Gemini and Perplexity tell potential customers about {company_name}: whether they recommend you, who shows up instead, and whether your details are correct.

You'll get your report within 48 hours.

If you'd like, we'll walk you through it personally. Book a free 15-minute call and we'll show you where you're losing customers and what to fix first:
👉 ${bookingUrl}

Best regards,`,
    notice: "You're receiving this email because you requested a free AI check on mrpicked.eu.",
  },
  SL: {
    subject: "Vaše AI-poročilo za {company_name} je v pripravi",
    body: `Pozdravljeni,

hvala za prijavo. Preverjamo, kaj ChatGPT, Gemini in Perplexity povedo potencialnim strankam o podjetju {company_name}: ali vas priporočajo, kdo se prikaže namesto vas in ali so vaši podatki pravilni.

Poročilo boste prejeli v 48 urah.

Če želite, vam ga osebno predstavimo. Rezervirajte brezplačen 15-minutni klic in pokazali vam bomo, kje izgubljate stranke in kaj najprej izboljšati:
👉 ${bookingUrl}

Lep pozdrav,`,
    notice: "To e-poštno sporočilo ste prejeli, ker ste na mrpicked.eu naročili brezplačen AI-pregled.",
  },
  HR: {
    subject: "Vaše AI izvješće za {company_name} je u pripremi",
    body: `Pozdrav,

hvala na prijavi. Upravo provjeravamo što ChatGPT, Gemini i Perplexity govore potencijalnim klijentima o tvrtki {company_name}: preporučuju li vas, tko se pojavljuje umjesto vas i jesu li vaši podaci točni.

Izvješće ćete dobiti u roku od 48 sati.

Ako želite, osobno ćemo vam ga predstaviti. Rezervirajte besplatan 15-minutni poziv i pokazat ćemo vam gdje gubite klijente i što prvo poboljšati:
👉 ${bookingUrl}

Srdačan pozdrav,`,
    notice: "Ovu poruku primate jer ste na mrpicked.eu zatražili besplatnu AI provjeru.",
  },
  IT: {
    subject: "Il tuo report AI per {company_name} è in preparazione",
    body: `Ciao,

grazie per esserti registrato. Stiamo verificando cosa ChatGPT, Gemini e Perplexity dicono ai potenziali clienti di {company_name}: se ti consigliano, chi compare al tuo posto e se i tuoi dati sono corretti.

Riceverai il report entro 48 ore.

Se vuoi, te lo illustreremo personalmente. Prenota una chiamata gratuita di 15 minuti e ti mostreremo dove stai perdendo clienti e cosa migliorare per prima cosa:
👉 ${bookingUrl}

Cordiali saluti,`,
    notice: "Ricevi questa email perché hai richiesto un'analisi AI gratuita su mrpicked.eu.",
  },
  DE: {
    subject: "Ihr KI-Bericht für {company_name} wird vorbereitet",
    body: `Guten Tag,

vielen Dank für Ihre Anmeldung. Wir prüfen gerade, was ChatGPT, Gemini und Perplexity potenziellen Kunden über {company_name} sagen: ob sie Sie empfehlen, wer stattdessen erscheint und ob Ihre Angaben korrekt sind.

Sie erhalten Ihren Bericht innerhalb von 48 Stunden.

Wenn Sie möchten, gehen wir ihn persönlich mit Ihnen durch. Buchen Sie ein kostenloses 15-minütiges Gespräch. Wir zeigen Ihnen, wo Sie Kunden verlieren und was Sie zuerst verbessern sollten:
👉 ${bookingUrl}

Mit freundlichen Grüßen`,
    notice: "Sie erhalten diese E-Mail, weil Sie auf mrpicked.eu einen kostenlosen KI-Check angefordert haben.",
  },
  HU: {
    subject: "Készül a(z) {company_name} AI-jelentése",
    body: `Üdvözöljük!

Köszönjük a jelentkezését. Most azt vizsgáljuk, mit mond a ChatGPT, a Gemini és a Perplexity a potenciális ügyfeleknek a(z) {company_name} vállalkozásról: ajánlják-e Önt, ki jelenik meg Ön helyett, és helyesek-e az adatai.

A jelentést 48 órán belül megkapja.

Ha szeretné, személyesen is bemutatjuk az eredményeket. Foglaljon egy ingyenes, 15 perces hívást, és megmutatjuk, hol veszít ügyfeleket, és min érdemes először javítani:
👉 ${bookingUrl}

Üdvözlettel:`,
    notice: "Azért kapja ezt az e-mailt, mert ingyenes AI-ellenőrzést kért a mrpicked.eu oldalon.",
  },
};

export function buildConfirmationEmail(input: Pick<ReportRequestInput, "language" | "business">) {
  const copy = translations[input.language];
  const company = input.business.replace(/[\r\n]+/g, " ").trim();
  const personalize = (text: string) => text.split("{company_name}").join(company);
  return {
    subject: personalize(copy.subject),
    text: `${personalize(copy.body)}\n${signature}\n\n${copy.notice}`,
  };
}
