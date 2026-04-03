---
title: "(Way too early) Comparison of legacy & new models"
category: Tournament
url: https://forum.numer.ai/t/way-too-early-comparison-of-legacy-new-models/4595
created_at: 2021-12-09T00:53:29.047000+00:00
last_posted_at: 2021-12-20T15:46:00.321000+00:00
posts_count: 28
views: 2421
tags: []
---

# (Way too early) Comparison of legacy & new models

---

### Post #1 — **yxbot** | 2021-12-09 00:53 UTC

Hello all:

How are you guys doing with your new models trained from the super massive dataset?  
or are you diamond handing your good old legacy models?

Now that the new dataset had been around for almost 4 months, and some of the new models have up to 10 resolved rounds under their belt, I thought it would be interesting to make some overall comparison.

Here is the comparison view of all of my legacy models v.s. new models - the first two are corr, and the last two are corr percentile

**corr (upper/lower: legacy/new)**  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/72a41726d1cd21b27f2fff2a5fdd6781ab1a70e4_2_690x437.png)image961×610 195 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/72a41726d1cd21b27f2fff2a5fdd6781ab1a70e4.png> "image")

**corr percentile (upper/lower: legacy/new)**  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cc3bddfd26fa829803ae09621d3c4c811bfe1bc7_2_690x448.png)image955×621 262 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cc3bddfd26fa829803ae09621d3c4c811bfe1bc7.png> "image")

**To be clear:** I think it is far too early to draw conclusions on any model’s performance until they have more than 20 resolved rounds but still find this interesting ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

what stands out for me for now is model performance divergency - my legacy models do tend to go up and down together, some are more stable than others, but they more or less bundle together. the new models however seem to be behaving quite differently in this aspect. For instance, for round289 my new models have more or less covered the whole spectrum, have not seen model performance spread quite so widely from my legacy bunch…

I am more or less using the same data pre-processing steps, similar algorithms, and not quite different validation setup. My guess is that the wider choice of features, and the newly available alternative targets are contributing quite heavily to this divergence.

Are you guys seeing the same phenomena?

May the burn be with you! ![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=13)

---

### Post #2 — **restrading** | 2021-12-09 01:09 UTC

Could the difference in performance (legacy vs new) be due to the difference in targets? 20D1L vs 20D2L nomi?

---

### Post #3 — **restrading** | 2021-12-09 01:10 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/yxbot/48/2906_2.png) yxbot:

> May the burn be with you!

Lol this was not how [@arbitrage](</u/arbitrage>) used to say it

---

### Post #4 — **yxbot** | 2021-12-09 01:22 UTC _(reply to #2)_

I thought both legacy and new model are 20D1L up till now?

---

### Post #5 — **restrading** | 2021-12-09 01:26 UTC _(reply to #4)_

If I understand correctly, the training target for new data is already 20D2L, but we are currently scored on 20D1L untill soon

---

### Post #6 — **gammarat** | 2021-12-09 02:51 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/yxbot/48/2906_2.png) yxbot:

> How are you guys doing with your new models trained from the super massive dataset?  
>  or are you diamond handing your good old legacy models?

I’m quite happy with the new data and have been phasing out my legacy models; the last of those I submitted 3 weeks or so ago.

Part of that is due to the size of the new data forcing me to rethink my approach, so with round 281 I took advantage of the extension to 50 models from 30 and introduced a somewhat different algorithm as well. The cumulative results are shown below:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5c14fcedf4e0343f538dd917d19353b9007967a5_2_690x199.jpeg)image1419×410 109 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5c14fcedf4e0343f538dd917d19353b9007967a5.jpeg> "image")

All but one are grey, that’s just because of the way Numerai has the colour tables set up. I have 2 parameters that govern this model, one that can take one of 4 discreet integer values, the other can take 5, which results in the clustering of the tracks. These are GammaRat 31 through 50.

Around round 285 (iirc, I don’t really keep track) I took the model above and introduced a new parameter, and replaced GammaRat 11 to 30 with that. (Those had previously used the legacy model). About half have really improved, and the rest not. But that’s ok, because it’s giving me a decent view of how these parameters interact. So I’m using that info to once again redesign the underlying algorithm. Fun and games, to be sure ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f7c154eb2759a4ba82b28d22070e5834b9c92a2b_2_690x192.jpeg)image1443×402 126 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f7c154eb2759a4ba82b28d22070e5834b9c92a2b.jpeg> "image")

GammaRat 1 to 10, my last legacy models, got dropped three weeks ago and replaced with a similar algorithm to the ones above. They don’t look great, but right now it’s too early to say for sure.

---

### Post #7 — **yxbot** | 2021-12-09 07:46 UTC _(reply to #3)_

