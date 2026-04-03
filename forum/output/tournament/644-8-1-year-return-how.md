---
title: "644.8% 1-year return - how?"
category: Tournament
url: https://forum.numer.ai/t/644-8-1-year-return-how/6343
created_at: 2023-05-03T22:21:45.647000+00:00
last_posted_at: 2023-05-09T08:25:12.890000+00:00
posts_count: 5
views: 1287
tags: []
---

# 644.8% 1-year return - how?

---

### Post #1 — **foxtrot** | 2023-05-03 22:21 UTC

On the leaderboard, I see a bunch of guys with 600%, 500%, 400% 1-year return. I do not understand how that’s possible, since according to the docs, _the maximum payout or burn per round is ±5%_. Somebody please explain to me how the 1-year return is calculated.

As I see it, since one round takes about a month to resolve, and your money is frozen during that time, the max you can get in a year is 1.05 ^ 12, which is about 80% return.

---

### Post #2 — **wigglemuse** | 2023-05-03 22:55 UTC

The 5% thing literally just started this week with daily payouts. Prior to now, we had weekly payouts where the max was 25%. Not that many people were getting anywhere near that, but it was possible. The rounds are overlapping so even though it takes one month to resolve, we’ve actually got our whole stake (kind of) staked on 4 rounds at a time (which is why the max was 1/4 = 25%). But now with daily rounds (5 per week) we’ll have 20 overlapping rounds (thus 1/20 = 5%), and so those are now compounding daily.

Still…don’t expect to get those huge numbers yourself, and don’t expect those that do get them for a period to go on getting them forever. But yeah, some people have done quite well.

---

### Post #3 — **foxtrot** | 2023-05-04 19:06 UTC _(reply to #2)_

So what you’re saying is that one can get leverage in staking, because the money staked is only frozen partially (for example, you stake 100, 5 is frozen, 95 is available for further staking)?

---

### Post #4 — **wigglemuse** | 2023-05-04 20:39 UTC _(reply to #3)_

Not quite like that. This is how it works. Let’s say got a model slot (“MODEL_A”). You stake 100 NMR on MODEL_A. Now that 100 just sits on that model and it staked in full on the predictions you upload to that slot. So day 1, round 1 starts, and your 100 NMR is staked with a max burn or payout of 5% (after 20 days) on that round. Next day round 2 starts – the same 100 NMR is also staked on round 2. For 20 trading days in a row, you’ll be staking 100 NMR on each of those rounds (the 100 hasn’t changed at all yet because it takes 20 days for the first round to resolve). Then after 20 days, round 1 is resolved, and your stake either goes up or down a bit depending on how did that round (I’m assuming compounding here) and that amount will be the stake for the next round. And then every day after that an old round will resolve and a new round will start, and that stake just grows or shrinks every day, but not by more than 5% of the amount it was at the start of the resolved round. (And that’s just because of math – if you could lose more than 5% a day on 20 overlapping rounds, you could actually go negative, so that’s why the limit is 5% and is also why the previous limit was 25% when there were only 4 overlapping rounds.) The payout factor is also 5x lower than it was before so one week still has the same overall “value” than before, it is just spread over 5 days now.

Also, MODEL_A doesn’t actually have to be the same model every day. You are just uploading predictions – how you come up with them is totally up to you, and you can change that method at will. Also, you don’t actually have to upload every round – any round you miss you simply won’t have anything at risk for that round (even though you’ll still be staked). If you just stop uploading predictions altogether, your stake will still just sit there on that slot until you request that it is released (which takes a month).

Signals is structured basically the same way in terms of the staking.

---

### Post #5 — **sneaky** | 2023-05-09 08:25 UTC

IMHO the main reason is that when TC was released there was little competition, because nobody knew what to optimize for. It seems that it is harder to get consistently crazy high TC now, because the models are more optimize for TC than before. But as wigglemuse wrote, the market changes all the time. What seems to be trend now, can change tomorrow.
