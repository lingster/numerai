---
title: "Echelon - a Numerai portfolio"
category: Tournament
url: https://forum.numer.ai/t/echelon-a-numerai-portfolio/5400
created_at: 2022-05-14T14:00:55.809000+00:00
last_posted_at: 2023-02-11T00:37:55.708000+00:00
posts_count: 14
views: 5865
tags: []
---

# Echelon - a Numerai portfolio

---

### Post #1 — **greyone** | 2022-05-14 14:00 UTC

Hello (Numerai) world!

We’re Echelon, a father-son duo who’s been participating as a team in Numerai. We started a year ago as a team of three who submitted predictions for the Signals tournament. With the passing of our algorithm developer in January, we pivoted from Signal model development to model investing. We are currently focused on Numerai Main Tournament model portfolio investment via [NumerBay](<https://numerbay.ai/>) (Thanks, Res & CoE!).

We wanted to share a bit about our thinking, and invite you to follow along with our results (including the good, the bad and the ugly!).

Our thinking

We’ve gotten to this point through a lot of trial and error. On that path, we’ve started to define (and refine!) our beliefs. They are:

  1. We believe in the Numerai data science community. It’s one of the most knowledgeable data science communities in the world.
  2. We believe in Numerai. We’re comfortable investing our own money into a tournament where Numerai acts as the referee and the results are somewhat a black box.
  3. We believe diversification will especially benefit staking on True Contribution (TC) due to how uniquely volatile and uncorrelated TC behaves.
  4. We believe this portfolio can evolve to outperform the Numerai Main Tournament stake weighted average if we can employ insights from modelers and Numerai personnel. (This is one way that we will measure our ‘success’.)
  5. We believe that this, in turn, will improve Numerai’s meta-model (only slightly; we’re certainly not [Richie Rich](<https://en.wikipedia.org/wiki/Richie_Rich_\(film\)>)) which is good for all of us.



We certainly don’t have all the answers, and don’t pretend to. If you have any feedback on the items above, we’d love to hear it.

How you can follow along

For transparency, we are creating a common Echelon name for all of our Numerai Main Tournament slots. They’ll each contain “ECHELON_” at the beginning. Rest assured that they’ll never be our own ML predictions, but predictions that we’ve purchased via NumerBay.

Periodically, we will report on some total risk characteristics – mainly the effect of diversification. Other than a bias towards some performance persistence, we do not currently have any alpha strategies. Over time, we believe alpha strategies will arise within the Numerai ecosystem as a result of modeler and Numerai personnel interactions and insights. We believe a fund within Numerai’s ecosystem will be a natural place for risk controlled tests and implementation of these strategies.

We also believe that cross modeler ensemble investing will offer benefits to the Numerai ecosystem. Our current Numerai model selection criteria include performance, Corr correlation, modeler methods, dialogue and community reputation.

We look forward to interacting with you and developing this approach. You can find us on RocketChat at [@greyone](</u/greyone>) (aka Gerry) or @aqsmith (aka Aaron). Excited to be a part of the Numerai community and can’t wait to see what’s next.

---

### Post #2 — **restrading** | 2022-05-14 14:21 UTC

[@greyone](</u/greyone>) Thanks for sharing and for using NumerBay. I’m planning to add the following features soon to make things like this (diversification) easier:

  1. (Essential) API for bulk download of performances of all models listed on NumerBay
  2. (Optional) Leveraging the above to build a simple in-browser portfolio optimizer where users can import their own performance numbers and use the above data to select the best diversifying models to buy.



Do you have any addition / opinion on the above?

---

### Post #3 — **by256** | 2022-05-14 18:15 UTC

Thanks for doing this openly. I’ve always wondered how a mini meta model of some of the best performing models would fare. Good luck! I’ll be following the ECHELON models and look forward to updates in the forum.

---

### Post #4 — **rigrog** | 2022-05-14 20:41 UTC

[@greyone](</u/greyone>), it sounds like you might be combining the the prediction files you purchase, to produce your own ECHELON_XXX prediction files. _Rank averaging_ is one way that might be done.

Or, are you just staking on those predictions as-is? For those predictions offered on a “stake only” basis, where you don’t get any file, this would be the only way to go.

Or maybe… a little of this, a little of that? Just curious.

---

### Post #5 — **greyone** | 2022-05-15 16:50 UTC _(reply to #4)_

[@rigrog](</u/rigrog>) , our current approach staking on predictions as-is. We do not foresee us being a driver of alpha additions. We do believe we can create additional ensemble options for modelers, either separately or in collaboration with other modelers, where their predictions remain secure from us, but we offer greater diversification and return exposure.

---

### Post #6 — **aqsmith08** | 2022-05-15 19:06 UTC _(reply to #2)_

Hey [@restrading](</u/restrading>) \- Thanks for your response. Some quick feedback from me –

  1. We have some scripts to hit the [Numerai API](<https://api-tournament.numer.ai/>) to grab model information, and then do some data wrangling to estimate model value. This is definitely interesting for us, but we’re already doing some of this ourselves so I’m not sure who much we’d use it.
  2. Hm, I may have to give this one some more thought. My initial reaction is that we do this via our scripts taking into account things like model performance, model correlation to other models, NumerBay purchase fees, and other things. My sense is that we likely wouldn’t be power users of that either, but I can totally see other NumerBay buyers would find that valuable.



How’s that for my two cents?! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #7 — **aqsmith08** | 2022-05-15 19:08 UTC _(reply to #3)_

[@by256](</u/by256>) Thanks for your kind response. Excited to give this a try and we’ll definitely be updating this forum thread with results in the future. ![:crossed_fingers:](http://forum.numer.ai/images/emoji/twitter/crossed_fingers.png?v=10)

---

### Post #8 — **restrading** | 2022-05-16 00:35 UTC

[@aqsmith08](</u/aqsmith08>) thanks for the response. I understand you have your own ways to do these. I will deprioritize these for now.

However, I think it would be helpful if there’s an easy tool to generally incentivize diversification for buyers and not just performance-chasing.

---

### Post #9 — **greyone** | 2022-05-16 01:54 UTC _(reply to #8)_

[@restrading](</u/restrading>) The features you have outlined will be very helpful for the community. Competitive ecosystems inevitably foster some cat and mouse behavior…we’re not immune.

---

### Post #10 — **zwk** | 2022-05-16 08:23 UTC

[@greyone](</u/greyone>) welcome to the jungle! I think FoF will be a really cool dimension to explore in order to activate our Numerbay market place, with more “non-data-scientist” / retail inflows.

Hopefully, with appropriate lending facilities, we can also imagine to create a “hedged” staking product in the future.

---

### Post #11 — **greyone** | 2022-05-19 20:50 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0257114b54689999a8b7dae318aab0ba487b112f_2_418x499.png)image1204×1437 117 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0257114b54689999a8b7dae318aab0ba487b112f.png> "image")

  
thank you BigCreeper!!

---

### Post #12 — **qeintelligence** | 2022-05-20 11:41 UTC _(reply to #11)_

Jeejj, lets hope many will follow! Ranked 3 now, LOL this is not Financial advice and no guarantees ofcourse ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10)

---

### Post #13 — **greyone** | 2023-02-09 23:33 UTC

Echelon’s Numerai portfolio results

We are sharing the results of Echelon’s Numerbay model portfolio and some observations as they may be some benefit to the community.

Echelon ran a Numerbay-sourced Numerai model portfolio from rounds 310 to 394 (41 rounds). We had three objectives.

  1. To establish a diversified approach to model portfolio selection.
  2. To test for what we believed was performance persistence, both in Corr and TC.
  3. To evolve towards a vehicle offering lower-risk performance-sharing for modelers with modeler-driven alpha judgment inputs.



Echelon’s model selection factors for the entire Numerbay Universe each week were: daily Corr and TC performance over 12 rounds, daily PCT’s of Corr and TC (for performance consistency), Sharpe ratios of Corr and TC, Model Corr and TC correlations, and qualitative modeler judgment.

We used Numerai’s Stake Weighted Index Performance (in orange) as a primary benchmark. Here is the universe/benchmark performance over the 41 rounds:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e64312e5167b46d7ea506b5d064e0d17fd9d643b_2_600x500.png)image870×725 104 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e64312e5167b46d7ea506b5d064e0d17fd9d643b.png> "image")

Here is Echelon’s performance vs the Stake-weighted Index:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5fff07c6589d963ee43dfbb0122e02da6af33a98_2_566x500.png)image975×860 110 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5fff07c6589d963ee43dfbb0122e02da6af33a98.png> "image")

