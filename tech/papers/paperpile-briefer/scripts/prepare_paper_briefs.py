# /// script
# requires-python = ">=3.11"
# ///
"""Prepare per-paper raw files and output paths for a daily Paperpile run."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def slugify(value: str, fallback: str) -> str:
    base = value or fallback
    base = base.lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    if not base:
        base = fallback
    digest = hashlib.sha1((value or fallback).encode("utf-8")).hexdigest()[:8]
    return f"{base[:72].strip('-')}-{digest}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--briefs-dir", required=True)
    parser.add_argument("--chat-dir", required=True)
    parser.add_argument("--paper-raw-dir", required=True)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()

    raw_path = Path(args.raw)
    data: dict[str, Any] = json.loads(raw_path.read_text())
    date = str(data.get("date") or raw_path.stem)

    brief_day_dir = Path(args.briefs_dir) / date
    chat_day_dir = Path(args.chat_dir) / date
    paper_raw_day_dir = Path(args.paper_raw_dir) / date
    brief_day_dir.mkdir(parents=True, exist_ok=True)
    chat_day_dir.mkdir(parents=True, exist_ok=True)
    paper_raw_day_dir.mkdir(parents=True, exist_ok=True)

    papers = []
    used_slugs: set[str] = set()
    for index, paper in enumerate(data.get("papers") or [], start=1):
        title = str(paper.get("title") or f"paper-{index}")
        paper_id = str(paper.get("id") or title)
        slug = slugify(f"{paper_id}-{title}", f"paper-{index}")
        if slug in used_slugs:
            slug = f"{slug}-{index}"
        used_slugs.add(slug)

        paper_raw_path = paper_raw_day_dir / f"{slug}.json"
        brief_path = brief_day_dir / f"{slug}.md"
        chat_path = chat_day_dir / f"{slug}.md"
        paper_raw_path.write_text(
            json.dumps(
                {
                    "date": date,
                    "source_export": data.get("source_export", ""),
                    "count": 1,
                    "paper_ids": [paper.get("id", "")],
                    "papers": [paper],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        papers.append(
            {
                "index": index,
                "id": paper.get("id", ""),
                "title": title,
                "slug": slug,
                "raw": str(paper_raw_path),
                "brief": str(brief_path),
                "chat": str(chat_path),
                "brief_rel": f"{date}/{slug}.md",
                "chat_rel": f"../chat/{date}/{slug}.md",
            }
        )

    manifest_path = Path(args.manifest)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps({"date": date, "count": len(papers), "papers": papers}, ensure_ascii=False, indent=2))
    print(f"[OK] Prepared {len(papers)} per-paper brief targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
