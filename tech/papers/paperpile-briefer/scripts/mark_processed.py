# /// script
# requires-python = ">=3.11"
# ///
"""raw JSONに含まれるpaper_idsを処理済み状態へ追加する。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--state", required=True)
    args = parser.parse_args()

    raw_path = Path(args.raw)
    state_path = Path(args.state)
    raw = json.loads(raw_path.read_text())
    ids = list(raw.get("paper_ids", []))

    if state_path.exists():
        state = json.loads(state_path.read_text())
    else:
        state = {"seen_ids": []}

    seen = set(state.get("seen_ids", []))
    seen.update(ids)
    state["seen_ids"] = sorted(seen)
    state["updated_at"] = datetime.now(timezone.utc).isoformat()

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2))
    print(f"[OK] Marked {len(ids)} papers as processed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
