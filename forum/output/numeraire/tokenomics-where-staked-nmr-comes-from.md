---
title: "Tokenomics, where staked NMR comes from"
category: Numeraire
url: https://forum.numer.ai/t/tokenomics-where-staked-nmr-comes-from/4988
created_at: 2022-02-23T13:14:23.974000+00:00
last_posted_at: 2022-03-13T14:38:47.337000+00:00
posts_count: 5
views: 2585
tags: []
---

# Tokenomics, where staked NMR comes from

---

### Post #1 — **nyuton** | 2022-02-23 13:14 UTC

Hi,

I see that the NMR at stake is increasing quickly, which is good.

What’s even more interesting for the future of NMR is, how much of this increase comes from payouts and how much is newly purchased and staked NMR. Obviously the payout comes from Numerai and it doesn’t increase demand or decrease supply. Newly purchased and staked NMR does.

So I did some calculations based on the data available through the api.  
You can find the details here: [numerai/Tokenomics.ipynb at main · nemethpeti/numerai · GitHub](<https://github.com/nemethpeti/numerai/blob/main/Tokenomics.ipynb>)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/482a207db5930b131e9a6802c7b3f59fb4f4698b_2_690x285.png)image893×369 46 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/482a207db5930b131e9a6802c7b3f59fb4f4698b.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0a6da392a1ad45a4d1b8766d028c2b903f2316f6.png)image656×130 5.68 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0a6da392a1ad45a4d1b8766d028c2b903f2316f6.png> "image")

Also wanted to figure out how many data scientists work behind these models. I couldn’t find a way to link models to users, so I just counted the models with >1NMR stake. That eliminates all models, which got some free NMR at the beginning.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/55a8bff9f2b7d12f1a8fd2d6273755e6916ddca1_2_690x292.png)image883×374 23.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55a8bff9f2b7d12f1a8fd2d6273755e6916ddca1.png> "image")

Please check out the notebook for more details

---

### Post #2 — **jay1100** | 2022-02-23 13:38 UTC

This is very interesting. Could you do the same plot for signals?

---

### Post #3 — **nyuton** | 2022-02-24 09:02 UTC _(reply to #2)_

Here it goes for Signals:

[github.com/nemethpeti/numerai](<https://github.com/nemethpeti/numerai/blob/main/Tokenomics_signals.ipynb>)

#### [Tokenomics_signals.ipynb](<https://github.com/nemethpeti/numerai/blob/main/Tokenomics_signals.ipynb>)

[`main`](<https://github.com/nemethpeti/numerai/blob/main/Tokenomics_signals.ipynb>)
    
    
    {
     "cells": [
      {
       "cell_type": "code",
       "execution_count": 2,
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
        "import seaborn as sns\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
    

This file has been truncated. [show original](<https://github.com/nemethpeti/numerai/blob/main/Tokenomics_signals.ipynb>)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7335fb5a9c6a5a92933ed3bf105bb89520cf2278_2_689x275.png)image1279×510 63.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7335fb5a9c6a5a92933ed3bf105bb89520cf2278.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f6f031f2c464be5e8ef7db0d4a5e17376c53ff3f_2_690x288.png)image1246×521 39.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f6f031f2c464be5e8ef7db0d4a5e17376c53ff3f.png> "image")

Alltogether it looking good!  
12% of the total circulating suppy is being utilized for staking at Numerai and it’s generating USD profit (for the fund).  
Over the inspected timeframe >3% of the supply was purchased for staking (without payouts)

If you compare it to bitcoin and others, which don’t have much utility at all ( holding and speculative trading is not a utility)…

More people and NMR are flocking to signals, while the tournament is stable. Despite the lowering payout ratio, people are not withdrawing their NMR.

---

### Post #4 — **jay1100** | 2022-02-24 09:52 UTC _(reply to #3)_

Very interesting. Thank you!

---

### Post #5 — **alexsunny123** | 2022-03-13 14:38 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> Alltogether it looking good!  
>  12% of the total circulating suppy is being utilized for staking at Numerai and it’s generating USD profit (for the fund).  
>  Over the inspected timeframe >3% of the supply was purchased for staking (without payouts)
> 
> If you compare it to bitcoin and others, which don’t have much utility at all ( holding and speculative trading is not a utility)…
> 
> More people and NMR are flocking to signals, while the tournament is stable. Despite the lowering payout ratio, people are not withdrawing their NMR.

thanks for the awesome information.
