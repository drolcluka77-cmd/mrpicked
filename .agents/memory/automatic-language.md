---
name: Automatic language selection
description: User requires browser-language defaults without IP or VPN detection.
---

Choose the default language from `navigator.language`, falling back to English. Do not use ipapi.is, IP location or VPN detection.

**Why:** The user explicitly replaced the earlier location/VPN request: “Pick the default language from the browser language (navigator.language), falling back to English. No VPN detection. Don’t change anything else.”

**How to apply:** Keep language detection client-side and preserve manual language selection. Do not add third-party IP lookups.
