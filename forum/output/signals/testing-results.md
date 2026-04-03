---
title: "Testing results"
category: Signals
url: https://forum.numer.ai/t/testing-results/1274
created_at: 2020-12-06T16:51:11.079000+00:00
last_posted_at: 2021-01-12T17:31:13.636000+00:00
posts_count: 9
views: 1483
tags: []
---

# Testing results

---

### Post #1 — **witloof** | 2020-12-06 16:51 UTC

I am running a test on one of my accounts: Witloof2

Last weekend I put in the following  
|bloomberg_ticker|signal|  
|AAL US|0.96|  
|AAN US|0.8|  
|ABG US|0.42|  
|ACM US|0.72|  
|ACN US|0.55|  
|ADT US|0.8|  
|AEO US|0.85|  
|AES US|0.43|  
|ALL US|0.78|  
|AMD US|0.67|  
|AMK US|0.35|  
|AMN US|0.56|  
|AOS US|0.62|

Currently my Corr is -.0049 and my mmc is -.0039

I assume the current Saturday results are for Wednesday and Thursday. (2 day lag)

Here is what the stocks did over those 2 days (the third column is the percentage change)

|AAL US|0.96||13|  
|AEO US|0.85||6.9|  
|AAN US|0.8||3.7|  
|ADT US|0.8||0|  
|ALL US|0.78||-0.1|  
|ACM US|0.72||-3.5|  
|AMD US|0.67||-0.5|  
|AOS US|0.62||0|  
|AMN US|0.56||2.9|  
|ACN US|0.55||-0.3|

As you can see, my 10 long predictions averaged 2.2%, and with weights, clearly much higher. I assume a .96 is weighted higher than a .55

|AES US|0.43||3.3|  
|ABG US|0.42||9.7|  
|AMK US|0.35||-2.2|

And my short predictions averaged up 3.6% (which is bad), but probably a bit lower given the weights (.35 having more weight than .43 on the sell side - for example)

Putting equal amounts of dollars on all 13 trades, you end up with a winning 2 days of close to 1% and probably over 1% with weighting.

My Question is 1) Am I making the correct assumptions above and 2) can I have a negative corr and mmc given these result?

---

### Post #2 — **wishingwell** | 2020-12-17 20:37 UTC

I am afraid this in’t so much of a reply, but a chance to state that I am also confused about targets.  
Looking at the signals_train_val_bbg.csv file I see that it consists of only Friday data for several tickers with each row having one of 5 target values. My assumption is that the target represents the price increase during the week relative to the market in general (is this assumption correct?)  
In order to check this assumption against real data I chose IBM to test, downloading the yfinance closing prices for both IBM and S&P 500(^GSPC). I could find no correlation between the target value for IBM and its relative performance against the S&P 500.

Am I making a mistake here in my understanding of the way the training data is built and what it represents ?

---

### Post #3 — **witloof** | 2020-12-22 16:59 UTC _(reply to #2)_

1. thanks for the response. Can anyone shed some light on why no one with any understanding of signals is chiming in here - including the people that built it?? We are just trying to get clarification on some assumptions we are making.

  2. I can add that the Friday data is used on the following wednesday, thursday, friday, monday results. FYI (not the following week)

---

### Post #4 — **smokh** | 2020-12-23 00:09 UTC

AFAIK targets are neutralized against some features

---

### Post #5 — **witloof** | 2021-01-10 00:20 UTC _(reply to #4)_

Thanks AFAIK, but I know targets are neutralized. My question is can your predictions make money and at the same time get a negative corr and a negative mmc? Even a simple yes or no would help.

---

### Post #6 — **themicon** | 2021-01-10 05:39 UTC _(reply to #5)_

No. Negative corr and mmc will give you a loss.

---

### Post #7 — **witloof** | 2021-01-10 18:34 UTC

Thanks, Thats what I thought. OK, going to try and corollate my broader results with the corr each week and see if this is the case.

---

### Post #8 — **mdo** | 2021-01-11 02:40 UTC _(reply to #5)_

I think [@themicon](</u/themicon>) may have misunderstood your question. It is definitely possible that your predictions could be directionally correct, i.e. “make money” as you say, but get a negative correlation with the target and negative MMC. This will happen if the unique component of your signal, i.e. what is left after neutralization, is in the wrong direction. In other words, you are providing a signal that is performing worse than the ones Numerai already has. I am reminded of the quote:  
“Gentlemen, today we have heard things that are new and are true. But the things that are true are not new, and the things that are new are not true.”  
The [docs](<https://docs.numer.ai/numerai-signals/signals-overview#signal-evaluation>) have more detail and please ask if you still have questions.

And you are really going to have to use more than a handful of tickers to get a good feel for your signal since you are scored on the whole universe.

---

### Post #9 — **witloof** | 2021-01-12 17:31 UTC

super helpful, Thanks mdo.
