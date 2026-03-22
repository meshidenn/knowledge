# HF Paper Tracker

Hugging Face Daily Papers を自動追跡し、テーマ別に分類・要約・スコアリングして Gmail に届けるシステム。

## アーキテクチャ

```
cron (ローカルPC)
  ├── fetch_papers.py      ← HF API からデータ取得（LLM なし）
  ├── claude -p "..."      ← CLAUDE.md を参照して分析（サブスク認証）
  ├── send_email.py        ← Gmail SMTP で通知
  └── git commit/push      ← 結果を papers/ に蓄積
```

- LLM呼び出しは全て Claude Code CLI 経由（サブスクリプション認証、API KEY 不要）
- 分析ロジックは `CLAUDE.md` に一元管理
- ローカルで手動実行する時も自動実行も同じ設定

## セットアップ

### 1. リポジトリを用意

```bash
git clone <your-repo-url>
cd hf-paper-tracker
chmod +x scripts/run_daily.sh scripts/run_weekly.sh
pip install requests
```

### 2. Claude Code にログイン済みであることを確認

```bash
claude --version   # インストール確認
claude /status     # ログイン状態確認
```

サブスク（Pro / Max）にログインしていれば OK。API KEY は不要。

### 3. Gmail アプリパスワードを設定

```bash
cat > .env << 'EOF'
GMAIL_ADDRESS=your@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
EOF
```

アプリパスワードの取得:
1. https://myaccount.google.com/security → 2段階認証を有効化
2. https://myaccount.google.com/apppasswords → アプリ名 `HF Paper Tracker` で作成
3. 16文字のパスワードを `.env` に記載

### 4. cron を設定

```bash
crontab -e
```

以下を追記（パスは実際の場所に置き換え）:

```cron
# 日次インテーク（平日朝9:00）
0 9 * * 1-5  cd /path/to/hf-paper-tracker && source .env && export GMAIL_ADDRESS GMAIL_APP_PASSWORD && scripts/run_daily.sh

# 週次トレンド分析（日曜10:00）
0 10 * * 0   cd /path/to/hf-paper-tracker && source .env && export GMAIL_ADDRESS GMAIL_APP_PASSWORD && scripts/run_weekly.sh
```

### 5. 動作確認

```bash
source .env && export GMAIL_ADDRESS GMAIL_APP_PASSWORD
./scripts/run_daily.sh
```

## ディレクトリ構造

```
hf-paper-tracker/
├── CLAUDE.md                    ← 設定の一元管理（@ で prompts/ を参照）
├── .env                         ← Gmail認証（gitignore済み）
├── prompts/                     ← 詳細プロンプト集（CLAUDE.mdから自動参照）
│   ├── daily_intake_prompt.md   ← 高速モード・テーマ特化モード等
│   ├── relevance_filter_prompt.md ← スコアリング詳細・比較版等
│   ├── deep_dive_dialogue_prompt.md ← Phase2-3テンプレ・テーマ別質問集
│   └── weekly_trend_analysis_prompt.md ← 運用Tips・検索ガイド
├── scripts/
│   ├── run_daily.sh             ← 日次cron エントリポイント
│   ├── run_weekly.sh            ← 週次cron エントリポイント
│   ├── fetch_papers.py          ← HF API → JSON
│   └── send_email.py            ← Gmail SMTP 送信
├── papers/
│   ├── daily/
│   │   ├── raw/                 ← 生データ (JSON)
│   │   └── 2026-03-22.md        ← 分析結果
│   └── weekly/
│       └── 2026-W13.md          ← 週次分析
└── logs/                        ← 実行ログ
```

## ローカルでの対話利用

```bash
cd hf-paper-tracker

# 論文の深掘り
claude "https://arxiv.org/abs/2403.xxxxx を深掘り分析して"

# 関連度フィルタ
claude "今週の論文に関連度フィルタをかけて"

# 週次分析（手動）
claude "今週の週次トレンド分析を実行して"
```

## PC スリープ対策

### macOS: launchd（推奨）

cron はスリープ中に動かないが、launchd はスリープ復帰後に未実行ジョブを拾う。

```bash
cat > ~/Library/LaunchAgents/com.hf-paper-tracker.daily.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.hf-paper-tracker.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>cd /path/to/hf-paper-tracker && source .env && export GMAIL_ADDRESS GMAIL_APP_PASSWORD && scripts/run_daily.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
EOF

launchctl load ~/Library/LaunchAgents/com.hf-paper-tracker.daily.plist
```

### Linux: systemd timer

```ini
# ~/.config/systemd/user/hf-paper-daily.timer
[Timer]
OnCalendar=Mon..Fri 09:00
Persistent=true
[Install]
WantedBy=timers.target
```

```bash
systemctl --user enable --now hf-paper-daily.timer
```
