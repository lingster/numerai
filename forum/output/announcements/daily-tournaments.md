---
title: "Daily Tournaments"
category: Announcements
url: https://forum.numer.ai/t/daily-tournaments/5766
created_at: 2022-10-21T18:54:58.163000+00:00
last_posted_at: 2022-10-21T18:54:58.278000+00:00
posts_count: 1
views: 5254
tags: []
---

# Daily Tournaments

---

### Post #1 — **slyfox** | 2022-10-21 18:54 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1a0e3a29fc12d68e728b028869a9036677af8c79_2_690x365.png)image3154×1671 493 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1a0e3a29fc12d68e728b028869a9036677af8c79.png> "image")

**TLDR**

  * daily rounds on Tournament and Signals starting next week
  * no code changes required to participate
  * payouts coming soon



**Why daily tournaments?**  
Numerai currently runs on a weekly cadence – weekly tournament, weekly meta model, weekly trading.

Research has shown that daily trading will improve the hedge fund’s performance and capacity. To support daily trading, we need a daily meta model, which in turn requires a daily tournament.

Getting to daily trading will be a huge milestone for Numerai and we need YOUR HELP to get us there!

**What is changing?**  
Starting next week, Numerai Tournament and Numerai Signals will open 4 new rounds a week on Tuesday, Wednesday, Thursday, and Friday, in addition to the current rounds opening on Saturdays.

Specifically, this means that after round 339 opening on Saturday October 21st, round 340 will be opening on Tuesday October 25th, round 341 will be opening on Wednesday October 26th, and so on.

The open time and submission deadline of the rounds opening on Saturdays will stay exactly the same as before. The new rounds opening on Tuesday-Friday will open earlier at ~13:00UTC and have a shorter 1 hour submission window.

**What do I need to do?**  
If you don’t want to participate in these new rounds, then there is nothing that you need to do. You can continue to participate once a week just like before.

If you do want to participate in the new rounds, then you can use the same* data and submissions API to run your daily model pipeline. And if you are already automated with Numerai Compute, then you can simply enable daily triggers on the models page of the website.

*V2, V3, V4 data files and signals universe will be available daily via the API but the legacy dataset zips will only be available for Saturday rounds and not the new weekday rounds. Validation data will continue to be updated weekly and not daily.

**Getting ready for the 1 hour submission window**  
If you are not yet automated, we strongly recommend that set up Numerai Compute. We are also happy to help with integrating any other set up you have (notebook, cron etc).

If your model just takes longer than 1 hour to run but you still want to participate, don’t worry. We will soon support a feature to let your late submissions automatically count towards the next round.

**Payouts coming soon**  
Initially, there will be no payouts for these new rounds and so the payout factor threshold for these rounds will be set to 0. This is meant to give everyone time to adjust their model pipelines and for us to fix any issues based on your feedback.

Once the system stabilizes, we will gradually decrease the payout factor threshold for rounds opening on Saturdays and increase the payout factor threshold for these new rounds opening Tuesday-Friday, keeping the overall payout factor the same, until we reach about a 70/30 split.

We expect this change to increase overall payouts (and burns!) due to a faster rate of compounding. We also expect the payout factor for these new rounds to be much higher for a period of time due to lower number of models participating.

More details regarding the upcoming changes to the payout factor threshold will be separately announced.
