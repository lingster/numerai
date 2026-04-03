---
title: "[New Feature] NumerBay Multi-option Pricing"
category: Council of Elders
url: https://forum.numer.ai/t/new-feature-numerbay-multi-option-pricing/4423
created_at: 2021-10-30T07:25:41.803000+00:00
last_posted_at: 2021-10-30T07:25:41.938000+00:00
posts_count: 1
views: 757
tags: []
---

# [New Feature] NumerBay Multi-option Pricing

---

### Post #1 — **restrading** | 2021-10-30 07:25 UTC

**NumerBay (<https://numerbay.ai/>) now supports multi-option pricing.**

**DISCLAIMER: NumerBay is in beta and may have unexpected issues. This is NOT an official Numerai project. Neither Numerai nor NumerBay will be liable for any loss.**

For issue reporting and feature requests, please feel free to post in the [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat or DM me.

* * *

**What is Multi-option Pricing?**  
Previously listings on NumerBay can only be sold one round at a time at a fixed price. With the new pricing scheme, sellers can offer buyers more flexible options such as bundling sales for multiple rounds (prepaid subscriptions), making volume discounts, setting different prices for different modes, etc.

* * *

**Please note the following:**

  1. The “Price” field for each option refers to the **total for that option** , not the equivalent unit price per round. Total price for any option still needs to be above 1 NMR. Duplicated price is not allowed.
  2. Mixed on/off-platform listing is allowed. However, **the first option is the default** for display to buyers.
  3. Please remember to save the pricing option first before saving the listing form.
  4. NumerBay does not yet send out weekly reminders to upload artifacts. Sellers need to remember to do so if they have active subscriptions
  5. `[Number of Rounds for Order] = [Pricing Option Bundled Quantity] x [Order Quantity]` (E.g. a buyer who bought `3` of “`2 x file @ 1.5000 NMR`” option needs to pay `3 x 1.5 = 4.5 NMR`, the order will be active for `3 x 2 = 6 rounds`)
  6. Duplicated purchase is not allowed, this also applies to active multi-round orders. If a buyer bought a subscription of 2 rounds, they can only make a new order for that product after the order completes in 2 weeks.



* * *

**New Listing Form**  


[![NumerBay 20211024 Multiple Pricing](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/36afcbc64e01e45c1e9585b3c77736547cf16376_2_434x500.png)NumerBay 20211024 Multiple Pricing2260×2598 300 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/36afcbc64e01e45c1e9585b3c77736547cf16376.png> "NumerBay 20211024 Multiple Pricing")

  


[![NumerBay 20211030 Update Pricing](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/94f1c952bfcbd8675b82f87f5071ba031edbd6d6_2_512x500.png)NumerBay 20211030 Update Pricing2242×2186 273 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/94f1c952bfcbd8675b82f87f5071ba031edbd6d6.png> "NumerBay 20211030 Update Pricing")

**New Multi-round Order Info Display**  


[![NumerBay 20211030 Order Info](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8602009e301ec4813b7f0eea892845ff4371f6c4_2_517x255.png)NumerBay 20211030 Order Info1532×758 82.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8602009e301ec4813b7f0eea892845ff4371f6c4.png> "NumerBay 20211030 Order Info")

**New Catalog Display**  
Buyer can select the pricing option in the dropdown, and set the quantity of that option to buy.  


[![NumerBay 20211024 Listing](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26596c106904cb864f85ec26f5be6ab39d0f72e1_2_690x166.png)NumerBay 20211024 Listing2036×492 60.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/26596c106904cb864f85ec26f5be6ab39d0f72e1.png> "NumerBay 20211024 Listing")

**New Product Display**  
A new “From the same seller” section has been added  


[![NumerBay 20211030 Product](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a87ef573ddd15b79ef8593dbb5fe467a56e6fff8_2_440x500.jpeg)NumerBay 20211030 Product2574×2924 582 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a87ef573ddd15b79ef8593dbb5fe467a56e6fff8.jpeg> "NumerBay 20211030 Product")

**New Payment Summary Page**  


[![NumerBay 20211030 Payment](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cc0578d173f330a0b1054f725af5ea9ec37fca74_2_690x470.png)NumerBay 20211030 Payment2564×1748 318 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cc0578d173f330a0b1054f725af5ea9ec37fca74.png> "NumerBay 20211030 Payment")

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

Third Milestone

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/restrading/48/2928_2.png) [[Milestone] NumerBay Stake Mode Beta](<http://forum.numer.ai/t/milestone-numerbay-stake-mode-beta/4330>) [Council of Elders](</c/council-of-elders/12>)

> NumerBay (<https://numerbay.ai/>) stake mode is now live for beta! Thanks for your support as always. DISCLAIMER: NumerBay is in beta and may have unexpected issues. This is NOT an official Numerai project. Neither Numerai nor NumerBay will be liable for any loss. This is the final milestone for core features as laid out in the proposal. However, there will be other feature releases and enhancements from time to time. For issue reporting and feature requests, please feel free to post in the [#nu…](<https://community.numer.ai/channel/numerbay>)

Dev Updates and Feature Releases  
See [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat

Thank you and happy sailing on NumerBay ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)
