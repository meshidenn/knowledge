# Paperpile Brief 2026-06-12 - Beyond uniform token-level trust region in LLM reinforcement learning

## 基本情報

- **タイトル**: Beyond uniform token-level trust region in LLM reinforcement learning
- **著者**: Renjie Mao, Xiangxin Zhou, Lvfang Tao, Yixin Ding, Yu Shi, Yongguang Lin, Yuheng Wu, Honglin Zhu, Qian Qiu, Wenxi Zhu
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: https://arxiv.org/abs/2606.10968 / PDF: https://arxiv.org/pdf/2606.10968.pdf / Project: https://hunyuan-cppo.github.io

## 落合陽一フォーマット

- **ひとことでいうと**: LLMのRLVRで使うPPO/GRPO系の一様なトークン単位trust regionを見直し、位置依存かつprefix累積を考慮するCPPOを提案した論文。
- **先行研究と比べてどこがすごい？**: PPO/GRPOはサンプルされたトークンのlikelihood ratio、DPPOはトークン分布のTV/KL divergenceを見るが、どちらも基本的に全位置で同じ閾値を使う。CPPOは「早いトークンのズレは後続全体に波及する」「prefix上のズレは累積する」という自己回帰生成の構造をtrust regionに直接入れる点が新しい。
- **技術や手法の肝はどこ？**: CPPOは通常のPPO/GRPO型のratio-advantage目的関数は保ち、更新を通すかどうかのマスクだけを変える。具体的には、早い位置ほど厳しく late token ほど緩い position-weighted threshold と、そこまでの weighted divergence 平均を抑える cumulative prefix budget を同時に満たす場合だけ更新を許す。
- **どうやって有効だと検証した？**: PDF本文によると、Qwen3系の複数設定、dense/MoE、Base/post-trainedモデルでRLVRを行い、AIME24/25/26 Avg@16を中心に比較している。比較対象はGRPO、CISPO、TRM、DPPO、MinPROなど。CPPOは4つのQwen3設定で最良のvalidation AIME24/25/26 Avg@16を達成し、Qwen3-30B-A3B-Baseでは図中で54.79という値が示されている。ただしPDF抽出テキスト由来なので、細かい表の数値は断定しすぎない。
- **議論はある？**: divergenceはTop-K reduced-TVなどの近似で計算され、完全な語彙全体のTVではない。評価は主に数学推論RLVR、Qwen3系、AIME中心なので、長文生成・コード・対話アラインメントなどへの一般化は本文からは限定的。閾値やweight floorなどのハイパーパラメータ感度は検証されているが、最適設定の理論的決定法はメタデータからは不明。
- **次に読む/試すなら**: DPPOとTRMを読んで、CPPOが「divergenceの測り方」ではなく「どこにbudgetを配るか」を変えている点を整理する。小型Qwen/数学データでGRPOにCPPOマスクだけを足す最小実験を組む。prefix budgetのログを取り、どの位置で更新が落ちるか可視化する。
- **キーワード**: `RLVR`, `PPO`, `GRPO`, `trust region`, `CPPO`, `prefix divergence`, `LLM reinforcement learning`, `AIME`

## 気になったこと

- CPPOのgainは、長いreasoning chainほど大きくなるのか。短答・短文タスクでも同じ設計が効くのか。
- position weightの形はどこまで理論式に従うべきで、実装では線形・指数・学習可能weightのどれがよいのか。
- prefix budgetで更新を止めると、探索を必要とする高entropy tokenまで抑えすぎるケースはないか。
- DPPOのTop-K reduced-TV近似を使う実装コストが、通常のGRPOに対してどれくらい増えるのか。
- FIPO、MinPRO、multi-step likelihood-ratio correction系と組み合わせると競合するのか補完するのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [mao2026-fn-beyond-uniform-token-level-trust-region-in-llm-reinforcement-f802aa20.md](../../chat/2026-06-12/mao2026-fn-beyond-uniform-token-level-trust-region-in-llm-reinforcement-f802aa20.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
