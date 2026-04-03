---
title: "Announcing the M6 Forecasting competition"
category: Data Science
url: https://forum.numer.ai/t/announcing-the-m6-forecasting-competition/4899
created_at: 2022-02-05T12:21:32.524000+00:00
last_posted_at: 2022-08-18T14:13:15.470000+00:00
posts_count: 13
views: 2755
tags: []
---

# Announcing the M6 Forecasting competition

---

### Post #1 — **smakridakis** | 2022-02-05 12:21 UTC

[![Promotion Ad](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2ff2320c07eab5f010f7272688aaca0b19c0f401_2_439x500.png)Promotion Ad598×680 361 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ff2320c07eab5f010f7272688aaca0b19c0f401.png> "Promotion Ad")

The aim of the M6 Competition is similar to the previous five: that is to empirically identify the most appropriate way of forecasting financial (stock and ETF) prices as well as to investigate the connection between the accuracy of such forecasts and the associated returns on investment. Its purpose is to shed new light on the EMH (Efficient Market Hypothesis) by explaining the poor performance of professionally managed funds, as well as the exceptional achievements of the likes of Warren Buffet, Peter Lynch and George Soros as well as celebrated firms including Blackstone, Bridgewater Associates and Renaissance Technologies. An objective of the M6 competition is to learn as much as possible about the factors producing above average financial returns and their relation to accurate forecasting while explaining deviations from the EMH and why they occur.

---

### Post #2 — **johnnywhippet** | 2022-02-05 12:48 UTC

[Announcing the M6 forecasting competition - International Institute of Forecasters](<https://forecasters.org/blog/2022/01/19/announcing-the-m6-forecasting-competition/#:~:text=The%20M6%20competition%20allows%20for,of%20time%20horizon%20and%20duration>).

---

### Post #3 — **perfect_fit** | 2022-02-07 17:41 UTC _(reply to #2)_

Awesome! Thanks for the heads-up! Will definitely monitor it. Each M competition results in so many interesting approaches, blog posts, papers, etc. on time-series forecasting!

---

### Post #4 — **autratec** | 2022-02-08 01:11 UTC

I am new to M6. Going through the content, looks like there are some similarity to Singal competition. Can any one share the thoughts of rank 1 to 5 and how to transfer our existing Signal model to join M6 ?

---

### Post #5 — **smakridakis** | 2022-02-08 08:09 UTC _(reply to #3)_

We hope to have a greater participation from the Numerai community as M6 is concerned in addition to forecasting with returns on investments.

---

### Post #6 — **smakridakis** | 2022-02-08 08:12 UTC _(reply to #4)_

Anything that will promote M6 to the Numerai community will help to improve participation

---

### Post #7 — **of_s** | 2022-02-08 14:20 UTC _(reply to #4)_

There’s an easy setup [here](<https://github.com/microprediction/precise/blob/main/examples_m6/m6_competition_entry.ipynb>) and [full definitions](<https://github.com/microprediction/precise/tree/main/precise/skatertools/m6>) available.

---

### Post #8 — **autratec** | 2022-02-10 06:59 UTC

can any one share more details how to covert an existing signal model to participate M6 ? for example, how to collect 50 equity and 50 ETF data ? any idea of generating rank 1 to rank 5 ? is it different target prediction ? how the decision should be calculated based on rank 1 to 5 ? and asset allocation strategy ?

---

### Post #9 — **of_s** | 2022-02-10 13:27 UTC _(reply to #8)_

In the links to the repo provided above, there are scripts that download the data from yahoo. You have to alter the security universe from the Signals ticker list as M6 is not a subset of Signals. This is also available in the M6 repo <https://github.com/Mcompetitions/M6-methods> .

In the `full definitions` link, there are scripts that use Monte Carlo methods to generate the rank probabilities, specifically: <https://github.com/microprediction/precise/blob/main/precise/skatertools/m6/quintileprobabilities.py>

The final step of generating portfolio weights, well, there’s a lot of options available also in the repo linked above:  
(<https://github.com/microprediction/precise/tree/main/precise/skaters/portfoliostatic>)

All of which require a covariance matrix to generate a portfolio. The linked repo also contains numerous methods of generating covariance matrices as well as Elo ratings of their out of sample performance.  
(<https://github.com/microprediction/precise/tree/main/precise/skaters/covariance>)  
Note the partial moments ones do quite well ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10)  
<https://github.com/microprediction/precise/blob/main/examples_colab_notebooks/elo_ratings_and_code_urls_2022_02.ipynb>

Finally, if you’re super lazy, you can just have one of the covariance matrices selected at random and one of the portfolio methods picked at random, generating a .csv submission file as demonstrated here:  
(<https://github.com/microprediction/precise/blob/main/examples_m6/m6_competition_entry.ipynb>)

You’re welcome!

---

### Post #10 — **lcrmorin** | 2022-02-13 16:28 UTC _(reply to #9)_

Not sure to understand how your MC method works. For the moment I mainly use simple randomised models. I am looking into pobabilistic modelling ([NGBoost: Natural Gradient Boosting for Probabilistic Prediction](<https://stanfordmlgroup.github.io/projects/ngboost/>)) for the ranking part. Not sure how to build decisions out of predictions / ranking. Will probably share some intro notebooks soon.

---

### Post #11 — **nick_richers** | 2022-05-10 03:51 UTC _(reply to #9)_

You can find microprediction slack invitation button everywhere on their website, but it is currently private to some email domains, is it on purpose? Someone here has access? Is it worth?

---

### Post #12 — **of_s** | 2022-05-10 04:00 UTC _(reply to #11)_

No idea about any email domain restrictions, but it’s a good overall discussion on time-series.

EDIT: The invites expire so that may be the issue, check out [microprediction (Peter Cotton) · GitHub](<https://github.com/microprediction>) if interested.

---

### Post #13 — **microprediction** | 2022-08-18 14:13 UTC _(reply to #12)_

Hi,

I’m the maintainer of a few packages (precise, timemachines etc) that may or may not be useful to those entering portfolio contests. Somebody from the microprediction slack pointed me to this thread.

Just a few quick responses, points:

  * Yeah sorry about the microprediction slack invite. I don’t know why they make it hard and there is no intent not to invite anyone. They just force me to recycle it every month so there are stale ones lying around. See [slack invite](<https://microprediction.github.io/microprediction/slack.html>) page for the definitive invite and hassle me if that’s stale. Or you can find me on LI and DM me your email.
  * I’m not involved with Numerai although I think it is a pioneering effort. I work for Intech Investments.
  * If you want to use online covariance estimation in Numerai you might be interested in [this doc page](<https://microprediction.github.io/precise/covariance.html>)
  * If you are entering M6 you’ll probably want to look at elsewhere in the same docs, though whether that translates to Numerai I don’t know.



Cheers,

Peter
