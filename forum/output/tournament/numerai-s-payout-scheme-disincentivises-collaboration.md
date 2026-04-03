---
title: "Numerai’s payout scheme disincentivises collaboration…"
category: Tournament
url: https://forum.numer.ai/t/numerai-s-payout-scheme-disincentivises-collaboration/2726
created_at: 2021-04-06T19:08:18.651000+00:00
last_posted_at: 2021-04-09T19:49:15.700000+00:00
posts_count: 7
views: 1281
tags: []
---

# Numerai’s payout scheme disincentivises collaboration…

---

### Post #1 — **jimmy_woodford** | 2021-04-06 19:08 UTC

…and I think that’s bad for everyone.

Numerai’s uniqueness relies on the fact that they have a thousand data scientists work for them to predict the stock market, while the average hedge fund might have a few dozen. But lately, I’ve been wondering whether a thousand data scientists who compete against each other are better than a dozen who collaborate. Because, unfortunately, MMC disincentivises collaboration.

Numerai’s stated goal for the original tournament is to maximise the correlation between the meta-model predictions and the targets. To achieve this, Numerai would like to ensemble predictions from their participants that

  * have a high correlation with the targets (call this “goal 1”) and
  * are independent from each other (“goal 2”).



Note that the more goal 1 is fulfilled, the less important goal 2 becomes; if one user submits “perfect” predictions, Numerai would actually like every user to submit the same­­—completely dependent—predictions.

To achieve their goal(s), Numerai try to devise a tournament payout scheme which makes participants internalise these goals. To facilitate an internalisation of goal 1, participants receive a return on their investment equal to their predictions’ correlation with the targets (“CORR”). To facilitate an internalisation of goal 2 is more intricate, since independence can only be defined in relationship to other participants and is thus a moving target. Numerai are currently trying to achieve this internalisation by giving participants the possibility to receive a return on their investment equal to (a multiple of) their predictions’ correlation with the targets after the former have been orthogonalised to the meta-model’s predictions (“MMC”). Note that MMC reflects both goal 1 and 2 simultaneously.

If we are in a world of participants who are completely isolated, the current payout scheme should work reasonably well. One issue is that participants cannot properly train their models for MMC. This makes it hard for them to internalise goal 2. A (flawed) remedy could be to publish historical meta-model predictions to use in training. Another issue is the opaqueness and volatility of MMC. A more radical remedy for this problem would be an overhaul of the payout scheme. For example, participants could receive a return equal to CORR x IND x c, where IND = (1 - CORR W METAMODEL) and c is some scalar. In my experience, correlation with the metamodel is much more stable than MMC and could thus help participants focus on goal 2.

However, we are in a world in which people are interconnected and constantly learn from each other. This is clear when you consider the exchange of thoughts, ideas, and memes that takes place within the active Numerai community here and especially on RocketChat. It has been quite amazing to me how much I was able to learn from all the smart and creative people who spend their valuable time explaining established and new ML concepts to rookies like me. But this poses a problem to Numerai’s current payout scheme: Neither CORR nor MMC make participants internalise the positive effects their sharing of knowledge and ideas has on other participants’ models’ correlation and independence. In fact, MMC introduces an incentive to harm the meta-model’s performance. (It is true that too much sharing of ideas might harm overall model-independence for the sake of correlation. However, some participants might have developed sophisticated procedures to make models more independent, but do not want to share them to not hurt their MMC score. Moreover, as overall correlation goes up, independence becomes less important. Lastly, the same idea, in the hands of different people, can lead to very different results.)

I have discovered multiple little tricks that have helped my models’ performance, a lot of which have not been discussed publicly. Surely, so has anyone else who spends enough time in this tournament. I believe that at least some helpful approaches have not been made public because of the antagonistic nature of MMC (and of the leaderboard bonus before it). This certainly has lead to models with lower correlation and has thus hampered goal 1. Moreover, if participants do not share their great ideas to enjoy their MMC gains in peace, the public discussion can become dominated by ideas pushed by the more vocal Numerai team—think feature “neutralisation”. In the end, this can lead to a scarcity of heterogeneous ideas being considered by the average participant. But this can make models less independent, hampering goal 2 as well.

