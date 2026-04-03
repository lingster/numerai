---
title: "[Milestone & Vote] NumerBay.ai Release and Future Features"
category: Council of Elders
url: https://forum.numer.ai/t/milestone-vote-numerbay-ai-release-and-future-features/3943
created_at: 2021-08-13T09:48:49.724000+00:00
last_posted_at: 2021-08-30T13:00:34.615000+00:00
posts_count: 17
views: 1686
tags: []
---

# [Milestone & Vote] NumerBay.ai Release and Future Features

---

### Post #1 — **restrading** | 2021-08-13 09:48 UTC

**NumerBay (<https://numerbay.ai/>) is Here!** Thanks to the support from the CoE and everyone interested in this project.

The code repository is public at <https://github.com/restrading/numerbay>

![NumerBay 20210801 seller flow](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2e818d7bc54c05e0d0a959e03ecb39358a33d9a5.gif)

For those who are not familiar with this project, this is the community marketplace originally proposed [here](<http://forum.numer.ai/t/proposal-numerai-community-marketplace/3622>) and is funded by the Numerai Council of Elders.

**This is an interim early release with support for generic 3rd party listing** of Numerai predictions, models, Signals predictions and Signals data. I would like to invite everyone (especially sellers who are currently listing their models on Gumroad) to try it out. You can get you models listed on NumerBay **for free** , so why not?

* * *

In the meantime, I am going to continue to work on the other various features of NumerBay, most prominent of which are on-platform listings and NMR payment support.

**Please vote on features that you would most like to see in the next major release.** I would prioritize features that are most in demand. Poll closes on August 20.

If you have features in mind that are not in the poll, or if you encounter any issue using NumerBay, please leave your comments here or post in the **#numerbay** channel on RocketChat.

Thank you and happy sailing on NumerBay ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

  * General - Sybil Robust Voting App / Numerai Analytics Dashboards / More community content on Homepage / etc.
  * Buyer - UX - Sort Model Listings by Numerai Rank / Rep
  * Buyer - UX - Filter Listings by Seller / Platform / Price
  * Buyer - UX - Favorites / Wishlists
  * Buyer - On-platform - More Web3 Auth Poviders (WalletConnect, Fortmatic, etc)
  * Buyer - On-platform - Seller Review / Reputation System
  * Buyer - On-platform - Seller Model Consistency Check
  * Buyer - On-platform - Purchase History & Management
  * Buyer - On-platform - Automated Submission
  * Seller - General - Public Profile Page
  * Seller - Off-platform - Gumroad API integration
  * Seller - Off-platform - Other Providers API (please specify in comments)
  * Seller - On-platform - Customer Management
  * Seller - On-platform - NMR Payment
  * Seller - On-platform - Fiat Payment
  * Seller - On-platform - Automated File Distribution to Customers
  * Seller - On-platform - Auction / Multi-tiered Pricing
  * Seller - On-platform - Subscription Sales
  * Seller - On-platform - Selling Stake Allowance (Instead of Raw Files)
  * Seller - On-platform - Discount Sales Options



0 voters

---

### Post #2 — **restrading** | 2021-08-13 10:25 UTC

GitHub repo has been transfered: <https://github.com/councilofelders/numerbay>

---

### Post #3 — **nyuton** | 2021-08-19 09:50 UTC

Hi,

Let’s sort the models by ranking by default.  
I guess that’s what potential inverstors will be looking for.

Thanks

---

### Post #4 — **nyuton** | 2021-08-19 09:52 UTC _(reply to #3)_

What about adding the option to filter out not staked models.

---

### Post #5 — **restrading** | 2021-08-19 10:02 UTC

[@nyuton](</u/nyuton>) Thanks for the suggestions. Both of those are in the pipeline. It is not as straightforward to implement as it seems. There are other functionalities that I need to finish before this is possible.

---

### Post #6 — **restrading** | 2021-08-21 02:11 UTC

Poll is closed, thank you for the inputs! I will work according to the priority set by the votes, with the following exceptions:

  * Subscription Sales: pending payment solution
  * Fiat Payment: pending payment solution



NMR Payment and most of On-platform features will be in the next major release. Before that happens, small features will be pushed from time to time.

---

### Post #7 — **nyuton** | 2021-08-27 13:56 UTC

My subscribers often use the purchesed predictions for ensembling.  
For this purpuse it would be useful to display the correlation with the metamodel on the model page.  
Low correlation has higher value for the buyer.

MMC is also useful. Payout can be 2xMMC.  
Sorting should be done by default on CORR+2xMMC  
This puts the highest value model first, instead of the highest CORR ranking model first.

---

### Post #8 — **restrading** | 2021-08-27 14:10 UTC _(reply to #7)_

Multiple sorting and filtering metrics are coming in the next feature release (should be some time next week or earliest this Sunday). However, default sorting will be by rank. Metamodel correlation can be added after that. Thanks for the suggestions.

---

### Post #9 — **rigrog** | 2021-08-27 15:34 UTC

Instead of buyers getting prediction files from sellers, let me propose a completely different model: 3rd party staking.

The 1st party is the model maker, the 2nd party is Numerai. The 3rd party staker would have a Numerai wallet, from which he would stake NMR on the 1st party’s model. Instead of getting the prediction file, the 3rd party gets the same earns/burns (in proportion to stake amount) as the 1st party on that model.

This would require some Numerai-provided structure, for automating the eventual unstaking, and then distributing the proceeds according to the terms agreed upon.

Thoughts?

---

### Post #10 — **restrading** | 2021-08-27 15:35 UTC _(reply to #9)_

This was already in the original proposal (called “Stake Mode”), it will be available at some point.

---

### Post #11 — **rigrog** | 2021-08-27 16:44 UTC _(reply to #7)_

If I were shopping for a model to buy, CORR + 2 MMC is the first thing I’d want to look at.

---

### Post #12 — **restrading** | 2021-08-27 16:53 UTC _(reply to #11)_

Noted, I’ll add this as a sorting option after the feature release.

---

### Post #13 — **restrading** | 2021-08-29 15:30 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> Let’s sort the models by ranking by default.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> What about adding the option to filter out not staked models.

[@nyuton](</u/nyuton>) Both of the above are now possible with the [recent feature release](<http://forum.numer.ai/t/updates-numerbay-the-community-marketplace/3844/11>). Thanks.

---

### Post #14 — **nyuton** | 2021-08-29 16:19 UTC _(reply to #13)_

Looks great! Thanks!

---

### Post #15 — **jrai** | 2021-08-29 17:29 UTC

All set on most recent CoE transfers (26 and 30 NMR transactions):  
<https://etherscan.io/tx/0x5d3fc33481e5b69e47157a3a099136927353adf90fb271e044e57968c14517db>  
<https://etherscan.io/tx/0xeef8abf9030e99e805b8b9fec8fa47a883a175bfa1058e7798813d65a014c7b0>

---

### Post #16 — **of_s** | 2021-08-30 12:49 UTC

Is MMC ranking possible?

---

### Post #17 — **restrading** | 2021-08-30 13:00 UTC _(reply to #16)_

Sorting by mmc rep is possible, I can add it in next commit.
