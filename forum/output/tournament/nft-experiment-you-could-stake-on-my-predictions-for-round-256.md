---
title: "NFT Experiment -- You could stake on my predictions for Round 256"
category: Tournament
url: https://forum.numer.ai/t/nft-experiment-you-could-stake-on-my-predictions-for-round-256/2379
created_at: 2021-03-15T14:55:48.918000+00:00
last_posted_at: 2022-04-01T13:04:18.490000+00:00
posts_count: 8
views: 3577
tags: []
---

# NFT Experiment -- You could stake on my predictions for Round 256

---

### Post #1 — **hb_scout** | 2021-03-15 14:55 UTC

I’d like to do an experiment: I put access to next week’s submissions for a couple of my models as NFTs on [Opensea.io](<https://opensea.io/collection/hb-numerai-predictions>)! When purchased, each NFT has an unlockable link to a Dropbox folder containing:

  1. The account’s submission from Round 255 that you can submit late on an open account to verify that you get the same results as my accounts,
  2. The model diagnostics from Round 255,
  3. The NFT logo “art”,
  4. Before midnight (PDT) on Saturday March 20, the account’s submission file for Round 256.



<https://opensea.io/collection/hb-numerai-predictions>

**Reasons to buy:**

  * To stake on someone else’s model.
  * To see the diagnostics for some other models.
  * To speculate that you can re-sell a rocket scientist’s submissions for a higher price (Note: you can write down the Dropbox link and resell. I don’t mind. I would get 5% royalties automatically).
  * Because you like my beautiful art.



**Reasons NOT to buy:**

  * **You can lose up to 25% of your stake** without knowing anything about the underlying model.
  * Gas fees alone will likely be >$50.
  * **This is not a subscription; you only get predictions for one new round.** If you want to use them, **you must submit before Round 256 closes on Monday March 22 at 14:30 UTC.**
  * Because you hate my beautiful art.



**These NFTs come with no guarantees whatsoever. I’m not liable for any losses due to the use of these files. No refunds guaranteed for any reasons.** I’ll be around to answer questions, but again, no guarantees for any support from me.

We’ll see how this experiment plays out this week. This might be the only time I try this or maybe I’ll keep it going!

For sale this week:  
[HB_FALCON](<https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/46413627275005670704339071978154489246892493263514731823890392848697332334593>) | Current Rank 4  
[HB_CLIPPER](<https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/46413627275005670704339071978154489246892493263514731823890392849796843962369>) | Current Rank 90 (with highest 3M return for all of Numerai)  
[HB_NOVA](<https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/46413627275005670704339071978154489246892493263514731823890392850896355590145>) | Current Rank 719 (a newer model since Round 241)  
[HB](<https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/46413627275005670704339071978154489246892493263514731823890392847597820706817>) | Current Rank 414 (OG model and formerly #1 on Leaderboard)

[Who am I? Watch my OHwA interview here.](<https://www.youtube.com/watch?v=jKI5dalRpn0&t=17s&ab_channel=Numerai>)

---

### Post #2 — **hb_scout** | 2021-03-15 15:03 UTC

The sale prices will decrease over the course of the week, getting cheaper as the round approaches. Average submissions on Numerai are earning about 2.5% after the 1-month lockup period. Therefore, an average submission is worth $100 per 100 NMR staked assuming $40/NMR. **Past performance does not predict future returns and there is high variation from week-to-week**. Staking on other peoples’ model could work out very poorly. It’s a gamble.

---

### Post #3 — **koyukon** | 2021-03-16 20:03 UTC _(reply to #2)_

Cool Idea. I have good experience with ML and Jupy labs. I am dirt poor tho so I will be buying your submission at the lowest point(~$45 USD I think). Is the code included in there? Im curios what you have done behind the scenes ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **hb_scout** | 2021-03-17 00:02 UTC _(reply to #3)_

The code isn’t included, just the submission files from Round 255 (to submit late) and Round 256 (after Saturday once Round 256 has been open for a few hours so the code can run). The code is certainly worth way more to me. The cheapest this submission will get is 0.025 ETH, but remember that the gas cost will likely be about 0.015 ETH too. If anyone buys before it gets that cheap, they might not put it back up for sale or might put it up for more. There’s only one NFT available per prediction.

**Edit:** Also remember that these predictions are completely worthless if you don’t plan on staking NMR on them. I just posted below my math where you can mess around with the assumptions and see if it’s worth buying based on how much NMR you might want to stake on these predictions.

---

### Post #5 — **hb_scout** | 2021-03-17 00:08 UTC _(reply to #4)_

**I did the math for how much someone might be willing to pay for a prediction NFT with the following assumptions:**

  * BIGGEST ASSUMPTION: HB_FALCON gets its 40-round average 2x MMC payout of 5.45%. Then `payout = (0.0545 * stake * usd_per_NMR)`
  * Targeted profit is some fraction of the payout a person would get if they staked on their own predictions. Define this as P between 0% and 100%. The other portion of the historical average payout is effectively pre-paid to me in advance to access the submission.
  * The NFT can be resold for some value between 0% and 100% of the original purchase price. This (conservatively?) assumes that no one out there is willing to pay more than you for that week’s predictions.
  * Gas is about $25 for the transaction. NMR is about $40/NMR. ETH is about $1800/ETH.



`profit = stake_payout - price - gas + resale`  
`price - resale = payout - profit - gas`  
`price - R*price = payout - P*payout - gas`  
`(1-R)*price = (1-P)*payout - gas`  
`price = [(1-P)*payout - gas]/(1-R)`  
`eth_price*1800 = [(1-P)payout - gas]/(1-R)`

`eth_price = [(1-P)*(0.0545*stake*40 - 25)]/[1800 * (1-R)]`

You can plug this into WolframAlpha to set different values of the how much you’re willing to stake (x), what fraction of the historical average payout you would hope to keep as profit (`P`), and what fraction of the purchase price you think you can resell for (`R`):  
`Solve[((1-P)*(0.0545 * x * 40 - 25))/(1800 * (1-R)), {x==500}, {P==0.5}, {R=0.5}]`  
The result is the price in ETH that someone would consider purchasing for if they thought that the submission for Round 256 will match the historical average ([Link to WolframAlpha equation](<https://www.wolframalpha.com/input/?i=Solve%5B%28%281-P%29*%280.0545+*+x+*+40+-+25%29%29%2F%281800+*+%281-R%29%29%2C+%7Bx%3D%3D500%7D%2C+%7BP%3D%3D0.5%7D%2C+%7BR%3D0.5%7D%5D>)). Adjust `x` to be the amount you want to stake, then you can mess around with your preferences and guess for `P` and `R`, or be optimistic and change the historical 5.45% to the full 25% earn like HB_FALCON got in Round 250.

---

### Post #6 — **koyukon** | 2021-03-17 16:01 UTC _(reply to #4)_

Gotcha. I was unaware that each submission is merely the resulting predictions from the model you designed. I don’t know why I didn’t make this connection but thanks for the education. I like your innovation trying to sell the predictions as NFTs and your attention to detail is awesome. I’m a newbie but I hope to create a model with a positive correlation in the next month or so. How long did it take you to get your model to be positively correlated and generate NMR instead of burning it?

---

### Post #8 — **hb_scout** | 2021-03-21 01:30 UTC _(reply to #6)_

Round 256 predictions are officially posted inside the experimental NFTs I have for sale on [Opeasea.io](<https://opensea.io/collection/hb-numerai-predictions>) for HB_FALCON (now #3 on the leaderboard), HB_CLIPPER, HB_NOVA, and HB.

Once again, total experiment, no guarantees of anything whatsoever and you can definitely have your stake burned.

---

### Post #10 — **joshwin072** | 2022-04-01 13:04 UTC

Nice Information, thanks for sharing
