---
title: "Regarding the MMC Sum"
category: Tournament
url: https://forum.numer.ai/t/regarding-the-mmc-sum/6842
created_at: 2023-12-07T02:03:14.513000+00:00
last_posted_at: 2023-12-08T09:52:08.775000+00:00
posts_count: 6
views: 819
tags: []
---

# Regarding the MMC Sum

---

### Post #1 — **murkyautomata** | 2023-12-07 02:03 UTC

When I proposed moving to MMC only, it was with the understanding that Numerai would place very large stakes on internal models to account for MMC being zero sum. In that scenario, users could earn a positive sum as long as the staked internal models earned a negative one. The condition for a positive user sum in this scenario would be that CORR is increased by giving a higher weight to the user meta-model relative to the benchmark models than the weight given in the fixed weight ratio. Essentially a positive sum would require that the users are “contributive” to the benchmark at a particular weight.

Having thought about it some more though, this wouldn’t quite work. The problem being that if benchmark models are consistently burning (condition for a positive sum), participants can earn MMC by inversing them until their effective net stake weight is reduced to the point that they no longer burn and MMC returns to being zerosum for the users. Numerai may not see this as much of a problem because they have observed a net sum from MMC, but we should look at what that sum really is.

First of all we should understand that what might be called “true MMC” will necessarily be zero-sum. True MMC being the stake weighted mean stake derivative of the CORR of a stake weighted mean vector with a target vector. This is fairly easy to demonstrate: <https://colab.research.google.com/drive/1sL0aqbT3h0jNka2G-GqBWlv0EsktCHI8?usp=sharing>. The current MMC though differs from true MMC in that the meta-model vector is gaussianized before being plugged in. This should be the only difference but if the predictions used to construct the meta-model are transformed differently than predictions used to calculate MMC, that could also affect the sum.

So if gaussianizing the meta-model creates some sum, what is that sum? Well Numerai MMC is still calculating the effect of adding some weight to user predictions, but adding that weight to the gaussianized meta-model rather than the actual stake weighted mean prediction. Less like the effect of adding weight to existing stake but more like adding weight to a different vector from zero. The stake weighted sum derivative (Numerai MMC) is then the effect of adding the stake weighted sum prediction (unguassianized metamodel) to the gaussianized meta-model. Demo: <https://colab.research.google.com/drive/1OLdRIEPEzR1KiEOxIKyueWyR-zqKGGyz?usp=sharing>. So under this scheme, MMC is positive if the gaussianized meta-model would have more CORR if it were more like the ungaussianized meta-model. Not exactly a great criterion. It may correlate with mean corr somewhat if the gaussianized meta-model has less kurtosis than the ungaussianized meta-model and therefore tends to have a smaller scale of CORR positive or negative, but it still really isn’t measuring mean user performance except maybe incidentally.

Given that we can expect a meta-model constructed from gaussianized predictions to already be fairly gaussian, it’s not too surprising the sum of Numerai MMC is very small. And because it’s also not very meaningful, it really shouldn’t be relied on to determine Numerai’s net payout. Mean CORR is a much better basis for this, which should imply some CORR multiplier per mandatory MMC multiplier and probably more than the 0.5 currently planned. Allowing MMC any impact on sum payout doesn’t make much sense in this light so I suggest using the zerosum true MMC instead.

A zero-sum MMC has a serious benefit in that it doesn’t require a payout factor because the net payout for it is always zero and doesn’t need to be limited by such. Having a payout factor on only CORR implies increasing CORR weight relative to MMC with decreasing total stake (across all users). This allows for a fair CORR to MMC ratio to be discovered by changing total stake in a market sense allowing total stake to find a stable equilibrium point.

---

### Post #2 — **bor1** | 2023-12-07 14:29 UTC

So, MMC is there to incentivize a diverse set of +corr predictions.

The current payout factor is about 0.1, so we have an effective multiplier of 0.05 x CORR + 0.3 x MMC. Assuming a model that perform ~equally on CORR and MMC, that would net you a return of 0.35. Richard thinks an effective multiplier of 0.05 x CORR + 0.2 x MMC is safer (a return of 0.25 in the ~equal scenario above)

You are advocating for the MMC component to be independent of the payout factor… so, say we do 1xCORR+0.2xMMC. After adjusting for the payout factor, we are effectively doing 0.1xCORR+0.2xMMC, getting to the ratio corr to mmc that Richard thinks to start with, with a return of 0.3 (in the ~equal scenario). Sounds good in theory.

I’m not that sure if the payout factor should have a dual purpose of both regulating the amount earned given the amount staked and the ratio CORR to MMC at the same time. Can you reason through that for me?

---

### Post #3 — **murkyautomata** | 2023-12-08 00:51 UTC _(reply to #2)_

CORR exists to provide an incentive to participate, MMC exists to train the meta-model.

The incentive component must be under a payout factor in order to manage the total payout and to provide negative feedback towards total stake size. If total stake drops, CORR rewards increase reducing further drops and finding equilibrium.

The training component has no reason to be to be tied to total stake size. Its magnitude needs to be great enough to train the meta-model efficiently without clipping. Allowing the magnitude to be tied to total stake would mean that at very large stakes the meta-model trains too slowly and that at low stakes payouts clip and become excessively volatile.

If the scale (pf) of CORR must be lower because the total stake size has increased and the need to incentivize staking at a certain rate has therefore dropped and the price of doing so increased, that does not also mean that the best contributors should be rewarded less for their contribution or that the worst should be burned less for theirs.

The relative scale of the two should be able to vary because the ideal scale of CORR varies and the ideal scale of MMC does not.

---

### Post #4 — **bor1** | 2023-12-08 09:37 UTC _(reply to #3)_

So we go for CORR * payoutfactor + MMC * efficient_learning_multiplier_set_by_Numerai.

  1. Numer.ai can adjust the payoutfactor at will to scale the non-zero-sum payouts back to a decent level.

  2. As you are helping everyone along, including team Numer.ai (thanks!), how would numer.ai calculate the efficient_learning_multiplier?

---

### Post #5 — **sneaky** | 2023-12-08 09:46 UTC

Doesn’t MMC still need payout factor so NMR does not run out too fast from the treasury? It is true that pure MMC is zero sum for users, because the burns are equal to gains, BUT burns are lost and gains come from the treasury unless I’m mistaken.

---

### Post #6 — **mic** | 2023-12-08 09:52 UTC _(reply to #5)_

Unless you recycle the MMC burn to the MMC winners? then the MMC payout component could be neutral to the treasury.
