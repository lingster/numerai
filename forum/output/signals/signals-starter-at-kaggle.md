---
title: "Signals Starter at Kaggle"
category: Signals
url: https://forum.numer.ai/t/signals-starter-at-kaggle/3894
created_at: 2021-08-02T11:21:27.594000+00:00
last_posted_at: 2021-10-15T08:12:13.105000+00:00
posts_count: 7
views: 1636
tags: []
---

# Signals Starter at Kaggle

---

### Post #1 — **katsu1110** | 2021-08-02 11:21 UTC

Hi all:D

I made a starter for Numerai Signals some time ago in the kaggle platform. The purpose was to encourage more people to join the Signals. This is another Signals starter using YFinance (free) stock price data, which I also update on a daily basis as a kaggle dataset.

**NOTEBOOK**

[[NumeraiSignals] Starter for Beginners](<https://www.kaggle.com/code1110/numeraisignals-starter-for-beginners#Merge-Targets-and-Features>)

**DATASET**

[YFinance Stock Price Data for Numerai Signals](<https://www.kaggle.com/code1110/yfinance-stock-price-data-for-numerai-signals>)

Although this end-to-end notebook uses the minimal set of features and modeling techniques, it has demonstrated OK-level performance so far.

[![スクリーンショット 2021-08-02 20.17.39](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9f1a45319f71068bb714dd79afa1d643b0a05ba6_2_690x292.png)スクリーンショット 2021-08-02 20.17.391824×774 83.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9f1a45319f71068bb714dd79afa1d643b0a05ba6.png> "スクリーンショット 2021-08-02 20.17.39")

By adding more features and/or using more sophisticated modeling, you can do even better.

---

### Post #2 — **katsu1110** | 2021-10-14 11:30 UTC

I needed to change my kaggle dataset a bit to avoid the potential OOM issue. If you use my kaggle dataset for the Numerai Signals, please see the following discussion to follow what has been changed:

<https://www.kaggle.com/code1110/yfinance-stock-price-data-for-numerai-signals/discussion/278429>

Presumably all you need to change in your pipeline is to use `pd.read_parquet` instead of `pd.read_csv`.

---

### Post #3 — **autratec** | 2021-10-15 01:00 UTC _(reply to #2)_

Hi Katsu1110, thanks for sharing the code.

I am trying your code cell by cell using colab. in the cell 13, try to fetch the data from kaggle:

df = pd.read_parquet(pathlib.Path(f’{CFG.INPUT_DIR}/full_data.parquet’))

And i get error:

FileNotFoundError: …/input/yfinance-stock-price-data-for-numerai-signals/full_data.parquet

Do i miss anything at configuration section ?

thx.

---

### Post #4 — **katsu1110** | 2021-10-15 03:30 UTC _(reply to #3)_

Hi autratec,

If you use the notebook outside Kaggle, you need to place the [stock price data from yfinance](<https://www.kaggle.com/code1110/yfinance-stock-price-data-for-numerai-signals>) in your environment.

If you haven’t downloaded the data in your colab environment, download it and replace the CFG class in the notebook with your data path.

---

### Post #5 — **autratec** | 2021-10-15 03:57 UTC _(reply to #4)_

thanks for the quick reply. i have tried use API to download the yahoo data. It took me around 1HR. but still working. unfortunately, my colab was crashed in the later steps due to lack of enough resource.

I need to figure the way to reduce the memory usage. btw, can you help come out al light version of data set, like SP500, rather than whole 5K stocks prediction which is pretty heavy to those free environment. Just a thought, and hope it can work.

---

### Post #6 — **katsu1110** | 2021-10-15 04:22 UTC _(reply to #5)_

Kaggle notebook is also free, you know. You can simply run my notebook on it without problems.

When it comes to the SP500, I have another dataset for the world indices. This may be something you might be interested in.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/118093b56a670645c3cfd2bcb23ad6f97bdce749.png) [kaggle.com](<https://www.kaggle.com/datasets/code1110/yfinance-world-indices-price-data>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4b513966f2cb173817a1b1830b09a666b397f275_2_500x500.jpeg)

### [Yfinance World Indices Price Data](<https://www.kaggle.com/datasets/code1110/yfinance-world-indices-price-data>)

Daily Updates of Major World Indices (Close, High, Low, Open, Volume)

---

### Post #7 — **autratec** | 2021-10-15 08:12 UTC _(reply to #6)_

kastu1110, i have just tried Kaggle notebook. the whole script is running fine, expect the final submission session. i made some minor changes and be able to submit it. thanks again of sharing the code.