I don’t know what a payout scheme that makes participants perfectly internalise Numerai’s goals looks like. This post has been written to point out some positive externalities that so far seem to have not been considered. I do have some related thoughts/suggestions on which others might further improve, though:

  * One option is to incentivise “productive” forum posts—ideally through NMR payments. Of course, this can lead to an overinflation of posts and comments, and we don’t want to end up like Kaggle, do we?
  * I still wonder whether the CORR x IND x c payout scheme could work. I have not thought about it deeply, but on the surface I like that it makes a clear distinction between goal 1 and goal 2. I guess it doesn’t solve the problem that helping other participants is disincentivised, though—it’s just less of a disincentive than MMC.
  * Maybe all Numerai really needs is CORR and they should just get rid of MMC. Participants cannot really train for meta-model independence, anyway. They might already have an incentive to train models which are independent from each other if they stake on more than one model, however. And even without an explicit incentive, I believe that humans like to try out their own, idiosyncratic approaches just for the sake of it, facilitating independence naturally.
  * Why not align Numerai’s and the participants’ goals more directly and make the return dependent on the correlation of the meta-model’s predictions with the targets (“MMCORR”)? To prevent free-riding, return could be dependent on something like CORR x MMCORR x c or CORR x a + MMCORR x b.



I’m not saying that Numerai participants don’t collaborate—quite on the contrary, as I have already stated above. But I believe that a lot of the “big” ideas have been held back, and that the current payment scheme incentivises this secrecy. This harms both Numerai as well as the participants.

---

### Post #2 — **liz** | 2021-04-07 02:57 UTC

interesting thoughts, thanks for sharing ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

Personally I don’t mind not being able to back test on MMC. It is possible to do this live, over time, given the model slots, though the width available may not satisfy most.

Not disagreeing with your notes on MMC, but related I think a larger factor influencing non-cooperation is the culture of the community. I feel a lot of parallels to other tech (mixing in finance too) communities I’ve engaged with over time, that I think can be a hindrance to cooperation, including specific flavors of competitiveness, and other factors.

That said, I don’t believe it’s actually necessary to hide much about a modeling approach, in order to still earn a decent MMC. To that end, I’ve spoken openly on DSC, and on rocketchat in public and private about my current approach and plans. At least for what I’m doing, there are orders of magnitude beyond trillions of ways to do it, so as long as I don’t give away my seed, no one will be able to duplicate my predictions. If someone explores this space and shares their thoughts/experiment results, I can also refine my approach.

I plan to share more soon and hope others do, too ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #3 — **lackofintelligence** | 2021-04-07 21:47 UTC

Actually, MMC gets better when the Meta Model improves. But the reason people are not incentivized by this fact is that they don’t understand it. I have tried to explain this in multiple places, but the response I get indicates that very few people understand. The result is, as you correctly assert, that MMC does not effectively induce collaboration. But this is the result of poor analysis of a complicated procedure or even marketing, not because the MMC procedure does not effectively reward collaboration.

I will once again briefly try to explain this assertion. The formula for MMC is:

\mathrm{MMC} = \hat{U} \cdot \hat{T} - (\hat{U} \cdot \hat{M} ) \times (\hat{M} \cdot \hat{T}) \tag{1}

where

\hat{U} \equiv Centerized unit vector representing predictions of a user.  
\hat{M} \equiv Centerized unit vector representing meta-model predictions.  
\hat{T} \equiv Centerized unit vector representing the resolved ground truth.

If the Meta Model is volatile (bad), then (\hat{M} \cdot \hat{T}) can fluctuate negative. When it does the product of all the terms right of U\cdot T in Eq. 1 add to the correlation and the pack herd mentality, represented by a large value of correlation to the Meta Model, (\hat{U} \cdot \hat{M} ) is rewarded. In this regime MMC incentivizes the exact opposite of its stated goal; its a regime where originality is not rewarded. The cure is to ensure that (\hat{M} \cdot \hat{T}) remains positive. Positivity cannot ever be guaranteed, but low Meta Model volatility can be worked toward as a community effort. At least that is my naive way of seeing it.

