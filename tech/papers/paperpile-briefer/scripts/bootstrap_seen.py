# /// script
# requires-python = ">=3.11"
# ///
"""初回運用前にPaperpile既存ライブラリを処理済みとして登録する。"""

from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("fetch_new_papers", SCRIPT_DIR / "fetch_new_papers.py")
fetch_new_papers = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(fetch_new_papers)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", required=True, help="Paperpile JSON/BibTeX export path")
    parser.add_argument("--state", required=True, help="Seen-state JSON path")
    args = parser.parse_args()

    refs = fetch_new_papers.load_export(Path(args.export).expanduser())
    state_path = Path(args.state).expanduser()
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(
            {
                "seen_ids": sorted(ref["id"] for ref in refs),
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "bootstrap_count": len(refs),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    print(f"[OK] Bootstrapped {len(refs)} existing papers as seen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
