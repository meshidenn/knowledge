# Paperpile Brief 2026-06-06 - Continual learning in modern Hopfield networks with an application to diffusion models

## 基本情報

- **タイトル**: Continual learning in modern Hopfield networks with an application to diffusion models
- **著者**: Ken Takeda, Masafumi Oizumi, Ryo Karakida
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: https://arxiv.org/pdf/2605.27975

## 落合陽一フォーマット

- **ひとことでいうと**: Modern Hopfield Network のエネルギーを使って、拡散モデルの継続学習で「どのサンプルが忘れられやすいか」「どのサンプルを replay すべきか」を説明・予測した論文。
- **先行研究と比べてどこがすごい？**: 拡散モデルの catastrophic forgetting を、FID や外部分類器ではなく、モデル内部の Hopfield energy landscape の変化として定式化している点。高エネルギー・外れ値的サンプルほど忘れられやすく、replay の効果も大きいという理論予測を、MHN、MHN-BM、Stable Diffusion v1.5、pixel-space DDPM で一貫して確認している。
- **技術や手法の肝はどこ？**: 忘却を `ΔE(x) = E(x|X_new) - E(x|X_old)` という Hopfield energy の上昇として定義する。等角クラスタ + 直交 outlier の可解な設定で、小さなタスク回転後に outlier 側の固定点のエネルギー上昇が cluster 側より大きいことを示す。さらに replay gain を「replay susceptibility × energy rise」に分解し、高エネルギー自己 replay が最も効くという選択基準を導く。
- **どうやって有効だと検証した？**: 理論解析に加えて、合成 MHN / MHN-BM で予測順序を確認。拡散モデルでは split CIFAR-10 を使い、Stable Diffusion v1.5 は VAE 固定・UNet fine-tuning、pixel-space DDPM は 32x32 CIFAR-10 で学習。Task 1 サンプルの Hopfield energy と、Task 2 後の reconstruction MSE が単調に対応することを確認し、top-K high-energy replay、random replay、bottom-K low-energy replay を比較している。
- **議論はある？**: 理論は「モデルが各タスク分布を十分よく近似する」場合の intrinsic forgetting に焦点を当てており、ニューラルネットの score function 学習そのものに由来する忘却は未解析。有限個の memory に制限され、記憶数が次元とともに増える場合や豊かなデータ多様体への拡張は未解決。画像以外、明示的 task boundary のない online continual learning などの検証も今後の課題。
- **次に読む/試すなら**: 
  1. 自分の diffusion fine-tuning 実験で Task 1 サンプルごとの Hopfield energy と reconstruction error の相関を測る。
  2. replay buffer を random ではなく top-K high-energy で組んで、同じメモリ予算で比較する。
  3. probability-flow ODE や時刻別 energy を使うと、より実用的な忘却指標になるか確認する。
- **キーワード**: `continual learning`, `modern Hopfield networks`, `diffusion models`, `catastrophic forgetting`, `memory replay`, `Hopfield energy`, `Stable Diffusion`, `DDPM`

## 気になったこと

- Hopfield energy を画像空間や latent 空間でどう正規化するかによって、サンプル選択がどれくらい変わるのか。
- split CIFAR-10 以外の、より実用的な domain shift や text-to-image personalization でも同じ high-energy replay が効くのか。
- reconstruction MSE ではなく、生成品質・概念保持・プロンプト追従性と energy がどこまで対応するのか。
- high-energy サンプルが単に外れ値やノイズを多く含む場合、replay が逆に性能を悪化させるケースはあるのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [takeda2026-xa-continual-learning-in-modern-hopfield-networks-with-an-app-2f9ea980.md](../../chat/2026-06-06/takeda2026-xa-continual-learning-in-modern-hopfield-networks-with-an-app-2f9ea980.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