---

### Post #4 — **jimmy_woodford** | 2021-04-08 16:09 UTC _(reply to #3)_

I see your point. However, this is only the case if \hat{M}\cdot\hat{T} is negative, which, judging from past performance should be more an exception than the rule. And even then, to receive a positive MMC, you’d have to have a better performance than the meta model. I agree that in your case individuality is not incentivised, but I don’t follow how your point connects to your statement that “MMC gets better when the Meta Model improves”, if we assume that your individual performance stays fixed. In the case you describe we still have dMMC/d(\hat{M}\cdot\hat{T}) < 0. Am I missing something?

I have an additional small question, if you find the time: Your measure for MMC is not scaled to correlation, since the neutralised prediction vector is usually not a unit vector, correct?

---

### Post #5 — **lackofintelligence** | 2021-04-09 01:31 UTC

Let me back up and say that I think that your post is great and that it has a lot of great ideas that we should investigate. I also appreciate the fact that you read my reply carefully.

Strict answers to your questions:

  1. \frac{d ( \mathrm{MMC})}{d ( \hat{M}\cdot\hat{T})} = -\hat{U} \cdot \hat{M} which depends on the sign of (\hat{U}\cdot\hat{M}).
  2. Yes, the neutralized prediction vector is: \hat{U} - \hat{U}\cdot\hat{M} \times \hat{M}, which is not unitized before being dotted into \hat{T}. However, I have asked whether this is mathematically correct and have not gotten a response yet. So there may be some additional scaling applied. There is certainly the user defined scaling missing but that is applied before adding back to CORR.



People can get worried when folks spend too much time thinking of ways to attack the system. But if you are correct that MMC disincentivizes cooperation, then would it not be a corollary that there is an incentive for attacking the Meta Model?

Less strict answers to your questions:

My main point is, without trying to explore the different avenues of attack hinted at, that when the Meta Model is not performing well it punishes model diversity. Are you aware of this discussion: [MMC punishes originality during burns](<http://forum.numer.ai/t/mmc-calculation-punishes-originality-during-meta-model-burns>)? It seems like enough people were concerned about this that, at least for awhile, it was something to worry about. Then some smart and generous people, whose names I unfortunately cannot mention, started talking about some really good ways to improve models and overall we came out of that burn period and have prospered very well since then, hiccups due to Numer.ai’s experiments notwithstanding.

Your’s and [@liz](</u/liz>) 's discussions have really been thought provoking to me. I am even starting to imagine a DAO of modelers who find a way to cooperate. I think I have some interesting ideas. But I would not be surprised to find that people are already doing something like that, maybe less formally.

---

### Post #6 — **liz** | 2021-04-09 02:51 UTC _(reply to #5)_

i can’t math right now but just wanted to chime in that i’d love to participate in cooperation experiments. also that a modeler member dao could do cool stuff in signals like purchase data or computing deals

---

### Post #7 — **jimmy_woodford** | 2021-04-09 19:49 UTC _(reply to #5)_

Thanks for your reply. The way I understand is that Numerai calculates MMC by taking the covariance of the neutralised prediction vector with the true outcomes and scaling it by .0841^{-1}.

I’m aware of the discussion on the issue of MMC rewarding redundancy in burn periods of the meta-model, altough I haven’t read all the comments. I understand that issue as an additional weakness of MMC in addition to the disincentive effect I have tried to describe.

I do believe that there is an incentive for individual users to attack the meta model to enhance their relative performance. However, I think that such an attack would be hard to pull off. You’d have to convince enough, probably quite clever, people to submit bad predictions. But let’s say for example you’re a user with a good track record or an otherwise good reputation who happens to have a decent model that mostly makes use of linear relations in the data. You’d certainly have an incentive to support the idea of feature neutralisation in order to make the meta model less correlated with yours, especially if you think that feature neutralisation is actually a bad idea.

I like your and [@liz](</u/liz>)’s idea about cooperation. The available data also allows to find users whose performance is independent from one’s own, making them potentially a good match.
