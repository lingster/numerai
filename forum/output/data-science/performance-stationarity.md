---
title: "Performance Stationarity"
category: Data Science
url: https://forum.numer.ai/t/performance-stationarity/151
created_at: 2020-04-12T01:13:08.660000+00:00
last_posted_at: 2021-03-06T18:12:25.962000+00:00
posts_count: 16
views: 8415
tags: []
---

# Performance Stationarity

---

### Post #1 — **richai** | 2020-04-12 01:13 UTC

You want the performance of your model to as much as possible be a stationary process. A model that goes up for 9 months in a row but then down for all of the last 3 months is less preferable than a model which has the 3 down months interspersed evenly throughout the year. These two models could have the same Sharpe ratio but the one with three down months in a row would have higher drawdown. A sophisticated investor would much prefer to see a model with a stationary track record because they tend to be more robust and tend to be more likely to continue to work into the future.

When I say stationary I tend to mean that the performance of your model is statistically similar to flipping a biased coin. Let’s say your model does well in 80% of eras, then your performance should look like flipping a coin with 80% bias on heads. Your performance should look like something like HHHHTHHHTHHHTHHHHT not something like this TTTHHHHHHHHHTTTTTHHHHHHHH i.e. it should lack autocorrelation / be memoryless / not have any long burn periods.

The challenge with stock market data is that almost all of the stock features are not stationary but the goal if for the model built with the features to be stationary. Quant features like value or momentum can work well for years and then stop working or work in the opposite direction for the next few years. Models trained on these non-stationary features will tend to also not have stationary performance and this is why so many quant models don’t generalize well out of sample – they have fit to regimes, they have not found stationary signals.

