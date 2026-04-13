#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "out" / "vep_status"
OUT_JSON = OUT_DIR / "gate_result.json"
OUT_SHA256 = OUT_DIR / "gate_result.json.sha256"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not OUT_JSON.exists():
        raise SystemExit("[ERROR] gate_result.json not found")

    if not OUT_SHA256.exists():
        raise SystemExit("[ERROR] gate_result.json.sha256 not found")

    data = json.loads(OUT_JSON.read_text(encoding="utf-8"))

    required = {"stage", "gate_model", "decision", "reason", "scores", "timestamp_utc"}
    missing = required - set(data.keys())
    if missing:
        raise SystemExit(f"[ERROR] missing keys: {sorted(missing)}")

    if data["decision"] not in {"accept", "pending", "reject"}:
        raise SystemExit(f"[ERROR] invalid decision: {data['decision']}")

    scores = data["scores"]
    for key in {
        "time_trust",
        "integrity_trust",
        "execution_trust",
        "identity_trust",
        "immediate_score",
        "total_trust",
    }:
        if key not in scores:
            raise SystemExit(f"[ERROR] missing score: {key}")
        value = scores[key]
        if not isinstance(value, (int, float)):
            raise SystemExit(f"[ERROR] non-numeric score: {key}")

    expected_immediate = round(
        scores["integrity_trust"] * scores["execution_trust"] * scores["identity_trust"],
        4,
    )
    if round(scores["immediate_score"], 4) != expected_immediate:
        raise SystemExit(
            f"[ERROR] immediate_score mismatch: expected {expected_immediate}, got {scores['immediate_score']}"
        )

    actual_digest = sha256_file(OUT_JSON)
    expected_digest = OUT_SHA256.read_text(encoding="utf-8").strip().split()[0]
    if actual_digest != expected_digest:
        raise SystemExit(
            f"[ERROR] sha256 mismatch: expected {expected_digest}, got {actual_digest}"
        )

    print("[OK] gate result verified")
    print(f"[OK] decision: {data['decision']}")
    print(f"[OK] sha256: {actual_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
