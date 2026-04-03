---
title: "What is the intended effect of gaussianization in Signals neutralization?"
category: Signals
url: https://forum.numer.ai/t/what-is-the-intended-effect-of-gaussianization-in-signals-neutralization/4333
created_at: 2021-10-14T16:12:05.731000+00:00
last_posted_at: 2021-10-21T01:33:03.225000+00:00
posts_count: 2
views: 927
tags: []
---

# What is the intended effect of gaussianization in Signals neutralization?

---

### Post #1 — **mugamma** | 2021-10-14 16:12 UTC

This old signals scoring example

[github.com](<https://github.com/numerai/example-scripts/blob/ac461829258858b6f342fd2ad55e076016912876/SignalsScoringExample.ipynb>)

#### [numerai/example-scripts/blob/ac461829258858b6f342fd2ad55e076016912876/SignalsScoringExample.ipynb](<https://github.com/numerai/example-scripts/blob/ac461829258858b6f342fd2ad55e076016912876/SignalsScoringExample.ipynb>)
    
    
    {
     "cells": [
      {
       "cell_type": "code",
       "execution_count": 326,
       "metadata": {},
       "outputs": [],
       "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import scipy"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "## Make Toy Dataframe Containing  Prediction Data"
       ]
      },
    

This file has been truncated. [show original](<https://github.com/numerai/example-scripts/blob/ac461829258858b6f342fd2ad55e076016912876/SignalsScoringExample.ipynb>)

(no longer in master BTW)

has this code after converting to ranks and re-centering on zero, and before calculating feature exposures.
    
    
    # gaussianize predictions to make the data more natural for the neutralization
    df["gaussianized_preds"] = scipy.stats.norm.ppf(df["ranked_preds2"])
    

What is it supposed to do? “more natural” is not helpful. Most data cleaning arguments don’t apply since the predictions were already converted to rank space.

Mathematically, it is reshaping the distribution so that the top and bottom **pre-neutralized** predictions are farther from the mean than they would have been in rank space.

Here’s an example with a 100 predictions and no holes.
    
    
    >>> scipy.stats.norm.ppf((df["x"].rank() - 0.5) / 100)
    array([-2.5758293 , -2.17009038, -1.95996398, -1.81191067, -1.69539771,
           -1.59819314, -1.51410189, -1.43953147, -1.37220381, -1.31057911,
           -1.25356544, -1.20035886, -1.15034938, -1.10306256, -1.05812162,
           -1.01522203, -0.97411388, -0.93458929, -0.89647336, -0.85961736,
           -0.82389363, -0.78919165, -0.75541503, -0.72247905, -0.69030882,
           -0.65883769, -0.62800601, -0.59776013, -0.5680515 , -0.53883603,
           -0.51007346, -0.48172685, -0.45376219, -0.42614801, -0.39885507,
           -0.37185609, -0.34512553, -0.31863936, -0.2923749 , -0.26631061,
           -0.24042603, -0.21470157, -0.18911843, -0.16365849, -0.13830421,
           -0.11303854, -0.08784484, -0.06270678, -0.03760829, -0.01253347,
            0.01253347,  0.03760829,  0.06270678,  0.08784484,  0.11303854,
            0.13830421,  0.16365849,  0.18911843,  0.21470157,  0.24042603,
            0.26631061,  0.2923749 ,  0.31863936,  0.34512553,  0.37185609,
            0.39885507,  0.42614801,  0.45376219,  0.48172685,  0.51007346,
            0.53883603,  0.5680515 ,  0.59776013,  0.62800601,  0.65883769,
            0.69030882,  0.72247905,  0.75541503,  0.78919165,  0.82389363,
            0.85961736,  0.89647336,  0.93458929,  0.97411388,  1.01522203,
            1.05812162,  1.10306256,  1.15034938,  1.20035886,  1.25356544,
            1.31057911,  1.37220381,  1.43953147,  1.51410189,  1.59819314,
            1.69539771,  1.81191067,  1.95996398,  2.17009038,  2.5758293 ])
    

Note the bigger spacings between values at the beginning and end compared to the middle. That means that the distribution is stretched from the previous uniform [0,1] from ranking and [-0.5,0.5] after recentering. With 5K signals, it’s stretched to about [-3.7,3.7], but it is stretched more at the ends than in the middle.

As far as I can tell, the principal effect is to increase the importance of the pre-neutralization extremes in the neutralization calculation. That’s a bit hand wavy, but it is well known that outlier values disproportionately affect ordinary linear regressions because of the quadratic penalty. Still hand waving, I think this increases the neutralization of pre-neutralization top and bottom signals, and more information is left behind in the middle which is neutralized less compared to without gaussianization.

This sounds wonky to me given the dialogue about TB200 after neutralization being interesting. The math overweights TB200 before neutralization.

At this point, I think it is pretty clear that Signals neutralization is not just doing this -

> The point of the neutralization is to isolate the original or orthogonal component of the signal that is not already present in known signals.  
>  (from [Overview | Numerai Docs](<https://docs.numer.ai/numerai-signals/signals-overview#neutralization>))

I imagine this gaussianization transform potentially opens up an exploit where the top and bottom predictions are designed to be neutralized to near zero, and the middle predictions are based on a linear model of features used by Numerai and can get paid for correlations with those features. The basic construction would use two linear models from features assumed to be used by Numerai. One would be for the pre-neutralization top and bottom predictions, and one would be for the middle predictions actually trying to get paid. The former would be mostly neutralized away, and the latter would survive and become the top and bottom neutralized predictions. But both would still look linear in Numerai features. The actual exploit would be harder than this brief description, since the initial rank space transformation would complicate things.

So what was really intended from gaussianization?

---

### Post #2 — **habakan** | 2021-10-21 01:33 UTC

Thanks for the interesting insight.  
Could we also consider neutralization in terms of OLS normality?  
The fact that the neutralization of numerai uses the normal equation suggests that it is the same problem as the estimation of OLS.  
If so, from the viewpoint of normality, it is also assumed that the residuals ε (prediction after neutralize in numerai) follow a normal distribution.  
However, there is a possibility that the neutralized ε does not follow a normal distribution depending on the features and predictions.  
In order to deal with this situation, we can think of the predictions as being Gaussianized in advance. (I understand that the Box-Cox transformation is a method proposed with a similar background.)  
However, the insufficient part of this idea is how it contributes to performance by guaranteeing that ε follows a normal distribution.
