---
title: "Signals payout improvement?"
category: Signals
url: https://forum.numer.ai/t/signals-payout-improvement/3107
created_at: 2021-04-27T13:43:22.895000+00:00
last_posted_at: 2021-05-27T16:57:31.143000+00:00
posts_count: 12
views: 1632
tags: []
---

# Signals payout improvement?

---

### Post #1 — **v1nc3n7** | 2021-04-27 13:43 UTC

Hi!

Signals payouts are currently low, and the Numerai team is looking for possible improvements. One purpose of this post is to discuss if the Signals’ payout curve could be modified to make Signals more attractive.

Below is the message that I originally posted in the chat:

> Currently, on Signals, a very high variance signal that is correct 56% of the time loses money. However, combining signals from multiple users should reduce the variance, and therefore such a very high variance signal may still be of interest for the meta-model. Here very high variance means a signal that reaches the payout cutoff in both directions all the time.  
>  Let’s consider now a more reasonable signal that is staked with 2xMMC to maximize profit. The fact that a 2x coefficient is applied both to correlation and MMC increases the variance. To simplify, let’s assume that the payout (equal to 2 x corr + 2 x MMC) only takes values in {+10%, -10%}. To be break-even, the signal must be correct 52.5% of the time. If the signal is correct 55% of the time, it will have an average return of 0.5%. To increase the return of such signal, we could make a change to the payout curve. What about attacks? It is important to notice here that to avoid attacks of type p | 1-p, the payout curve doesn’t have to be symmetric. Taking into consideration how returns are compounded, a payout function x |-> x if x >= 0 and x / (1 – x) if x < 0 would make p | 1-p attacks just break-even. With such a payout function, the previous signal would have a return that goes up from 0.5% to 0.96%, that is almost the double. Furthermore, if the signal is correct only 52.5% of the time, rather than being break-even, it would now have a positive return of 0.48%.  
>  I believe that the above payout function would be more in line with the purpose of Signals, that is gathering new original signals that could improve the meta-model, even if these signals are very weak. Furthermore, this change would be particularly easy to implement.

I am going to give a few more details now.

To simplify the problem, let’s consider that our weekly result (for example 2corr + 2mmc) only take values in \\{r, -r\\}. Let’s check how often we must get a positive result with the current symmetric payout curve in order to get break-even:

(1 + r)^p (1 – r)^{1 – p} = 1 \iff p = \frac{-\log(1-r)}{\log(1+r) - \log(1-r)}.

That means that if our results take only values in \pm 25\%, we need to be correct \frac{-\log(1-0.25)}{\log(1+0.25) - \log(1-0.25)} = 56.3\% of the time to be break-even.  
If the values are in \pm 10\% (resp. \pm 5\%), the predictions need to be correct 52.5\% (resp. 51.25\%) of the time to be break-even.

We see here that any signal that doesn’t have a high number of positive eras will probably either lose money or barely make any money. That seems contradictory to the fact that with Signals, we have to bring our own data, and while such data can be of interest to Numerai, we cannot expect to have results as good as the ones we can get in the classic tournament that is using expensive financial data.

Let’s now consider an asymmetric payout curve defined by:

f(x) = \left\\{\begin{array}{ll} x \text{ if } x \ge 0 \\\ \frac{x}{1 – x} \text{ if } x < 0 \end{array} \right.

This function as the following property: (1 + f(x)) (1 + f(-x)) = 1.  
That is if we submit p and 1 – p, we get as results corr and -corr, and therefore the payout is break-even.
    
    
    def f(x):
        if x >= 0:
            return x
        else:
            return x / (1 - x)
    
    
    r = 0.1
    print('With results in +-0.10:')
    for c in [55, 52.5, 51]: # c is percentage of correct predictions
        payout = ((1 + f(r))**c * (1+f(-r))**(100-c)) ** (1 / 100) - 1
        print(f'- if the signal is correct {c}% of the time, the average payout is {payout * 100 :.2f}%')
    
    
    
    With results in +-0.10:
    - if the signal is correct 55% of the time, the average payout is 0.96%
    - if the signal is correct 52.5% of the time, the average payout is 0.48%
    - if the signal is correct 51% of the time, the average payout is 0.19%
    

We could also add to this payout function a small penalty. That would make signals with very high variance and no prediction value lose a bit of money rather than just being break-even:
    
    
    def f(x, eps):
        if x >= 0:
            return x
        else:
            return x / (1 - x) + eps * x
    

That’s all for today, thank you for reading ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)

---

### Post #2 — **of_s** | 2021-04-27 14:11 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/v/43a26b/48.png) v1nc3n7:

> That seems contradictory to the fact that with Signals, we have to bring our own data, and while such data can be of interest to Numerai, we cannot expect to have results as good as the ones we can get in the classic tournament that is using expensive financial data.

It is an apples to oranges comparison to the classic tournament due solely to the difference of the prediction windows. If Signals were extended to predicting returns a month out, then we could generalize to data quality statements. I doubt the classic tournament would have such positive results predicting 6 days out…

Otherwise, your payout suggestion is sensible to reward participation with lower percentages.

---

### Post #3 — **degerhan** | 2021-04-27 17:56 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/of_s/48/2627_2.png) of_s:

> apples to oranges comparison to the classic tournament due solely to the difference of the prediction windows

