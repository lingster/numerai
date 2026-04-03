---
title: "Another way to optimize for TC"
category: Data Science
url: https://forum.numer.ai/t/another-way-to-optimize-for-tc/5740
created_at: 2022-10-03T09:38:43.794000+00:00
last_posted_at: 2023-01-05T16:35:47.967000+00:00
posts_count: 23
views: 2946
tags: []
---

# Another way to optimize for TC

---

### Post #1 — **nyuton** | 2022-10-03 09:38 UTC

Hi,

We have seen some great forum posts on how other metrics are correlated with TC and how to optimize for it.  
Like these ones here:  
<http://forum.numer.ai/t/true-contribution-details/>  
<http://forum.numer.ai/t/a-true-contribution-backtest/>

One key aspect has been overlooked so far, even tough it seems obvious and [@richai](</u/richai>) even talked about it briefly during Numercon. He said, that a models correlation with the metamodel should be below 0.5, if we we want a significant contribution from it.

TC is kind of a measure of uniqueness. So is the correlation with the metamodel. The above mentioned posts ignore this simple metric, even though it seems meaningful.

I’ve downloaded the closed round details for all staked models from round 300 and looked at the correlations.

To cut things short. Here is the data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9ca09f53c4150211dcbb0d066470ceb409bdbe1.png)image607×214 7.24 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9ca09f53c4150211dcbb0d066470ceb409bdbe1.png> "image")

As expected we get negative correlation between TC and corrWMetamodel. While the correlation of TC and corrWMetamodel is lower than that of other metrics, it’s still significant.

Here I plot the mean TC agains the deciles of metamodel correlation.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12bed08c3fc2d7002bddf5465f373c247eda9aa4.png)image505×319 24.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12bed08c3fc2d7002bddf5465f373c247eda9aa4.png> "image")

---

### Post #2 — **nyuton** | 2022-10-03 12:21 UTC

Things get even more clear, when I select models only with >10NMR steak:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8d0a2c1638e92bffc041309dfd2fcb9c77d5bd18.png)image512×338 25.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8d0a2c1638e92bffc041309dfd2fcb9c77d5bd18.png> "image")

Looks like [@richai](</u/richai>) was right and we should clearly seek to optimize for low metamodel correlation.

---

### Post #3 — **nyuton** | 2022-10-03 12:49 UTC

Notebook available here, just in case you want to tweak the parameters:

