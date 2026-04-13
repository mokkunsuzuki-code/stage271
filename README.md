# Stage268: Verification Score

## Overview

Stage268 introduces a **deterministic verification score model** that evaluates trust from four independent dimensions and publishes the result as a reproducible public score.

This stage extends the previous verification work by turning evidence into a visible trust evaluation.

The score is published as both:

- machine-readable JSON
- human-readable public page

---

## Core Concept

Stage268 evaluates trust using four components:

- **Time Trust**
- **Integrity Trust**
- **Execution Trust**
- **Identity Trust**

These are combined as:

**Total Trust = Time × Integrity × Execution × Identity**

This is not a claim of absolute security.

It is a **reproducible evidence-based trust index**.

---

## What This Stage Adds

Stage268 adds:

- a deterministic trust scoring model
- reproducible score generation
- local score verification
- GitHub Actions score verification
- public GitHub Pages publication for the score
- a visual verification score page

This transforms the system from:

- evidence exists

into:

- evidence is scored and publicly visible

---

## Verification Dimensions

### 1. Time Trust

Measures the time-anchoring status of evidence.

Examples:

- Bitcoin-related evidence detected
- OpenTimestamps-related evidence detected
- confirmations parsed or not yet parsed

Current interpretation example:

- `0.25` = Bitcoin-related evidence found but confirmations not parsed
- `1.00` = strong finalized Bitcoin confirmation state

### 2. Integrity Trust

Measures whether artifacts are content-bound and tamper-detectable.

Examples:

- SHA256 files exist
- OpenTimestamps proof files exist

### 3. Execution Trust

Measures whether execution evidence exists.

Examples:

- GitHub Actions workflows exist
- CI-linked evidence exists
- run URL evidence exists

### 4. Identity Trust

Measures whether results are bound to identified signers.

Examples:

- signature files exist
- public key files exist
- multi-signer configuration exists

---

## Formula

The score is computed as:

`Total Trust = Time × Integrity × Execution × Identity`

This multiplicative model is important.

If one trust dimension is weak, the total score drops accordingly.

This makes weak trust dimensions visible instead of hidden.

---

## Output

Stage268 generates:

- `out/verification_score/verification_score.json`
- `out/verification_score/verification_score.json.sha256`
- `out/verification_score/verification_score.md`

Public page:

- `site/index.html`

Published files:

- `site/verification_score.json`
- `site/verification_score.md`

---

## Public Verification Page

Stage268 publishes a public score page through GitHub Pages.

This page displays:

- Total Trust
- Time Trust
- Integrity Trust
- Execution Trust
- Identity Trust
- raw JSON score output

This makes trust evaluation publicly visible and reproducible.

---

## What This Stage Proves

Stage268 proves that:

- trust can be modeled deterministically
- evidence can be converted into a reproducible score
- the result can be verified locally
- the result can be verified in CI
- the result can be published publicly as a verification page

---

## Important Accuracy

Stage268 does **not** prove absolute security.

It does **not** claim that a score alone is sufficient for full security review.

It proves something narrower and more important:

- trust evidence can be measured
- weak points can be surfaced
- trust can be published reproducibly

---

## Why This Stage Matters

Earlier stages created evidence.

Stage268 makes that evidence measurable.

This is the shift from:

- “evidence exists”

to:

- “trust is evaluated and publicly visible”

That is a major step toward real external review and policy gating.

---

## Current Meaning of the Score

A score such as:

- Time Trust = `0.25`
- Integrity Trust = `1.00`
- Execution Trust = `1.00`
- Identity Trust = `1.00`
- Total Trust = `0.25`

means:

- most trust dimensions are strong
- one weak trust dimension is pulling the total score down

This is not a failure of the model.

This is exactly what the model is supposed to reveal.

---

## Public URL

Verification Score page:

`https://mokkunsuzuki-code.github.io/stage268/`

---

## Local Usage

Build the verification score:

```bash
python3 tools/build_verification_score.py

Verify the generated score:

python3 tools/verify_verification_score.py
GitHub Actions

Stage268 includes:

verification score build
verification score verification
GitHub Pages deployment

This means the score is:

generated locally
reproducible in CI
published publicly
Strategic Position

Stage267 made verification trust visible.

Stage268 makes multi-dimensional trust measurable.

This stage is the transition from:

verification visibility

to:

trust scoring
Next Direction

A natural next stage is to introduce policy behavior such as:

accept
pending
reject

based on trust evaluation rules.

That would turn score visibility into enforcement.

License

MIT License

Copyright (c) 2025 Motohiro Suzuki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.