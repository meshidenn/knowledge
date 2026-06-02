# /// script
# requires-python = ">=3.11"
# ///
"""Write a daily index for per-paper Paperpile briefs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    date = manifest.get("date", "")
    papers = manifest.get("papers", [])

    lines = [
        f"# Paperpile Daily Brief {date}",
        "",
        f"新しく追加された論文: {len(papers)}本",
        "",
        "## 論文別brief",
        "",
    ]

    for paper in papers:
        lines.append(f"{paper['index']}. [{paper['title']}]({paper['brief_rel']}) / [chat]({paper['chat_rel']})")

    lines.extend(
        [
            "",
            "## モバイルで続ける",
            "",
            "- Obsidian Mobileでこの日次目次を開き、気になる論文の `chat` リンクを開く。",
            "- chatファイルの本文をChatGPT mobileへ貼ると、その論文について追加質問できる。",
            "",
            "## 運用メモ",
            "",
            "- `skip` はPaperpile export内で既に処理済み、またはwiki stub生成時に既存ファイルがあるため再作成しなかった件数を指す。新規brief対象から除外されたという意味ではない。",
        ]
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n")
    print(f"[OK] Wrote daily index: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
