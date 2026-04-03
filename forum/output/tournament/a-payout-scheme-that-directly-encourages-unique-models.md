---
title: "A Payout Scheme that Directly Encourages Unique Models"
category: Tournament
url: https://forum.numer.ai/t/a-payout-scheme-that-directly-encourages-unique-models/3039
created_at: 2021-04-24T04:28:19.450000+00:00
last_posted_at: 2021-04-26T00:03:15.824000+00:00
posts_count: 10
views: 1211
tags: []
---

# A Payout Scheme that Directly Encourages Unique Models

---

### Post #1 — **jacob_stahl** | 2021-04-24 04:28 UTC

A Payout Scheme that Directly Encourages Unique Models

The current payout system rewards correlation with live targets, and loosely rewards originality with mmc. But mmc doesn’t do enough to encourage a wide spread of unique models. This is evident if you look at the largest stakers in the tournament, many of them have a >.8 correlation with the metamodel. Whats worse is that anyone can place a gigantic stake on the example predictions, and be rewarded for 0 contribution to the tournament.

I’ve come up with a mechanism that can mitigate this problem I call the “conformity tax”. The tax works by scaling a model’s payout based on its metamodel correlation and some threshold. It has the effect of increasing the risk of putting a huge stake on a model that is highly correlated with the metamodel.

The code below demonstrates how the conformity tax works
    
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    np.random.seed(1)
    

We need to generate simulated payouts that reflect actual tournament data. It is safe to assume real payouts are Pareto distributed, but I am only guessing what the real distribution looks like. They are sorted and ranked in descending order.
    
    
    num_payouts = 1000
    largest_payout = 600
    
    a = 2 # distribution shape (not from actual Numerai data!, this is 
    an assumption)
    P = (np.random.pareto(a, num_payouts)) # Normal Payouts
    P = np.sort(P) * (largest_payout / np.max(P)) # Rescale distribution and sort
    ranks = np.flip(np.arange(num_payouts)) + 1
    
    plt.bar(ranks, P, width=1)
    plt.xlabel("Ranks")
    plt.ylabel("Positive Payouts")
    plt.savefig("payouts.png")
    

[![payouts](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5c250391584b74e499903fb84f74f9a1574372c7.png)payouts432×288 3.29 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5c250391584b74e499903fb84f74f9a1574372c7.png> "payouts")
    
    
    total_payed_out = np.sum(P)
    print(total_payed_out)
    

> 30192.954174991097

Next we create a distribution of metamodel correlations. Again,  
this is only a guess because I haven’t aggregated real data from  
the leaderboard.
    
    
    # more assumptions
    mean_corr_mm = .6
    std_corr_mm = 0.15
    
    # distribution of metamodel correlations
    M = np.clip(np.random.normal(mean_corr_mm, std_corr_mm, num_payouts), 0, 1)
    count, bins, ignored = plt.hist(M, 100, density=True)
    plt.xlim(0,1)
    plt.xlabel("Correlation with metamodel")
    plt.savefig("corr_with_mm.png")
    

[![corr_with_mm](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b6d53a3243fd2dc7eda88d2b1ba642848c01339b.png)corr_with_mm432×288 3.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b6d53a3243fd2dc7eda88d2b1ba642848c01339b.png> "corr_with_mm")

This is the conformity tax. It leaves payouts untouched until they reach a certain threshold. Everything after that is scaled based on the model’s meta model correlation. Models with low meta model correlation are taxed lightly, and models with high meta model correlation are taxed heavily. Notice that losses are untouched. If a model has a high correlation with the metamodel, putting a huge stake on it has diminishing returns, but not diminishing potential losses. This makes it more risky to put a large stake on a model that doesn’t contribute to the metamodel.
    
    
    def conformity_tax(P, M, threshold): #(payouts, metamodel_correlations, threshold) => adjusted payouts
        M = np.clip(M, 0, 1)# negative correlation has no effect
        P_prime = np.minimum(P, threshold) + np.maximum(P - threshold, 0) * (1 - np.maximum(M, 0))
        return P_prime
    
    threshold = 50
    payouts = np.linspace(-75, 200, 100)
    
    uncorrelated = conformity_tax(payouts, np.ones(100) * 0, threshold)
    slightly_correlated = conformity_tax(payouts, np.ones(100) * 0.2, threshold)
    highly_correlated = conformity_tax(payouts, np.ones(100) * 0.8, threshold)
    example_preds = conformity_tax(payouts, np.ones(100) * 0.95, threshold)
    
    plt.plot(payouts, uncorrelated, color = "blue", label='mm_corr 0')
    plt.plot(payouts, slightly_correlated, color = "green", label='mm_corr 0.2')
    plt.plot(payouts, highly_correlated, color = "orange", label='mm_corr 0.8')
    plt.plot(payouts, example_preds, color = "red", label='mm_corr 0.95')
    
    plt.xlabel("Payout (NMR)")
    plt.ylabel("Adjusted Payout with threshold of 50")
    plt.legend()
    
    plt.savefig("simulated_payouts.png")
    

[![simulated_payouts](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bffac8463df5dc4ba6ae7508f506b8f6a563b9fc.png)simulated_payouts432×288 13.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bffac8463df5dc4ba6ae7508f506b8f6a563b9fc.png> "simulated_payouts")

