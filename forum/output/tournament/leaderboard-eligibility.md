---
title: "Leaderboard eligibility"
category: Tournament
url: https://forum.numer.ai/t/leaderboard-eligibility/2704
created_at: 2021-04-05T21:11:54.668000+00:00
last_posted_at: 2021-04-07T16:02:35.590000+00:00
posts_count: 4
views: 1169
tags: []
---

# Leaderboard eligibility

---

### Post #1 — **dion81** | 2021-04-05 21:11 UTC

hello, i made my first submission but i am not in the leaderboard, which submissions are eligible for the leadearboard?

---

### Post #2 — **themicon** | 2021-04-05 22:37 UTC

If you just submitted your first “daily score” will be out on Thursday, but a single round is 4 weeks long. The daily scores from now until your first round resolves don’t really matter, only the final score at the end of the 4 weeks.

The leaderboard is the weighted average over the last 20 rounds. So you are going to need to wait at least 24 weeks before you will have a full idea of your position on the leaderboard. Empty rounds have a -0.1 correlation score for every round you don’t submit.

This is a long game and the leaderboard isn’t what you should be focusing on. With the rounds being 4 weeks long, you are going to have to be patient to see the results of your modelling work.

---

### Post #3 — **dion81** | 2021-04-07 08:58 UTC _(reply to #2)_

Thank you very much for your reply!really appreciated …my next concern is how to optimize the numbers appeared in ‘‘performance’’, ‘‘risk’’, ‘‘mmc’’(3 each)?  
all i found are these formulas :

def _score(sub_df: pd.DataFrame) → np.float32:  
“”“Calculates Spearman correlation”""  
return spearmanr(sub_df[“target”], sub_df[“prediction”])[0]
    
    
    # Calculate metrics
    corrs = df.groupby("era").apply(_score)
    payout_raw = (corrs / 0.2).clip(-1, 1)
    spearman = round(corrs.mean(), 4)
    payout = round(payout_raw.mean(), 4)
    numerai_sharpe = round(sharpe_ratio(corrs), 4)
    mae = mean_absolute_error(df["target"], df["prediction"]).round(4)
    
    
    
    Shouldn't be a formula for each of 9 metrics (performance,risk,mmc)?

---

### Post #4 — **ml_is_lyf** | 2021-04-07 16:02 UTC _(reply to #3)_

Take a read of this, should answer your questions on the definitions of the metrics

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png)

[Model Diagnostics Update](<http://forum.numer.ai/t/model-diagnostics-update/902>) [Announcements](</c/announcements/8>)

> [[image]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/abfec3344ca67c7e6b56e400a615d77dc1117dba.png> "image") Starting with the coming round, you will receive additional information about your model when you submit. These metrics will better inform users about the strengths and weaknesses of their models, and give users more direction and insight into the nuances of this unique problem. The metrics are split into 3 categories. Performance - Overall measures of performance over the validation set. Risk - Different ways to assess how likely it is that your model has severe burns in the futur…
