---
title: "Model ranked low....predictions CSV comparison?"
category: Tournament
url: https://forum.numer.ai/t/model-ranked-low-predictions-csv-comparison/1610
created_at: 2021-02-08T17:43:16.328000+00:00
last_posted_at: 2021-02-08T20:07:45.704000+00:00
posts_count: 6
views: 838
tags: []
---

# Model ranked low....predictions CSV comparison?

---

### Post #1 — **goldnumberone** | 2021-02-08 17:43 UTC

I submitted a model and was ranked very low; I see a lot of other people that have tied at that rank so I’m wondering if there’s a fundamental problem with the submitted predictions CSV.

Can someone in a higher rank share one of their older predictions CSV files? Or is there an example I can look at on the Numerai site?

---

### Post #2 — **arbitrage** | 2021-02-08 17:45 UTC

you can download the example predictions and compare. the corresponding model is numer.ai/integration_test

---

### Post #3 — **wigglemuse** | 2021-02-08 18:11 UTC

Can you clarify what you are talking about? Your leaderboard rank is cumulative over 20 rounds, so when someone submits for the first time they will always have a horrible rank because it takes time to build it up. (Even if you are doing awesome on the round you submitted.)

---

### Post #4 — **goldnumberone** | 2021-02-08 18:16 UTC _(reply to #3)_

I was wondering if my predictions CSV had errors in it that would cause low rankings but what you said makes sense, it’ll build up rank over time.

Though I did discover issues when comparing my predictions CSV to the example predictions; my submission has far less precision (0.25 instead of 0.2499 for example).

---

### Post #5 — **wigglemuse** | 2021-02-08 18:26 UTC _(reply to #4)_

Yeah, you should avoid ties in your predictions as much as possible, i.e. try to have all unique values. (Even though there are only 5 target values because of the way we are scored it is best not to have ties.) So more precision is good – go for that.

---

### Post #6 — **goldnumberone** | 2021-02-08 20:07 UTC _(reply to #5)_

Awesome, looks like I had an issue within my machine learning code and was copying over the wrong column.

Looks like this now ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9)
    
    
    id,prediction_kazutsugi
    n0003aa52cab36c2,0.46591565012931824
    n000920ed083903f,0.4782555401325226
    n0038e640522c4a6,0.5369644165039062
    n004ac94a87dc54b,0.48990345001220703 
    

Just submitted to make sure it validates and it looks good.

Thanks for the help!