In a previous posts, Michael gave code for neutralizing models to feature exposures. While there’s no guarantee that this creates stationarity in performance out of sample, in tests it tends to help because feature neutralization will reduce to zero any linear bets on the non-stationary factors. [MMC2 and Feature Neutralization](<http://forum.numer.ai/t/mmc2-and-feature-neutralization/93>)

I wanted to open up discussion on this topic as it’s unusual in most machine learning contexts to care about stationarity or the ordering of your performance. I think many Numerai users cared about getting the highest possible mean correlation score and then began to care about getting the best possible Sharpe. I think the next frontier will be reaching stationarity.

Does anyone explicitly try to learn a model to optimize for stationarity? How?

Does anyone look at [ADF tests](<https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test>) on their performance or on the feature’s performance in their model construction? Or remove features with too much autocorrelation in their correlation with the target from era to era?

How can you train a model on the Numerai training data to ensure stationarity at least over the training set i.e. enforce that you don’t have especially long periods of strong performance or underperformance over the training eras? Bonus: does a model with stationarity over the training set work out of sample better than one without? Extra bonus: if you optimize for stationarity in the training of your model is that better than optimizing for Sharpe?

PS In Marcos’ book Advances In Financial Machine Learning you can see a discussion on stationarity in chapter 5  
PPS You can bet AQR wished value had more stationary performance <https://www.aqr.com/Insights/Perspectives/Its-Time-for-a-Venial-Value-Timing-Sin>

---

### Post #2 — **mdo** | 2020-04-12 07:10 UTC

Great post Richard, much appreciated! These issues have been on my mind recently as I’ve been playing around with fitting models to feature neutral targets. I’ve been testing out the Sortino ratio as an alternative to Sharpe for doing hyperparameter selection, because it makes sense to me to only penalize downside volatility/variance. Interestingly I’m finding that Sortino does favor different and narrower ranges of hyperparameters than Sharpe.
    
    
    def sortino_ratio(x, target=.02):
        xt = x - target
        return np.mean(xt) / (np.sum(np.minimum(0, xt)**2)/(len(xt)-1))**.5
    

After reading your post and doing some internet searching I came across this document which proposes a modification to Sharpe, they call Smart Sharpe, which takes autocorrelation into account. If anyone is interested I threw together a simple implementation to help clarify it to myself. I also created the “Smart” version of Sortino by including the autocorrelation penalty term to perhaps get the best of both worlds.  
[keyquant.com](<https://www.keyquant.com/Download/GetFile?Filename=%5CPublications%5CKeyQuant_WhitePaper_APT_Part2.pdf>) [](<https://www.keyquant.com/Download/GetFile?Filename=%5CPublications%5CKeyQuant_WhitePaper_APT_Part2.pdf>)

### [GetFile](<https://www.keyquant.com/Download/GetFile?Filename=%5CPublications%5CKeyQuant_WhitePaper_APT_Part2.pdf>)

2.02 MB
    
    
    def ar1(x):
        return np.corrcoef(x[:-1], x[1:])[0,1]
    
    def autocorr_penalty(x):
        n = len(x)
        p = ar1(x)
        return np.sqrt(1 + 2*np.sum([((n - i)/n)*p**i for i in range(1,n)]))
    
    def smart_sharpe(x):
        return np.mean(x)/(np.std(x, ddof=1)*autocorr_penalty(x))
    
    def smart_sortino_ratio(x, target=.02):
        xt = x - target
        return np.mean(xt)/(((np.sum(np.minimum(0, xt)**2)/(len(xt)-1))**.5)*autocorr_penalty(x))

---

### Post #3 — **richai** | 2020-04-12 21:56 UTC _(reply to #2)_

Amazing response! This is why we have a forum! I hadn’t heard of Smart Sharpe but that paper makes a lot of sense. Maybe we should use use code and switch to showing Smart Sharpe over validation when uploading predictions. [@master_key](</u/master_key>)

---

### Post #4 — **ssh** | 2020-05-06 21:36 UTC _(reply to #2)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> 
>     def autocorr_penalty(x):
>         n = len(x)
>         p = ar1(x)
>         return np.sqrt(1 + 2*np.sum([((n - i)/n)*p**i for i in range(1,n)]))
>     

played a little for a few rounds with suggested smart version of sharpe and sortino.  
not realized at first from the math that suggested autocorr_penalty(x) in favour of negative auto correlation. Negative autocorrelation means era correlation jumping up and down around mean each next era. Correct me if I’m wrong but desired property of stationary is to have AR1 close to 0, not to -1.  
I’m trying loss function that have an inverse value of original function autocorr_penalty() in case of negative autocorrelation:
    
    
    # In R style 
    autocorr_penalty2 <- function(x) {
      ap <- autocorr_penalty(x)
      if(ap < 1)  { 
    	return (1/(ap) ) #  ap == 0 when  AR1(x) == -1 
      } else {
       return (ap)
      }
    }

---

### Post #5 — **of_s** | 2020-05-06 21:41 UTC _(reply to #4)_

Use the absolute value of the autocorrelation as the penalty…they both represent **certainty** , which is what the measure is trying to penalize.

---

### Post #6 — **mdo** | 2020-05-06 22:02 UTC _(reply to #4)_

Yeah, I had wondered about that too and after thinking more I think you’re right. I’m guessing the paper didn’t address this because negative AR1 coefficients just don’t happen in the long time-series data they are analyzing. To prevent wonkiness when using as a penalty I agree with [@of_s](</u/of_s>) that you should just modify the function to:
    
    
    def autocorr_penalty(x):
        n = len(x)
        p = np.abs(ar1(x))
        return np.sqrt(1 + 2*np.sum([((n - i)/n)*p**i for i in range(1,n)]))

---

### Post #7 — **of_s** | 2020-05-06 22:07 UTC

If interested, I had written about this years ago.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fd5d78edb9d884c7c2737875bc2bfe1de4d28492.png) [linkedin.com](<https://www.linkedin.com/pulse/expected-partial-moments-fred-viole/>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/631bcec55eeaeafa78710d082a1a8e1688784f1d.png)

### [Expected Partial Moments](<https://www.linkedin.com/pulse/expected-partial-moments-fred-viole/>)

If you haven't already, please view my recent posts for more on partial moments in a behavioral finance and statistics context: The Elements of Variance Nonlinear Nonparametric Statistics Using Partial Moments Behavioral Finance and Partial Moments I...

Reading time: 4 min read

---

### Post #8 — **arbitrage** | 2020-05-07 14:25 UTC _(reply to #7)_

are you a Finance PhD?

---

### Post #9 — **of_s** | 2020-05-07 14:39 UTC _(reply to #8)_

Not technically, but I have several areas of research I could successfully defend for one! ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #12 — **lackofintelligence** | 2020-06-26 15:05 UTC

It it is a mystery to me how a model could know about the order of eras. How?

Let me answer that question. By introducing an era variable.

Then if you want to use out of sample eras to train parameters via CV the only correct CV to use is time-series CV, otherwise a data leak is introduced. There are numerous problems with time series CV, eg,

  1. inefficiency
  2. the chosen parameters are not optimal for the size of the final dataset
  3. 0.02 percent (percent!) of people are actually do it or even know how to do it.



So I think this line of reasoning is doubtful.

---

### Post #13 — **lackofintelligence** | 2020-06-27 18:48 UTC _(reply to #12)_

Let me give a little more detail on some types of era variables and their significance:

  1. A categorical variable: Its just a grouping variable. In theory it cannot tell you anything about the order of eras. Some kind of grouping variable is used for ranking. Loss functions that utilize auto-correlations cannot make use of it for optimization and there is no problem with data leakage so any kind of CV scheme can be used.
  2. A real or integer ordinal variable. This type of variable introduces a data leak. Only time-series CV can be used or you will overfit. Loss functions that utilize auto-correlation will definitely see improved CV at your peril.
  3. A real nonordinal context variable: Context variables can be engineered in any way so I am talking about context variables that are specifically not ordinal with respect to time by design. But one has to be cautious with them. If they are well designed any type of CV can be used to get improved model parameters. Loss functions that utilize time-based auto-correlation probably will not see improvement from them. But if they do then your model is approaching chaos since nearby in time eras may have similar context variables.

---

### Post #14 — **perfect_fit** | 2020-09-18 12:09 UTC

Great thread! Does the current Sharpe calculation in the diagnostics panel (Validation Sharpe) already include this autocorrelation penalty? Also, are there any plans to add (smart) Sortino to the diagnostics panel?

---

### Post #15 — **jrb** | 2020-09-19 09:12 UTC _(reply to #14)_

I can tell you that the Validation Sharpe currently displayed on the website does not include autocorrelation penalty. And that’s because I calculate the metrics locally and the numbers displayed on the website match my local results. I’m not in a position to answer your second question, I hope someone from the team will.

---

### Post #16 — **richai** | 2020-09-19 17:31 UTC _(reply to #14)_

No plans for Sortino right now. It did seem to be quite good but also very similar to Sharpe. I remember at one point we had some success with models trained on custom loss function of smart Sortino.

---

### Post #17 — **pacio** | 2021-03-06 17:42 UTC _(reply to #2)_

Thanks for sharing the paper.

Help me understand why you use `p**i`. This paper uses subscript _i_ to indicate that it’s autocorrelation coefficient `p` at lag _i_ , which would be `ar(x[:i])`.

---

### Post #18 — **mdo** | 2021-03-06 18:12 UTC _(reply to #17)_

Read page 48 for the formula