[github.com](<https://github.com/nemethpeti/numerai/blob/main/MM%20Corr%20on%20TC.ipynb>)

#### [nemethpeti/numerai/blob/main/MM Corr on TC.ipynb](<https://github.com/nemethpeti/numerai/blob/main/MM%20Corr%20on%20TC.ipynb>)
    
    
    {
     "cells": [
      {
       "cell_type": "code",
       "execution_count": 1,
       "metadata": {
        "colab": {
         "base_uri": "https://localhost:8080/"
        },
        "id": "3ZopopM9WCP_",
        "outputId": "157095a8-b46e-4eed-e283-d3994d4b6c47"
       },
       "outputs": [],
       "source": [
        "from numerapi import NumerAPI, utils\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "# initialize API client\n",
    

This file has been truncated. [show original](<https://github.com/nemethpeti/numerai/blob/main/MM%20Corr%20on%20TC.ipynb>)

---

### Post #4 — **kayeffnumeraitor** | 2022-10-03 18:02 UTC

Hello, thanks for the nice plots. I am not too surprised by these, as 100% correlation with the meta model also means most of the stake is already on this kind of prediction = low TC.

I have one problem though, as your post title mentions “optimize” for TC. For trying to optimize for TC by optimizing not being correlated with the meta model, you need the actual meta model predictions, which is something that i really wish would come with the train/test parquet files as an additional column.

Without these, it is again less “optimization” and more “cooking”, meaning you try out anything and stick with what (seemingly) works.

---

### Post #5 — **shatteredx** | 2022-10-03 19:40 UTC

Here are corr w/meta model bins in case anyone else is interested:  
[-1,  
0.4285466351580885,  
0.5349795884635565,  
0.6019820548100896,  
0.6484948268044857,  
0.691438100728163,  
0.7332765115467375,  
0.7667744838998147,  
0.8015134126302096,  
0.8459169152554307,  
1]

---

### Post #6 — **annon** | 2022-10-04 00:47 UTC _(reply to #4)_

I agree. I am currently using example prediction instead of metamodel prediction to improve TC.  
Because example has high corr with metamodel.  
If metamodel prediction is published, I think it would be very useful to improve TC.  
Is there any problem with making it public?

---

### Post #7 — **nyuton** | 2022-10-04 06:40 UTC _(reply to #4)_

You can approximate the MM with the example prediction and train your model to be differrent.  
Or, you can wait until the next Friday, where you get the exact figure on the MM correlation.  
MM correlation doesn’t change a lot over time, so seeing one can be enough. It’s still a lot faster feedback loop than waiting months for TC.

---

### Post #8 — **nyuton** | 2022-10-04 07:07 UTC _(reply to #5)_

Yup, thanks for adding it.

Unfortunately there isn’t much data in the low correlation range. Even though having low or even negative correlation could be very useful and profitable.

---

### Post #9 — **kayeffnumeraitor** | 2022-10-04 14:52 UTC _(reply to #6)_

I think it would only be a “problem” if the tournament would comprise of 1 very large staked model. In this case their predictions would be “leaked”. In the current tournament i dont see a problem with it.

---

### Post #10 — **greyone** | 2022-10-04 22:42 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d8d90a24dee8c5615e2f8956bd176330f2c2869f_2_601x500.png)image798×663 42.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d8d90a24dee8c5615e2f8956bd176330f2c2869f.png> "image")

  
Of the models that stake on TC, their collective record has been consistently positive since Round 322. Anything notable change since then?

---

### Post #11 — **wigglemuse** | 2022-10-04 23:29 UTC _(reply to #10)_

I think you’ll see corr tracking the same way. Some periods are just easier. (In other words, I don’t think any great discovery was made around 322 or the staking got any smarter – just normal ups & downs.) A rough difficulty score for each round can be had simply by looking at the percentage of all models that are positive vs negative for corr or tc for that round. When judging my own models I want them to be doing relatively well both in easy & hard rounds.

---

### Post #12 — **greyone** | 2022-10-05 10:13 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a43fe6e4f81261bee514299eb4ad98940144be25_2_583x500.png)image735×630 20.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a43fe6e4f81261bee514299eb4ad98940144be25.png> "image")

  
Good point. Looking back further, R308 to R322 was a TC bear…at least for TC staked models…

---

### Post #13 — **greyone** | 2022-10-05 10:15 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2970d1fc56fec348f83e81f5fa2154413cad793b_2_581x500.png)image724×622 30.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2970d1fc56fec348f83e81f5fa2154413cad793b.png> "image")

  
oddly, TC of Corr only staked models did well in that period.

---

### Post #14 — **greyone** | 2022-10-05 10:17 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e1d872d15da487ad9a7178bfc09839a4b644dfa2.png)image712×514 18.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e1d872d15da487ad9a7178bfc09839a4b644dfa2.png> "image")

  
relative performance is much smoother.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a582ea9f1e6785cae709ca6915d4062e48f25056_2_401x500.png)image730×910 31.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a582ea9f1e6785cae709ca6915d4062e48f25056.png> "image")

(DATA PRIOR TO R311 is not valid. Method mistakenly used models staking on MMC as using TC)

Only since R308 has the corr of TC staked models started to underperform the corr of Corr only models. Perhaps that is a sign of TC models turning up their focus and efficacy on TC.

---

### Post #15 — **restrading** | 2022-10-05 13:52 UTC _(reply to #14)_

[@greyone](</u/greyone>) TC staking only started since round 311. Also, how do you define a “TC staked model”? Do you take into account the change of their multipliers each round?

---

### Post #16 — **wigglemuse** | 2022-10-05 14:22 UTC

Yeah, there is some TC backfill there where no one was actually staking on TC. But yes also in all my newer TC-focused stuff I’ve just dropped even looking at corr – they are quite weak on corr.

---

### Post #17 — **greyone** | 2022-10-05 15:06 UTC _(reply to #15)_

[@restrading](</u/restrading>) thanks for catching that error. Method defined TC models by using the minimum absolute difference between actual NMR payout and the calculated options at 1C, 1C.5TC, 1C1TC, 1C2TC and 1C3TC. If min was 1C then that model was labeled Corr only. All others were labeled TC. Ergo, the data before Round 311 is in error because method assumes models betting on MMC were using TC. So discard all preR311 info. Appreciate you pointing the error.

My work often exemplifies the adage “one must be willing to be a fool before you can become wise”.

---

### Post #18 — **dzheng1887** | 2022-10-06 21:03 UTC _(reply to #6)_

I have been requesting this earlier this year for that reason to no avail ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12)

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/f475e1/48.png) [Historical Meta Model Predictions](<http://forum.numer.ai/t/historical-meta-model-predictions/5545>) [Tournament](</c/tournament/7>)

> Also, I believe in the meeting (something I watched on YouTube), they were saying we may have historical meta model predictions (and other generic model predictions) available to us for use in our models. Has that been released yet or still in progress? I would find the historical meta model predictions to be extremely valuable if I could find that somewhere. Thanks. 

<https://rocketchat.numer.ai/channel/feedback?msg=rfkgJ4Q8Tc7ZL6rYx>

How high is the example pred corr with meta model? I think statistically 90% correlated is probably sufficient to meaningfully proxy meta model but I am guessing based on rule of thumb

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/f475e1/48.png) [CORR with Meta Model](<http://forum.numer.ai/t/corr-with-meta-model/5569>) [Tournament](</c/tournament/7>)

> Hey would anyone have a model that is 90%+ correlation with meta model? I am trying to understand about what is in meta model to replicate it. I was thinking perhaps trying the Light GBM starter code they provided but figured I ask here first. Thanks.

---

### Post #19 — **wigglemuse** | 2022-10-06 21:12 UTC _(reply to #18)_

They said in today’s fireside that this is coming. (Historical meta-model predictions and probably also the ability to get historical TC estimates based on same.) Eventually we’ll get it…

---

### Post #20 — **dzheng1887** | 2022-10-06 21:13 UTC _(reply to #19)_

Thank you, between my job and other things, hard to keep up with this.

Never even gotten around to that LightGBM starter code haha, always worry about sinking time in without getting anything tangible out of it.

Can’t believe it’s already October too

---

### Post #21 — **nyuton** | 2022-12-08 10:27 UTC

@correlator created a chart that belongs here:  
It’s the distribution of the standard deviation of TC

As it seems, lower MMcorr comes with higher TC AND with higher volatility

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/37c1549bd05cbe54318151ad77dfc52250f029f0_2_690x358.png)image2464×1280 142 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/37c1549bd05cbe54318151ad77dfc52250f029f0.png> "image")

---

### Post #22 — **henrybecker361** | 2023-01-05 15:47 UTC

I’m not really surprised by the results, since a 100% correlation with the meta model also means most of the stake is already on that kind of prediction, which results in a low TC.

I do have one issue though. Your post title mentions “optimizing” for TC, but to really optimize for TC by trying to not be correlated with the meta model, you need the actual meta model predictions. It would be really helpful if the train/test parquet files included an additional column with these predictions.

Without that information, it feels like we’re just “cooking” - trying out anything and going with what seems to work, rather than truly optimizing.

Do you know if there’s a way to access the meta model predictions or if they’ll be included in future train/test parquet files?

---

### Post #23 — **wigglemuse** | 2023-01-05 16:35 UTC _(reply to #22)_

They are included with the new dataset. You can download them right now → [Numerai](<https://numer.ai/data/v4.1>)

see this: [Super Massive Data: Sunshine](<http://forum.numer.ai/t/super-massive-data-sunshine/5977/>)
