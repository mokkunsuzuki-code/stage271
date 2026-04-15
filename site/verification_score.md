# Stage270 Verification Score

Stage270 reuses the deterministic trust score from Stage268.

**Total Trust:** `0.5`

## Component Scores

- **Time Trust:** `1.0`  (measured)
- **Integrity Trust:** `1.0`  (sha256:yes, ots:yes)
- **Execution Trust:** `0.5`  (workflows:yes, ci_evidence:no)
- **Identity Trust:** `1.0`  (signatures:yes, public_keys:yes, multi_signer:yes)

## Formula

`Total Trust = Time × Integrity × Execution × Identity`

## Important Meaning

- This is a reproducible trust index.
- This score is later used by the Stage270 gate.
- Time settlement may remain pending even when other dimensions are strong.