Here is a comparison of Echelon’s results versus two other Numerai portfolio approaches (Crowdcent and ATOL) over the time period that all portfolio had results for (22 rounds: 329 to 394). We chose these two portfolios because their model ensembles are significant in stake size (25% of total Numerai stake) and we highly respect their approaches. In Round 394, Crowdcent’s 12 slot 154,191 stake made up 17.5% of total Numerai stake and ATOL’s 14 slot 65,531 stake made up 7.5% of total.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3d9bc2ddc210af331f62ffd692b9973a199d886c_2_610x500.png)image975×799 132 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3d9bc2ddc210af331f62ffd692b9973a199d886c.png> "image")

Here is a relative performance chart (portfolio vs stake-weighted benchmark) that more clearly illustrates the portfolio’s “non-beta” performance.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cd96433087337b4d28a6169fcec850dfac4b3dfe_2_677x500.png)image954×704 105 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cd96433087337b4d28a6169fcec850dfac4b3dfe.png> "image")

Comments:

During the first 2/3’s of Echelon’s activities, Echelon had success in selecting models that could at least match Numerai’s Stake Weighted index. Additionally, we were happy with the diversification the portfolio was achieving. After R349, Echelon had 4 consecutive negative periods of amounts that we considered out of bounds for the portfolio’s diversification and approach. While Echelon’s absolute and relative performance surged back after R369, this performance was largely achieved by high stake concentration on Paul (and later also on Redqueen, another ricricric model). Because heavy model-specific staking was not in our original intent, we have currently stopped staking on Numerbay models.

We still believe successful portfolio approaches will (and should!) develop that can benefit the modeler community.

We will remain active in this extraordinary community/endeavor in other ways. Appreciate you all for letting us non-modelers participate in this alien venture, and a huge kudos to ResTrading for his work on Numerbay.

Gerry (greyone) & Aaron (aqsmith)  
2/9/2023

Appendix charts (for information and transparency):  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4af47c851f15a5bc71ad0c8c6d1640fca4ff6e5a.png)image561×414 31.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4af47c851f15a5bc71ad0c8c6d1640fca4ff6e5a.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/716ad0fa355ae0fcbaceac39d2447f0c7cc0e207_2_690x457.png)image714×473 60.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/716ad0fa355ae0fcbaceac39d2447f0c7cc0e207.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/daeffd8741bb47add2b5f8616588aec28f8bf65b.png)image664×471 32.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/daeffd8741bb47add2b5f8616588aec28f8bf65b.png> "image")

---

### Post #14 — **autratec** | 2023-02-11 00:37 UTC

Good job. Thanks for the update.
