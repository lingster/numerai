---
title: "Bias in the TC? - low CORR, high TC"
category: Tournament
url: https://forum.numer.ai/t/bias-in-the-tc-low-corr-high-tc/5799
created_at: 2022-10-28T07:36:14.950000+00:00
last_posted_at: 2022-10-28T18:59:12.544000+00:00
posts_count: 3
views: 616
tags: []
---

# Bias in the TC? - low CORR, high TC

---

### Post #1 — **virgo94** | 2022-10-28 07:36 UTC

Hi all,

This is my first post here. I joined the Numerai tournament almost one year ago and have two models submitted since then. One model is essentially the Numerai advanced example, which takes hours to train and evaluate, while the other is a small and simple neural network that trains in a few minutes on my laptop. Motivated by the new daily tournaments, I caught up with the recent developments of Numerai by watching the youtube videos last weekend. I understood why the hedge fund is making this change, so last weekend, I set up the automatic submission of my model predictions on Numerai Compute. I also noticed a couple of things I wanted to discuss here, hence my post.

  * Did I understand correctly that the new Numerai metamodel needs as many diverse model predictions as possible? Hence, is there a new TC score rewarding more diversity over CORR factors? I am asking this as I suddenly saw my simplistic neural network model scoring bottom rank in CORR20 to enter the 200 TC Rank. In contrast, the Numerai example model scoring higher correlation has a median/low TC (I assume everyone has a similar model submitted).
  * Does the new TC scoring system introduce any potential bias? I mean, is diversity rewarded more than correlation? What will happen, e.g. in my case, to finance the new few-dollar expenses I now have from Numerai Compute, will be to finally stack some NMR to cover the cost of the AWS fee. But this will only happen on the simple model where I have a huge TC. Besides adding variety to the Numerai metamodel, I don’t see how my model scoring extremely low correlation is helping the Numerai metamodel.



I apologise for the long post. Curious to hear your thoughts.

---

### Post #2 — **wigglemuse** | 2022-10-28 14:49 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/v/8c91f0/48.png) virgo94:

> Did I understand correctly that the new Numerai metamodel needs as many diverse model predictions as possible? Hence, is there a new TC score rewarding more diversity over CORR factors? I am asking this as I suddenly saw my simplistic neural network model scoring bottom rank in CORR20 to enter the 200 TC Rank. In contrast, the Numerai example model scoring higher correlation has a median/low TC (I assume everyone has a similar model submitted).

The metamodel has always needed diverse predictions, that’s not a change. TC is just a new way to encourage it. And TC should by its nature reward more diversity, yes, but it doesn’t technically directly oppose itself to CORR (even if that will be a side-effect for many) – it is trying to score how well your model fits in with all the other models to create the metamodel and which models they want to emphasize more and which they want to de-emphasize. (Expressed as stakes.)

Nothing has changed about the CORR scoring – if your model plummets on CORR that is because the world has changed or the current situation anyway is behaving differently – we are in a new financial environment. With CORR and especially with TC (which is much more volatile), don’t assume that the scores you get on your models now are going to be the scores you are going to get consistently forever. _ALL_ models will go up & down at times. You’ve just seen how they can change on your own models.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/v/8c91f0/48.png) virgo94:

> Does the new TC scoring system introduce any potential bias? I mean, is diversity rewarded more than correlation? What will happen, e.g. in my case, to finance the new few-dollar expenses I now have from Numerai Compute, will be to finally stack some NMR to cover the cost of the AWS fee. But this will only happen on the simple model where I have a huge TC. Besides adding variety to the Numerai metamodel, I don’t see how my model scoring extremely low correlation is helping the Numerai metamodel.

If you’re getting huge TC, then you are helping the metamodel. Models can contribute in important ways even if they aren’t great as standalone models of the market – that’s the magic of a diverse ensemble. So TC does reward diversity (as a side-effect – it isn’t scoring CORR or diversity directly), but it has to be _useful_ diversity and how useful can really only be evaluated over time – random numbers can do quite well on TC over short time-periods. “Usefulness” is what TC is directly scoring, or trying to. (Read over the technical details and discussion elsewhere – there has been a ton of it for months.)

But again, what I said earlier – everything goes up & down at times. If your CORR model has been doing consistently well for a long time and it is dipping now then it will likely recover and do decently well again but is having a rough patch at the moment. Totally normal, even in times when the present is more similar to the recent past. But we’ve entered a new situation that is in many ways dissimilar to the recent past (and even less-than-recent past). So hopefully not all our models have become useless because of very different macro environment recently, but it is certainly possible that some have/will.

---

### Post #3 — **kayeffnumeraitor** | 2022-10-28 18:59 UTC

What you are generating each round is a ranked list of stocks that Numerai can use to generate actual trades. However, Numerai cannot trade all of them, mostly because of risk constraints. It is totally possible that you can have high corr, but in the end none of the stocks that actually correlated can be traded. Also, if I understand it correctly, TC also introduces prices, so some of the rows are also weighted.

So I model TC as: randomly select a few of your predictions, generate somewhat random weights for each remaining row, and calculate a “weighted” corr (does this even exist?)
