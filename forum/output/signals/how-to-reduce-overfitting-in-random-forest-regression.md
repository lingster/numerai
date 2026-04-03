---
title: "How to Reduce Overfitting in Random Forest Regression"
category: Signals
url: https://forum.numer.ai/t/how-to-reduce-overfitting-in-random-forest-regression/3608
created_at: 2021-06-16T12:26:48.569000+00:00
last_posted_at: 2021-06-18T21:28:55.220000+00:00
posts_count: 3
views: 1757
tags: []
---

# How to Reduce Overfitting in Random Forest Regression

---

### Post #1 — **kaiomarques93** | 2021-06-16 12:26 UTC

Hi,

I am trying to predict stocks prices using Random Forest Regression (rfr), and I’m using a function from scikit-learn like this

**rfr=RandomForestRegressor(random_state=200, oob_score=True, max_features=‘sqrt’)**

Now, I am using the r2_score with the test set and the predicted values to get an idea of the model’s accuracy. However I’m always getting a value for r2 above 0.9 which I think to be odd.

My data set has 30k data points. The only variable that I’m to change is the random_state. The goal of this post is to find an effective variable of the model which is able to control overfitting.

---

### Post #2 — **sneaky** | 2021-06-18 11:06 UTC

Hi, bias-variance tradeoff is a complex issue. I think it is well described for RandomForests here: <https://towardsdatascience.com/random-forests-and-the-bias-variance-tradeoff-3b77fee339b4> .

---

### Post #3 — **ageonsen** | 2021-06-18 21:28 UTC

How about setting max_features=int(1)?  
This is a good reference for Numerai Tournament;  
[https://poseidon01.ssrn.com/delivery.php?ID=029123122124116016116079103000088086046017064042000030023121064104123102009109030098059042125003033000013011018067017083069092045061037061029013099121103079098068046061084090104007105026069123066115104022026082067025122108023065086113079113019101024&EXT=pdf&INDEX=TRUE](<https://poseidon01.ssrn.com/delivery.php?ID=029123122124116016116079103000088086046017064042000030023121064104123102009109030098059042125003033000013011018067017083069092045061037061029013099121103079098068046061084090104007105026069123066115104022026082067025122108023065086113079113019101024&EXT=pdf&INDEX=TRUE>)
