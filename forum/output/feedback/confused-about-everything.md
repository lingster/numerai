---
title: "Confused about everything"
category: Feedback
url: https://forum.numer.ai/t/confused-about-everything/1934
created_at: 2021-02-20T23:32:10.062000+00:00
last_posted_at: 2021-03-29T07:34:01.004000+00:00
posts_count: 18
views: 5274
tags: []
---

# Confused about everything

---

### Post #1 — **slice0bri** | 2021-02-20 23:32 UTC

![:woman_shrugging:t4:](http://forum.numer.ai/images/emoji/twitter/woman_shrugging/4.png?v=9)What is this? How does this work?

---

### Post #2 — **wigglemuse** | 2021-02-20 23:48 UTC

That’s a little vague. Try the docs: <https://docs.numer.ai/>

---

### Post #3 — **slice0bri** | 2021-02-21 00:05 UTC _(reply to #2)_

I have a coinbase account on my phone which led me here.

---

### Post #4 — **ml_is_lyf** | 2021-02-21 09:50 UTC

Lex did an interview with the founder, I think it’s all explained really well there. If you look at the timestamps there’s also a point where they just talk about NMR, if you’re mainly interested in that.

Here’s the link:

Richard Craib: WallStreetBets, Numerai, and the Future of Stock Trading | Lex Fridman Podcast

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3dc2c2e67aa8b7b3cfaa328d7124500b7f342bdc.jpeg) ](<https://www.youtube.com/watch?v=ziQSpuST6Es&t=1877s>)

---

### Post #5 — **asteeber** | 2021-02-25 20:09 UTC

NumerAI is an ongoing data science tournament where participants process NumerAI provided data and upload predictions. People stake (i.e. bet) on their predictions using NMR (NumerAI’s native token). Payouts depend on your prediction’s correlation with the real-life data (there are other payout mechanisms but those are more complicated).

NumerAI might be for you if you have a background in some/all of the following: economics, finance, data science, machine learning, data processing languages like python, panda, R, SQL, etc.

Hope this help! I’m a beginner too!

---

### Post #6 — **pock3t** | 2021-02-26 21:09 UTC

**TL;DR: getting paid in NMR is not a good incentive enough, no value if the raw signals/predictions are not shared**

On my side, the problem is not really in understanding how Numerai works (I think), but really, what’s the value?

I’m an algotrader myself, having built tons of data collectors, tried almost every possible ML/RL techniques, used statistical approaches, etc…

So, if I understood correctly, I will give signals/predictions one round after another, and … what, I get paid in monkey money = NMR? The whole purpose would be to benefit back from the aggregated intelligence of algo traders like myself participating in the leaderboard, but seems like this is a ‘luxury’ only for hedge funds to enjoy?

Another way to say it:

As long as the raw signals generated on the leaderboard are not shared, I’m clueless on why anyone would either want to stake NMRs (regular users) or spend time sending their signals/prediction to Numerai (algo traders).

Thoughts?

---

### Post #7 — **ml_is_lyf** | 2021-02-27 00:20 UTC _(reply to #6)_

I think monkey money is the wrong way to look at it. I’m assuming you’ve never come across Ethereum before? That’s what NMR is based on. I’d recommend to go read up on what Ethereum is and what it can do. I think using it in this context makes a lot of sense. As we have a staking system which is pretty similar to proof by stake. And with it being a cryptocurrency the fund doesn’t have to worry about paying people directly. Also as the fund pays out more NMR as new people join and returns compound, they’ll have to buy back more from the markets to make payouts, which will drive up the price further. Also as NMR is finite and participants burn NMR when their models perform poorly, the amount of NMR in circulation will decrease over time further driving up the price.

---

### Post #8 — **pock3t** | 2021-02-27 00:39 UTC

Very familiar with Ethereum and ERC20 based tokens like NMR is, but actually, money doesn’t even need to be involved here.

The whole value proposition of Numerai should be to share the signals, otherwise we (as algo traders participating to the leaderboard with our predictions) are just sharing the results of our hard work… to enrich hedge funds?

I’m not much into the $GME drama, but you see where I’m going: why would I agree to give my predictions to hedge funds if I can’t get access to what they have access to?

Leaving the NMR monkey money aside and how much speculation we can make out of it, it feels like this is an unbalanced deal from the ground up, in its core proposition/the way its architectured.

Sorry for the directness, European here not trying to be aggressive but not used to polish everything up neither, please change my mind ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #9 — **ml_is_lyf** | 2021-02-27 01:29 UTC _(reply to #8)_

No worries about the directness.

The way I look at it is that the fund is giving us access to data that we couldn’t afford as individuals. Even assuming we had access to some good data, I think the concept is really nice as it abstracts all the complexities of acting on our predictions, all we have to do is give them the predictions of our models each week and stake on our models. Personally I also really like how it drills the problem down to just data science, without having to worry too much about the financial domain knowledge.

Maybe it is an unbalanced deal, but from my perspective at least, they’re enabling us to do something which would be a lot harder as individuals.

---

### Post #10 — **themicon** | 2021-02-27 08:28 UTC _(reply to #9)_

It seems like you are talking past one another here. There are two sides to Numerai. There is a data science tournament and a more traditional quant platform.

In the Numerai tournament (data scientist focussed), Numerai provide the data for the data scientists to model. The data are obfuscated, so none of the data scientists can “steal” the predictions and use the algorithms they develop to make predictions on the stock market.

In Numerai Signals (quant focussed), Numerai provide the platform for trading. The hedge fund is already set up, they can trade thousands of stocks. You provide the data and predictions here. If your predictions are “unique” in some way and is very different from all other quant models, then Numerai has the infrastructure and resources to trade using your predictions and compensate you for that “uniqueness”.

Why upload your signals to Numerai instead of trading it yourself? For some people it is just much easier than having to do all this yourself (not counting all the regulatory complexities). If you think you have a signal that works on the markets and can consistently “beat” the other traders and quants, then Numerai is a way to prove that. They will give you instant feedback on how well your signals are doing compared to everyone else.

Hope that helps.

EDIT:  
As for the NMR token, the reason they use it instead of any other currency/token is because they need the ability to “burn/destroy” the token for predictions that don’t work. Anyone can upload thousands of signals and get lucky in the market with pure random guessing. This does not help the hedge fund in any way and they will be paying for nothing. If you need to stake “money” (being NMR in this case) and then have it destroyed when you are wrong or hurting the hedge fund, then that deters most of the bad actors.

---

### Post #11 — **ml_is_lyf** | 2021-02-27 09:29 UTC _(reply to #10)_

Ah yes, sorry, I went a bit off-topic in my previous post. That’s a nice summary

---

### Post #12 — **pock3t** | 2021-02-27 18:51 UTC

Interesting points, thank you for the feedbacks

---

### Post #13 — **ml_is_lyf** | 2021-03-04 18:42 UTC

[@pock3t](</u/pock3t>) Just came across this question at this timestamp in the fireside chat, seems really similar to your question <https://youtu.be/mbwMXUzPot4?t=3255> . One of the key points is that there are cases where you can get much higher returns submitting predictions as a signal and then staking on them, than trading yourself based on your signal

---

### Post #14 — **rowen40** | 2021-03-22 04:17 UTC _(reply to #5)_

Hi, i am also a beginner. I do have some background in economics and finance. At the moment i am reading and learning all about ML and Python. So far i haven’t found out how a economics and finance background can help me. Can you please point me in the right direction? Thanks!

---

### Post #15 — **senadorancap** | 2021-03-22 12:25 UTC _(reply to #14)_

1- Learn Python or R for machine learning (Udemy is all u need)

2- Pick some machine learning starter projects like titanic and mnist

3- Pick advanced projects at Kaggle, must be something that forces you to implement feature engineering, hipertunning, ensemble, etc. I do recommend: [Elo Merchant Category Recommendation | Kaggle](<https://www.kaggle.com/c/elo-merchant-category-recommendation>)

4- take notes about every concept that people are talking about in the community (forum and rocketchat), implement some of those concepts with the baseline code provided by the Numerai team

5- Numerai is about research and tries new things, the field is huge of opportunities so have fun and enjoy the process =)

---

### Post #16 — **rowen40** | 2021-03-22 12:53 UTC _(reply to #15)_

Thanks!  
This is helpfull!

---

### Post #17 — **asteeber** | 2021-03-24 19:14 UTC _(reply to #14)_

Do you have any experience with econometrics? There are modelling strategies in economic modelling that you can carry over to NumerAI: instrumenting, inter-correlation analysis, applying the intuition of the market efficiency hypothesis, etc. Here’s a really great book that you could read to ground yourself in some of the most important econometric strategies:  


[![PXL_20210324_191339572.MP](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/cd4fb87e49d12cd6d8c01044d0173f65bc92f793_2_375x500.jpeg)PXL_20210324_191339572.MP3024×4032 2.84 MB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cd4fb87e49d12cd6d8c01044d0173f65bc92f793.jpeg> "PXL_20210324_191339572.MP")

---

### Post #18 — **rowen40** | 2021-03-29 07:34 UTC _(reply to #17)_

Thanks for the tip Asteeber!
