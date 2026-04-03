---
title: "What exactly is neutralization?"
category: Data Science
url: https://forum.numer.ai/t/what-exactly-is-neutralization/2016
created_at: 2021-02-26T21:25:14.380000+00:00
last_posted_at: 2021-12-08T15:19:26.293000+00:00
posts_count: 12
views: 7025
tags: []
---

# What exactly is neutralization?

---

### Post #1 — **minokawa** | 2021-02-26 21:25 UTC

The final stage of the data pipeline is the data neutralization, however it’s a technique I’ve not come across and googling the term “data neutralization” leads to nothing I can find!?

Is this a term that Numerai has adopted or is it known as something else in general data science?

And in terms of what it’s actually doing, it seems to be softening up the correlations of the predictions against the features, but I don’t have a great understanding of it, can anyone offer a more thorough explenation of data neutralization please ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) ?

---

### Post #2 — **gbrecht** | 2021-02-26 21:38 UTC

The idea is that you use a linear model (that is defined by the features) and you subtract that from your predictions, therefore removing that signal from your predictions or in other words: neutralizing them against the features.  
On youtube there is excellent material from arbitrage and also in the forum there is an in depth post on this.

---

### Post #3 — **minokawa** | 2021-02-26 22:25 UTC

Thanks! I think I understand it in terms of the subtraction from a naive linear model ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

In the `analysis_and_tips` notebook however ([example-scripts/analysis_and_tips.ipynb at master · numerai/example-scripts · GitHub](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>)) the neutralization function defined there doesn’t seem to make a linear model of any sort but instead subtracts a proportion of some dot product of the pseudo-inverse of features (see code below), this is quite confusing.
    
    
    def _neutralize(df, columns, by, proportion=1.0):
        scores = df[columns]
        exposures = df[by].values
        scores = scores - proportion * exposures.dot(numpy.linalg.pinv(exposures).dot(scores))
        return scores / scores.std(ddof=0)

---

### Post #4 — **themicon** | 2021-02-27 08:58 UTC _(reply to #3)_

Here is the reason that we want to feature neutralize: [Feature Exposure Clipping Tool, and working code to deploy locally | Numerai FN Special Part 3 - YouTube](<https://www.youtube.com/watch?v=LQBjZL-PnLU#t=6m46s>)

And the notebook discussed in that video can be found here: [twitch/FE_Clipping_Script.ipynb at master · jonrtaylor/twitch · GitHub](<https://github.com/jonrtaylor/twitch/blob/master/FE_Clipping_Script.ipynb>)

---

### Post #5 — **dnos** | 2021-02-27 18:32 UTC

Someone correct me if I’m wrong but I like to think of it as removing any one feature’s influence on predictions such that the resulting predictions are evenly influenced by all dependent features

---

### Post #6 — **kreator** | 2021-03-01 06:59 UTC _(reply to #5)_

I would say that a linear model/the inverse of the matrix is “influenced” by all columns/features. The computation generally involves all columns to get the result for one column. But for the rest I mainly agree. In my understanding you take out the **linear** effect of the features and want to get something that depends more on the aggregate of all features.

---

### Post #7 — **inadacondition** | 2021-03-05 22:56 UTC

I was also confused by the way neutralization was done. I could see that what we are getting at is simply running a linear regression of predictions on features then residualizing that out from predictions. That was the idea in my mind, but as you mentioned, the code itself uses a pseudo-inverse and not the normal inverse of variance of predictors formula.

Well it turns out a pseudo-inverse is the solution to the least squares problem. I have a little explainer below. I assume an L-2 norm, of course if we change the norm then we change how we “neutralize”, which could be a interesting avenue:

[![Screen Shot 2021-03-05 at 5.53.56 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/06379dc278e3bac5bb48e8d8c5448ea843631009.png)Screen Shot 2021-03-05 at 5.53.56 PM1046×754 27.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/06379dc278e3bac5bb48e8d8c5448ea843631009.png> "Screen Shot 2021-03-05 at 5.53.56 PM")

---

### Post #8 — **finchalex** | 2021-05-12 16:44 UTC

A **neutralization** reaction is when an acid and a base react to form water and a salt and involves the combination of H+ ions and OH- ions to generate water. The **neutralization** of a strong acid and strong base has a pH equal to 7. … Table 1: The most common strong acids and bases

* * *

[Custom Bottled Water](<https://www.thewaterdepot.com/>)

---

### Post #9 — **wigglemuse** | 2021-05-12 17:49 UTC _(reply to #8)_

Most awesome “first post spam” I’ve yet seen…

---

### Post #10 — **one5hot76** | 2021-05-16 15:21 UTC

I was reading a chapter out of Machine Learning for Finanace by Jannes Klaas, yesterday. I hadn’t realized that with raw data a single feature’s “signal” could overpower signals received by the other features causing feature bias. The example it used was fraud cases in a bank transaction database where fraud was approximately 1% of the data. If you trained your model based on the data “as is”, the model would be biased towards valid transactions. If you neutralize the features then all of the signals have an equal vote towards the outcome and your model will be able to learn from all of them. At least that is how I understand it, now.

---

### Post #11 — **akak2021** | 2021-10-28 07:14 UTC

I’m a newbie and came across this great thread in the process of learning about neutralization. Thank you very much. I am new in Numerai, so forgive me if my comments are too obvious.

I think that the neutralization of a prediction for risky features is the first order approximation of the operation that removes the component that the risky feature contributes **alone** , leaving only **the interactions with other features**.

For simplicity, we will consider neutralizing for just one feature x_1.

Without loss of generality, we can assume that the true target value y is deterministically determined by the following function

![CodeCogsEqn\(1\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cac3a0bb32cf66a6419be4a4f9d035cbb7d9ee49.gif) (Eq.1)

Please note that f(x_1) is the component that only x contributes to y.

Under the assumption of ignoring terms above the second order, the neutralization for x_1 is equivalent to deleting f(x_1).

This result can be obtained through a calculation to find α and β that minimize the squared error of Eq.(1) and ![CodeCogsEqn\(2\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c2737126bd69f1e5d5f1de773d8616bc6e90026b.gif). (Unless my algebraic calculations are wrong…)

Since it is only a first-order approximation, this argument does not hold if the absolute value of the feature value is large.

I would appreciate any feedback.

---

### Post #12 — **bluesapphire** | 2021-12-08 15:19 UTC

Hello everyone, I’m new here - thanks for the excellent discussion on this thread.  
Let me offer a very simplistic Finance point of view:

Butchering traditional theory here, but return of a single security can be modeled as  
return = beta*market_return (call this the ‘linear model’, where market return is replaced by many worthy factors, and beta is a matrix) + alpha (the stock’s idiosyncratic return/excess return, which comes from the merit of the company/ability of management/etc)

So in this modeling exercise, by neutralizing (or subtracting the linear risk model) we are trying to break down into quartiles all current stocks according to their ability to generate excess return.

Needless to say, ‘neutralization’ is a necessary step in running a ‘market neutral’ fund.

(OK, now just think of the traditional quants, whose models stop at that linear risk model - that’s more than 70% of the industry)

Comments?
