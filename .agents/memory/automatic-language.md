---
name: Automatic language selection
description: User's country-based language requirement and VPN default.
---

Choose the page's initial language automatically from the customer's country. When a VPN is detected, automatic selection must use English.

**Why:** The user requested “avtomatsko v jeziku glede na lokacijo stranke, ce uporablja vpn pa naj bo v eng”.

**How to apply:** Keep country and VPN detection as separate checks; do not replace them with browser-language detection or treat missing VPN data as proof of no VPN.
