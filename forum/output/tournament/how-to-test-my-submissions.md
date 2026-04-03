---
title: "How to test my submissions?"
category: Tournament
url: https://forum.numer.ai/t/how-to-test-my-submissions/5782
created_at: 2022-10-24T05:56:32.841000+00:00
last_posted_at: 2022-10-27T17:28:25.632000+00:00
posts_count: 9
views: 784
tags: []
---

# How to test my submissions?

---

### Post #1 — **babs5000** | 2022-10-24 05:56 UTC

Hi all, please guide this newbie.  
How do I test if my submersion data is any good?

---

### Post #2 — **kayeffnumeraitor** | 2022-10-24 06:55 UTC

Your actual submissions will get pending scores daily around a week after you submitted them. The final result will be 4 weeks after your submission.

If you want to test your model, you can train your model on the training data only. When you are logged in and on the leaderboard page, on the left side you can find “Diagnostics Tool”, click on that, there you can find a download link for the validation data. Create predictions with your earlier trained model for this data and upload it on the diagnostics page, then you will get some metrics.

---

### Post #3 — **babs5000** | 2022-10-24 08:40 UTC _(reply to #2)_

Thanks for your reply. I’m still a bit confused. When I upload my predictions to the diagnostics page I get the metrics there, but I have no idea if it’s any good or not. To what is the data compared? Any hints on what to make with the results there?

---

### Post #4 — **kayeffnumeraitor** | 2022-10-24 12:50 UTC _(reply to #3)_

I am not using the diagnostics page because it did not exist when I started Numerai, so it would be helpful if you could be more specific to what metrics you have questions for.

---

### Post #5 — **shatteredx** | 2022-10-24 15:03 UTC _(reply to #3)_

If you hover your mouse over each score in the diagnostics tool, it will tell you what percentile you fall into (higher is better).

I forget what the percentile bins were based on. It was explained somewhere here or in rocketchat. My recollection is that it’s based on the example model.

Last point: CORR performance is mostly irrelevant now that TC is here with 3x payout multiplier. If you want big returns, you need big TC, and there’s no way to do “diagnostics” for TC yet unfortunately ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12)

---

### Post #6 — **babs5000** | 2022-10-25 09:28 UTC _(reply to #5)_

Thank you for the reply shatteredx, much appreciated. ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)  
Maybe a last question ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12): What measures in the diagnostic tool should be compared with the example model to be of any use?

---

### Post #7 — **shatteredx** | 2022-10-25 15:08 UTC _(reply to #6)_

Well, last year I would look at CORR and MMC since we were paid based on both of those.

Now, I am most interested in TC since that has the 3x payout, but unfortunately it’s not part of the diagnostics. For me, I am not even trying to develop high CORR models anymore as TC is much more lucrative.

---

### Post #8 — **babs5000** | 2022-10-27 09:33 UTC _(reply to #7)_

Thank you for the reply, from your payouts I can see you are experienced in this field. ![:champagne:](http://forum.numer.ai/images/emoji/twitter/champagne.png?v=12)

Can you please guide the newbie?  
I suppose you are not using the example model provided each week. Do you use that model as a base and include additional stock market functions for example EMA, Stochastic, etc. Can you please give me an idea where to start with a proper TC based model. Your insight here would mean a lot.

---

### Post #9 — **shatteredx** | 2022-10-27 17:28 UTC _(reply to #8)_

My reply will probably disappoint you ![:grin:](http://forum.numer.ai/images/emoji/twitter/grin.png?v=12) I have failed to make a high TC model myself, so I buy a good model from <https://numerbay.ai/>
