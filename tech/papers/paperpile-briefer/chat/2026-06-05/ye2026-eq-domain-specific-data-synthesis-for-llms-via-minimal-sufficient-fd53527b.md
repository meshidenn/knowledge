# Chat Prompt 2026-06-05

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Domain-specific data synthesis for {LLMs} via minimal sufficient representation learning

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-05 - Domain-specific data synthesis for LLMs via minimal sufficient representation learning

## 基本情報

- **タイトル**: Domain-specific data synthesis for LLMs via minimal sufficient representation learning
- **著者**: Tong Ye, Hang Yu, Tengfei Ma, Xuhong Zhang, Jianguo Li, Peng Di, Peiyu Liu, Jianwei Yin, Wenhai Wang
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 明示的なドメイン説明や手作業プロンプトなしに、参照例だけからドメイン固有の合成データを作るための DOMINO という手法を提案した論文。
- **先行研究と比べてどこがすごい？**: 既存のデータ合成は「このドメインは何か」を自然言語で記述してプロンプト設計する演繹的アプローチに依存していたのに対し、本論文は参照サンプル集合からドメイン表現を帰納的に学習する点が新しい。ドメイン特性が言語化しにくい現実的状況を対象にしている。
- **技術や手法の肝はどこ？**: DOMINO は、参照例から「最小十分なドメイン表現」を学習し、それを合成データ生成のガイドに使う。prompt tuning と contrastive disentanglement objective を組み合わせ、ドメインレベルのパターンと個別サンプル由来のノイズを分離することで、過学習を抑えつつドメインらしさを保つ設計。
- **どうやって有効だと検証した？**: PDF本文はなく、abstract ベース。暗黙的なドメイン定義が必要な coding benchmark で評価し、DOMINO が生成したデータで fine-tuning すると、強い instruction-tuned backbone に対して Pass@1 が最大 4.63% 改善したとされる。比較対象やデータセット詳細、統計的有意性はメタデータからは不明。
- **議論はある？**: PDF本文がないため詳細な限界は不明。参照例集合の質・量にどれだけ依存するか、学習された「ドメイン表現」が本当に最小十分かをどう実証するか、coding 以外のドメインで同様に効くかは確認が必要。抽象では理論的に合成分布の support 拡大を示すとあるが、仮定や証明条件はメタデータからは不明。
- **次に読む/試すなら**: 1. DOMINO の目的関数と prompt tuning の実装単位を確認する。2. 参照例数を変えた ablation を見る。3. 自分の対象ドメインで、自然言語説明ありのデータ合成と参照例のみの DOMINO 型合成を比較する。
- **キーワード**: `domain-specific data synthesis`, `LLM fine-tuning`, `minimal sufficient representation`, `contrastive disentanglement`, `prompt tuning`, `synthetic data`

## 気になったこと

- 「最小十分なドメイン表現」を何に対して十分と定義しているのか。
- 参照例が少ない、偏っている、ノイズを含む場合に DOMINO がどこまで安定するのか。
- coding benchmark 以外、たとえば医療、法律、社内文書、数理問題などでも有効か。
- 合成データの多様性向上とドメイン整合性のトレードオフをどう測っているのか。
- 生成器として使う LLM と fine-tuning される LLM が同じか別か。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
