---
title: "【日本語】Numerai Signals について雑談・質問"
category: Other Languages
url: https://forum.numer.ai/t/numerai-signals/2537
created_at: 2021-03-25T14:59:45.982000+00:00
last_posted_at: 2021-08-23T21:36:33.307000+00:00
posts_count: 6
views: 1772
tags: []
---

# 【日本語】Numerai Signals について雑談・質問

---

### Post #1 — **ageonsen** | 2021-03-25 14:59 UTC

最近Signalsを始めたので立ててみました。

Numerai Signals についてざっくばらんに語りましょう。

---

### Post #2 — **ageonsen** | 2021-03-25 15:12 UTC

現在、こちらのフォーラムを参考にしてモデルを作成しています。

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/surajp/48/2961_2.png) [Signals: Plugging in the data from Quandl](<http://forum.numer.ai/t/signals-plugging-in-the-data-from-quandl/2431>) [Signals](</c/signals/10>)

> Quandl example model: [example_model_quandl.py](<https://github.com/numerai/example-scripts/tree/master/signals/quandl>) Google Colab notebook: [Signals_Quandl_EOD_baseline.ipynb](<https://github.com/parmarsuraj99/numerai-guides/blob/master/Signals_Quandl/Signals_Quandl_EOD_baseline.ipynb>) [Quandl](<https://www.quandl.com>) is a financial, economic, alternative data marketplace which provides premium and free data. One such data source is [End of Day US Stock Prices by QuoteMedia](<https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices>) (premium, so need to set API_KEY in example_model_quandl.py). Updated daily, this data feed offers end of day prices, dividends, adjustments and splits for US publicly traded stocks with history to 1996. Prices are provided bot… 

R256 ではsklearn のGradientBoostingRegressorを用いてモデルを作成しました。以下がそのパフォーマンスです。  


[![スクリーンショット 2021-03-26 0.06.37](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/5de517770aaa0eb6888dbe512d804007d225a9d8_2_690x442.jpeg)スクリーンショット 2021-03-26 0.06.371818×1166 179 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5de517770aaa0eb6888dbe512d804007d225a9d8.jpeg> "スクリーンショット 2021-03-26 0.06.37")

  
データのノイズが多いからか、n_estimators が大きすぎるとテストデータでのパフォーマンスが悪いのが印象的でした。Tournamentでも使える知見が得られそうです。

tree の数が少ない場合にもパフォーマンスが良いとされるrotation forest がうまくワークするかも？

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0ca4b70edfa318955615a5f7df7409d69c022a89.png) [Packt](<https://www.packtpub.com/en-us/learning/how-to-tutorials/rotation-forest-classifier-ensemble-based-feature-extraction/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/94edf399330f528b1429d5cdfc70a888e5d96f0f.png)

### [Rotation Forest - A Classifier Ensemble Based on Feature Extraction](<https://www.packtpub.com/en-us/learning/how-to-tutorials/rotation-forest-classifier-ensemble-based-feature-extraction/>)

Rotation Forest - A Classifier Ensemble Based on Feature Extraction

オルタナティヴデータなどを用いることができれば面白そうですが、どうやって銘柄分集められるのかわからないでいます。

---

### Post #3 — **tit_btcqash** | 2021-03-25 15:22 UTC _(reply to #2)_

オルタナティブデータを集められれば収益の源泉になりそう、というのは分かってるのですが、そこに時間をかけるならnumerai tournamentをやった方がリターンが良さそうですよね。。

---

### Post #4 — **ageonsen** | 2021-03-25 15:26 UTC _(reply to #3)_

収益だけを目指すと確かにTournamentのパフォーマンスが良すぎるんですよねぇ。

私は将来的にSignalsのPayoutがよくなるとみて、今のうちから取り組んでいます。ゲームとしては自由度が高く、Tournamentより面白いのでやっています。うまくいけば個人的な運用にも使えそうですしね。

---

### Post #5 — **ageonsen** | 2021-03-25 15:29 UTC

オルタナティヴデータについてはこのCourseraのコースの４つ目の講座が良いかもです。

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c175b0ccf101d18f525be8ece457358086ac8a40.png) [Coursera](<https://www.coursera.org/specializations/investment-management-python-machine-learning>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/5b47e470a02d5c5e0c21ba292391b65d520a1ac4_2_690x361.jpeg)

### [Investment Management with Python and Machine Learning](<https://www.coursera.org/specializations/investment-management-python-machine-learning>)

Offered by EDHEC Business School. Enroll for free.

日本株限定になりますが、こちらの論文も気になっています。

[saa.or.jp](<https://www.saa.or.jp/journal/prize/pdf/2018_nishiie_tsuda.pdf>) [](<https://www.saa.or.jp/journal/prize/pdf/2018_nishiie_tsuda.pdf>)

### [2018_nishiie_tsuda.pdf](<https://www.saa.or.jp/journal/prize/pdf/2018_nishiie_tsuda.pdf>)

2.66 MB

---

### Post #7 — **olivepossum** | 2021-08-23 21:36 UTC _(reply to #2)_

Have not tried it yet but found an open source implementation of a Rotation Forest Classifier [GitHub - digital-idiot/RotationForest: Implementation of the Rotation Forest by Rodriques et al. 2006<](<https://github.com/digital-idiot/RotationForest>)
