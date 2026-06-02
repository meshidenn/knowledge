# Chat Prompt 2026-06-02

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- {GrepSeek}: Training Search Agents for Direct Corpus Interaction

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-02 - GrepSeek: Training Search Agents for Direct Corpus Interaction

## 基本情報

- **タイトル**: GrepSeek: Training Search Agents for Direct Corpus Interaction
- **著者**: Alireza Salemi, Chang Zeng, Atharva Nijasure, Jui-Hui Chung, Razieh Rahimi, Fernando Diaz, Hamed Zamani
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: LLM検索エージェントに、事前構築インデックスではなくコーパスへ直接シェルコマンドを発行して証拠を探させる Direct Corpus Interaction 型検索エージェント GrepSeek を訓練した論文。
- **先行研究と比べてどこがすごい？**: 既存の検索エージェントが自然言語クエリやキーワードをretrieverに投げ、事前計算された文書表現インデックスからランキングを受け取るのに対し、GrepSeekはコーパス自体を探索環境として扱う。7つのオープンドメインQAベンチマークで全体として最良の token-level F1 と Exact Match を達成したとされる。
- **技術や手法の肝はどこ？**: 大規模コーパス上でRLを直接回す不安定さを避けるため、二段階訓練を使う。まず answer-aware Tutor と answer-blind Planner で検証済みかつ因果的に根拠づけられた検索軌跡を作る。次に Group Relative Policy Optimization, GRPO, で直接コーパス操作を通じた検索方策を改善する。さらに、シェルベース検索を最大 7.6 倍高速化する、意味保存かつ byte-exact な sharded-parallel execution engine を導入する。
- **どうやって有効だと検証した？**: 7つのオープンドメイン質問応答ベンチマークで評価し、token-level F1 と Exact Match を比較している。比較対象の詳細、各ベンチマーク名、アブレーションの有無はメタデータからは不明。
- **議論はある？**: 純粋に語彙的なコーパス操作は、表層形のずれが大きいクエリで限界があると分析されている。つまり、同義語・言い換え・抽象的推論が必要な検索では、既存の意味ベースretrievalを補完する位置づけになりそう。再現性、コマンド空間の制約、セキュリティ、実行コストはメタデータからは不明。
- **次に読む/試すなら**: arXiv本文を探して、実際に許可されるシェルコマンド空間とプロンプト/報酬設計を確認する。小規模QAコーパスでgrep/ripgrepベースのエージェントを最小再現する。表層一致が弱い質問でsemantic retriever併用の必要性を検証する。
- **キーワード**: `LLM search agent`, `direct corpus interaction`, `GrepSeek`, `GRPO`, `open-domain QA`, `shell-based retrieval`, `grep`

## 気になったこと

- byte-exact equivalence を保った sharded-parallel execution engine が、どの範囲のシェルコマンドまで対応しているのか。
- Tutor が answer-aware で生成した軌跡を使うことで、実運用時の探索方策にどの程度リーク的なバイアスが入るのか。
- lexical interaction の弱点を補うために、semantic retriever とどう組み合わせるのが最も自然か。
- GRPOの報酬は最終回答品質だけなのか、検索軌跡や証拠品質も評価しているのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
