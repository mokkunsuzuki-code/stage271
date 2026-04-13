# Stage269 Gate Model

Stage269 introduces a VEP gate on top of the Stage268 verification score.

## Core Design

The gate has three outputs:

- accept
- pending
- reject

## Immediate Gate

Immediate Gate evaluates:

- Integrity Trust
- Execution Trust
- Identity Trust

If any of these is incomplete, the result is:

- reject

This is fail-closed behavior.

## Settlement Gate

Settlement Gate evaluates:

- Time Trust

If time settlement is not yet complete, the result is:

- pending

This is not reject.

It means the evidence is not fully settled yet.

## Final Meaning

- `accept` = fully publishable / deployable
- `pending` = not rejected, waiting for time settlement
- `reject` = fail-closed, stop pipeline

## Why This Matters

This avoids two bad extremes:

- fail-open: unsafe artifacts still pass
- over-reject: time settlement delay causes false rejection

Stage269 introduces policy behavior without misclassifying normal Bitcoin settlement delay as failure.
