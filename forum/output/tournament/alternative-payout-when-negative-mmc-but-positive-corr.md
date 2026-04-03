---
title: "Alternative payout when negative MMC but positive CORR"
category: Tournament
url: https://forum.numer.ai/t/alternative-payout-when-negative-mmc-but-positive-corr/594
created_at: 2020-07-01T07:17:30.794000+00:00
last_posted_at: 2020-07-08T13:47:39.609000+00:00
posts_count: 22
views: 2412
tags: []
---

# Alternative payout when negative MMC but positive CORR

---

### Post #1 — **bor1** | 2020-07-01 07:17 UTC

> Can we get some variant of **“if MMC < 0 then min(0, max(CORR, MMC)), else MMC”** to get less burned if your CORR is better than your MMC?

So we had people ask about some variant of MMC scoring that doesn’t burn people that try to make a model that does well during burns (me included) - we just went through a phase where a CORR of 0.012 or so would get you a negative MMC of -0.033, because you are outcompeted by models that do well now, but would burn heavily during burn times. That seems unwanted behavior long-term for numer.ai, and is a strong disincentive to stake MMC with models that try to do well across all eras, as you burn when things are good, and you won’t make up for that during the shorter periods when things are bad and your model’s CORR still does consistently OK.

The above formula is quite nice in that there is no weird jumps in behavior as CORR or MMC goes above/below 0.0. What it does is that when MMC is above 0, your score is MMC. When MMC is below 0 and CORR is above 0, your score is 0. When MMC and CORR are below zero, your score is the max of the two. The last of those rules prevent the formula from having a weird jumping behavior the moment your CORR crosses to below 0, but you could tinker with that part and make it “When MMC and CORR are below zero, your score is CORR”.

---

### Post #2 — **ssh** | 2020-07-01 09:56 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/bor1/48/3286_2.png) bor1:

> Can we get some variant of **“if MMC < 0 then min(0, max(CORR, MMC)), else MMC”** to get less burned if your CORR is better than your MMC?

I could also see the logic of this. This metric would be reasonable if the tournament organizers do not want to punish too hard MMC staked models with a positive correlation, even if the models have a negative MMC score. These models will be penalized with 0 returns. Here are our current distribution of unresolved rounds for MMC vs. COR and MMC3 (as I called the new proposed metric) vs. COR:

[![COR_MMC_MMC3_r217_214b](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0fe5137c5e5ef15f5d672660ca9b3ce50884e441.png)COR_MMC_MMC3_r217_214b1200×700 21.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0fe5137c5e5ef15f5d672660ca9b3ce50884e441.png> "COR_MMC_MMC3_r217_214b")

---

### Post #3 — **of_s** | 2020-07-01 12:16 UTC _(reply to #2)_

