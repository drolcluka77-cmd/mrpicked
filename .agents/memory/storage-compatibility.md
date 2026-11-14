---
name: Managed storage SDK compatibility
description: Compatibility constraint between the Replit storage credential template and Google Storage SDK major versions.
---

Do not upgrade the Google Cloud Storage SDK to a new major without verifying an actual managed-storage upload.

**Why:** The Replit sidecar credential template failed with Google Cloud Storage v9 and “Unable to detect a Project Id”, despite passing type checks. The unchanged template worked with Storage v7 and google-auth-library v9.

**How to apply:** Retain compatible dependency majors unless the managed credential setup is officially updated. Verify uploads and streaming, not just compilation, when changing storage dependencies.
