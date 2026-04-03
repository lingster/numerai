---
title: "[Request for Proposal] One of you writes a Kashi Lending/Borrowing Tutorial for up to 5 NMR"
category: Council of Elders
url: https://forum.numer.ai/t/request-for-proposal-one-of-you-writes-a-kashi-lending-borrowing-tutorial-for-up-to-5-nmr/3707
created_at: 2021-07-03T17:22:32.225000+00:00
last_posted_at: 2021-07-15T21:46:30.234000+00:00
posts_count: 15
views: 1548
tags: []
---

# [Request for Proposal] One of you writes a Kashi Lending/Borrowing Tutorial for up to 5 NMR

---

### Post #1 — **hb_scout** | 2021-07-03 17:22 UTC

Hi all, I’m trying something new, a Council of Elders **Request for Proposals**.

**We would like to solicit proposals from you all to write a Kashi NMR Lending/Borrowing tutorial**. To submit a “proposal” to this request, you would just have to respond in this thread as opposed to make a new proposal forum post in the suggested format.

SushiSwap Kashi lending for NMR-USDC: [Sushi](<https://app.sushi.com/bento/kashi/lend/0x7bee2161afa1aee4466e77bed826a41d5a28db46>)  
SushiSwap Kashi borrowing for NMR-USDC: [Sushi](<https://app.sushi.com/bento/kashi/borrow/0x7bee2161afa1aee4466e77bed826a41d5a28db46>)

**What we would like** : a Medium post, or a post on a similar platform, that can be widely distributed that explains in simple and clear steps how to 1) lend your NMR on Kashi and 2) how to borrow NMR on Kashi. It could be two separate posts if that is more clear as well.  
The target audience for #1 would be holders of NMR that do not want to participate in the Numerai tournament, but want to get some returns on their holding by lending out their NMR. Lending NMR can be framed as a method for “staking on other participants” given that there is consistent demand for this feature on the forum and on RocketChat. The risks involved in lending, such as liquidation, should be briefly explained.  
The target audience for #2 would be Numerai tournament participants that want to leverage or hedge their stake. Again the risks involved in borrowing should be explained.

**Suggested proposed pay** : The CoE is willing to pay **up to 5 NMR for this effort**. We would like the person that fulfills the proposal request to log their hours and would suggest $25/hour pay, approximately 6 hours of effort = $150 ~= 4.7 NMR. Before transferring the funds to the person who fulfills the proposal, the CoE will also request the opportunity to send over any suggested edits or additions.

**How fulfilling the request for proposals will work** : _This is definitely a trial of Requests for Proposals so if you have suggestions for this part, please let us know!_ The first person that seriously states their intent to fulfill the proposal in this thread will then have the first rights to collecting the bounty. **They will then have 3 days to finish the proposed work** or the rights to collect the bounty will be passed on to the next person who then seriously states their intent to deliver.  
The CoE has chatted about this already and agreed to the amount we’re willing to pay, but we’re not going to create any sort of contract to escrow the funds for something this size. We’ll simply transfer the funds from the multi-sig treasury after completion of the task.

I hope this sounds interesting to everyone! I would really love for there to be a mass distribution of these tutorials so that we can help create a robust lending market. I think there’s a lot of liquidity out there in the community that hasn’t heard about the Kashi pool yet or just isn’t confident enough to give it a shot. This could be a major development for NMR if we can collectively get this to take off! Thanks

---

### Post #2 — **jorijnsmit** | 2021-07-03 18:57 UTC

