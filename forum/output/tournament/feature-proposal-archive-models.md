---
title: "[Feature proposal] Archive models"
category: Tournament
url: https://forum.numer.ai/t/feature-proposal-archive-models/6661
created_at: 2023-09-08T15:55:31.725000+00:00
last_posted_at: 2023-09-08T17:24:36.768000+00:00
posts_count: 5
views: 474
tags: []
---

# [Feature proposal] Archive models

---

### Post #1 — **numerologist** | 2023-09-08 15:55 UTC

As title. For record-keeping purposes, we cannot delete models. Add an archive button for unstaked models so that we can archive them and reuse the slots they used.

While preserving record-keeping, this brings a number of benefits:

  * Fix leaderboard discrepancy. Right now, the Data Scientists dashboard is utterly inaccurate. This is because it punishes scientists who run aggressive experiments with 0.01 NMR staked. With the archive feature, we could just close any current experiment and start another in a new slot. The leaderboard would function like a credit rating: it would consider only open (active) slots for computing stats.
  * No need to mix up old experiments with the new ones by reusing old models’ slots.
  * Slots use optimization. If any experiment doesn’t work out, you can just shut down the model and free up the slot in advance so that you can have more slots later when you’re ready to run new experiments.

---

### Post #2 — **ark** | 2023-09-08 16:51 UTC

We stake-weight average your scores, so all of the models w/ .01 stake should have little-to-no impact on your score if you have any other primary model with non-trivial stake.

---

### Post #3 — **numerologist** | 2023-09-08 17:00 UTC _(reply to #2)_

Nice, good to know. But the proposal still stands for the other benefits mentioned. Curious to hear from the community if this would be useful or if there are any objections.

And yes, I understand that a lot of people prioritize stake management or other things in feature requests, but also let’s note that this one should be fairly easy to implement (1 flag in db, maybe a bit of FE work) with IMO tremendous benefits for the buck. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #4 — **ark** | 2023-09-08 17:12 UTC _(reply to #3)_

We’ve considered allowing the deletion of models since I joined, the only push back on this might be that we want to prevent the destruction of payout records. I’ll let [@slyfox](</u/slyfox>) comment more on whether / if we will do model deletion / archiving as a feature anytime soon.

---

### Post #5 — **numerologist** | 2023-09-08 17:24 UTC _(reply to #4)_

Sounds good, thanks.

Just to add, another reason why archiving (compared to deleting) might be more beneficial: tax agencies. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)  
We’ve got to keep records too.
