import nodemailer, { type Transporter } from "nodemailer";
import type { ReportRequestInput } from "@workspace/api-zod";
import { buildConfirmationEmail } from "./confirmation-email";

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
    const confirmationEmail = buildConfirmationEmail(input);
    try {
      const confirmation = await transport.sendMail({
        from,
        to: input.email,
        replyTo: "info@mrpicked.eu",
        ...confirmationEmail,
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
