---
title: "[Milestone] NumerBay On-Platform Sales Beta"
category: Council of Elders
url: https://forum.numer.ai/t/milestone-numerbay-on-platform-sales-beta/4174
created_at: 2021-09-21T11:10:31.325000+00:00
last_posted_at: 2021-09-21T11:10:31.485000+00:00
posts_count: 1
views: 726
tags: []
---

# [Milestone] NumerBay On-Platform Sales Beta

---

### Post #1 — **restrading** | 2021-09-21 11:10 UTC

**NumerBay (<https://numerbay.ai/>) on-platform sales is now live for beta!** Thanks to the continued support from the CoE and everyone interested in this project.

**DISCLAIMER: NumerBay on-platform feature is in beta and may have unexpected issues. You are advised not to make big transactions. Neither Numerai nor NumerBay will be liable for any loss incurred.**

If you don’t know about NumerBay, it is the community marketplace funded by the Numerai Council of Elders. You can refer to the threads at the bottom of this post for history.

For issue reporting and feature requests, please feel free to post in the [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat or DM me.

Another thread on future feaures and voting will be posted later this week.

* * *

**What is on-platform sales?**  
The initial version of NumerBay only supported linking to listings on third-party platforms and sellers have to self-manage file distributions. Buyers also needed to pay fees to external platforms.

With this new release, sellers can now opt to list their Numerai product artifacts (predictions csv, model notebooks, etc.) natively on NumerBay which allows them to receive payments in NMR and distribute files to buyers (and even to automate this process using the REST API endpoints). Buyers can now make payments to sellers directly without a rent-seeking middleman. And thanks to the support from the Numerai team, NMR transactions from Numerai wallets are currently gas-free.

**IMPORTANT: Currently, buyers must only initiate transactions from their Numerai wallets, transactions from other wallets will not be acknowledged.**

* * *

**Demo walkthroughs**  
[Placeholder for demo video]

* * *

**Know issues and temporary workarounds**

  1. Round rollover timing can vary week-to-week. Transactions too close to submission deadline may have issues with conrfirmation and artifact upload/download. In future, activities will be disabled close to the submission deadline until rollover completes. [_Workaround: don’t buy products or download too close to the submission deadline_]
  2. Related to 1. Orders made immediately after the submission deadline for the next round might still be counted towards the previous round and will be considered expired once rollover happens. This will be fixed soon together with 1. [_Workaround: don’t buy products for the next round immediately after the submission deadline of previous round. You can check whether a round rollover has happened by checking the “round” number in any product page_]
  3. There was a rare issue with payment transaction timestamp, probably a fault with my local machine or external system. Sometimes when a payment is made too quickly the payment timestamp ends up being before the order creation time. The exact cause has not been identified yet. [_Workaround: After making an order, wait about 30 seconds before making payment through your Numerai wallet_]
  4. ~~Email notifications are disabled as they are autoflagged by the current email provider as spam. This will be available as soon as the provider issue gets resolved.~~



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

Dev Updates and Feature Releases  
See [#numerbay](<https://community.numer.ai/channel/numerbay>) channel in rocket chat

Thank you and happy sailing on NumerBay ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)
