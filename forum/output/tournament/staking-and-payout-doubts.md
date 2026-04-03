---
title: "Staking and payout doubts"
category: Tournament
url: https://forum.numer.ai/t/staking-and-payout-doubts/436
created_at: 2020-05-19T06:13:30.647000+00:00
last_posted_at: 2020-05-22T08:12:19.449000+00:00
posts_count: 7
views: 1809
tags: []
---

# Staking and payout doubts

---

### Post #1 — **correlator** | 2020-05-19 06:13 UTC

I am just starting out here and have a bunch of doubts which couldn’t be clarified by existing threads or docs. Help me understand the staking, payouts better.

  1. Is the stake submission dependent or there is just one stake value which applies to multiple submissions.
  2. I made a submission in round N with stake 1 NMR. For the next round I make another submission. I am more confident on the latest model so I want to stake more say 5 NMR. Going to numer.ai/models I click on manage stake and increase the stake to 5 for the latest model. So, starting next round I have staked 6 NMR total. Now, is the 6 NMR stake value also applicable to the (bad) first submission? Ideally it should be 1 NMR.
  3. Considering that I want to stake in each round, do we need to explicitly manage the stake for the latest model and increase the stake?

---

### Post #2 — **mendrinos** | 2020-05-19 08:07 UTC

I’m afraid I can only help with the first question you have as I am also new here. I believe stakes are model dependent. For example, if you have two models you can use one as a ‘stable’ version of your model which you know performs fairly well and use the other model to test your new experiments. This allows you to stake on your stable model so you are more likely to earn money and you don’t have to worry about your second model burning your stake if it does not perform well.

---

### Post #3 — **quantnosticator** | 2020-05-19 13:19 UTC

Each individual model has its own stake. (“Model” maybe isn’t the best term they could have used there since you can change the actual predictive model week to week and submit it under that same “model” name – but each named slot is currently independent, yes.) And the stake on that slot will keep rolling over and be applied to further rounds until you do a withdrawal, assuming you submit on those further rounds. If you skip a round, there is a reputation penalty (for leaderboard rank purposes), but it will not jeopardize your stake. However, understand that rounds are 4 weeks long overlapping, so there are 4 active rounds at a time.

---

### Post #4 — **correlator** | 2020-05-21 05:02 UTC _(reply to #3)_

Do the payouts always revert to the stake and never to the wallet?  
My understanding is that the payouts are rolled back to the stake after each week (Thursday).  
But that round is resolved only after 4 weeks so the final payout considered is the one after 4 weeks. So what happens after 4 weeks, is it reverted to stake or paid in wallet. This 1 week, 4 week thing makes it confusing.

---

### Post #5 — **mendrinos** | 2020-05-21 08:48 UTC _(reply to #4)_

Each week a new round opens for submissions however each round lasts for four weeks meaning that at any one time there are four rounds running. At the end of each round your payout for that round is payed out into your stake automatically and so your stake for the next round is increased. You can then I believe withdraw some of your stake to your wallet but i think there is a delay until in progress rounds are resolved (I may be wrong about that)

---

### Post #6 — **correlator** | 2020-05-22 04:11 UTC _(reply to #5)_

Let’s say I submitted and staked 100 NMR in round N, and subsequently I did not make any submissions (ever). If there is no submission there cannot be a stake, where does the payout for round N go then?

---

### Post #7 — **mendrinos** | 2020-05-22 08:12 UTC _(reply to #6)_

I believe that it would still be paid into your stake but your stake would not increase or decrease (maybe) until you submit again. Someone else might want to confirm or deny this as I’m unsure.
