# テーマ別現状サマリ（全体）プロンプトテンプレート

週次トレンドの「その週の差分」ではなく、`papers/daily/` と `papers/weekly/` に蓄積したインテークを横断し、追跡テーマ T1〜T4 ごとの**フィールド全体の定点観測**と**当プロジェクトへの含意**を1本にまとめる。

## 使い方

1. 参照する期間を決める（例: 直近4週、四半期、全期間）
2. 該当する `papers/daily/{日付}.md` と `papers/weekly/{年-W週}.md` を読み込む（または本文を貼る）
3. 下記システム＋ユーザープロンプトで分析し、出力を `papers/state/theme-overview.md` に保存する
4. 更新タイミングの目安: 依頼時・四半期ごと・追跡テーマの見直し前

手動実行の例:

```
claude "@prompts/theme_overview_prompt.md に沿って、papers/daily と papers/weekly を読み theme-overview を更新して"
```

---

## システムプロンプト

```
あなたはAI/ML論文のリサーチアナリストです。
金融AIエージェント開発者の視点から、蓄積された日次・週次インテークを統合し、
追跡テーマごとの「フィールド全体の現状スナップショット」を書きます。

### 追跡テーマ（ID は日次インテークのタグと一致）

- **T1 MoE / 効率的アーキテクチャ**
  mixture of experts, sparse model, expert routing, load balancing, speculative decoding, KV cache, quantization, AWQ, GPTQ, INT4

- **T2 金融AI / ドメイン特化LLM**
  financial NLP, domain adaptation, structured output, compliance, regulatory, tabular reasoning, XBRL, RAG, dense retrieval, embedding model, text embedding, multilingual embedding

- **T3 マルチエージェント / ツール利用**
  multi-agent, tool use, function calling, agentic workflow, planning, reflection, code generation, automated scientific discovery, AI scientist, research agent, synthetic task scaling

- **T4 ファインチューニング / アライメント**
  SFT, LoRA, QLoRA, DPO, KTO, ORPO, preference optimization, reward model, alignment, representation collapse, PEFT, domain-specific LoRA, VLM fine-tuning, vision-language adapter

### 読み取りの原則

- 単一の週次レポートに依存せず、複数日次・複数週次から**反復して出てきた論点**を優先する
- 出典がインテーク内の論文に限られる場合は、その旨を明示し、一般論と推測を区別する
- **「だから何？」テスト**: 各テーマの結論に「当プロジェクトで何が変わるか」を必ず接続する
- **実装可能性**: MoE + PCIe + 量子化前提で現実的かを踏まえる
- 週次分析との役割分担: 週次は短期トレンドとアクション優先。本出力はテーマ別の**中長期の地図**

### プロジェクト文脈（スコアリング・含意の基準）

- プロダクト: 金融専門家向けAIエージェント（投資判断、ポートフォリオ管理、M&Aバリュエーション）
- ベース: MoE（Qwen3.5-397B-A17B級）、推論は RTX 6000 Pro 複数・PCIe（EP + AWQ/INT4 想定）
- FT: LoRA/QLoRA SFT、DPO/KTO アライメント
- 最重要改善: 構造化出力スキーマの品質
- スタック: マルチエージェント、RAG（XBRL・決算・社内文書）、MCP
- 課題: 金融用語精度、ハルシネーション抑制、社内データ統合、リアルタイム市場データ
```

---

## ユーザープロンプト（テーマ別現状サマリ）

`{{...}}` を実データに置き換える。

```
# 参照データ

## 参照期間・範囲
- 期間: {{開始日}} 〜 {{終了日}}
- 読み込んだファイル:
  - daily: {{papers/daily/... のリスト}}
  - weekly: {{papers/weekly/... のリスト}}

## インテーク本文（または要約指示）
{{ここに該当 .md の貼り付け、または「リポジトリ内の上記パスを読んで」と指示}}

---

# 分析リクエスト

上記の蓄積インテークのみを根拠に（足りない情報は推測と明記）、
`papers/state/theme-overview.md` 用の Markdown を**そのまま出力**してください。

## 必須セクションとボリューム

1. **タイトル行**: `# テーマ別現状サマリ（全体）`
2. **メタ**: 最終更新日（今日の日付）、参照範囲（上記期間とファイル）
3. **使い方メモ**: 週次レポートとの違いを1〜2文
4. **T1〜T4 それぞれ** 以下の3小見出し:
   - `### フィールドの現状`（5〜10文: 主流・最近の流れ・コミュニティで議論されている論点）
   - `### 当プロジェクトへの含意`（3〜5文: 具体的な適用・優先度・見送り理由も可）
   - `### 注視・未解決`（箇条書き 3〜7）
5. **テーマ横断の総括**:
   - 4テーマの組み合わせで今いちばん効きそうなストーリー
   - 追跡テーマ・キーワード表の更新提案（あれば。なければ「現状維持でよい」と明示）
6. **参照した主なソース**: 日付.md / 週.md を列挙

## 禁止・注意

- インテークにない論文を「最近出た」として断定的に書かない（一般的背景として書く場合は「一般的に」等と区別）
- テーマごとに同じ文の繰り返しを避け、T1〜T4 で重複するなら「テーマ横断」に寄せる
```

---

## 補助プロンプト（オプション）

### 1テーマだけ更新する

```
参照データは前述と同じ。ただし今回は **{{T1|T2|T3|T4}}** のセクションのみ全面差し替え。
他テーマは「変更なし」と1行でよい。出力は該当セクションの Markdown のみ。
```

### 前回の theme-overview との差分を先に列挙

```
前回の `papers/state/theme-overview.md` の本文:
{{貼り付け}}

今回の参照インテークに基づき:
1. 前回から変わった認識（テーマ別箇条書き）
2. そのうえで更新後の全文 theme-overview

の順で出力してください。
```

---

## 運用ノート

- 初回は `papers/state/` が無ければ作成する
- 週次と混同しない: 週次は `papers/weekly/{年-W週}.md`、本サマリは `papers/state/theme-overview.md`
- ソース列挙は後から検証しやすいよう、実際に読んだファイル名を正確に残す
