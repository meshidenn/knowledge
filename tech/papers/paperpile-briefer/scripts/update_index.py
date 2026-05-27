# /// script
# requires-python = ">=3.11"
# ///
"""GitHub/Obsidianで読みやすいbrief一覧とlatestリンクを更新する。"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def first_heading(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def build_index(briefs_dir: Path, chat_dir: Path, limit: int) -> str:
    files = sorted((path for path in briefs_dir.glob("*.md") if DATE_RE.match(path.name)), reverse=True)
    latest = files[0] if files else None
    lines = [
        "# Paperpile Briefs",
        "",
        "Paperpileに追加した論文を、落合陽一フォーマットでまとめた日次briefです。",
        "",
    ]
    if latest:
        chat_path = chat_dir / latest.name
        lines.extend(
            [
                "## 最新",
                "",
                f"- Brief: [{first_heading(latest)}]({latest.name})",
                f"- Chat prompt: [{chat_path.as_posix()}](../chat/{latest.name})",
                "",
            ]
        )
    lines.extend(["## 最近のbrief", ""])
    if files:
        for path in files[:limit]:
            chat_exists = (chat_dir / path.name).exists()
            chat_link = f" / [chat](../chat/{path.name})" if chat_exists else ""
            lines.append(f"- [{first_heading(path)}]({path.name}){chat_link}")
    else:
        lines.append("- まだbriefはありません。")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--briefs-dir", required=True)
    parser.add_argument("--chat-dir", required=True)
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    briefs_dir = Path(args.briefs_dir)
    chat_dir = Path(args.chat_dir)
    briefs_dir.mkdir(parents=True, exist_ok=True)
    index_path = briefs_dir / "README.md"
    latest_path = briefs_dir / "latest.md"

    index_path.write_text(build_index(briefs_dir, chat_dir, args.limit))

    files = sorted((path for path in briefs_dir.glob("*.md") if DATE_RE.match(path.name)), reverse=True)
    if files:
        shutil.copyfile(files[0], latest_path)
    elif latest_path.exists():
        latest_path.unlink()

    print(f"[OK] Updated {index_path}")
    if files:
        print(f"[OK] Updated {latest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
