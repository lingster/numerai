---
title: "Model stake increase not executed and incorrect warnings about stake balance"
category: Feedback
url: https://forum.numer.ai/t/model-stake-increase-not-executed-and-incorrect-warnings-about-stake-balance/3467
created_at: 2021-05-29T07:41:42.009000+00:00
last_posted_at: 2021-05-29T09:55:14.768000+00:00
posts_count: 3
views: 646
tags: []
---

# Model stake increase not executed and incorrect warnings about stake balance

---

### Post #1 — **ml_is_lyf** | 2021-05-29 07:41 UTC

Last Monday/Sunday (can’t remember the exact day but it was one of those) I staked 3.049 NMR on two different models I have. But I’ve just realized my stakes are still pending, so did not go in this round.

I’m quite confused why they’d still be pending. The only clue I have is that I am now seeing “Warning: Increasing amount greater than current wallet balance” on both of my staked models. I have 6.098 NMR in my accounts wallet (this is what CoinTracker tells me and also what Numerai shows when I cancel my stakes pending), so this warning doesn’t make sense. I tried decreasing my stake to both model to 3.048 (in case it was a rounding error on my balance), and I still had the warning. I then tried decreasing my stakes to 3.04 (in case you can only stake to 2 d.p.) but I am still getting the warning.

For reference, I’ve increased my stake many times now, and I’ve never seen anything like this before.

I am really confused what is going on. Is anyone else experiencing similar or has in the past?

I suppose it’s possible I may have accidentally staked 3.05 instead of 3.049 NMR, which would have been more than my wallet balance. Its hard to tell as at least on the UI, when you stake to more than 2 d.p., it seems to round to the nearest second d.p (e.g. 3.049 is shown an 3.05). Or when its rounding does it actually then try and take that amount?

---

### Post #2 — **minou** | 2021-05-29 08:46 UTC

There was a recent change to the deadline for stake changes, so exactly when your change was made could be the issue. Sunday should have been fine, but if it was made after 14:30 UTC on Monday, the change would be effected on the next round.

---

### Post #3 — **ml_is_lyf** | 2021-05-29 09:55 UTC _(reply to #2)_

Damn that’s probably what it was then, thanks ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

It’d be nice if the team could make the staking deadline clearer on the website though. Especially when they plan on changing it.
