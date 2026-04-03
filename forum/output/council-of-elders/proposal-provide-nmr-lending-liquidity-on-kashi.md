---
title: "[Proposal] Provide NMR lending liquidity on Kashi"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-provide-nmr-lending-liquidity-on-kashi/3633
created_at: 2021-06-21T19:30:05.499000+00:00
last_posted_at: 2021-07-24T13:09:25.999000+00:00
posts_count: 28
views: 2934
tags: []
---

# [Proposal] Provide NMR lending liquidity on Kashi

---

### Post #1 — **jorijnsmit** | 2021-06-21 19:30 UTC

## Sushi’s Kashi

Recently I stumbled upon Sushi’s lending/borrowing platform Kashi, and discovered it allows for the creation of custom isolated markets. NMR is supported by this due to it having a good Chainlink oracle which is required by the Kashi protocol.

Anyway I was able to get NMR whitelisted by Sushi and multiple NMR pair markets were created. Some liquidity was provided by the community on [the USDC/NMR pair](<https://app.sushi.com/bento/kashi/borrow/0x7bee2161afa1aee4466e77bed826a41d5a28db46>)—totalling ~700 NMR at time of writing—which is completely borrowed out at the moment.

I think the fact that the Kashi pool is maxed out clearly shows that there is demand for more borrowing opportunities. This, combined with for example the efforts by Numerai to [enable NMR borrowing on Aave](<https://governance.aave.com/t/arc-add-support-for-nmr/3982>) is reason for me to believe it is worth considering to provide NMR from treasury to a Kashi contract (I suggest USDC-NMR).

## Why borrowing: use case

Borrowing allows Numerai tournament users to participate in staking NMR on their models **without** exposing themselves to NMR price fluctuations. When creating the borrowing transaction, NMR is borrowed at its current market rate (e.g. at $50). In order to do so, collateral has to be provided—USDC or some other stablecoin being the logical choice. Let’s say a collateral worth $1000 is provided. In all cases, one can only borrow against 75% of this collateral. So 15 NMR (750/50) can then be borrowed. An annual percentage rate (APR) is then charged to the borrower’s position and an almost equal APR is paid to the lender. This rate changes every 8 hours and is dependent on the supply/demand; the algorithm always aiming for a utility of the pool of 80%. See [this page of Kashi’s FAQ for more info on the workings of their elastic rate](<https://docs.sushi.com/faq-1/kashi-bentobox-faq>).

Now whenever the borrower wants his collateral back, he can pay back the 15 NMR + interest. So as long as expected return on tournament staking > Kashi interest rate borrowing makes sense.

Note that as a borrower the risk of getting your collateral liquidated does exist; this becomes possible when the USD value of your borrowed asset (NMR) surpasses 75% of the USD value of your collateral. A liquidator can then swap your collateral for the borrowed asset in order to pay back the lender, plus collect a 12% fee [[source]](<https://dev.sushi.com/bentobox/contracts>). Therefore it is probably wise to anticipate some increase of NMR price and only borrow against maybe 25% or 50% of your collateral (depending on your expected maximum increase in price for NMR, plus your willingness to pay the 12% fee in case of liquidation).

## Why lending

Put some NMR to work outside the tournament, while providing a valuable service to the community.

## TLDR

I propose to provide NMR from treasury to the USDC-NMR Kashi contract (`0x7bee2161afa1aee4466e77bed826a41d5a28db46`).

---

### Post #2 — **jorijnsmit** | 2021-06-21 19:40 UTC

Btw I thought about doing a video walkthrough of borrowing NMR using MetaMask—not sure if needed.

---

### Post #3 — **johnnyjohnny** | 2021-06-21 20:24 UTC

How does Kashi decide the interest rate? 2.24% APY seems terrible. As an NMR holder, I’d never lend in at that rate, even just compared to staking on the examples. One would think that a market driven mechanism would increase the interest rate as the available NMR is lent out. The fact that 100% of what is available is lent out and the APY is only at 2% seems to clearly indicate there is more demand than supply at 2% and the rate needs to go up.

---

### Post #4 — **jorijnsmit** | 2021-06-21 20:47 UTC _(reply to #3)_

Of course anyone is free to decide what to do with their NMR. My proposal is to lend out NMR from treasury, not for you to do so. Treasury has no alternative that I am currently aware of that generates yield—I’m also pretty sure they don’t stake on (example) models.

As to the calculation of the interest rate: as written in my proposal, Kashi’s FAQ has detailed description of their elastic interest rate: [Kashi/BentoBox FAQ - Sushi](<https://docs.sushi.com/faq-1/kashi-bentobox-faq>).

---

### Post #5 — **johnnyjohnny** | 2021-06-21 20:55 UTC _(reply to #4)_

Got it, key excerpt for anyone interested “If the utilization goes above the maximum target utilization, the interest rate doubles every eight hours. At 100%, utilization it doubles every 8 hours. At 90% it’s much slower, and at 80% it’s stable.”.

Since utilization is at 100%, presumably the interest rate will rapidly increase.

---

### Post #6 — **master_key** | 2021-06-21 22:37 UTC

> That’s why USDC is a logical choice; as long as it keeps its peg of 1:1 your position is not at risk of defaulting.

Is this accurate? I thought liquidation was based on the value of the borrowed token vs the value of your collateral. So if NMR price goes up too much, your collateral would not longer be cover your debt, so you would get liquidated with penalty. (but also your NMR that you now have would be worth more than it was before as well, so it’s not so bad except for the liquidation penalty).

---

### Post #7 — **hb1** | 2021-06-22 00:51 UTC

I like the proposal and I think it would be a good idea to add liquidity to Sushi if Aave is going to take a long time.

I do think we would need to add some conditions to the proposal for how/why/when the Council would remove liquidity. If no one is borrowing and the NMR could be used for a more interesting proposal, can the Council remove at any time? Should another proposal be made to remove the liquidity, same as adding it? Should it be moved to Aave once lending is available there instead? Those would be interesting to add.

---

### Post #8 — **jorijnsmit** | 2021-06-22 17:48 UTC _(reply to #6)_

You are right, this is indeed the case. The reason I didn’t notice this is because the “limit used %” in the UI is based on the last known oracle price to the contract. Since it doesn’t update by itself (you have to force it and include it in an on-chain tx), that value remained static for me.

Anyway I’ll amend the opening post with correct liquidation info.

---

### Post #9 — **jorijnsmit** | 2021-06-22 17:48 UTC _(reply to #7)_

Sure. Let’s say the initial deposit is for a period of a year. Six months after this deposit, council decides whether they should (1) reduce their position when possible, with the goal of closing their position by the end of 12 month period, (2) increase their position—either at a regular interval or all at once, or (3) keep their position as is.

Of course any of this can be overruled at any time with a new proposal which passes.

---

### Post #10 — **giulianociccone** | 2021-06-23 07:00 UTC

I like the proposal, specially as it would generate extra source of yield for the treasury. It would be interesting to define clear conditions about ‘the program’ as my main concern is the recall risk.

---

### Post #11 — **jrai** | 2021-06-24 23:12 UTC

We probably shouldn’t wait around for an aave market. Aave is considered to be safer and more established, so it would probably be the best choice, but it may be a while. Kashi seems like a good option for now.

How much should we be allocating? There are 289 NMR in treasury and some other proposals to fund soon too. Like 150 NMR?

---

### Post #12 — **mic** | 2021-06-25 00:49 UTC

What are the risks for the lender?

---

### Post #13 — **aventurine** | 2021-06-25 06:32 UTC

We are sort of discussing general questions and other SushiSwap topics on the rocketchat if the group is interested in the information to possibly add to proposal [Numerai Community](<https://community.numer.ai/channel/numeraire?msg=W2xgoveWByBsJ96Z5>)

---

### Post #14 — **aventurine** | 2021-06-25 06:40 UTC

Also I created a #SushiSwap-Kashi channel to the rocketchat if anyone is interested

---

### Post #15 — **jrai** | 2021-06-25 18:35 UTC _(reply to #12)_

Mainly just smart contract risk I guess, any bugs in the lending pool could mean total loss of funds

---

### Post #16 — **mic** | 2021-06-25 23:05 UTC _(reply to #15)_

Thanks. I think there might also be a risk if NMR price goes up a lot quickly and the lender doesn’t liquidate in time, based on the discussions in chat.

---

### Post #17 — **mugamma** | 2021-06-26 04:10 UTC _(reply to #11)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> How much should we be allocating? There are 289 NMR in treasury and some other proposals to fund soon too. Like 150 NMR?

Is this enough to be material for any meaningful objective? Seems like one participant could get borrow it all and get all the benefit.

---

### Post #18 — **jorijnsmit** | 2021-06-26 09:03 UTC _(reply to #17)_

I agree. To be honest I was talking about Numerai’s treasury itself. Ballpark I’d say if only 10% of current classic stakers (~500k NMR) would be interested in borrowing, Kashi pool would need to be ~50k NMR. That’s not yet taking into consideration Signals and/or the chance of that 10% being a low estimate.

From what I can gather, treasury (`0x1248C66Bb94607Cf6b80D3AEc3E62A9FE421e210`, `0x0000000000377D181A0ebd08590c6B399b272000` and `0x67b18F10C0Ff8C76e28a383B404E8e6FDEfe2050`) currently holds ~5m NMR.

Another approach would be to promote it and let the community source it. We’ve basically been seeing this already; the pool quadrupled to ~3k NMR (!) since posting this proposal.

Increasing liquidity does not only enable more users to make use of it, but it should also stabilise the interest rate which I think is just as important.

---

### Post #19 — **autratec** | 2021-06-26 09:36 UTC _(reply to #18)_

Existing pricing model used by defi has some fundamental defects, and could be easily attacked with help from flashloan. Unless the liquid is large enough, the price could be easily manipulated and liquidity provider will suffer the lose.

---

### Post #20 — **jorijnsmit** | 2021-06-26 09:48 UTC _(reply to #19)_

What do you mean by “the pricing model used by defi”? Are you talking about the Chainlink oracle? I don’t see how that can be attacked with a flashloan?

---

### Post #21 — **jrai** | 2021-06-27 21:13 UTC

CoE executed a transaction lending 200 NMR to the Kashi pool <https://etherscan.io/tx/0xdb67dd0418553ddf64bb79da14e4457ed1b855eb3fc627cc295423f3b79632d4>

---

### Post #22 — **jorijnsmit** | 2021-06-27 21:32 UTC _(reply to #21)_

Awesome!!! Happy farming ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) ![:man_farmer:](http://forum.numer.ai/images/emoji/twitter/man_farmer.png?v=9)

And great news for anyone wanting to borrow of course!

---

### Post #23 — **andralienware** | 2021-07-22 00:20 UTC _(reply to #21)_

I’m not too familiar with how to use etherscan to well. Did you just look up the CoE wallet? Does anyone also happen to know the address of the Erasure contracts and how to see things like burns and adds to people’s stakes on etherscan?  
Thanks

---

### Post #24 — **eleven_sigma** | 2021-07-23 08:05 UTC

I want to borrow 5000 NMR for a year (at least for six months) and at the end of period return the same amount (5000) of NMR.  
I would like to pay a fixed and known amount of interest, based on initial price (155K USD aprox).  
Which should be this interest rate? 10%? 20%?  
Where can I do this kind of transaction?  
Sorry if some of this is trivial but I never worked with these platforms.

Added:  
Should the interest be paid in NMR or USD?

---

### Post #25 — **jorijnsmit** | 2021-07-23 08:55 UTC _(reply to #24)_

At a fixed rate will need a different contract. Currently there’s 4k+ NMR available to borrow at [SUSHI](<https://app.sushi.com/borrow/0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46>) at an elastic interest rate (charged in NMR).

See for a better understanding of this elastic interest rate and on using Kashi to lend or borrow NMR my articles:

  * [Kashi NMR Lending: Earn APR Without Staking on a Model | by Gosuto | Jul, 2021 | Medium](<https://gosuto.medium.com/kashi-nmr-lending-earn-apr-without-staking-on-a-model-108c49bc464d>)
  * [Kashi NMR Borrowing: Stake on Your Model Without NMR Price Exposure | by Gosuto | Jul, 2021 | Medium](<https://gosuto.medium.com/kashi-nmr-borrowing-stake-on-your-model-without-nmr-price-exposure-bc687fcacd9f>)

---

### Post #26 — **eleven_sigma** | 2021-07-23 09:05 UTC _(reply to #25)_

If I have understood the elastic interest rate, if I borrow all the offer then the interest will skyrocket. Is necessary a bigger pile of NMR in Kashi…

---

### Post #27 — **elon_ai** | 2021-07-24 12:02 UTC _(reply to #6)_

you are correct, i didn’t fully understand this and was almost liquidated during an NMR price spike (presumably would have incurred some fees in the transaction). Luckily I was able to add more USDC to the collateral.

---

### Post #28 — **eleven_sigma** | 2021-07-24 13:09 UTC _(reply to #27)_

So for to be safe, we need to have as collateral aprox 2X of value of NMR borrowed, so if NMR spike 50-80% you still be covered.  
This borrow is special, as not used for short (that is a real risk). Using the NMR for stacking you have the risk of loss if your models underperform, but you are free of risk in NMR change value.
