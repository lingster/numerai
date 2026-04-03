---
title: "[Milestone] NumerBay Stake Mode Beta"
category: Council of Elders
url: https://forum.numer.ai/t/milestone-numerbay-stake-mode-beta/4330
created_at: 2021-10-13T16:30:42.669000+00:00
last_posted_at: 2021-10-13T21:40:38.231000+00:00
posts_count: 2
views: 1052
tags: []
---

# [Milestone] NumerBay Stake Mode Beta

---

### Post #1 — **restrading** | 2021-10-13 16:30 UTC

**NumerBay (<https://numerbay.ai/>) stake mode is now live for beta!** Thanks for your support as always.

**DISCLAIMER: NumerBay is in beta and may have unexpected issues. This is NOT an official Numerai project. Neither Numerai nor NumerBay will be liable for any loss.**

This is the final milestone for core features as laid out in the proposal. However, there will be other feature releases and enhancements from time to time.

For issue reporting and feature requests, please feel free to post in the [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat or DM me.

* * *

**What is Stake Mode?**  
Previously the on-platform sale on NumerBay requires distribution of predictions files to buyers and provides no means of automation for submissions. When a product is listed in stake modes, NumerBay submits for the buyers without distribution of raw files. Sellers can also choose to impose a Stake Limit for their customers.

* * *

**Listing Modes**  


[![NumerBay 20211013 Listing Modes](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4bb1d99a04bdf78890be503528c7cc7512e5ed9f_2_690x99.png)NumerBay 20211013 Listing Modes3360×484 72 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4bb1d99a04bdf78890be503528c7cc7512e5ed9f.png> "NumerBay 20211013 Listing Modes")

  1. **Distribute File** : Buyers can download files. Sellers can either upload file artifact or add external URL. Buyers can optionally choose to desginate a model slot for submission during checkout. The file to submit will be the latest CSV artifact file uploaded by the seller
  2. **Stake Only** : Buyers cannot download files. Sellers can only upload file as product artifact. Buyers must designate a model slot for submission during checkout.
  3. **Stake Only with Limit** : Same as above but with a stake limit for buyers. Target Stake Value is calculated as `TARGET_STAKE = CURRENT_STAKED_AMOUNT + PENDING_STAKE_CHANGE`. When `TARGET_STAKE > STAKE_LIMIT`, the pending stake change will be set to keep the target stake value below the stake limit.



* * *

**(Optional) Artifact Validation Endpoint for API Users**  
A new [artifact upload validation endpoint](<https://numerbay.ai/docs#/products/validate_upload_backend_api_v1_products__product_id__artifacts__artifact_id__validate_upload_post>) is now available. API users can call this endpoint after uploading artifact to NumerBay to get immediate confirmation of upload success/failure, instead of waiting for 10 minutes. This makes the API workflow similar to Numerai’s (request upload URL → upload → validate). Buyers who have emails will receive notifactions for the new upload. Submissions will happen for confirmed orders immediately.

Please refer to the example notebook for details: <https://github.com/councilofelders/numerbay/blob/master/NumerBay%20Example.ipynb>

[![NumerBay 20211013 Example Notebook](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/43ec8e514616144a8082e153d46c1eed7f4d72b4_2_477x500.png)NumerBay 20211013 Example Notebook2342×2454 456 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/43ec8e514616144a8082e153d46c1eed7f4d72b4.png> "NumerBay 20211013 Example Notebook")

* * *

**Know issues and temporary workarounds**

  1. There may be payment confirmation failure if a buyer tries to buy multiple products concurrently. _[Workaround: Buy one product at a time, only start buying something else when the previous order is confirmed]_



* * *

**Past threads**  
Original Proposal

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/restrading/48/2928_2.png) [[Proposal] Numerai Community Marketplace](<http://forum.numer.ai/t/proposal-numerai-community-marketplace/3622>) [Council of Elders](</c/council-of-elders/12>)

> Thanks to [@arbitrage](</u/arbitrage>) for the draft feedback. This proposal follows the [format](<http://forum.numer.ai/t/how-to-write-a-coe-proposal/3287>) suggested by [@jrb](</u/jrb>) Anything in the below proposal is open for discussions and changes. Thank you for the feedback in advance. 1.Proposal Tl;dr: I’d like to build an open-sourced prototype of a StockX-style marketplace for Numerai model predictions. A static mockup: [[image]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1c846a30a072b7d30f4b8eeb48f33e66d4aba879.png>) Ideation: The idea hit me during my recent [GPU hunting craze on StockX](<https://stockx.com/nvidia-evga-geforce-rtx-3090-ftw9-ultra-gaming-24gb-gddr6x-backplate-graphics-card-24g-p5-3987-kr>). StockX is a stock-market-like online marketplace for consumer goods (s… 

Project Updates

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/restrading/48/2928_2.png) [[Updates] NumerBay - The Community Marketplace](<http://forum.numer.ai/t/updates-numerbay-the-community-marketplace/3844>) [Council of Elders](</c/council-of-elders/12>)

> Hi CoE and everyone interested in NumerBay, The [original NumerBay proposal](<http://forum.numer.ai/t/proposal-numerai-community-marketplace/3622/32>) has become too long to navigate, so I’m starting this new one to post exclusively about updates to the project. In addition, I’m testing out the Wiki function to allow anyone to add feature requests. Thanks for your support. 

First Milestone

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/restrading/48/2928_2.png) [[Milestone & Vote] NumerBay.ai Release and Future Features](<http://forum.numer.ai/t/milestone-vote-numerbay-ai-release-and-future-features/3943>) [Council of Elders](</c/council-of-elders/12>)

> NumerBay (<https://numerbay.ai/>) is Here! Thanks to the support from the CoE and everyone interested in this project. The code repository is public at <https://github.com/restrading/numerbay> [[NumerBay 20210801 seller flow]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2e818d7bc54c05e0d0a959e03ecb39358a33d9a5.gif> "NumerBay 20210801 seller flow") For those who are not familiar with this project, this is the community marketplace originally proposed [here](<http://forum.numer.ai/t/proposal-numerai-community-marketplace/3622>) and is funded by the Numerai Council of Elders. This is an interim early release with support for generic 3rd party listing of Numerai predictions, models, Signals p… 

Second Milestone

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/restrading/48/2928_2.png) [[Milestone] NumerBay On-Platform Sales Beta](<http://forum.numer.ai/t/milestone-numerbay-on-platform-sales-beta/4174>) [Council of Elders](</c/council-of-elders/12>)

> NumerBay (<https://numerbay.ai/>) on-platform sales is now live for beta! Thanks to the continued support from the CoE and everyone interested in this project. DISCLAIMER: NumerBay on-platform feature is in beta and may have unexpected issues. You are advised not to make big transactions. Neither Numerai nor NumerBay will be liable for any loss incurred. If you don’t know about NumerBay, it is the community marketplace funded by the Numerai Council of Elders. You can refer to the threads at the … 

Dev Updates and Feature Releases  
See [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat

Thank you and happy sailing on NumerBay ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **rigrog** | 2021-10-13 21:40 UTC

The correct way to do stake mode, is for the buyer and seller to agree on a _comission rate_. E.g. if the agreed rate is 1%, then the buyer could stake 100 NMR and pay the seller 1 NMR… OR stake 735 NMR and pay the seller 7.35 NMR, and so forth. This gives the smooth scalability, that buyers and sellers will want.

To get the same effect, from “Stake Only, with Limit”: the seller would set the price at 1 NMR, and the limit at 100 NMR. Then the seller can only get full value, by staking a whole multiple of 100 NMR, and making the same transaction that many times.

Since 100 NMR would be too much for most prospective buyers, the seller will adjust by also offering _the same prediction_ at a price of 0.1 NMR, with a stake limit of 10 NMR. And so on, and so forth…

That’s the crufty noise, your platform will have to deal with… _unless_ you provide the natural, intuitively expected comission rate model in the first place.

EDIT: Restrading made a very strong case, that “tiered pricing” will provide the needed flexibility, in some ways even more (like price breaks for higher volume). It’s kinda complicated, and my models aren’t currently good enough that I need to figure it out yet.

Go over to #Numerbay on chat, to learn more.
