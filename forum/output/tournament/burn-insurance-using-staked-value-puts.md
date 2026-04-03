---
title: "Burn Insurance Using Staked Value Puts"
category: Tournament
url: https://forum.numer.ai/t/burn-insurance-using-staked-value-puts/205
created_at: 2020-04-21T04:31:28.718000+00:00
last_posted_at: 2020-04-24T17:33:13.401000+00:00
posts_count: 3
views: 1525
tags: []
---

# Burn Insurance Using Staked Value Puts

---

### Post #1 — **of_s** | 2020-04-21 04:31 UTC

I wanted to share a proposal I put together to fill the significant impending void of the daily bonus.

Shared Numerai and Participant Objectives:  
1\. Correlation performance  
2\. Consistency  
3\. Longevity

Originality is a Numerai specific objective, which MMC2 recognizes.

The problem is the burns. The daily bonus goes a long way in offsetting burns, but since it is being phased out, how to effectively replace it? _**Options, specifically puts on staked values.**_

Note that the daily bonus rewarded longevity, but longevity could also be achieved with consistent performance. If participants are continuously making (or not losing) they will continue submitting. The missing round penalty also supports continuous submitting. The put option outlined below provides a way which will help with the participant consistency, thus aiding in achieving longevity.

Provide each participant with the static Black-Scholes price (along with input values to verify) or a binomial option expansion on their net staked value (less deposits) time series for a 5 day-out put (either European or American…that’s debatable), using their current net stake value of the opening of the round for the strike price.

Using Black-Scholes as an illustration to the effects of _sigma_ (sd of stake value net of deposits):

[![BSM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/4f6e65601c7e24bb12d7d1a2dd473c91aa042e3a_2_690x301.png)BSM1571×687 89.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4f6e65601c7e24bb12d7d1a2dd473c91aa042e3a.png> "BSM")

which reduces greatly due to the following parameter values:

  * _K_ = _S_
  * _r_ = 0
  * _(T-t)_ = 5



[![reduction](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c27055409cbb8c8149f0560823a1c2c46695212d.png)reduction386×212 4.28 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c27055409cbb8c8149f0560823a1c2c46695212d.png> "reduction")

Obviously, this results in lower put prices for higher Sharpe models due to a lower _sigma_ of payouts. An auxiliary Numerai objective of less volatile models!

Now to apply MMC2…

(M:R) is the ratio of overall MMC2 to Reputation. (M:R) currently rewards orthogonality as well as positive correlation scores, objectives 1 and 2 above.

  * R = max(0, R) to avoid rewarding negative reputations.
  * M = max(0, M) to avoid rewarding negative MMC2.
  * 0:0 = 0
  * (M:R) = min((M:R), 1)



P(1 – (M:R)) would be the ultimate put price to protect my staked value. By keeping these wagers separate from the stakes, withdrawal is not locked up for 4 weeks, satisfying participants’ desire for greater liquidity.

The problem with MMC2 as it is now, is that it merely reflects the correlation score when you have 0 meta-model correlation. There is no incentive to wager on it considering it has no hedging properties. If I wanted to simply double my exposure, I’d just double my stake!  
Further, to all the xgboosters out there, a side wager on current MMC2 is a losing proposition, again offering no hedge or mitigation like the daily bonus did.

This proposal puts (pun intended!) forth a viable hedging structure commensurate with all parties’ objectives.

**Questions / Feedback Received:**

_so we allow you to buy put options on your own model - which allow you to reclaim some lost stake in case your model burns?_ Yes, burn insurance via standard options pricing.

_And can you explain how M:R factors in mathematically? I understand that you get a better price if you have a better MMC:Rep ratio, but how does that math lead to a more “correct” option pricing?_ The correction is a reward, in order to augment the properties Numerai wants in participant models.

_It seems like arbitrary discount ratio to me right (although perhaps still pushing towards what we want)?_ Completely arbitrary, to support all of the above mentioned objectives for both Numerai and participants. Remember, this is a manner in which to substitute the daily bonus (which was arbitrary) and offer participants weekly liquidity as well as burn insurance.

_And wouldn’t options for you be price 0?_ No, my ratio is still negative and the put price would be the full amount for all of my models. Currently “MADMIN” would be the only one to benefit from this ideal state…update: this response did not age well!

_And wouldn’t you be able to attack this by submitting a model with very low volatility for awhile until put options become very cheap, and then submit a really crazy volatile model with much less risk because of the option?_ And why would I want to ruin all of the cumulative work it too to get my (M:R) to said point! The models being locked for 4 weeks is far too risky to exploit such a scenario. Also, the increase in _sigma_ increases the option price weekly. If I could time submitting such models in the first place I would have done so by now, but the obfuscation of features kind of prevents this.

I look forward to further discussion and thoughts, thanks!

---

### Post #2 — **krizmanic** | 2020-04-24 14:28 UTC

What do you mean the bonus is being phased out? <https://docs.google.com/document/d/1o3-J8qFyo7aQQZ8BIja0Lmw7Gr81sPVYazq6v41-ENI/edit#> The newest documentation does not seem to state that.

---

### Post #3 — **jrdi** | 2020-04-24 17:33 UTC _(reply to #2)_

[@krizmanic](</u/krizmanic>) I think it’s been mentioned in the chat but also here: [Leaderboard Bonus Exploit Uncovered](<http://forum.numer.ai/t/leaderboard-bonus-exploit-uncovered/200>)
