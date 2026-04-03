---
title: "Why does staking wait until Thursday?"
category: Tournament
url: https://forum.numer.ai/t/why-does-staking-wait-until-thursday/3616
created_at: 2021-06-18T01:24:25.790000+00:00
last_posted_at: 2022-05-12T16:33:17.305000+00:00
posts_count: 8
views: 1036
tags: []
---

# Why does staking wait until Thursday?

---

### Post #1 — **swarm** | 2021-06-18 01:24 UTC

Hi, just started staking my first model, fingers crossed! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

I was wondering why staking is applied so much later than predictions, which are already made on Monday. Doesn’t this put the metamodel at somewhat of a disadvantage as it is acting on data delayed ~3 days?

I know the time horizon is long, ~4 weeks, but still, large movements can happen in 3 days. And there are probably other hedge funds using machine learning (perhaps on similar underlying features that were used to generate the Numerai features) that apply their predictions immediately.

---

### Post #2 — **mic** | 2021-06-18 02:29 UTC

The input data is delayed, so we have to wait at least for the overlap to elapse.

---

### Post #3 — **restrading** | 2021-06-18 03:20 UTC

Stake changes depend on the results of the resolving round which happens on Wednesday, hence it is not possible before that

---

### Post #4 — **liz** | 2021-06-18 04:45 UTC

stakes are not converted to fiat by numerai in that way.

---

### Post #5 — **wigglemuse** | 2021-06-18 12:14 UTC

The staking and submission deadline are not on Sunday night, but they are on Monday morning – before trading. Staking deadline was for a while later in the week (which yes didn’t quite make sense), but now it is the same as the submission deadline. (You can still submit after that and it will be scored, but you can’t stake on it for that round and it won’t be used in the metamodel.) And Numerai never gets our stakes to be used by them in any way, they are just locked up on the blockchain for the duration of staking to be given back to us (with additional earnings) or burned.

---

### Post #6 — **swarm** | 2021-06-18 12:59 UTC

During fall and winter the 14:30 UTC deadline does coincide with market open, but during daylight savings time in the spring and summer I think it’s 1 hour after market open.

So it sounds like Numerai can indeed apply our predictions immediately in trading Monday market open (which is good and what we want). But here is a scenario:

  1. Consider one of our predictions is interpreted as a positive signal to increase Apple share holdings
  2. Numerai hedge fund acts on that and buys the additional shares Monday morning
  3. For the next 3 days, the share price rises quickly because maybe they just introduced an amazing product
  4. On Thursday, our actual stakes start to be scored, but by then the excitement has started dying out so share price stops going up
  5. For the rest of the month, the share price ends up higher than Monday open, but slightly lower than Thursday open. Numerai would be in the green, and prediction maker would be in the red (maybe?).



So is there a possibility for the Numerai hedge fund to make a profit from a prediction that the prediction maker doesn’t get rewarded for?

---

### Post #7 — **wigglemuse** | 2021-06-18 17:18 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/9de053/48.png) swarm:

> So is there a possibility for the Numerai hedge fund to make a profit from a prediction that the prediction maker doesn’t get rewarded for?

Absolutely. And vice-versa. And it isn’t like they are necessarily exiting the position after 4 weeks either – they are making decisions to enter/exit/adjust positions each week (or even more often now that Signals is involved also). Our predictions help them make those decisions, but we are rewarded for making good predictions in a specific time frame, not for success or failure of real life trading. Personally, this disconnect is a nonissue for me, but it really seems to bother some people that we aren’t “directly” driving the hedge fund and getting rewarded out of hedge fund profits (explicitly tied to our performance).

---

### Post #9 — **johnnywhippet** | 2022-05-12 16:33 UTC

because my scores are always lower on a thursday ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)
