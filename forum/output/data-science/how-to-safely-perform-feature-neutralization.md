---
title: "How to Safely Perform Feature Neutralization"
category: Data Science
url: https://forum.numer.ai/t/how-to-safely-perform-feature-neutralization/1015
created_at: 2020-10-03T01:54:11.239000+00:00
last_posted_at: 2020-10-03T23:54:10.449000+00:00
posts_count: 4
views: 2771
tags: []
---

# How to Safely Perform Feature Neutralization

---

### Post #1 — **lackofintelligence** | 2020-10-03 01:54 UTC

For some time I have been investigating feature neutralization as the final step in a prediction pipeline. The idea has been, instead of just sprinkling on feature neutralization using some arbitrary neutralization proportion and testing with the validation set, or worse, live, to find the value of the proportion that optimizes for the metric I am working with. In all of my attempts so far just using the standard formulas given in various posts that can be found on chat, in the hints notebook and here in the forum, that effort has been disappointing. Those runs always end with the optimization picking a value of zero for the feature neutralization proportion, pretty much proving that standard feature neutralization is no good for my models. It does not seem to matter if the feature neutralization is performed grossly or by era.

Before [@mdo](</u/mdo>) made his post about a different FN take, I started to get some clues that not all linearity is bad and recently switched to using a regularized linear model to calculate the exposed components of my models. That is the trick, the optimization converges on a value of the FN proportion that is significantly greater than zero (or 0.1 for that matter).

I am not going to share any code, sorry. But I will just quickly summarize: Dont use numpy or scipy versions of pinv. Instead find, or better create, a simple linear algorithm that is regularized using both L1 and L2 constraints.

---

### Post #3 — **jrb** | 2020-10-03 14:04 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> In all of my attempts so far just using the standard formulas given in various posts that can be found on chat, in the hints notebook and here in the forum, that effort has been disappointing. Those runs always end with the optimization picking a value of zero for the feature neutralization proportion, pretty much proving that standard feature neutralization is no good for my models.

Well then, perhaps it’s time to consider building better models, and stop throwing away entire feature groups as your user name suggests. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #4 — **lackofintelligence** | 2020-10-03 20:47 UTC _(reply to #3)_

There has got to be an art to piling one presumption on top of another presumption. Can we stick to the data science discussion, please? I would be very happy if you said something like, “that doesn’t work”, here’s why, etc. I am sure its not hard for you to quickly cook up some regularization code schemes that other people can easily utilize. I am sure people would applaud you for that.

Hit the poll I made on data science using any models pre - [@mdo](</u/mdo>) FN alternative take, just not using a metric that explicitly takes into account the feature exposure.

---

### Post #5 — **jrb** | 2020-10-03 23:54 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> I am sure its not hard for you to quickly cook up some regularization code schemes that other people can easily utilize. I am sure people would applaud you for that.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> I am not going to share any code, sorry.

I’ll just follow suit.
