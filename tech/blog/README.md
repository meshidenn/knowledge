# tech/blog — 週次技術記事まとめ

Zenn（いいね）・Qiita（ストック）した記事を週次で自動収集し、まとめを生成する。

## ディレクトリ構成

```
tech/blog/
├── scripts/
│   ├── fetch_articles.py   # Zenn/Qiita から記事取得
│   └── run_weekly.sh       # エントリポイント
├── raw/                    # 生データ (YYYY-WW.json)
├── weekly/                 # 週次まとめ (YYYY-WW.md)
├── summary.md              # トピック別全体まとめ
├── .env                    # 認証情報（git管理外）
└── .env.example            # .env のテンプレート
```

## セットアップ

### 1. .env を作成

```bash
cp .env.example .env
```

`.env` を編集:

```env
ZENN_USERNAME=your_zenn_username   # Zenn のユーザー名
QIITA_TOKEN=your_qiita_api_token   # Qiita の個人用アクセストークン
```

**Qiita トークンの発行:**
Qiita → 設定 → アプリケーション → 個人用アクセストークン → `read_qiita` スコープで発行

### 2. uv のインストール（未導入の場合）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 使い方

```bash
cd tech/blog
bash scripts/run_weekly.sh
```

実行すると以下が生成される:

| ファイル | 内容 |
|---------|------|
| `raw/YYYY-WW.json` | 取得した記事の生データ |
| `weekly/YYYY-WW.md` | 今週のトピック別まとめ |
| `summary.md` | 全トピックの現状まとめ（累積更新） |

## cron 設定（毎週月曜 9:00 に自動実行）

```bash
crontab -e
```

```cron
0 9 * * 1 cd /home/hiroki/play/knowledge/tech/blog && bash scripts/run_weekly.sh >> logs/weekly.log 2>&1
```

```bash
mkdir -p logs
```
