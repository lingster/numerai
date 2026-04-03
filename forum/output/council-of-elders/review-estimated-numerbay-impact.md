---
title: "[Review] Estimated NumerBay Impact"
category: Council of Elders
url: https://forum.numer.ai/t/review-estimated-numerbay-impact/5518
created_at: 2022-06-18T06:59:03.074000+00:00
last_posted_at: 2022-06-18T06:59:03.217000+00:00
posts_count: 1
views: 861
tags: []
---

# [Review] Estimated NumerBay Impact

---

### Post #1 — **restrading** | 2022-06-18 06:59 UTC

**Tl;dr: 94475 NMR are staked using predictions bought on NumerBay as of round 320, accounting for 9.6% of total stake in the tournaments (5.9% in Numerai main tournament and 24.5% in Signals)**

This is hardly the most exciting time to talk about NumerBay given the recent armageddon in crypto. But it’s been a year since this project started and I would like to share some numbers on its impact on the Numerai community and suggest some future improvements.

**Estimated Stake**  
The following chart shows the total amount of estimated NMR staked on predictions bought on NumerBay over time. A similar chart was shared earlier in RC but had some bugs causing under-estimation which have now been fixed.

[![NumerBay 20220618 Estimated Stake](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/79907be70cb20a464310466da577845e7c8dc856_2_504x500.png)NumerBay 20220618 Estimated Stake1824×1806 143 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/79907be70cb20a464310466da577845e7c8dc856.png> "NumerBay 20220618 Estimated Stake")

The interactive chart is available at [the stats page](<https://numerbay.ai/stats>).

As of round 320, a total of **94475.225 NMR** are staked using predictions bought on NumerBay (46681.72 NMR in Numerai main tournament and 47793.505 NMR in Signals), accounting for **9.6% of total stake** in the tournaments (5.9% of Numerai main tournament and 24.5% of Signals).

**Approach for Estimation**  
For orders using auto-submission, the destination model’s stake for the round is used. For orders not using auto-submission, the total stake of buyers’ models with matching file name is used. Multi-round orders are flattened before estimation.

**This is an under-estimation of NumerBay’s total impact**  
The estimation does not include:

  * Users who used auto-submission but also submitted files to other slots
  * Users who had insufficient API permissions for NumerBay to perform file matching
  * Users who used files for other purposes such as ensembling with their own



**Sales Leaderboard**  
A sales leaderboard is now available [here](<https://numerbay.ai/sales-leaderboard>).

[![NumerBay 20220618 Leaderboard](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d10e414b2fd946d720449fe3b6dc4284089ba574_2_562x500.png)NumerBay 20220618 Leaderboard1801×1600 221 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d10e414b2fd946d720449fe3b6dc4284089ba574.png> "NumerBay 20220618 Leaderboard")

**Other Usage Stats**

  * Number of users: **242**
  * Number of listings: **363**
  * Total quantity sold: **847**
  * Total sales value: **1560.55 NMR**
  * Average unique visitors per day: **225**



**Pain Points and Potential Improvements**

  1. **Return chasing vs. diversification** : most purchases are concentrated on the top models at any point in time which suggests return-chasing behaviors. It would be better to both the buyers and the tournament as a whole to encourage more diversification. Tools need to be created to guide users towards models that not necessarily maximize past returns but complement well with their portfolios.
  2. **Portfolio management** : Many users buy more than 1 models per round and weight stakes across them. Tools can be created to track their performance and to aid decisions on portfolio weights.
  3. **Auto-submission limitation** : The auto-submission function on NumerBay currently does not allow changes after purchase. This makes multi-round purchases difficult to manage. Soon support for per-round adjustment of submission destinations will be added for multi-round orders.
  4. **Still web2** : NumerBay relies heavily on Numerai’s API and is therefore still largely a web2 app despite using MetaMask etc for other purposes such as encryption.
  5. **Lack of refund mechanism** : There is no automatic refund mechanism for missing submissions. For obvious reasons NumerBay does not hold the payments. In future as NumerBay migrates to web3 it could be possible to introduce some on-chain solution for automatic conflict resolution
  6. **Reward for modelers vs stakers** : It is not hard to see from the sales values and estimated stake that the two are out of proportion. This may become better when direct staking and profit sharing are introduced in future.



**Thank you!**  
The platform can’t be successful without its buyers and sellers. I would like to thank the CoE, the Numerai team and all the users on NumerBay for their continuous support and trust. It’s been a great learning experience for me as well. I’m committed to continue to improve the platform in future.
