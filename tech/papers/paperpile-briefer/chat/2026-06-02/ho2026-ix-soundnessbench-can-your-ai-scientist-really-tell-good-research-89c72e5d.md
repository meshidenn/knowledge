# Chat Prompt 2026-06-02

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- {SoundnessBench}: Can your {AI} scientist really tell good research ideas from bad ones?

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-02 - SoundnessBench: Can your AI scientist really tell good research ideas from bad ones?

## 基本情報

- **タイトル**: SoundnessBench: Can your AI scientist really tell good research ideas from bad ones?
- **著者**: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: AI研究エージェントやLLMが、研究アイデアの方法論的な健全性を事前に見抜けるかを測るベンチマーク SoundnessBench を提案した論文。
- **先行研究と比べてどこがすごい？**: 既存ベンチマークが仮説生成やレビュー全体の評価に寄りがちな中で、「計算資源を使う前に、その研究案が方法論的に成立しそうか」を評価対象にしている点。ICLR投稿から再構成した1,099件の機械学習研究提案に、reviewer soundness sub-score を紐づけている。
- **技術や手法の肝はどこ？**: 論文完成後の採否予測ではなく、proposal-stage で回収可能な soundness を測る設計。ICLR投稿をもとに研究提案を再構成し、査読者の soundness スコアと照合し、source paper に対する監査も行っている。
- **どうやって有効だと検証した？**: 12種類の frontier LLM に対して評価し、通常プロンプトでは低 soundness の提案を過大評価する optimism bias が広く見られることを示した。強めのプロンプトでは false positive が減る一方で false negative が増える傾向も報告している。
- **議論はある？**: SoundnessBench は full-paper review outcome の正確な予測ではなく、proposal-stage soundness の評価として解釈すべきと明記されている。公開コーパス汚染、論文特定フレーズ、表層特徴、人手監査品質などの交絡も検討しているが、メタデータからは各統制の詳細やモデル別結果は不明。
- **次に読む/試すなら**: SoundnessBench のデータ構成とラベル定義を確認する。自分の研究アイデア評価プロンプトで false positive / false negative の偏りを測る。AI reviewer / AI scientist 系ベンチマークとの比較表を作る。
- **キーワード**: `AI scientist`, `LLM evaluation`, `research proposal`, `soundness`, `benchmark`, `peer review`

## 気になったこと

- reviewer soundness sub-score がどの程度一貫していて、研究案単体の品質ラベルとしてどれほど信頼できるのか。
- 「aggressive prompting」が具体的にどんな指示設計なのか。
- frontier LLM 12種類のうち、どのモデルがどのタイプの誤判定をしやすいのか。
- ICLR由来の提案に偏ることで、他分野や非トップ会議の研究評価にどこまで一般化できるのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
