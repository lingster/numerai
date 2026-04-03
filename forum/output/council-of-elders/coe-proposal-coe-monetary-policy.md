---
title: "COE Proposal: COE “Monetary Policy”"
category: Council of Elders
url: https://forum.numer.ai/t/coe-proposal-coe-monetary-policy/5405
created_at: 2022-05-15T22:31:03.719000+00:00
last_posted_at: 2022-05-22T19:35:51.467000+00:00
posts_count: 10
views: 1158
tags: []
---

# COE Proposal: COE “Monetary Policy”

---

### Post #1 — **dev0n** | 2022-05-15 22:31 UTC

With the recent crypto market volatility, there may be renewed interest (at least there is from me) in the ability to remove NMR currency risk and focus on model returns in fiat (i.e. USD).

It is possible today to borrow NMR on the NMR/USDC pair on Kashi lending (see: [Kashi NMR Borrowing: Stake on Your Model Without NMR Price Exposure | by Gosuto | Medium](<https://gosuto.medium.com/kashi-nmr-borrowing-stake-on-your-model-without-nmr-price-exposure-bc687fcacd9f>) ).

However, the current borrow rate is ~70% APY, which is rather high. [https://app.sushi.com/kashi/0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46?pair=0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46&chainId=1](<https://app.sushi.com/kashi/0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46?pair=0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46&chainId=1>)

Previous proposals have asked the COE to add liquidity to that pair (ex: [[Proposal] Provide NMR lending liquidity on Kashi](<http://forum.numer.ai/t/proposal-provide-nmr-lending-liquidity-on-kashi/3633>) )

This proposal is different: Instead of one off proposals to add liquidity, set a “monetary policy”: The COE sets a target borrow APY of 20% or less on the NMR/USDC market.

There would need to be further specification on how COE decides how to tradeoff hitting the borrow APY vs funding other worthwhile projects. At the very least, it could be policy to keep most of the treasury in the contract until needed for funding specific projects, particularly since it will help the COE grow the treasury over time.

---

### Post #2 — **jay1100** | 2022-05-16 09:42 UTC

In general there is not enough NMR in the kashi lending pool. Whenever a few people borrow or repay money the APY jumps a lot. Therefore at the moment it is not a real solution. COE or Numerai would have to put more NMR into the pool (at least several thousand NMR more). Then the APY would automatically be more stable (and be a more real reflection of what the market is willing to pay). Moreover it would allow more people to lend NMR and remove the currency risk. At the moment the pool is just way too small.

---

### Post #3 — **uuazed** | 2022-05-16 12:12 UTC

I like the idea of putting more NMR into the Kashi pool.

---

### Post #4 — **restrading** | 2022-05-16 12:32 UTC _(reply to #3)_

Would lending more NMR be equivalent to letting more people short it, hence lower price?

---

### Post #5 — **zwk** | 2022-05-16 13:03 UTC _(reply to #4)_

Indeed, need to restrict the borrowed NMR to be staked only, no re-selling allowed (at least for those from CoE or treasury reserve). Not sure if that’s possible at smart contract level (when the credit is granted, the NMR goes directly to stake model).

---

### Post #6 — **wigglemuse** | 2022-05-16 13:04 UTC

Somebody just brought this up on RC too. Shorting would surely be a thing during times like this when there is a big sudden downturn, but wouldn’t that be over fairly quickly (to lock in short profits)?

And the time to borrow (for stakers) is when you think the price might be too high (but you just don’t know). If I wanted to add more stake or get into the tournament NOW, I certainly wouldn’t be borrowing – I’d be buying at this low price.

Nevertheless, adding some to a lending pool is probably good. (I’d wait for some market stability first though.)

---

### Post #7 — **dev0n** | 2022-05-17 00:11 UTC

One thing to add is that if this was the policy of the COE, there would be more confidence for stakers since they would be less worried about the borrow APY spiking while their funds are locked up.

---

### Post #8 — **mundan** | 2022-05-22 11:52 UTC

Two things to say:

1- I don’t trust stablecoins.  
2- As NMR and bigger crypto (BTC, ETH) are highly correlated, hedging can be done in the USD/ETH pair, for instance. With this solution  
a) you don’t need to change anything  
b) you hedge against crypto market volatility  
c) you bet on NMR price going up against ETH (or BTC).

I think this is the best solution so far. However, I don’t know how to best implement it (maybe some options of some crypto ETF in tdameritrade platform?) What do you think?

---

### Post #9 — **zwk** | 2022-05-22 14:38 UTC _(reply to #8)_

One might get short ETH exposure directly from the inverse index ETF <https://indexcoop.com/polygon-inverse-iethfli>.  
However, the efficacity of the hedge is very dependent on the market regime/timing. For instance, if you get your stake hedged with ETH from 2022, thanks to the increasingly high correlation during recent market correction, the hedged portfolio outperformed unhedged one, but still under water. For the sake of simplicity, assuming nmr annual stake yield is 100%. (the legend shows the % of initial capital at the end of the period)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/847ab63929dccae012a5f7e2dec43aa8b4d8ba9f_2_690x490.png)image797×567 94.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/847ab63929dccae012a5f7e2dec43aa8b4d8ba9f.png> "image")

However, if one tries to hedge sysmetically for long term, the hedged portfolio turns out to be the worst, due to the low vol, positive drift, and decorrelation regime.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d25ff2835e910ce54b8dd0abc2ac5278026ce73d_2_690x481.png)image813×567 90.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d25ff2835e910ce54b8dd0abc2ac5278026ce73d.png> "image")

More things can be done to improve the hedged performance, such as dynamic hedge based on market regime switching, time-varying beta, etc…

---

### Post #10 — **mundan** | 2022-05-22 19:35 UTC _(reply to #9)_

Probably because of my ignorance, I don’t understand why the hedged version is at a loss. If annual yield is 100% and hedging gives a -smth% yield (hedging cost), shouldn’t we have something around 112.5%* from stake yield minus the hedge cost? Is the hedging cost too high or am I missing the impact of the ETH/NMR ratio? Also, are you comparing half going to the hedging strategy and half going to staking, vs full staking?

thanks for the very informative plots and for pointing to the ETF ![:hugs:](http://forum.numer.ai/images/emoji/twitter/hugs.png?v=10) This is the very first practical hedging option that I see, although (A) you made a strong point on how it might not be worth it and (B) it is still USDC based.

*assuming 100% / 4 to correspond to the returns of the first 4+ months because of compounding + assuming half of the money is staked and half used in the hedge