or shall I say “may the burn be against you” ![:joy:](http://forum.numer.ai/images/emoji/twitter/joy.png?v=10)

---

### Post #8 — **restrading** | 2021-12-09 07:57 UTC _(reply to #7)_

“May the burn be in your favor™” ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #9 — **yxbot** | 2021-12-09 08:18 UTC _(reply to #8)_

oh haha I see, appropriately trademarked

---

### Post #10 — **yxbot** | 2021-12-09 08:21 UTC _(reply to #6)_

nice, interesting to see how this developed.  
I haven’t fully replicated all my modelling methods on the new dataset yet - with the newer data update coming, probably I will do more after December.

Nevertheless, after a few tough rounds, most of the legacy models seem to have recovered - some of them never suffered in the first place - so I am just happy seeing them running. I would definitely keep most of my new models at least for 20 rounds to see how they play out longer terms ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #11 — **wigglemuse** | 2021-12-09 14:13 UTC

I think a possibly underrated subject of the new data is all the new targets. I think they’ve been maybe more helpful to me than the new data itself.

---

### Post #12 — **platemort** | 2021-12-09 14:48 UTC

Do you have the cumulative scores plotted? I can’t make much out of these plots.

---

### Post #13 — **platemort** | 2021-12-09 14:54 UTC

My experience is that my legacy workflow has beat a similar workflow on the new data. I don’t have all the comparison data together to show, but yesterday my legacy model returned 4.8% and was 95 percentile on corr and mmc. My co-modeler burned -0.4% and was 40 percentile on corr and mmc. I’m not excited about being forced down the new data route.

---

### Post #14 — **yxbot** | 2021-12-09 14:56 UTC _(reply to #12)_

No not yet, good idea though, I will add that when I come to further work in my dashboard

---

### Post #15 — **yxbot** | 2021-12-09 14:59 UTC _(reply to #11)_

Yes that is one of my observations at the moment, from my point of view seems some of the new targets are more volatile than Nomi

Not sure how much they help though, probably need a longer runway to see. For now my legacy models are out performing the new ones simply by being more stable

---

### Post #16 — **yxbot** | 2021-12-09 15:00 UTC _(reply to #13)_

It is my recent rounds observation too, although I think more rounds are needed to draw any conclusions.

I don’t like being pushed to use new dataset neither. Have you tried to 300+ features they said are closely related to the legacy features?

---

### Post #17 — **platemort** | 2021-12-09 15:05 UTC _(reply to #16)_

I have not tried only using those. I didn’t realize that there was a list of features that were “closely related” to legacy features. I remember the question being asked about which features are the old features and the answer being that none are the same because of the timing differences. Is that list published or maybe I just missed it in the original announcement?

---

### Post #18 — **platemort** | 2021-12-09 15:25 UTC _(reply to #6)_

Needs fact checking but from memory the tournament 3 month avg was around 15-20% when the new data came out and is now at 7.7%. I was around 25% when it came out and now I’m at 49%. I’m assuming that the meta model is currently dominated by models on the new data set, while I have been playing it safe and sticking with my legacy model while I see how the new data performs.

Green is staked legacy, Orange is unstaked legacy experiments, Cyan is unstaked super massive.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/33be5c94554ba87b23269f7903a293bbdfb684db_2_690x200.png)image923×268 22.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/33be5c94554ba87b23269f7903a293bbdfb684db.png> "image")

---

### Post #19 — **yxbot** | 2021-12-09 17:15 UTC _(reply to #17)_

from the team’s [October Updates](<http://forum.numer.ai/t/october-2021-updates/4384>)  
under **New Feature Metadata** \- the “legacy” set

> **Legacy** : 304 of the original 310 features that were carried over to the new dataset. You can use this set to achieve nearly the same model as the legacy data.

---

### Post #20 — **platemort** | 2021-12-09 18:04 UTC _(reply to #19)_

Are we to assume that it is the first 304 features?

---

### Post #21 — **yxbot** | 2021-12-09 18:36 UTC _(reply to #20)_

from RocketChat a while ago…  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bbcef860a00476100ed4756016f8774eadc930e3_2_690x314.png)image931×425 69.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bbcef860a00476100ed4756016f8774eadc930e3.png> "image")

---

### Post #22 — **platemort** | 2021-12-09 19:32 UTC _(reply to #21)_

I remember that post. It doesn’t help though if I understood your suggestion correctly since they won’t tell us which ones are the 304 to be isolated.

---

### Post #23 — **themicon** | 2021-12-09 19:52 UTC _(reply to #22)_

The JSON file tells you which 304 features are the old “legacy” features. You should read this again: [October 2021 Updates](<http://forum.numer.ai/t/october-2021-updates/4384>)

---

### Post #24 — **aventurine** | 2021-12-10 06:41 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/825620193b2482d600c6ed7373cd2d285b9b9cae_2_690x255.png)image1274×472 44.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/825620193b2482d600c6ed7373cd2d285b9b9cae.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1a31cb5ced6851319941f24ad9c77b469687fcd5_2_690x259.png)image1266×476 44.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1a31cb5ced6851319941f24ad9c77b469687fcd5.png> "image")

Looks like two of my models on new data seem OK but can be better. The best ones so far for me are low to almost 0 proportion feature neutralized models. MMC not so hot.

---

### Post #25 — **autratec** | 2021-12-10 13:51 UTC

I have tried to loaded two versions of examples weekly, legacy vs mass , legacy performance is better.

---

### Post #26 — **platemort** | 2021-12-12 19:42 UTC _(reply to #23)_

Thanks, I missed that communication.

---

### Post #27 — **kenfus** | 2021-12-13 21:21 UTC

It seems that some new targets are indeed better for live data. I will still wait 3-4 more weeks, then change to either a single model or an ensemble model on the new data.

---

### Post #28 — **sneaky** | 2021-12-20 15:46 UTC

How hard is the new data validation set? If I apply my old pipeline from the old dataset I get model with these stats on the new validation dataset: corr 0.01 sharpe 0.4; however, the same model trained on the old dataset manages to do 2.5x better on both stats on the old validation dataset. Is the new validation dataset significantly harder or is my pipeline not easily transferable? Do you have same experience?
