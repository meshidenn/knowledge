# /// script
# requires-python = ">=3.11"
# ///
"""
日次 Markdown の「## スキップした論文」を、raw JSON と突き合わせて arXiv リンク付きで上書きする。
本文で既に URL として現れた arxiv_id は「ピックアップ済み」とみなし、スキップ一覧から除外する。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKIP_HEADING = "## スキップした論文"
# /abs/1234.5678 または /abs/1234.56789（任意で v1 サフィックス）
ARXIV_RE = re.compile(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,7})(?:v[0-9]+)?", re.I)


def featured_ids_from_markdown(md: str) -> set[str]:
    """スキップ節より前の本文に出てくる arXiv ID（ピックアップ済み）。"""
    idx = md.find(SKIP_HEADING)
    prefix = md[:idx] if idx != -1 else md
    return {m.group(1) for m in ARXIV_RE.finditer(prefix)}


def format_skip_section(date: str, skipped: list[dict]) -> str:
    lines = [
        SKIP_HEADING,
        "",
        "（テーマ外。クリックで arXiv へ。`papers/daily/raw/"
        + date
        + ".json` の `arxiv_id` と対応）",
        "",
    ]
    for p in skipped:
        aid = (p.get("arxiv_id") or "").strip()
        title = (p.get("title") or "Unknown").strip()
        if not aid:
            lines.append(f"- {title}")
            continue
        label = title if len(title) <= 120 else title[:117] + "…"
        lines.append(f"- [{label}](https://arxiv.org/abs/{aid})")
    lines.append("")
    return "\n".join(lines)


def merge_markdown(md: str, new_section: str) -> str:
    idx = md.find(SKIP_HEADING)
    if idx == -1:
        return md.rstrip() + "\n\n" + new_section
    return md[:idx].rstrip() + "\n\n" + new_section


def main() -> None:
    ap = argparse.ArgumentParser(description="Rewrite skip section with arXiv links from raw JSON.")
    ap.add_argument("markdown", type=Path, help="Path to papers/daily/YYYY-MM-DD.md")
    ap.add_argument("raw_json", type=Path, help="Path to papers/daily/raw/YYYY-MM-DD.json")
    args = ap.parse_args()

    if not args.raw_json.is_file():
        print(f"[ERROR] JSON not found: {args.raw_json}", file=sys.stderr)
        sys.exit(1)
    if not args.markdown.is_file():
        print(f"[ERROR] Markdown not found: {args.markdown}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(args.raw_json.read_text(encoding="utf-8"))
    date = data.get("date") or args.raw_json.stem
    papers: list[dict] = data.get("papers") or []

    md = args.markdown.read_text(encoding="utf-8")
    featured = featured_ids_from_markdown(md)
    skipped = [p for p in papers if (p.get("arxiv_id") or "").strip() not in featured]

    new_section = format_skip_section(str(date), skipped)
    out = merge_markdown(md, new_section)
    args.markdown.write_text(out, encoding="utf-8")

    print(f"[OK] Skip section: {len(skipped)} papers (featured {len(featured)} ids in body) → {args.markdown}")


if __name__ == "__main__":
    main()
