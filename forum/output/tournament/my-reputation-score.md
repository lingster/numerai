---
title: "My reputation score"
category: Tournament
url: https://forum.numer.ai/t/my-reputation-score/3705
created_at: 2021-07-03T11:37:24.392000+00:00
last_posted_at: 2021-07-03T17:42:57.987000+00:00
posts_count: 5
views: 870
tags: []
---

# My reputation score

---

### Post #1 — **autratec** | 2021-07-03 11:37 UTC

As a newbie, joined tournament since June 2021, and submitted prediction couple times, I assume my reputation score should close 0. But currently, my score is close to -0.1, which more like a punishment to the repeating missing submissions.

Any advice here ?

---

### Post #2 — **ml_is_lyf** | 2021-07-03 11:59 UTC

Answered here:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/v_newbie/48/613_2.png) [Why all my model scores started from -0.1?](<http://forum.numer.ai/t/why-all-my-model-scores-started-from-0-1/2645>) [Tournament](</c/tournament/7>)

> Hi guys, All my submissions started from -0.1. The first model I submitted was from the tutorial notebook so I thought it was because the late submisssion. But the models I submitted in time last week were all started from -0.1 as well. Is it expected please? Many thanks, V

---

### Post #3 — **autratec** | 2021-07-03 12:40 UTC _(reply to #2)_

Here was what written in the document:

The first late or missed submission will receive the score equivalent to the `example_predictions`. Subsequent late or missed submissions will receive a very low score of `-0.1`.

-0.1 is like a punishment for the second missing submission which might not be appliy to me as a new comer.

---

### Post #4 — **ml_is_lyf** | 2021-07-03 15:59 UTC _(reply to #3)_

Yep, newcomers are treated as if they missed submissions for rounds before they joined. The reason for that is your score over a couple of rounds isn’t informative as to how well your model performs. If they took rounds as 0 for new joiners for rounds they’d missed, you’d have new joiners all over the leaderboard, and their ranks would be volatile until they hit the 20 rounds of history. This would make the leaderboard noisy, and it’d be hard to see which models are performing well over time. The way its setup newcomers start at the bottom of the board and rise up, which is much more natural.

---

### Post #5 — **gammarat** | 2021-07-03 17:42 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> Any advice here ?

Yes, don’t worry about it ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)  
If you want a better estimate of how your models are performing, go to your “models” page, and look at the rainbow graph at the bottom. Set the graph type to “cumulative”, take the most recent values, and divide those by the number of rounds they have actually been submitted. This gives a number that can be compared more reasonably against the leaderboard.

FWIW, if for some reason you can’t make a submission on a given week, (e.g. your model crashed or you’ve got the flu, that sort of one off thing), just submit the example prediction that comes with the data. That will keep you from getting a -0.1 score on that week’s round.
