---
title: "Regimes, turbulence, matching eras, and whatnot"
category: Data Science
url: https://forum.numer.ai/t/regimes-turbulence-matching-eras-and-whatnot/6356
created_at: 2023-05-10T18:35:31.775000+00:00
last_posted_at: 2023-05-12T16:31:36.580000+00:00
posts_count: 2
views: 880
tags: []
---

# Regimes, turbulence, matching eras, and whatnot

---

### Post #1 — **gammarat** | 2023-05-10 18:35 UTC

I’m putting this in Data Science rather than Signals as although my focus primarily Signals based, I think it could be applied (eventually) to defining regimes in the Tournament as well. If, of course, if these ideas pan out to start with (always dubious ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)). I’m also quite curious as to what other people think about this issue–is it real? is it addressable? if it is addressable, how are you addressing it? That sort of thing.

And, fwiw, [this post on the Discord chat](<https://discord.com/channels/894652647515226152/1089609932518731827/1105837140992073768>) got me to thinking about writing this.

In any case, regime change is a topic that’s been kicked around here for awhile (search on “regime” or “clustering eras” for previous threads).

At the moment, I’m considering this as a turbulence type problem in the sense that regimes range from fairly laminar (better performing stocks remain better performing) to quite turbulent (ranking becomes highly unpredictable). Are there ways to classify such behaviour? (Never say never, ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)).

So I thought I would start with a highly reduced problem. I work with the daily close of the Toronto Stock Exchange (using bulk data from [EOD Historical](<https://eodhistoricaldata.com/>), and then look at the consistency of rankings from day to day.

To form that, at each day, I take the relative return of each stock over the previous 20 days is calculated and the returns are ranked. Then I take the relative returns of each stock for each of the next 20 days relative to the start day, and rank those These are then rank correlated against the start day rankings.

If I plot those out for the 1,5,10, and 20 day intervals, I get something like this:  


[![turbulence20230510](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/eba817efb1da2a7d3a4dadbed913010542ba54de_2_690x258.jpeg)turbulence202305101120×420 58.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eba817efb1da2a7d3a4dadbed913010542ba54de.jpeg> "turbulence20230510")

To me, atm., the most recent data on the top (blue) line is looking quite similar to Jan '22 or Feb '21. And in general, it’s interesting how the coherence responds to political and social events

Other external factors that might be worth looking at include, interest rates. The [St. Louis Federal Reserve](<https://fred.stlouisfed.org/categories>) has tons of material that might help. (It also has an easy to use API). For example, here’s a chart I made up of the difference between junk bond rates and ten year treasuries:

[![CCC10yr](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/abb12a3ce5e392f49bb532589afddf19970d5fac_2_690x257.jpeg)CCC10yr1126×420 25.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/abb12a3ce5e392f49bb532589afddf19970d5fac.jpeg> "CCC10yr")

which (to me) indicates we might be heading into a few problems. ![:scream:](https://emoji.discourse-cdn.com/twitter/scream.png?v=13)

---

### Post #2 — **anthill** | 2023-05-12 16:31 UTC

One thing I worry about on the Tournament side is that the training data we have goes back something like 20 years or so. This was a period of historically low and stable interest rates. Now that this period is ending and interest rates are moving back to their historical norm it’s not obvious that the training data we have will be representative of this new regime. It’s possible we’ll see lower performance for some time.
