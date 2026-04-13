#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCORE_PATH = ROOT / "out" / "verification_score" / "verification_score.json"
OUT_DIR = ROOT / "out" / "vep_status"
OUT_JSON = OUT_DIR / "gate_result.json"
OUT_SHA256 = OUT_DIR / "gate_result.json.sha256"
OUT_MD = OUT_DIR / "gate_result.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_outputs(payload: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    digest = sha256_file(OUT_JSON)
    OUT_SHA256.write_text(f"{digest}  gate_result.json\n", encoding="utf-8")

    lines = [
        "# Stage270 Gate Result",
        "",
        f"**Decision:** `{payload['decision']}`",
        "",
        f"**Reason:** {payload['reason']}",
        "",
        "## Scores",
        "",
        f"- Time Trust: `{payload['scores']['time_trust']}`",
        f"- Integrity Trust: `{payload['scores']['integrity_trust']}`",
        f"- Execution Trust: `{payload['scores']['execution_trust']}`",
        f"- Identity Trust: `{payload['scores']['identity_trust']}`",
        f"- Total Trust: `{payload['scores']['total_trust']}`",
        "",
        "## Gate Meaning",
        "",
        "- `accept`: publishable / deployable",
        "- `pending`: not rejected, but waiting for time settlement",
        "- `reject`: fail-closed, stop pipeline",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not SCORE_PATH.exists():
        print("[ERROR] verification_score.json not found")
        return 1

    data = json.loads(SCORE_PATH.read_text(encoding="utf-8"))
    c = data["components"]

    time_score = float(c["time_trust"]["score"])
    integrity_score = float(c["integrity_trust"]["score"])
    execution_score = float(c["execution_trust"]["score"])
    identity_score = float(c["identity_trust"]["score"])
    total_score = float(data["total_trust"])

    immediate_score = round(integrity_score * execution_score * identity_score, 4)

    decision = "accept"
    reason = "All trust dimensions satisfy policy."
    exit_code = 0

    if integrity_score < 1.0:
        decision = "reject"
        reason = "Integrity failure: hash/OTS evidence is incomplete."
        exit_code = 1
    elif execution_score < 1.0:
        decision = "reject"
        reason = "Execution failure: CI/workflow evidence is incomplete."
        exit_code = 1
    elif identity_score < 1.0:
        decision = "reject"
        reason = "Identity failure: signature/public-key evidence is incomplete."
        exit_code = 1
    elif immediate_score < 1.0:
        decision = "reject"
        reason = "Immediate gate failure: one non-time trust dimension is incomplete."
        exit_code = 1
    elif time_score < 1.0:
        decision = "pending"
        reason = "Time settlement pending: Bitcoin confirmations are not fully settled yet."
        exit_code = 0
    else:
        decision = "accept"
        reason = "All gate conditions satisfied including settled time trust."
        exit_code = 0

    payload = {
        "stage": "stage270",
        "gate_model": {
            "immediate_gate": "integrity × execution × identity",
            "settlement_gate": "time",
        },
        "decision": decision,
        "reason": reason,
        "scores": {
            "time_trust": round(time_score, 4),
            "integrity_trust": round(integrity_score, 4),
            "execution_trust": round(execution_score, 4),
            "identity_trust": round(identity_score, 4),
            "immediate_score": immediate_score,
            "total_trust": round(total_score, 4),
        },
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }

    write_outputs(payload)

    print(f"[INFO] decision: {decision}")
    print(f"[INFO] reason: {reason}")
    print(f"[INFO] immediate_score: {immediate_score}")
    print(f"[INFO] total_trust: {total_score}")
    print(f"[INFO] output: {OUT_JSON}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
