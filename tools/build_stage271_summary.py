#!/usr/bin/env python3
import json
from pathlib import Path

def get_reviewer_name(data):
    if isinstance(data.get("reviewer"), dict):
        return data["reviewer"].get("display_name", data["reviewer"].get("id", "unknown"))
    if isinstance(data.get("reviewer_identity"), dict):
        return data["reviewer_identity"].get("display_name", data["reviewer_identity"].get("id", "unknown"))
    if isinstance(data.get("reviewer"), str):
        return data["reviewer"]
    return "unknown"

def get_result(data):
    return data.get("review_result", data.get("result", "unknown"))

def get_target(data):
    return data.get("target_artifact", data.get("target", "unknown"))

def main():
    reviews = sorted(Path("review_records").glob("*.json"))
    summary_lines = []
    summary_lines.append("# Stage271 External Review Linked Proof")
    summary_lines.append("")
    summary_lines.append("## Overview")
    summary_lines.append("Stage271 records external review outcomes as verifiable artifacts.")
    summary_lines.append("")
    summary_lines.append("## Review Records")

    if not reviews:
        summary_lines.append("- none")
    else:
        for p in reviews:
            data = json.loads(p.read_text(encoding="utf-8"))
            review_id = data.get("review_id", p.stem)
            reviewer_name = get_reviewer_name(data)
            result = get_result(data)
            target = get_target(data)
            summary_lines.append(
                f"- {review_id} | reviewer={reviewer_name} | result={result} | target={target}"
            )

    summary_lines.append("")
    summary_lines.append("## Output")
    summary_lines.append("- out/review_chain/review_chain_verification.json")
    summary_lines.append("- out/review_chain/latest_review_pointer.json")
    summary_lines.append("")

    out = Path("out/review_chain/stage271_summary.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"[OK] wrote {out}")

if __name__ == "__main__":
    main()
