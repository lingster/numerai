---
title: "TC isn't really True Contribution"
category: Tournament
url: https://forum.numer.ai/t/tc-isnt-really-true-contribution/6767
created_at: 2023-11-02T21:16:20.648000+00:00
last_posted_at: 2023-11-02T22:34:36.953000+00:00
posts_count: 2
views: 591
tags: []
---

# TC isn't really True Contribution

---

### Post #1 — **eleven_sigma** | 2023-11-02 21:16 UTC

To put it plainly, the primary issue with the recent performance of the fund is TC, the second issue is TC, and the third issue is also TC…

TC may be an optimal metric from Numerai’s perspective, but it has several serious problems:

  * What TC claims to be and what it actually is are not the same at all. TC should represent the true contribution of a model to the metamodel. For this, it’s essential that TC is calculated as “leave one out.” Initially, TC was calculated as an average of several out-of-bag (OOB) values. This made some sense, but if a model had the misfortune of being in OOB with other poor models, it negatively affected the calculation. For an accurate average OOB calculation, extensive resampling would be necessary. Both leave one out (LOO) and OOB methods consume excessive CPU resources.

  * Then came the new TC calculation method, based on the gradients of a layer in optimization software used for metamodel calculation. All good, right? Well, NO. This way of calculating TC is what’s known as “in-data,” meaning it uses the same data used to train the model. Any in-data performance calculation is overfit and biased toward data (variables, where in this case each variable is a model) that provides more degrees of freedom to the process being tuned/optimized. Models that are very different from the rest and/or have a lot of random noise offer many degrees of freedom to the process, and it overfits them. This overfitting is reflected in high gradients, and Numerai interprets this as good models with high TC.

  * Let’s draw a parallel with something we all know. Consider a gradient boosting model tuned with lightgbm where each variable is a model. TC would be equivalent to calculating the relative importance of each variable (model). What happens with the built-in importances provided by lightgbm? We all know that they are overfit to variables with higher cardinality or greater variability, simply because they provide more degrees of freedom (more candidates for split points) to the process. This is easily seen by adding several purely random variables to the model and calculating their built-in importance to find that some are surprisingly “important.” How do we know the correct way to calculate the importance of a variable (model)? That’s why other techniques are used to measure variable importance, such as randomly permuting their values and observing the impact on performance. The same thing happens with TC as it’s currently calculated. It’s an overfitted and biased measure toward models that are different from the rest and have variability (random noise). Many data scientists have achieved high TC scores by playing by these rules, without paying attention to CORR, even forcing CORR to be negative as another way to differentiate themselves from the rest and be attractive to the metamodeling process, thereby obtaining high TC scores. The fund has bet on these models, and there are the results obtained. In a way, Numerai has achieved “WYGIWYP” (What you get is what you paid for).

  * Last but not least, even in the case where TC is the best metric and it’s well calculated, what good is a metric that data scientists cannot reproduce or calculate? These two characteristics must be essential for any metric. Without them, it’s impossible to optimize them. What have people done? Test, test, and test. We’ve started a “genetic” optimization race in which successful experiments have led to the next generation of experiments. Models with correlations of 0.10 with the metamodel, even some with negative correlations. Anything goes if the TC lottery yields a positive value. We’ve stopped optimizing reasonable metrics and started searching for the philosopher’s stone.




Now, my two cents: Numerai needs CORR and diversity. Why not reward precisely that? CORR and low correlation with the metamodel. Something easy to calculate and optimize. I believe it’s time to acknowledge that the experiment has not gone well, and common sense should prevail.

* * *

---

### Post #2 — **wigglemuse** | 2023-11-02 22:34 UTC

But TC is symmetrical, so random noise and uncorrelatedness can account for large magnitude of TC scores (maybe), but it can’t account for polarity/direction as it is exactly as difficult to get a score with a given positive value than it is to get the same score on the negative side. Random nonsense will not get you high positive TC in the long run – it will go to average of zero with enough rounds. And there are plenty of models with good corr and low metacorr. It should be easy to tell if TC is measuring anything useful if you are behind the scenes and can look at the real stocks models are rating high and low. It is inscrutable from our POV, but could it really also be inscrutable on the hedge fund side? Seems like they would have abandoned it long ago if it really is just praising nonsense [overall] that is obvious nonsense. And while yes, many of us having been doing lots of experiments to figure out where TC might lie (no other choice), I gotta believe we are still training on something – on the targets. (I train on all of them.) So even if we “aren’t paying attention to corr”, what that actually means in practice is that we recognize that TC doesn’t have a target and the specific corr target that they’ve chosen to pay on (for corr scores) isn’t necessarily super-relevant to TC. (But if you checked all the targets, you’d probably find some high corrs to some of them on a high TC model even if it isn’t getting great scores on Cyrus or Nomi or whatever the current official corr target was.) So low-CWMM doesn’t [necessarily] equal random noise, it is just optimized for something else that isn’t shown.
