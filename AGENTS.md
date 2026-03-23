# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## リポジトリ概要

個人の技術知識を蓄積・自動追跡するモノレポ。Claude Code CLI（サブスクリプション認証、API KEY 不要）を分析エンジンとして使用する。

```
knowledge/
├── tech/
│   ├── papers/hf-paper-tracker/   ← HF Daily Papers の自動追跡・分析
│   └── blog/                      ← Zenn/Qiita いいね・ストック記事の週次まとめ
```

## Python スクリプトの実行

全スクリプトは [uv](https://docs.astral.sh/uv/) の **PEP 723 インライン依存**で動かす（`pyproject.toml` なし）。

```bash
uv run scripts/fetch_papers.py          # 依存は各スクリプト先頭の `# /// script` ブロック
uv add requests --script scripts/foo.py # 依存追加
```