Been ![:clap:](https://emoji.discourse-cdn.com/twitter/clap.png?v=13) saying ![:clap:](https://emoji.discourse-cdn.com/twitter/clap.png?v=13) this ![:clap:](https://emoji.discourse-cdn.com/twitter/clap.png?v=13) for ![:clap:](https://emoji.discourse-cdn.com/twitter/clap.png?v=13) months ![:clap:](https://emoji.discourse-cdn.com/twitter/clap.png?v=13)

---

### Post #4 — **wigglemuse** | 2020-07-01 15:02 UTC

The first question always is of course “Under this proposal, what happens when you submit p/1-p models?” If between the two models you get a guaranteed payout, then it is a no go. I’m just starting my first cup of coffee, so I couldn’t possibly analyze that properly right now.

I guess it is somewhat of an open question what happens to MMC scores with flipped models – do they flip symmetrically? In fact I think I will use a couple of my unstaked accounts to submit a p/1-p model right now and find out in the next few days.

Anyway, the basic scenario with a p/1-p pair is you’d have one guaranteed corr > 0 and so under such a rule mmc would be minimum 0 even if it was really < 0\. And then the other of the pair would be guaranteed corr < 0, but possibly under the right conditions could have a positive mmc. So does having one half of the pair a guaranteed no loss open up an attack? I guess the problem might be when you have a corr < 0 but with a positive mmc, then the flipped pair would get a positive corr but with a guaranteed 0 minimum mmc (and very possibly might get a positive mmc). I just don’t have a handle on whether flipped models have predictable mmc effects or not. Gonna do an experiment on that…

---

### Post #5 — **bor1** | 2020-07-01 19:51 UTC

So the question is, can you do a p/1-p with MMC. That seems to be possible, looking at my p/1-pish goodtimes and badtimes model. Here I flipped the correlation and MMC scores of the badtimes model, and overlayed it on the goodtimes model:  


[![goodandbadtimes](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/787483fae4ad5960ec1b62eade5b6b63f79b4287_2_690x317.png)goodandbadtimes1405×647 95.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/787483fae4ad5960ec1b62eade5b6b63f79b4287.png> "goodandbadtimes")

The next plot contains three lines - one is the sum of the correlations of the badtimes and goodtimes model per round. The average of these sums is slightly positive (yay! 0.0043 per round - slightly better than a strict p/1-p). If you sum mmc, it is pretty much 0.0 on average, and if you sum the mmc-deburner, you get a similar average as that of correlations (0.0034). So at least in my variant of p/1-p, the deburner isn’t a large problem, especially when you consider just submitting the example predictions will net you an insane average of 0.0246 per round in Kaz between round 168 and now.

[![pminusp](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/18191a35dd8dd08181ede392ea15d677057a03c4_2_690x312.png)pminusp1430×647 98.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/18191a35dd8dd08181ede392ea15d677057a03c4.png> "pminusp")

Here is the raw data for “badtimes,goodtimes” for rounds 172-217.
    
    
    correlation:
     ("0.0089,-0.0184" "0.0841,-0.1041" "0.0558,-0.0620" "0.0305,-0.0361" "0.0073,0.0121" "-0.0317,0.0411" "-0.0715,0.0687" "-0.0402,0.0269" "-0.0163,-0.0066" "0.0046,-0.0122" "0.0428,-0.0530" "0.0488,-0.0538" "0.0467,-0.0465" "0.0174,-0.0195" "0.0200,-0.0134" "0.0247,-0.0256" "0.0218,-0.0136" "0.0442,-0.0498" "0.0598,-0.0589" "0.0543,-0.0618" "0.0571,-0.0548" "0.0364,-0.0227" "0.0146,-0.0094" "-0.0178,0.0118" "-0.0182,0.0167" "-0.0048,0.0037" "-0.0088,0.0162" "0.0382,-0.0303" "0.0287,-0.0254" "-0.0323,0.0393" "-0.0235,0.0270" "0.0683,-0.0645" "0.1250,-0.0915" "0.0985,-0.0648" "0.0924,-0.0885" "0.0485,-0.0156" "0.0122,-0.0125" "0.0447,-0.0351" "0.0569,-0.0536" "0.1077,-0.1151" "0.0660,-0.0590" "0.0497,-0.0215" "0.0260,-0.0061" "0.0050,0.0309" "0.0066,0.0179" "0.0369,-0.0315")
    
    mmc:
    ("0.0284,-0.0321" "0.0873,-0.1189" "0.0627,-0.0730" "0.0322,-0.0417" "-0.0120,0.0253" "-0.0406,0.0512" "-0.0737,0.0778" "-0.0494,0.0330" "-0.0141,-0.0112" "0.0089,-0.0167" "0.0295,-0.0527" "0.0298,-0.0488" "0.0400,-0.0465" "0.0058,-0.0139" "0.0117,-0.0089" "0.0188,-0.0249" "0.0167,-0.0114" "0.0449,-0.0566" "0.0493,-0.0605" "0.0630,-0.0738" "0.0582,-0.0608" "0.0303,-0.0193" "0.0137,-0.0090" "-0.0073,0.0063" "0.0021,0.0062" "0.0056,-0.0021" "0.0055,0.0096" "0.0472,-0.0374" "0.0196,-0.0219" "-0.0333,0.0442" "-0.0128,0.0229" "0.0510,-0.0566" "0.0819,-0.0640" "0.0593,-0.0390" "0.0566,-0.0698" "0.0068,0.0118" "-0.0077,-0.0029" "0.0227,-0.0236" "0.0389,-0.0488" "0.1090,-0.1295" "0.0541,-0.0587" "0.0262,-0.0102" "0.0014,0.0076" "-0.0242,0.0568" "-0.0227,0.0419" "0.0073,-0.0135")

---

### Post #6 — **wigglemuse** | 2020-07-02 21:45 UTC

So I uploaded a couple of 1-p models (to my existing models) yesterday, and the results today are exactly symmetrical (opposite) on MMC as well as CORR, so I guess that answers that.

And it also means that getting positive or negative MMC are equivalently difficult, and if you were able to be consistently negative on MMC, you could just flip that model and be consistently positive. So the trick with MMC is to stay consistently on the same side of zero, same as CORR. So then is being performant on MMC exactly as difficult as being performant on CORR?

---

### Post #7 — **joakim_arvidsson** | 2020-07-03 06:34 UTC _(reply to #6)_

Interesting, thanks for doing that. I wonder if rewarding (and burning) both would make sense? I.e. CORR + MMC.

---

### Post #8 — **bor1** | 2020-07-03 08:24 UTC _(reply to #6)_

Cool. So, with a symmetrical payout, staking on both should net you 0 (either CORR or MMC). I guess we could just take a few models (integration_test, for example), fake a 1-p for it (just flipping CORR and MMC), and see how much of a risk-free benefit you get staking on both integration_test and flipped_integration_test, if the payout was **“if MMC < 0 then min(0, max(CORR, MMC)), else MMC”**.

Still think that a minor risk-free benefit (<0.005 per round) isn’t that much of a problem (people still need to rebalance stake on both accounts to keep it risk-free, making p/1-p very detectable, and 0.005 per round is just 20% of example_predictions’ average performance).The burden of policing that might be offset for Numer.ai by a larger number/focus on MMC staking.

Edit: checked a p/1-p of integration test. That would get a risk-free performance of 0.0021 with the MMC deburner enabled and constant rebalancing (versus an average performance of 0.0246 when just submitting the example predictions).

---

### Post #9 — **bor1** | 2020-07-04 09:32 UTC _(reply to #8)_

One thing that might alleviate what I find the most annoying situation (where models that are overfitting for goodtimes cause a penalty for models that do modestly well in both good and bad times), is to put a cap in the MMC calculation on CORR (say, any CORR score above 0.06 is counted as 0.06 for MMC calculation purposes).

---

### Post #10 — **of_s** | 2020-07-04 16:16 UTC _(reply to #9)_

I think the following would incentivize **`MMC`** model construction (if that’s what Numerai truly wants…):

First, MMC should be constructed directly from meta-model correlation **`(meta_corr)`** ,

**`MMC = 1 + (1 - max(0, meta_corr))^2`**

which rewards uniqueness to then be used to augment performance correlation **`(corr)`** whereby,

**`if(corr> 0) MMC * corr else min(0, corr + (MMC * abs(corr)))`**

This leads to the following situations:

  * For a negative **`corr`** and 0 **`meta_corr`** you receive a 0 score.

  * For a positive **`corr`** and 0 **`meta_corr`** you receive double the **`corr`** result.

  * For a negative **`corr`** and unit **`meta_corr`** you receive a score equal to the negative **`corr`** result.

  * For a positive **`corr`** and unit **`meta_corr`** you receive a score equal to the positive **`corr`** result.




Burns are lessened and potentially eliminated for offering unique models. Further, unique positive models are rewarded up to double as currently offered.

---

### Post #11 — **wigglemuse** | 2020-07-04 16:35 UTC _(reply to #10)_

Would that incentivize uniqueness to the point of just randomness? Must think about that. If MMC relies only on meta_corr, that’s something we can backtest right now with available information. Somebody break out the graphs.

---

### Post #12 — **joakim_arvidsson** | 2020-07-04 20:14 UTC _(reply to #11)_

That’s my main worry. CORR + MMC is simple and non-gamable, and why I like it.

---

### Post #13 — **of_s** | 2020-07-05 03:43 UTC _(reply to #11)_

It’s highly unlikely that randomness (if you could get it purely orthogonal to meta model to maximize **`MMC`**) would generate a result consistently greater than example predictions. Remember, the model still has to perform, regardless of uniqueness multiplier!

---

### Post #14 — **wigglemuse** | 2020-07-05 15:04 UTC _(reply to #13)_

Doesn’t have to be better than the examples, just would have to make money. Have to make sure there isn’t a risk-free attack vector there.

---

### Post #15 — **of_s** | 2020-07-05 15:26 UTC _(reply to #14)_

The expectation is 0 from randomness.

Incorporating the fixed costs mentioned of ~ 0.01, will further deteriorate any possible systemic gains from random submissions.

How else do you propose to reward and incentivize unique alpha? Because the current iteration of MMC is not accomplishing that!

---

### Post #16 — **wigglemuse** | 2020-07-05 17:42 UTC _(reply to #15)_

Costs are not paid by the users, not sure why that would be relevant. (Just as the performance of the examples are not.) Neither is whether the current system is any good or not, or even the system you propose. Outside of the one issue I am speaking of anyway, namely “Is it attackable?” Maybe it isn’t, but clever attacks are usually non-obvious to me.

You are giving direct value to uncorrelatedness from the metamodel. If you can get zero meta_corr, you are guaranteed zero loss for that submission. Even with a negative CORR, right? And if you get a positive CORR, you get paid CORR * muliplier.

So you while you probably can’t squarely hit zero meta_corr, maybe you could get close to zero and downside risk would be very minimal. And then you could randomly hope to get a positive corr with your near-zero meta_corr and get paid with a multiplier. And you could submit several different ones of these each week hoping to eek out a basically risk-free percent or two. Your scheme _sounds_ asymmetric to me (as there is no multiplier on the downside) where randomness could give you a slight edge, which might make it attackable. Somebody needs to run simulations on that unless you can analytically demonstrate that it is not attackable like that or in some similar way. ( I can go run such simulations, but if it can be proven that it is not needed, then I won’t bother.)

ANY proposal needs to pass that test, that’s all I’m saying. Lots of them sound reasonable until you play around with it and realize they’d be giving away free money and it isn’t going to work.

---

### Post #17 — **of_s** | 2020-07-05 17:50 UTC _(reply to #16)_

They were giving free money for the leaderboard bonus which originally MMC was supposed to replace (this was asymmetric)…now essentially they are giving free money for example predictions!

If you are going to incentivize unique orthogonal performance, then yes, any sufficiently uncorrelated model will provide a tailwind, however, if you require the 0.01 barrier coupled with a 0 expectation from pure randomness, then it is a losing proposition long term for such unwanted behavior.

---

### Post #18 — **wigglemuse** | 2020-07-05 18:19 UTC _(reply to #17)_

Leaderboard bonus was not free money – you had to earn it with sustained good performance (ranking). And the example predictions are a good model, but they are a just a model like any other with the same risks attached – it is not guaranteed to do well, it just does tend to do well (right now).

Neither involves uploading garbage predictions that don’t really predict anything and are not helpful to the metamodel in any way AND getting paid for it. That’s an attack – earning a leaderboard bonus or betting on the examples is not an attack.

It seems like you are letting your hatred of the current MMC system sway your judgement of alternatives. I am not defending the current system, or even thinking about it here. Pretend there is no current MMC system – it is not relevant to whether a new proposal is workable or good or bad or attackable. Anything attackable will be attacked, and so that’s a serious flaw if it exists, and that would likely be enough to prevent its adoption. So are you saying that making an non-attackable MMC system (that incentivizes the right things) is impossible and they just need to suck it up and ban accounts they think are abusing their privileges? Which is basically what they did before in theory if not it practice (previous attackers made a fortune and are still active users in some cases), but it really seems like they want to get away from that and go with “code is law” if they can manage it.

Now come on, you know what an attack is really. And “the current system sucks” is not an argument for any particular alternative, only that there should be one. So any proposal has to be vetted and run the gauntlet of exploring potential problems so it too doesn’t need to be replaced shortly after adoption. So welcome to the vetting process, nothing personal. Is your proposal worth advocating for, or is maybe Mike’s idea of CORR+MMC better, or your or bor’s more simplified ideas about MMC should never be 0 with positive CORR (without multipliers, etc). We need to analyze (and probably simulate) the logical consequences of any proposal and hash these things out. Going straight into implementation of not-fully-thought-out systems is the reason we keep having to keeping changing them after all…

---

### Post #19 — **of_s** | 2020-07-05 18:42 UTC _(reply to #18)_

I don’t hate MMC, it was a legitimate first step to incentivize behavior beneficial to Numerai long term, in fact I’ve staked exclusively on it because you cannot let perfect be the enemy of good when there are countless trade-offs that have to be made.

But it’s time to admit defeat for the current MMC and merely adding it to CORR can offset and eliminate a profitable model with a negative MMC. This is far more egregious than a tailwind from orthogonality to the meta-model (type I vs. type II error consideration). This is not “a sway in my judgement,” but a documented result people are experiencing with less correlated to meta-model and positive performance.

Long term consistent lower volatility models are exceptionally helpful to the meta-model, but the current version of MMC does not reward this across eras as others have pointed out as well. Again, define the specific objective you want to incentivize, in this instance, unique alpha, not unique alpha with moving goalposts across eras.

Again, uploading random predictions with the cost barrier Richard identified of ~0.01 is a losing proposition that does not seem vulnerable long term. Every proposal and implementation thus far has been replaced within months, and nowhere have I said this should be implemented without testing, nor did I mention anything about “banning accounts”. It’s easy to point fingers, but it should be accompanied by a viable solution. Please refrain from misquoting or misrepresenting what I’ve stated, thanks.

---

### Post #20 — **wigglemuse** | 2020-07-05 18:54 UTC _(reply to #19)_

Ok, well I tried anyway.

---

### Post #21 — **jrb** | 2020-07-08 12:46 UTC _(reply to #18)_

[@wigglemuse](</u/wigglemuse>) Leaderboard bonus was (still is until it goes away in September) free money (perhaps, easy money would be more articulate), regardless of how you spin it. And I say this as someone who has [benefited](<https://numer.ai/ethr>) from that scheme, albeit not by submitting tweaked example predictions.

Sure, example predictions is just another model. But, how many of your models (or mine for that matter) have the consistent public track record that [integration_test](<https://numer.ai/integration_test>) has? Especially in the light of what you [said](<https://community.numer.ai/channel/general?msg=kZMtQDzo89ZhiMY96>) on rocket chat yesterday (that you shuffle models around every week). With that prior, staking on example predictions is a lower risk strategy than staking on a new novel model that one would’ve built. Leaderboard bonus only exacerbated that problem. And to state the obvious MMC is a genuine attempt at ameliorating that problem.

Also, the proof is in the pudding. I’ve seen a few high stakes accounts with novel models switch to submitting example predictions (or tweaked versions of it) after suffering a couple of rounds of burns. I’m not going to name them here, it’s quite easy to spot them from the daily scores. Is this switching behavior not indicative of what people percieve to be the lower risk strategy?

---

### Post #22 — **wigglemuse** | 2020-07-08 13:47 UTC _(reply to #21)_

Yeah, it is definitely lower-risk. But it is not an _attack_ – it is not a mathematical scheme worked out so that it is nearly impossible to lose. That’s what I mean by “free money”, like actually free. Purposely opening up such an loophole (attack vector) when one of the reasons they are getting rid of the bonuses is to close an existing loophole (that madmin was using) is probably not something they are going to go for, right? That’s my entire point with the free money thing. So yes, there is a distinction between easy money and free money, and legit models and attack schemes.
