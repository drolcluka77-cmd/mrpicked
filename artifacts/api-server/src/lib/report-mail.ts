import nodemailer, { type Transporter } from "nodemailer";
import type { ReportRequestInput } from "@workspace/api-zod";

const confirmationCopy = {
  EN: ["We've received your request", "Thank you for requesting your free Picked report.", "We'll email your report within 48 hours."],
  SL: ["Prejeli smo vaše povpraševanje", "Hvala za naročilo brezplačnega poročila Picked.", "Poročilo vam bomo poslali po e-pošti v 48 urah."],
  HR: ["Primili smo vaš upit", "Hvala što ste zatražili besplatno Picked izvješće.", "Izvješće ćemo vam poslati e-poštom u roku od 48 sati."],
  IT: ["Abbiamo ricevuto la tua richiesta", "Grazie per aver richiesto il report Picked gratuito.", "Riceverai il report via email entro 48 ore."],
  DE: ["Wir haben Ihre Anfrage erhalten", "Vielen Dank für Ihre Anfrage zum kostenlosen Picked-Bericht.", "Sie erhalten Ihren Bericht innerhalb von 48 Stunden per E-Mail."],
  HU: ["Megkaptuk a kérését", "Köszönjük, hogy kérte az ingyenes Picked jelentést.", "A jelentést 48 órán belül elküldjük e-mailben."],
};

export function createSmtpTransport() {
  const { SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SMTP_FROM } = process.env;
  const port = Number(SMTP_PORT);
  if (!SMTP_HOST || !SMTP_USER || !SMTP_PASS || !SMTP_FROM ||
      !Number.isInteger(port) || port < 1 || port > 65535 ||
      /[\r\n]/.test(SMTP_FROM)) {
    throw new Error("SMTP_CONFIGURATION_INVALID");
  }
  return nodemailer.createTransport({
    host: SMTP_HOST,
    port,
    secure: port === 465,
    requireTLS: port !== 465,
    auth: { user: SMTP_USER, pass: SMTP_PASS },
    connectionTimeout: 10_000,
    greetingTimeout: 10_000,
    socketTimeout: 20_000,
    logger: false,
    debug: false,
  });
}

export function createReportDelivery(transport: Transporter, from: string) {
  return async (input: ReportRequestInput) => {
    const notification = await transport.sendMail({
      from,
      to: "info@mrpicked.eu",
      replyTo: input.email,
      subject: "Picked — novo povpraševanje za brezplačno poročilo",
      text: [
        "Novo povpraševanje s spletne strani Picked",
        `Podjetje: ${input.business}`,
        `E-pošta: ${input.email}`,
        `Jezik: ${input.language}`,
        `Soglasje za nasvete in nadaljnja sporočila: ${input.consent ? "DA" : "NE"}`,
        `Čas prejema (UTC): ${new Date().toISOString()}`,
        `Referenca: ${input.requestId}`,
      ].join("\n"),
      disableFileAccess: true,
      disableUrlAccess: true,
    });
    if (!notification.accepted?.length) throw new Error("SMTP_RECIPIENT_REJECTED");
    const copy = confirmationCopy[input.language];
    try {
      const confirmation = await transport.sendMail({
        from,
        to: input.email,
        replyTo: "info@mrpicked.eu",
        subject: `Picked — ${copy[0]}`,
        text: `${copy[1]}\n\n${input.business}\n\n${copy[2]}\n\nPicked\ninfo@mrpicked.eu`,
        disableFileAccess: true,
        disableUrlAccess: true,
      });
      return { accepted: true, confirmationSent: !!confirmation.accepted?.length };
    } catch {
      // The owner's copy already arrived: never ask the visitor to resubmit it.
      return { accepted: true, confirmationSent: false };
    }
  };
}

let deliver: ReturnType<typeof createReportDelivery> | undefined;
export async function deliverReport(input: ReportRequestInput) {
  deliver ??= createReportDelivery(createSmtpTransport(), process.env.SMTP_FROM!);
  return deliver(input);
}
