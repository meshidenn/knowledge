# Paperpile Brief 2026-06-06 - A primer in post-training reasoning data: What we know about how it works

## 基本情報

- **タイトル**: A primer in post-training reasoning data: What we know about how it works
- **著者**: Yaoming Li, Guangxiang Zhao, Qilong Shi, Lin Sun, Xiangzheng Zhang, Tong Yang
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: https://arxiv.org/abs/2606.02113 / arXiv:2606.02113

## 落合陽一フォーマット

- **ひとことでいうと**: LLMの推論能力を伸ばすポストトレーニング用データについて、150本以上の公開研究・システム報告を整理し、「どんなデータか」「何が有用性を決めるか」「どう作るか」「どうスケールするか」を帰属可能にするためのサーベイ。
- **先行研究と比べてどこがすごい？**: データセット、RLレシピ、報酬モデル、ベンチマーク、フロンティアモデル報告に散らばっていた知見を、「prompt-responseペア」ではなく「verifier-bearing feedback interface」として再定義している点。長いCoT、難しい問題、大量データ、成功軌跡、optimizerの違いといった直感的説明を疑い、検証器・ベースモデル・系譜・scaffold・推論予算まで含めた帰属フレームに落としている。
- **技術や手法の肝はどこ？**: 推論データをドメイン別ではなく、検証契約で分類する。具体的には、プログラム実行や証明で検証できるデータ、環境との相互作用で検証できるエージェントデータ、人間/LLM judgeやrubricが必要なデータに分ける。その上で、正しさはverifier相対、難しさはbase model相対、trace品質はtrajectory相対、coverageはlineage相対だと整理する。
- **どうやって有効だと検証した？**: 新しいモデル訓練や独自実験ではなく、PDF本文では150本以上の公開研究・技術報告をレビューし、DeepMath-103K、DAPO、PRM800K、Math-Shepherd、OpenThoughts、DeepSeek-R1、Qwen3、Kimi K1.5などの事例から共通する設計変数と落とし穴を抽出している。したがって有効性はメタ分析的な整理であり、著者ら自身がレシピを再実行して性能比較したものではない。
- **議論はある？**: 限界は明確で、閉じた商用パイプライン、非公開データ混合、未公開のverifier version、compute/inference budget、contamination auditは扱えない。さらに、サーベイは形式的なメタ分析ではなく、peer-reviewed paper、arXiv、technical report、model cardが混在する。各verifierの妥当性や汚染の有無も独立検証していない。
- **次に読む/試すなら**: DeepMath-103K、DAPO、OpenThoughtsのデータ構築レシピを比較する。自分の推論データセットに対して、verifier、base pass-rate、lineage、filter、inference budgetのメタデータ表を作る。長いCoTではなく「どの時点でどの検証信号が入るか」で既存データを再分類する。
- **キーワード**: `post-training`, `reasoning data`, `RLVR`, `verifier`, `chain-of-thought`, `data lineage`, `reward model`, `LLM reasoning`

## 気になったこと

- 「verifier-bearing sample」という単位を、実際のPaperpile/Obsidian内の論文管理メタデータにどう落とすと再利用しやすいか。
- RLVRの改善が「新能力の獲得」なのか「base policy内の到達可能軌跡の強化」なのかを、最小実験でどう切り分けるか。
- エージェント軌跡では、成功ログだけでなく失敗・retry・状態差分を保存すべきという主張を、SWE-agentやtool-use評価でどう実装するか。
- closed modelの報告を含むサーベイなので、実際に再現可能なopen recipeだけに絞った二次リストが欲しい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [li2026-fk-a-primer-in-post-training-reasoning-data-what-we-know-about-ho-8c936437.md](../../chat/2026-06-06/li2026-fk-a-primer-in-post-training-reasoning-data-what-we-know-about-ho-8c936437.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
