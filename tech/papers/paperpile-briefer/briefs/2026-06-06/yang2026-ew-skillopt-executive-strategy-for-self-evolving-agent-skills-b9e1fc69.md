# Paperpile Brief 2026-06-06 - SkillOpt: Executive Strategy for Self-Evolving Agent Skills

## 基本情報

- **タイトル**: SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- **著者**: Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: https://arxiv.org/abs/2605.23904 / PDF: https://arxiv.org/pdf/2605.23904.pdf / Code: https://aka.ms/SkillOpt

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェントの「スキル文書」を、重み更新ではなくテキスト空間上で訓練対象として扱い、実行ログから検証付きで改善する最適化手法 SkillOpt を提案した論文。

- **先行研究と比べてどこがすごい？**: 手書きスキル、一発生成スキル、自己修正型スキル、TextGrad、GEPA、Trace2Skill、EvoSkill などに対して、スキル編集を「制御された訓練ループ」として定式化している点が新しい。6ベンチマーク、7ターゲットモデル、3実行ハーネスの52条件すべてで最良または同率最良と報告している。GPT-5.5では no-skill から direct chat 平均 +23.5、Codex loop +24.8、Claude Code +19.1 ポイント改善したとされる。

- **技術や手法の肝はどこ？**: 凍結されたターゲットモデルに現在の skill document を与えてロールアウトし、その成功・失敗軌跡を別の optimizer model が解析する。optimizer は add/delete/replace 形式の局所編集を提案し、テキスト版 learning rate として編集数の上限を設ける。候補スキルは held-out validation で現在スキルを厳密に上回った場合だけ採択され、却下編集は rejected-edit buffer として次回以降の負例に使う。さらに epoch-wise slow/meta update により、短期編集と長期的な手続き知識を分離している。

- **どうやって有効だと検証した？**: SearchQA、SpreadsheetBench、OfficeQA、DocVQA、LiveMathematicianBench、ALFWorld の6ベンチマークで評価。direct chat、Codex、Claude Code の3ハーネス、frontier-scale GPT から小規模 Qwen までの7モデルで比較している。ベースラインは no skill、人間作成スキル、一発LLM生成スキル、Trace2Skill、TextGrad、GEPA、EvoSkill。加えて、編集境界、validation gate、rejected buffer、slow/meta update などの ablation と、モデル間・ハーネス間・近接ベンチマーク間の transfer 実験を行っている。

- **議論はある？**: 評価結果は強いが、最適化には別の高性能 optimizer model と大量の訓練時トークンが必要で、SearchQA や DocVQA では cost per point が高い。PDF本文上では、細かい表の数値は抽出崩れの可能性があるため断定しすぎない方がよい。また、対象ベンチマークの範囲では有効でも、長期運用でスキルが環境変化やタスク分布変化にどう耐えるかは追加検証が必要。validation gate が強い分、探索が保守的になりすぎる可能性もある。

- **次に読む/試すなら**: 
  1. 公開コードで `best_skill.md` の生成ループと edit_apply_report の実装を確認する。
  2. 自分のエージェントタスクで「スキル文書 + held-out validation + bounded edit」だけの最小版を試す。
  3. GEPA、EvoSkill、Trace2Skill との違いを、編集粒度・検証方法・デプロイ時コストの観点で比較する。

- **キーワード**: `agent skills`, `text-space optimization`, `LLM agents`, `skill learning`, `validation gate`, `prompt optimization`, `Codex`, `Claude Code`

## 気になったこと

- optimizer model に GPT-5.5 のような強いモデルを使う前提が、実運用コストとしてどの程度許容されるか。
- held-out validation が小さい場合、厳密改善ゲートが偶然のスコア変動をどれだけ拾ってしまうか。
- スキルが300〜2,000 tokens程度に収まるという主張は魅力的だが、より複雑なドメインでは肥大化しないのか。
- 自分のタスクに適用するなら、まず scorer と validation split をどう設計するかが一番重要になりそう。
- 「スキル文書を訓練する」という発想は、プロンプト最適化よりも運用・監査に向いた抽象化に見える。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [yang2026-ew-skillopt-executive-strategy-for-self-evolving-agent-skills-b9e1fc69.md](../../chat/2026-06-06/yang2026-ew-skillopt-executive-strategy-for-self-evolving-agent-skills-b9e1fc69.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
