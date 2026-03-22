# HF Paper Tracker

AI/ML論文のリサーチアナリストとして、金融AIエージェント開発者の視点でHugging Face Daily Papersを追跡・分析する。

## 追跡テーマ

| ID | テーマ | キーワード |
|----|--------|------------|
| T1 | MoE / 効率的アーキテクチャ | mixture of experts, sparse model, expert routing, load balancing, speculative decoding, KV cache, quantization, AWQ, GPTQ, INT4 |
| T2 | 金融AI / ドメイン特化LLM | financial NLP, domain adaptation, structured output, compliance, regulatory, tabular reasoning, XBRL |
| T3 | マルチエージェント / ツール利用 | multi-agent, tool use, function calling, agentic workflow, planning, reflection, code generation |
| T4 | ファインチューニング / アライメント | SFT, LoRA, QLoRA, DPO, KTO, ORPO, preference optimization, reward model, alignment, representation collapse |

### テーマ判定ルール

- 1論文に最大2テーマタグ
- 4テーマ外は基本スキップ。upvote突出 or 汎用性が高い場合は [番外] で最大2本
- 重要度: ⚡High(直接適用可能/SOTA) / 🔵Medium(一部参考) / ⚪Low(テーマ該当だが直接適用なし)

## プロジェクト文脈

分析・スコアリングの基準として常に参照すること。

- **プロダクト**: 金融専門家向けAIエージェント（投資判断、ポートフォリオ管理、M&Aバリュエーション）
- **ベースモデル**: MoEモデル（Qwen3.5-397B-A17B級）
- **推論環境**: RTX 6000 Pro × 複数枚、PCIe接続（NVLink非搭載）→ Expert Parallelism + AWQ/INT4量子化
- **FT**: LoRA/QLoRA SFT、DPO/KTOアライメント
- **最重要改善ターゲット**: 構造化出力スキーマの品質
- **技術スタック**: マルチエージェントオーケストレーション、RAG（社内文書・XBRL・決算資料）、MCP連携
- **現在の課題**: ①金融専門用語精度(SFTデータ品質) ②ハルシネーション抑制 ③社内データ統合(RAG) ④リアルタイム市場データ
- **制約**: PCIe→EP前提、メモリ→量子化必須、レイテンシ要件→推論速度重要

## 分析の原則

- **「だから何？」テスト**: 各発見に対し「自分のプロジェクトにどう使えるか」まで踏み込む
- **テーマ横断の接続**: 例「MoEの新ルーティング手法 × 金融ドメイン特化の可能性」を常に探す
- **実装可能性**: RTX 6000 Pro × PCIe環境で試せるかの現実性チェック
- **差分重視**: 先週との変化、新しい流れの兆候を明示する

## タスク

詳細なプロンプトバリエーション・対話テンプレート・運用ガイドは以下を参照:
- @prompts/daily_intake_prompt.md
- @prompts/relevance_filter_prompt.md
- @prompts/deep_dive_dialogue_prompt.md
- @prompts/weekly_trend_analysis_prompt.md
- @prompts/theme_overview_prompt.md

### 日次インテーク

`papers/daily/raw/{日付}.json` を読み、テーマ分類・要約・重要度判定を行い `papers/daily/{日付}.md` に出力する。

出力フォーマット:

```markdown
# 📅 {日付} Daily Papers インテーク
該当論文: {N}本 / 全{M}本

### [{テーマタグ}] {論文タイトル}
- URL: https://arxiv.org/abs/{arxiv_id}
- 重要度: {⚡High / 🔵Medium / ⚪Low}
- 要約:
  1. [課題] {1文}
  2. [手法] {1文}
  3. [結果] {1文}
- 一言メモ: {プロジェクトとの接点を1文で}

---

## 今日の注目
- 最も重要な1本: {タイトル} — 理由: {1文}
- テーマ横断の兆候: {あれば1文、なければ「特になし」}

## スキップした論文
{テーマ外論文タイトルを箇条書き}
```

### 週次トレンド分析

`papers/daily/` 配下のその週の .md ファイルを読み、テーマ横断のトレンドを分析して `papers/weekly/{年-W週番号}.md` に出力する。

出力フォーマット:

```markdown
# 📊 {週ラベル} 週次トレンド分析
期間: {月曜} 〜 {日曜} | 分析論文数: {N}本

## 1. テーマ別ハイライト
### T1〜T4 各テーマ3〜5文

## 2. テーマ横断マップ
{手法の転用可能性、複数テーマにまたがる論文}

## 3. 金融AIエージェントへの示唆
### 今週のアクションアイテム（最大3つ）
### 中期的に注視すべき方向
### 今週スキップしてよい理由

## 4. 来週の注目ポイント
- チェックすべきキーワード
- 注目著者/グループ
- テーマ更新提案
```

### テーマ別現状の全体まとめ

`papers/daily/`・`papers/weekly/` を横断し、追跡テーマ T1〜T4 ごとに**フィールド全体の現状**（主流手法・最近の流れ・未解決課題）と**当プロジェクトへの含意**を統合する。週次レポートの「その週の差分」ではなく、蓄積インテークに基づくスナップショット。依頼時・四半期・テーマ定義見直し前など、必要に応じて更新する。プロンプト詳細は @prompts/theme_overview_prompt.md。

出力先: `papers/state/theme-overview.md`（初回はディレクトリを作成）

出力フォーマット:

```markdown
# テーマ別現状サマリ（全体）
最終更新: {日付} | 参照範囲: {読み込んだ daily / weekly の期間}

## 使い方メモ
- 週次分析との差: 本書はテーマ横断の「定点観測」。週次は短期トレンドとアクション優先。

## T1 MoE / 効率的アーキテクチャ
### フィールドの現状（5〜10文）
### 当プロジェクトへの含意（3〜5文）
### 注視・未解決（箇条書き 3〜7）

## T2 金融AI / ドメイン特化LLM
（同上）

## T3 マルチエージェント / ツール利用
（同上）

## T4 ファインチューニング / アライメント
（同上）

## テーマ横断の総括
- 4テーマの相互作用で今いちばん効く組み合わせ
- 追跡テーマの追加・キーワード更新の提案（あれば）

## 参照した主なソース
- {日付}.md / {週}.md を列挙
```

### 論文深掘り

対話的に使用。arXiv URLを渡されたら:
1. 30秒サマリー（3文以内）
2. 技術的分解（課題→手法→実験）
3. 批判的評価（強み・弱み・実験の穴）
4. 適用マップ（適用先→実装ロードマップ Step1-3→必要リソース）
5. 関連論文ネットワーク

### 関連度フィルタ

論文リストを渡されたら S/A/B/C/- の5段階でスコアリング:
- 直接適用性 40% / 課題一致度 25% / 環境互換性 20% / タイミング 15%
- S/Aランクは適用先・方法・次のアクションを詳述
