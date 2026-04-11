# Stage266: Verified Public Evidence

## Overview

Stage266 introduces **Verified Public Evidence**.

This stage enables:

- Public verification via URL
- Browser-based verification of manifest / receipt / OTS proof
- OpenTimestamps status visibility (pending / confirmed)
- Deterministic verification status published as JSON
- Visual verification state display via GitHub Pages

This transforms:

- "Evidence exists" → "Evidence status is publicly verifiable"

---

## Public Verification URL

👉 https://mokkunsuzuki-code.github.io/stage266/

Anyone can open this URL and verify:

- Manifest file
- Receipt
- OpenTimestamps proof
- Current verification status

---

## What This Stage Proves

- Evidence is publicly accessible via URL
- Verification inputs are reproducible
- OpenTimestamps proof is verifiable
- Verification status is machine-readable (JSON)
- Verification state is human-readable (UI)

---

## OpenTimestamps Status

The page shows:

- pending → waiting for Bitcoin confirmation
- confirmed → anchored in Bitcoin block

When confirmed, it will include:

- block height
- timestamp (UTC)

---

## Architecture

### CI (GitHub Actions)

- Generate release manifest
- Generate receipt
- Stamp with OpenTimestamps
- Upgrade OTS proof
- Verify OTS status
- Generate `verification_status.json`

### GitHub Pages

- Reads `verification_status.json`
- Displays verification state
- Provides public artifact URLs

---

## Key Files


out/release/
├── release_manifest.json
├── release_manifest.json.ots
├── github_actions_receipt.json

docs/
├── index.html
└── status/verification_status.json


---

## Verification Model

This stage separates:

- Evidence generation (CI)
- Evidence verification (OTS)
- Evidence presentation (Pages)

This ensures:

- reproducibility
- transparency
- public verifiability

---

## Important Notes

- "pending" is expected immediately after stamping
- confirmation occurs when Bitcoin anchor is finalized
- verification does not rely on trust in this repository
- anyone can independently verify the proof

---

## Evolution

Stage265:
→ Public verification URL

Stage266:
→ Verification status visibility (this stage)

---

## License

MIT License

