# /// script
# requires-python = ">=3.11"
# ///
"""生成済みbriefから、チャットで追加質問するためのMarkdownプロンプトを作る。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--brief", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    raw_path = Path(args.raw)
    brief_path = Path(args.brief)
    output_path = Path(args.output)

    raw = json.loads(raw_path.read_text())
    brief = brief_path.read_text()
    titles = "\n".join(f"- {paper.get('title', '')}" for paper in raw.get("papers", []))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"""# Chat Prompt {raw.get("date", "")}

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

{titles or "- （対象なし）"}

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

{brief}
"""
    )
    print(f"[OK] Wrote chat prompt: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
