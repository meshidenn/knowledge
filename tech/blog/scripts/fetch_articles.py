# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.32.5",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Zenn（いいね）と Qiita（ストック）から直近7日分の記事を取得し
raw/YYYY-WW.json に保存する。
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

# --- 定数 ---
JST = timezone(timedelta(hours=9))
NOW = datetime.now(JST)
WEEK_LABEL = NOW.strftime("%Y-W%V")
CUTOFF = NOW - timedelta(days=7)  # 直近7日

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
RAW_DIR = REPO_DIR / "raw"
OUTPUT_PATH = RAW_DIR / f"{WEEK_LABEL}.json"


def load_env() -> tuple[str, str]:
    """環境変数をロードして (zenn_username, qiita_token) を返す。"""
    load_dotenv(REPO_DIR / ".env")
    username = os.environ.get("ZENN_USERNAME", "")
    token = os.environ.get("QIITA_TOKEN", "")
    if not username:
        print("[ERROR] ZENN_USERNAME が未設定です (.env を確認してください)")
        sys.exit(1)
    if not token:
        print("[ERROR] QIITA_TOKEN が未設定です (.env を確認してください)")
        sys.exit(1)
    return username, token


def fetch_zenn_likes(username: str) -> list[dict]:
    """Zenn でいいねした記事を取得する（直近7日分）。"""
    articles = []
    page = 1
    while True:
        url = f"https://zenn.dev/api/articles?liked_by={username}&order=latest&count=20&page={page}"
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"[WARN] Zenn API エラー (page={page}): {e}")
            break

        data = resp.json()
        items = data.get("articles", [])
        if not items:
            break

        for item in items:
            # liked_at がない場合は published_at で代用
            liked_at_str = item.get("liked_at") or item.get("published_at", "")
            try:
                liked_at = datetime.fromisoformat(liked_at_str.replace("Z", "+00:00"))
            except Exception:
                continue

            if liked_at < CUTOFF:
                return articles  # 古い記事に達したら終了

            articles.append({
                "source": "zenn",
                "title": item.get("title", ""),
                "url": f"https://zenn.dev{item.get('path', '')}",
                "liked_at": liked_at_str,
                "topics": [t.get("name", "") for t in item.get("topics", [])],
                "emoji": item.get("emoji", ""),
            })

        page += 1

    return articles


def fetch_qiita_stocks(token: str) -> list[dict]:
    """Qiita でストックした記事を取得する（直近7日分）。"""
    articles = []
    page = 1
    headers = {"Authorization": f"Bearer {token}"}

    while True:
        url = f"https://qiita.com/api/v2/authenticated_user/stocks?page={page}&per_page=20"
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"[WARN] Qiita API エラー (page={page}): {e}")
            break

        items = resp.json()
        if not items:
            break

        for item in items:
            created_at_str = item.get("created_at", "")
            try:
                created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
            except Exception:
                continue

            if created_at < CUTOFF:
                return articles  # 古い記事に達したら終了

            articles.append({
                "source": "qiita",
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "liked_at": created_at_str,
                "topics": [t.get("name", "") for t in item.get("tags", [])],
                "emoji": "",
            })

        page += 1

    return articles


def main() -> None:
    if OUTPUT_PATH.exists():
        print(f"[SKIP] {OUTPUT_PATH} は既に存在します")
        sys.exit(0)

    username, token = load_env()

    print(f"[INFO] 取得期間: {CUTOFF.strftime('%Y-%m-%d')} 〜 {NOW.strftime('%Y-%m-%d')}")

    print("[1/2] Zenn いいね記事を取得中...")
    zenn_articles = fetch_zenn_likes(username)
    print(f"      {len(zenn_articles)} 件")

    print("[2/2] Qiita ストック記事を取得中...")
    qiita_articles = fetch_qiita_stocks(token)
    print(f"      {len(qiita_articles)} 件")

    all_articles = zenn_articles + qiita_articles
    if not all_articles:
        print("[WARN] 記事が0件です")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "week": WEEK_LABEL,
        "fetched_at": NOW.isoformat(),
        "cutoff": CUTOFF.isoformat(),
        "count": len(all_articles),
        "articles": all_articles,
    }
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"[OK] {OUTPUT_PATH} に保存しました（計 {len(all_articles)} 件）")


if __name__ == "__main__":
    main()
