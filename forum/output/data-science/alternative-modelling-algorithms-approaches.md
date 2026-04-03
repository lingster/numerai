---
title: "Alternative Modelling Algorithms & Approaches"
category: Data Science
url: https://forum.numer.ai/t/alternative-modelling-algorithms-approaches/76
created_at: 2020-03-25T20:53:11.694000+00:00
last_posted_at: 2020-07-05T17:27:36.369000+00:00
posts_count: 5
views: 3429
tags: []
---

# Alternative Modelling Algorithms & Approaches

---

### Post #1 — **wacax** | 2020-03-25 20:53 UTC

I would like to share some of my explorations in the seemingly infinite field of Machine Learning algorithms that could be applied to the Numerai tournament. I shared this answer on Stack Exchange so now I’m sharing it with you guys. I encourage others to share and discuss in this thread interesting approaches to modeling the Numerai dataset.

[datascience.stackexchange.com](<https://datascience.stackexchange.com/questions/57367/classification-training-using-probabilites-and-not-raw-classes-factors>) [ ![wacax](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8e8c9349809b4e24cb8ac559fbeb41a4d2009966.jpeg) ](<https://datascience.stackexchange.com/users/13023/wacax>)

####  [Classification training using probabilites and not raw classes (factors)](<https://datascience.stackexchange.com/questions/57367/classification-training-using-probabilites-and-not-raw-classes-factors>)

**classification, research**

asked by [ wacax ](<https://datascience.stackexchange.com/users/13023/wacax>) on [10:24PM - 10 Aug 19 UTC](<https://datascience.stackexchange.com/questions/57367/classification-training-using-probabilites-and-not-raw-classes-factors>)

My intention was to not use a regular regression loss objective to model the Numerai dataset which works well. I was interested in an approach that sees these values between 0-1 as probabilities that an observation belongs to a class.

**Beta Regression**  
In short, it represents y as distribution of probabilities of a target belonging to a class (or any other event). The link function for this regression restricts y^∈[0,1]. Interestingly, it doesn’t work if y = 0 or y = 1; two values present in the Numerai dataset.

[stats.stackexchange.com](<https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution>) [ ![ffriend](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b73fe84459ce19173d20a16e97b187b6439b0b3e.png) ](<https://stats.stackexchange.com/users/3305/ffriend>)

####  [What is the intuition behind beta distribution?](<https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution>)

**distributions, beta-distribution, intuition, beta-binomial-distribution**

asked by [ ffriend ](<https://stats.stackexchange.com/users/3305/ffriend>) on [03:31PM - 15 Jan 13 UTC](<https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution>)

Because the values 0 and 1 are in the Numerai dataset, the beta distribution is not the best representation of the Numerai dataset target, however, by approximating the zeroes to 0.01 and ones to 0.99 (or other similar values) the algorithm will be able to learn parameters for its model, in a hackish kinda way.  
Keep in mind that the closest the value replacement is to either 0 or 1, the most biased towards the extremes the data points will represent.  


[![7YgUM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/62fe77d67edecbafa6b1c2bff78cfefd3c594dda.png)7YgUM480×480 4.23 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/62fe77d67edecbafa6b1c2bff78cfefd3c594dda.png> "7YgUM")

**Regression Models For Ordinal Data**  
Ordinal data regression is more straightforward. It’s still a type of regression analysis but this one is popular in social sciences where there are options that can be ordered such as a rating from 1 to 5, 1 being very poor and 5 being excellent. Modeling such a problem is complex and requires the learning of thresholds as well as the modelling of the target.  
The final predictions are odds of belonging to an (ordered) class or, if a weighted mean is used for all probabilities, a continuous target similar to a regression prediction.

**Regression with a Logistic Link Function**  
It’s easier if you implement the loss function by hand than if you use a library. Xgboost supports the inclusion if you specify reg:logistic as the objective function. Other libraries like Keras can support similar behavior as well.  
This is clearly the easiest one to implement and interpret results.

---

### Post #2 — **bor1** | 2020-03-26 12:40 UTC

Beta regression sounds as an interesting variant to try. Trying to wrap my head around it, especially combined with this part of the [“analysis_and_tips”](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>) python notebook, which (if I get this right) says that models trained on the two _**extreme classes versus the rest**_ both generate more or less the same result, while models trained on any of the _**middle classes versus the rest**_ generate results that are alike, but negatively correlated with the models trained on the extreme classes.

# The first and last class are highly correlated
    
    
    corrs=numpy.corrcoef(logistic.predict_proba(df[features]).T)
    plt.imshow(corrs, vmin=-1, vmax=1, cmap="RdYlGn")
    corrs
    

[![download](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6b34025f6990c8b2d268f0e2d8ec2ccfdc40cbe5.png)download245×248 1.31 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6b34025f6990c8b2d268f0e2d8ec2ccfdc40cbe5.png> "download")

Maybe beta regression, rather than logistic regression changes that picture. Interesting thought. Alternatively, maybe there is some way to break up the tournament into 5 class-vs-other-classes, and put the results back together. The whole “extremes are correlated” reminds me of my **badtimes** and **goodtimes** models, which are also almost p/1-p :-). Have to think more.

---

### Post #3 — **lackofintelligence** | 2020-07-04 22:52 UTC

[@wacax](</u/wacax>) , I think there is a nice use for the beta distribution – one that keep staring us in the face. This may be parallel or incongruent to what you are doing. Either way, do you have a routine for estimating its parameters and the errors on those parameters? There is a NIST article outlining the maximum likelihood method of obtaining the parameters using estimates of the moments of the distribution which are used to obtain initial values. Looks a bit hairy, but I am wonder how different the maximum likelihood estimates would be from the initial estimates and if simple propagation of errors on the statistics would give values that one could be confident in.

<https://www.itl.nist.gov/div898/handbook/eda/section3/eda366h.htm>

---

### Post #4 — **wacax** | 2020-07-05 01:05 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> do you have a routine for estimating its parameters and the errors on those parameters?

No, I don’t. Hopefully, if you figure it out, you can share with us more about this mysterious use you are talking about.

---

### Post #5 — **lackofintelligence** | 2020-07-05 17:27 UTC

Yup, I figured out how to do it. The mysterious use is to use the beta function to fit the out-of-sample scores during cross-validation. Why the beta function? Because it naturally lives on an interval, and comes with skew and excess kurtosis, unlike the Normal distribution which does not live on an interval and has no skew or excess kurtosis. We can map the beta function to the interval of correlations, [-1,1]. Once you have used maximum likelihood to fit the distribution of scores you can derive any kind of estimator you like from it. In particular maximum likelihood estimates are robust against spurious fluctuations that are statistically guaranteed to occur during parameter optimization. See how nicely it fits our data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/6178af5332549d3acff15ead09065b4a357b31c6_2_690x245.png)image1045×372 24.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6178af5332549d3acff15ead09065b4a357b31c6.png> "image")

  
I also considered the Logit-Normal, but in the limit that the standard deviation goes to zero, the skew and excess kurtosis also go to zero and that is contrary to what is observed. I am exploring the Beta-Ratio, the ratio of the areas of the fitted beta distribution above and below some threshold, in some sense similar to the sortino ratio, but it remains finite no matter where you set the threshold.