Following up on the comment from [@of_s](</u/of_s>), and with the huge caveat that this data is 10+ years old and the below rows are cherry-picked, rank-based predictions that drove an S&P500 market neutral fund for 5+ years. Annual returns averaged 20.2% which used to be among the top of the heap for market-neutral systematic funds.

Prediction Horizon weeks | 1 | 2 | 4 | 13  
---|---|---|---|---  
Return metric, for horizon | 4.79 | 17.41 | 40.54 | 149.68  
Return metric, avg per week | 4.79 | 8.71 | 10.14 | 11.51  
Alpha contribution (annualized) | -0.20% | 5.09% | 6.48% | 8.58%  
  
My intuition is a 2 to 4 week prediction window will yield better results for signals. And the performance gap between main tournament and signals might be supporting my intuition. However, feel free to give me a hard time about this ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) as I haven’t done a study with recent data or the signals universe.

I think I heard [@mdo](</u/mdo>) say before that targets matter more than modeling techniques – I wonder if numerai has done or will do a study to determine optimal signals target horizon.

---

### Post #4 — **gund** | 2021-04-28 09:57 UTC

Interesting! Can you please explain how you came up with this formula?

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/v/43a26b/48.png) v1nc3n7:

> `payout = ((1 + f(r))**c * (1+f(-r))**(100-c)) ** (1 / 100) - 1`

Or why do you consider the payout is (1+r)^p * (1-r)^(1-p)? Expected payout shouldn’t it be something like (1+r)_p + (1-r)_(1-p)?

---

### Post #5 — **v1nc3n7** | 2021-04-28 11:24 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/of_s/48/2627_2.png) of_s:

> It is an apples to oranges comparison

Indeed, it is not such a great comparison. For sure, the shorter prediction window makes the problem significantly more difficult. Overall, due to the multiple differences, the correlation we get on Signals should be on average way less good than the one on the classic tournament, and the variance should also be higher. That’s why rewarding lower percentages seems important.

---

### Post #6 — **v1nc3n7** | 2021-04-28 11:30 UTC _(reply to #3)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/degerhan/48/3449_2.png) degerhan:

> |Prediction Horizon weeks|1|2|4|13|
> 
> |Return metric, for horizon|4.79|17.41|40.54|149.68|  
>  |Return metric, avg per week|4.79|8.71|10.14|11.51|  
>  |Alpha contribution (annualized)|-0.20%|5.09%|6.48%|8.58%|

What would be great is to be able to make predictions at different horizons. Furthermore, having multiple targets to optimize for could improve the results. That’s actually what I would prefer.  
But from the data you show, if we had to stick to only one horizon, 2 weeks could be a sweet spot for Numerai since it would still be significantly different from the classic tournament.

---

### Post #7 — **v1nc3n7** | 2021-04-28 11:47 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/g/8edcca/48.png) gund:

> Interesting! Can you please explain how you came up with this formula?

The name of the variable is not a good choice, average return might be better.  
Here, f(0.1) and f(-0.1) are respectively the returns for positive and negative rounds. Over 100 rounds, let’s assume that 55 rounds are positive. Then the invested amount will be multiplied by a coefficient (1 + f(0.1))^{55} (1 + f(-0.1))^{45}. To get the average per round, we raise to the power of 1/100.

---

### Post #8 — **of_s** | 2021-04-28 14:30 UTC _(reply to #5)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/v/43a26b/48.png) v1nc3n7:

> and the variance should also be higher.

Why should the variance (of correlations) be higher? I would think the longer the timeframe, the more dispersed the scores.

If you proxy the 6 day returns with noise, then while scores on average will be lower, their variance or range should be too.

---

### Post #9 — **v1nc3n7** | 2021-04-28 14:58 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/of_s/48/2627_2.png) of_s:

> Why should the variance (of correlations) be higher?

I was thinking with respect to the scaled correlation, so it would be proportionally higher. It is probably better to say that Sharpe would be lower. Thank you for following ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)

---

### Post #10 — **_liamhz** | 2021-05-26 19:44 UTC

Does this payout curve prevent p | 1-p attacks whenstakes are rebalanced amongst the models trying to exploit the payouts?

Model A has a corr of 0.05, model B has a corr of -0.05. Both are staked with 1NMR

After a round, we get the following stake values (assuming payouts on 1xCorr and 0xMMC for simplicity)

Model A: 1.05  
Model B: 0.952380952 (1 + -0.05 / (1 - -0.05))

After the two models rebalance their stakes to be equal between them, each will have a stake of 1.00119048NMR ((1.05 + 0.952380952) / 2)

---

### Post #11 — **v1nc3n7** | 2021-05-27 09:15 UTC _(reply to #10)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/_liamhz/48/1368_2.png) _liamhz:

> Does this payout curve prevent p | 1-p attacks whenstakes are rebalanced amongst the models trying to exploit the payouts?

You are right, it doesn’t prevent attacks. It does allow weaker signals to get positive returns, but at the cost of opening a breach to attacks. The error above is that in the case of p | 1-p attacks, we are not compounding the returns consecutively with respect to one initial stake, but separately with respect to two stakes. Since we don’t want to let room for any attack, this payout is not a good proposal. This means we have to keep a purely symmetrical payout function, and that weak signals will not be able to get a positive return. My bad for this mistake.

---

### Post #12 — **_liamhz** | 2021-05-27 16:57 UTC

No worries, I really appreciate the effort you put into designing this! It was interesting enough that internally we had started thinking about implementing this, which is why I spent the time searching for attacks.
