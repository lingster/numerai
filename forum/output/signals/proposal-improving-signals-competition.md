---
title: "[Proposal] Improving Signals Competition"
category: Signals
url: https://forum.numer.ai/t/proposal-improving-signals-competition/5218
created_at: 2022-04-06T00:31:34.317000+00:00
last_posted_at: 2022-04-21T17:59:27.628000+00:00
posts_count: 6
views: 1263
tags: []
---

# [Proposal] Improving Signals Competition

---

### Post #1 — **katsu1110** | 2022-04-06 00:31 UTC

This topic might have been discussed before, but as one of the Signals participants, I would like to stress what I think how Signals can be improved.

Currently most of the top submissions seem to be based on my Signals starter:

[[NumeraiSignals] Starter for Beginners](<https://www.kaggle.com/code/code1110/numeraisignals-starter-for-beginners>)

This is apparently not great given that the original intention to introduce Signals was to reward participants with unique data. The abovementioned starter uses the imcomplete yfinance data, which is apparently not unique (I am afraid that the volatility in performance in Signals is derived from this incompleteness with the yfinance data).

This situation is understandable, given that Signals reward participants who cover most of the ticker universe. It is very very hard to get consistent and yet unique data for all the ticker universe.

How can we improve Signals then?

I think Signals should have an evaluation metric limited to particular country or industry.

For example, I am Japanese, and I should have an access to rich data related to the Japan stock market. As this new kaggle competition begins, JPX (Japanese stock exchange) is very willing to provide rich data via API to users.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/37a98e1838181621919a052a67b4ceedfd2bf98f.png) [kaggle.com](<https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d31feefbdcdc1b124d6c2f6b07cfa6c6e612e2a7.png)

### [JPX Tokyo Stock Exchange Prediction](<https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction>)

Explore the Tokyo market with your data science skills

But I cannot have something similar from US or Korea.

So even though my data about Japan might be rich, I would not be able to use them for Signals. How unfortunate.

Numerai community is now very international, so Signals might want to leverage that by collecting unique submissions about particular country or industry. The job for Numerai is to ensemble them nicely to cover all the universe.

This approach might have a potential to improve the meta model much further as it now accepts all the niche but rich unique data from Signals.

Thanks

---

### Post #2 — **richai** | 2022-04-09 04:10 UTC

I like it but how do we do it?

Suppose you predict on 500 Japanese stocks only. How should we score you vs someone who predicted on all 5000 stocks? 500 predictions is less valuable to us but still valuable but if someone is predicting whole universe it feels like they should be able to earn more which is why we fill with 0.5s any missing stocks and score you both the same.

---

### Post #3 — **katsu1110** | 2022-04-11 09:50 UTC _(reply to #2)_

I was thinking about simply limiting the universe for scoring: if I understood correctly, when Numerai One wants to long a stock in Japan, it has to short something within Japan to build a safe LS position. If this is correct, local signal (may work only in Japan) may be still useful for Numerai, and calculating corr or mmc only using Japan stocks should be possible.

I understand that for Numerai things are easier if users predict all the stocks, and if missing, the median fill is performed. Maybe in the end Numerai does not need such ‘local signal’ I proposed.

But still, how about giving feedback about localized scores (e.g., score for only US stocks etc) to users?

If, for example, there is a guy who is extremely good at predicting US stock returns but very bad at doing so for Asian stocks, he may not earn much in Signals at the end of the day. He may leave. But if those localized scores are given, he can realize his weakness in his portfolio, and he may be able to find someone who is good at Asian stocks but not good at US ones in the rocketchat. Then they can start to collab. They can now submit great signals covering most of the universe and earn a lot in Signals, and Numerai can also benefit from them and improve its meta model.

…Yeah I guess the last half of my argument may be a fairly tale, but in my book giving feedback about localized scores seems to be a step to improve Signals. If everyone is using yfinance or something similar that Numerai already has, I am afraid that Signals may end up with being an impoverished version of the Tournament.

---

### Post #4 — **richai** | 2022-04-11 17:25 UTC _(reply to #3)_

I think a lot of this gets solved with True Contribution on Signals. We are experimenting with versions that don’t fill in 0.5s before doing True Contribution and other versions that don’t. We should be close to a decision on this in a few months.

---

### Post #5 — **elay_ai** | 2022-04-12 02:13 UTC

Hi, I think using the same data doesn’t break the spirit of Signals. You can make an original signal based on some trading strategies or by calculating directly more advanced features based on maths models. but yes I was convainced by others in fact that yahoo data is not good enough. plus it is hard for peaple to get unique alternative data…

---

### Post #6 — **jrai** | 2022-04-21 17:59 UTC _(reply to #4)_

Neutralization should also be done _before_ filling NaNs with 0.5s in Signals for normal correlation scoring. If someone submits 10 stocks, the other 4990 stocks are filled with 0.5 and then the neutralization happens, the submission is way more representative of the neutralization process (the performance of the linear combination of Numerai’s features that we’re neutralized against) than it is representative of the initial 10 stocks the person submitted.

I think it would be helpful to get a UNC score so we can see the overall influence that neutralization is having on the raw correlation scores across different model types. IC was also a great addition and I’m sure TC will be interesting too.
