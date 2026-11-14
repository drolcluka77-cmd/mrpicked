---
name: Email delivery preference
description: User's choice of email delivery method and recipients' roles.
---

Use the user's own SMTP provider rather than switching to an email API service. Form submissions should notify the owner and send a receipt confirmation to the visitor.

**Why:** The user explicitly requested SMTP and selected both delivery paths.

**How to apply:** Preserve this choice when extending email features; request any changed credentials only through the secure secrets flow.
