---
title: "[Noob question] One more question about time series"
category: Tournament
url: https://forum.numer.ai/t/noob-question-one-more-question-about-time-series/2609
created_at: 2021-03-31T06:14:13.087000+00:00
last_posted_at: 2021-04-02T07:21:03.399000+00:00
posts_count: 4
views: 1047
tags: []
---

# [Noob question] One more question about time series

---

### Post #1 — **rpica** | 2021-03-31 06:14 UTC

Hello everyone,

I’m a data scientist newbie to the stock market, trying to wrap my head around numerai.

The first shock as a complete newbie has been that the data is so anonymized. After reading docs and forum, I understand: the data that the hedge fund provide is actually one of its assets and apparently expensive to get. Ok, I understand.

However, the fact that the stock ids are not only anonymized but changes randomly from era to era, has me very confused. Aren’t we losing an extremely important bit of the information? To try to give the magnitude of what I am (mis)understanding: the current AI revolution with deep learning has started and continues in big part since people took advantage first of the geometric structure of the data (CNN applied to image) and ongoing with temporal/sequencial structure of the data (RNNs and its variants applied to NLP and any sequence-type data).

**Aren’t we losing a lot by removing this information?** Just imagine image classification with the position of the pixels randomized, or NLP with the words shuffled.

What is the reason to remove the id consistency over time? That it would somehow make possible a des-anonymization of the data?

If an answer is that the temporal information of each stock is somehow embedded in the row, spread through the features, I would argue that just like we want collective intelligence applying data science over the features, it might be as important to do it over time, rather than having that axis of the information used for us in a fixed way.

In addition, any possible correlation between different stocks over time is lost as we can’t track them over time. Maybe this is better from a stock prediction point of view, I don’t know.

Just trying to understand here, I hope there is something that I missed!

Thank you in advance!

---

### Post #2 — **sneaky** | 2021-03-31 18:49 UTC

Hi, I’m newbie as well. I’m guessing that, if you had stocks link throughout eras you would be able to find out (atleast partialy) which stock is which; thus, the anonymization would be broken.

---

### Post #3 — **profricecake** | 2021-04-01 06:55 UTC

Hi [@rpica](</u/rpica>) \- welcome to the tournament!

![](http://forum.numer.ai/user_avatar/forum.numer.ai/rpica/48/2776_2.png) rpica:

> **Aren’t we losing a lot by removing this information?** Just imagine image classification with the position of the pixels randomized, or NLP with the words shuffled.

Speaking for myself, I agree that yes we are losing a lot of potentially-useful information when id coherence across eras is deliberately obfuscated.

One guess for why they’re doing this is that they don’t want us building up individual models on a per-asset basis, as that would be a return to company/asset modeling instead of market modeling “en masse.”

Another is the concern that you and [@sneaky](</u/sneaky>) both raise, namely, that to reveal this information might make it easier to de-anonymize the data and/or reveal something about the hedge fund that is otherwise proprietary.

Whatever the reasons, we’ve got the data you’ve got. Good luck with it!

---

### Post #4 — **rpica** | 2021-04-02 07:21 UTC _(reply to #3)_

Thank you for your replies!

I would still appreciate to understand how it’s worth it to exchange such information (which again, leveraging it drove the current AI revolution) for stronger anonymization.