I like this idea and I’m willing to give it a shot tomorrow. As stated [before](<http://forum.numer.ai/t/proposal-provide-nmr-lending-liquidity-on-kashi/3633/2>) I thought about making a video tutorial on how to lend/borrow NMR; I think I’ll do that and accompany it with a written summary?

In regards to Requests for Proposals; I think these should just be called bounties. At least that’s a common way I see other DAOs do it. If more ideas for tasks such as this one exist, it could even be worth it to set up a channel (#bounties, #contribute?) for it on RocketChat. And indeed escrowing is then overkill, communicating about it here on the forum and/or RocketChat should be sufficient.

---

### Post #3 — **hb_scout** | 2021-07-03 19:15 UTC _(reply to #2)_

That sounds great! [@jorijnsmit](</u/jorijnsmit>) gets first dibs. Do you think 3 days is sufficient to make the tutorials or decide to pass off the rights to claim the bounty to the next person?

---

### Post #4 — **jorijnsmit** | 2021-07-03 19:23 UTC _(reply to #3)_

Yea for sure, think I can have a draft done tomorrow. Most of the content I have at hand already probably, from my initial research into Kashi and my proposal around it.

---

### Post #5 — **jorijnsmit** | 2021-07-05 10:10 UTC _(reply to #4)_

I submitted a draft for an article to [@hb_scout](</u/hb_scout>) on chat.

---

### Post #6 — **aventurine** | 2021-07-09 06:47 UTC _(reply to #5)_

[@hb_scout](</u/hb_scout>) is this still being reviewed or was a link submitted somewhere already? Im interested in reading it. Besides the general chat also maybe throw the link in the kashi channel. [@jorijnsmit](</u/jorijnsmit>)

---

### Post #7 — **jorijnsmit** | 2021-07-09 18:34 UTC _(reply to #6)_

Was able to process the feedback. Just published part 1, which focuses on lending. Part 2 will focus on borrowing.

Part 1: [Kashi NMR Lending: Earn APR Without Staking on a Model | by Jorijn Jacko Smit | Jul, 2021 | Medium](<https://gosuto.medium.com/kashi-nmr-lending-earn-apr-without-staking-on-a-model-108c49bc464d>)

---

### Post #8 — **mic** | 2021-07-10 03:03 UTC _(reply to #7)_

It is a good introduction to the high level concepts and risks.

A few friendly comments:

It could have more tutorial to it, more on the “how to”. I know it is not so good to be too specific because things change rapidly on these platforms, but maybe it is necessary for the audience.

Liquidation could be further discussed, what does it mean to “become a liquidator yourself” and how do you become one?

Who effectively pays the liquidation bonus - the lender or borrower?

Is it a typo “When under 70% (ie less than 80%…” ?

---

### Post #9 — **jorijnsmit** | 2021-07-10 07:06 UTC _(reply to #8)_

There is also an idea to do a video tutorial. I’ll think about this after release part 2, I could maybe combine lending and borrowing in the same video.

To become a liquidator one would have to write a script that keeps tabs on borrowing positions and calls the smart contract’s [liquidation function](<https://dev.sushi.com/bentobox/interfaces/lending-pair#liquidate-nonpayable-address-uint-256-address-address-bool>) where needed. Definitely a more advanced endeavour.

Liquidation bonus is subtracted from the borrower’s collateral. I’ll make this more clear the article.

Typo fixed. Cheers.

---

### Post #10 — **_liamhz** | 2021-07-12 18:17 UTC _(reply to #8)_

Agreed that it’d be nice to have some “how to” tutorial screenshots with the Kashi interface in both of the Medium posts

---

### Post #11 — **jorijnsmit** | 2021-07-14 17:30 UTC

Part 2 has just been published here: [Kashi NMR Borrowing: Stake on Your Model Without NMR Price Exposure | by Gosuto | Jul, 2021 | Medium](<https://gosuto.medium.com/kashi-nmr-borrowing-stake-on-your-model-without-nmr-price-exposure-bc687fcacd9f>).

Thanks for all the proofreading, feedback, shares, etc. The NMR community is so much bigger than I thought! Most of all thanks to [@hb_scout](</u/hb_scout>) for this bounty. It was fun to come in touch with my inner blogger a bit more ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

As agreed upon with the council, these two articles fulfil the bounty. I know there’s quite some demand for a video tutorial as well—I will think about doing one after Sushi’s next release. I got a feeling those new features will impact Kashi as well (in a good way). I am also still exploring the idea of a handy dashboard to monitor this lending market.

Requesting for the bounty to be transferred directly to my Numerai address; `0x00000000000000000000000000000000000212f8`.

---

### Post #12 — **aventurine** | 2021-07-14 17:49 UTC _(reply to #11)_

Article is awesome. I think [@_liamhz](</u/_liamhz>) was hoping to see some more “how to” screenshots. Is there a way to edit the articles to include maybe some screenshots of the lending platform with a little step by step like 1) Buy USDC 2) add to wallet 3) connect to sushiswap…etc?

---

### Post #13 — **hb_scout** | 2021-07-14 23:31 UTC _(reply to #12)_

The interfaces are all changing in about a week so we’ll request some new materials for the new versions at that point. I think quick video tutorials will be the most useful to serve that purpose, but screenshots added to these articles would be a good addition too. These articles do a great job at giving me the info to have the confidence that borrowing/lending would be useful, safe, profitable, etc. The other product will show us what buttons to click when we’ve made that decision!

---

### Post #14 — **jrai** | 2021-07-15 19:23 UTC

Payment executed! <https://etherscan.io/tx/0x0932666a4dce77b581e532e466877d77ded80a347b160b5c6dbc8d00c2ff9b08>

Thanks [@jorijnsmit](</u/jorijnsmit>)

---

### Post #15 — **aventurine** | 2021-07-15 21:46 UTC _(reply to #14)_

Is this first payment to non CoE community participant for a proposal? I think the only other out payment so far was for reimbursement for multisig correct? If so, Awesome!