The plot below shows the effect on payouts at various threshold levels.  
# conformity tax at various thresholds  
P_prime_100 = conformity_tax(P, M, threshold = 100)  
P_prime_50 = conformity_tax(P, M, threshold = 50)  
P_prime_10 = conformity_tax(P, M, threshold = 10)
    
    
    plt.bar(ranks, P, width=1, color = "red", label = "No threshold")
    plt.bar(ranks, P_prime_100, width=1, color = "orange", label = "T = 100")
    plt.bar(ranks, P_prime_50, width=1, color = "green", label = "T = 50")
    plt.bar(ranks, P_prime_10, width=1, color = "blue", label = "T = 10")
    plt.xlabel("Ranks")
    plt.ylabel("Positive Payouts")
    plt.legend()
    plt.savefig("simulated_thresholds.png")
    

[![simulated_thresholds](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/526254b26a8b7dfbe3c1a9ec02ef8b716ec27602.png)simulated_thresholds432×288 6.57 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/526254b26a8b7dfbe3c1a9ec02ef8b716ec27602.png> "simulated_thresholds")

  
The conformity tax also reduces the amount of NMR minted every round. It could potentially replace the current payout factor that taxes everyone and increase the longevity of Numerai’s NMR supply.

(Disregard the hacky-ass labels, I’m a noob at matplotlib)
    
    
    total_payouts = [np.sum(P), np.sum(P_prime_100), 
    np.sum(P_prime_50), np.sum(P_prime_10)]
    plt.bar(range(0, 8, 2), total_payouts, width=1, color = "blue")
    plt.xticks(range(0, 8, 2))
    plt.xlabel("Normal        threshold 100        threshold 50        threshold 10")
    plt.ylabel("Total NMR payed out")
    plt.savefig("total_nmr.png")
    

[![total_nmr](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c7c016d28525abc7426fba88b6e0eee49719bfe8.png)total_nmr432×288 3.84 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c7c016d28525abc7426fba88b6e0eee49719bfe8.png> "total_nmr")

---

### Post #2 — **jimmy_woodford** | 2021-04-24 09:56 UTC

This looks similar to the CORR*INDEPENDENCE payout that I have proposed (where INDEPENDENCE = 1 - correlation with meta model). I think two issues with your idea are 1. asymmetric payouts, since losses are not taxed in the same way as gains and 2. an arbitrary threshold which penalises large stakes.

---

### Post #3 — **jacob_stahl** | 2021-04-24 19:12 UTC _(reply to #2)_

I see the asymmetric payouts as a feature, not a bug. I think we a agree that non original models should have smaller payouts, but why should they be protected from losses more than original models?

I also think that large stakes on non original models SHOULD be penalized. Your stake determines how much of the metamodel you control. Should big chunks of the metamodel be controlled by similar models? Doesn’t that defeat the purpose of an ensamble?

I still don’t know what the optimal value of the threshold should be, and I’m open to ideas.

---

### Post #4 — **mic** | 2021-04-25 04:28 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jacob_stahl/48/881_2.png) jacob_stahl:

> I also think that large stakes on non original models SHOULD be penalized

Example model isn’t the only non original model

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jacob_stahl/48/881_2.png) jacob_stahl:

> Should big chunks of the metamodel be controlled by similar models?

That’s the purpose of staking

Perhaps payout factor could be a function of MMC and calculated on an individual model basis? Higher payouts would then be made available to more original models.

---

### Post #5 — **liz** | 2021-04-25 13:50 UTC _(reply to #3)_

I think the implication is that asymmetric payouts are vulnerable to the P/1-P attack

---

### Post #6 — **gammarat** | 2021-04-25 18:26 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jacob_stahl/48/881_2.png) jacob_stahl:

> I still don’t know what the optimal value of the threshold should be, and I’m open to ideas.

Just make it zero sum, for example by putting the earn/burn threshold at the centroid (stake weighted mean) of corr. As for MMC, are unoriginal models really a problem? As I understand it (I may well be wrong) the reward comes that part of a submission that is orthogonal to the rest while being positive on corr. So if everyone is submitting the same predictions, then they won’t have much of an orthogonal component in the first place.

---

### Post #7 — **jacob_stahl** | 2021-04-25 22:02 UTC _(reply to #5)_

Some certainly are. If a payout scheme has a reward past a certain threshold, then 2 opposite high variance models can exploit it. However, mine has a tax past a certain threshold based on meta model correlation. Is there a specific reason mine can be exploited by P/1-P?

---

### Post #8 — **liz** | 2021-04-25 22:10 UTC _(reply to #7)_

perhaps it isn’t exploitable that way. the math is a bit beyond me at the moment.

---

### Post #9 — **jacob_stahl** | 2021-04-25 22:12 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> Perhaps payout factor could be a function of MMC and calculated on an individual model basis? Higher payouts would then be made available to more original models.

Thats interesting. I still prefer payout as a function of metamodel correlation. Metamodel correlation clipped at zero has the same range as payout factor (0 to 1), making that function more straight forward and simple.

---

### Post #10 — **of_s** | 2021-04-26 00:03 UTC

This discussion has been ongoing with unfortunately no progress to report:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/bor1/48/3286_2.png) [Alternative payout when negative MMC but positive CORR](<http://forum.numer.ai/t/alternative-payout-when-negative-mmc-but-positive-corr/594>) [Tournament](</c/tournament/7>)

> Can we get some variant of “if MMC < 0 then min(0, max(CORR, MMC)), else MMC” to get less burned if your CORR is better than your MMC? So we had people ask about some variant of MMC scoring that doesn’t burn people that try to make a model that does well during burns (me included) - we just went through a phase where a CORR of 0.012 or so would get you a negative MMC of -0.033, because you are outcompeted by models that do well now, but would burn heavily during burn times. That seems unwante…
