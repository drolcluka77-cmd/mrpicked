---
name: Email delivery preference
description: User's choice of email delivery method and recipients' roles.
---

Use the user's own SMTP provider rather than switching to an email API service. Form submissions should notify the owner and send a receipt confirmation to the visitor.

**Why:** The user explicitly requested SMTP and selected both delivery paths.

**How to apply:** Preserve this choice when extending email features; request any changed credentials only through the secure secrets flow.

The visitor's return message must always be in the customer's language.

**Why:** The user explicitly required “naj bo vedno v jeziku stranke”.

**How to apply:** Translate the subject and the whole message, including the receipt explanation, when adding or revising a supported language.
