---
title: "TC vs. Legacy Data"
category: Tournament
url: https://forum.numer.ai/t/tc-vs-legacy-data/5204
created_at: 2022-04-03T09:40:56.483000+00:00
last_posted_at: 2022-04-04T16:09:07.400000+00:00
posts_count: 3
views: 857
tags: []
---

# TC vs. Legacy Data

---

### Post #1 — **factorsparsity** | 2022-04-03 09:40 UTC

Hi,I have legacy data models and new data models and all the staked ones are performing alright now and are pretty similar. However, according to the current data my legacy models will still perform somewhat ok (a bit worse than before) while my new data models will fail catastrophically. It’s actually impressive how well the TC value accentuates the difference between those two classes of models even though there are several different approaches used in both groups.  
Any thoughts on that? Wigglemuse?

---

### Post #2 — **rigrog** | 2022-04-03 19:55 UTC

I used v3 (“supermassive”) for a while, but to barely fit in my limited hardware (16 Gb) I had to combine 1050 features into 210 (5 to 1). I saw no improvement over v2 (“legacy”), so I’ve since gone back to v2.

The next round (311) will have > 90% of the target values provided, and how could that not improve every model’s performance? I have high hopes for my own.

Since you have v2 and v3–>v4 models to compare, I’d be keenly interested how that comparison looks in the upcoming “target rich environment”. Please post an update!

Numerai won’t directly provide that target info for v2 models, because reasons ![:sob:](http://forum.numer.ai/images/emoji/twitter/sob.png?v=10) , so it’s up to us to do some fiddling. For each ‘test’ row in v2/numerai_tournament_data.csv, find the row in v4/numerai_validation_data.csv with the same ‘id’ field [edit: AND data_type == ‘validation’], then copy the ‘target’ value from that row into the empty ‘target’ field of the v2 row. Whew! Good luck to both of us!

---

### Post #3 — **wigglemuse** | 2022-04-04 16:09 UTC

My thoughts are that we’ll see what happens. But if it is giving you a signal that your new models suck on TC, that’s not surprising and maybe you should tread lightly with the new scoring. Remember, TC is new for the team as well – when they put out data v3 they were trying to give us data that would do better on the then-current metrics. And for some people that’s been true, others not so much. There was nothing wrong with the old data – for me the main advantage of the newer data was that it was weekly. I also ended up using an averaged 210 feature set for most models (although not because of space limitations, it just worked better with what I was doing). I think the 420 medium set was probably the best way to go for most people on v3 data. And now with the release of all these new eras, I would think pretty much everybody would want to use that for new models, but if you have a legacy model that looks good on TC already, no reason not to keep submitting it.

I know that I will be going through my old submissions (back to round 200 where TC is filled-in) and maybe reviving some of those old ideas that I will redo on new data…
