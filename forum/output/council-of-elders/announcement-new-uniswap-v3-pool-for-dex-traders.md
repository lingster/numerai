---
title: "[Announcement] New Uniswap v3 pool for DEX traders"
category: Council of Elders
url: https://forum.numer.ai/t/announcement-new-uniswap-v3-pool-for-dex-traders/5313
created_at: 2022-04-25T17:00:21.070000+00:00
last_posted_at: 2022-04-26T08:08:45.377000+00:00
posts_count: 3
views: 1141
tags: []
---

# [Announcement] New Uniswap v3 pool for DEX traders

---

### Post #1 — **aventurine** | 2022-04-25 17:00 UTC

In a dazzling feat of coordination, planning, and execution the CoE has created a new pool on Uniswap v3 for DEX traders.

Total Tokens Locked:  
3.41K NMR  
18.21 ETH

Support for DEX traders is very important for NMR price stability and liquidity.

Please see below link for pool information

<https://info.uniswap.org/#/pools/0x8df016708a66377dae191ca6f9fff4705a3d951f>

---

### Post #2 — **arbitrage** | 2022-04-25 17:02 UTC

This is a huge accomplishment and would NOT have been possible but for the support of the community and Numerai. Cheers everyone!

---

### Post #3 — **aventurine** | 2022-04-26 08:08 UTC

Great question and answer in RocketChat.

“I haven’t been following all the swaps. Is there any documentation to the risks of adding liquidity to Uniswap v3? Can you get liquidated as a liquidity provider? What is the reward you get for providing liquidity?”

Answer:  
No you cannot get liquidated on uni V3. In Uniswap v3, LP’s can concentrate their capital within custom price ranges, providing greater amounts of liquidity at desired prices. We set our price range fairly high. Whereas Uniswap v2 required all users to provide liquidity across the entire price curve from 0 to infinity, Uniswap v3 allows LP’s to optionally concentrate capital in the price range they believe will generate the highest return. There is an issue we identified on v3 at the 0.3% fee range so we opted for now to use the higher 1% fee best for more exotic pairs that are particularly subject to monotonic price movements(pair correlation issues with high volatility swings) We are currently researching a fix for the 0.3% fee and possibly move the liquidity over later(0.3% fee range is best for most pairs and can handle pretty large price swings as well) If the price goes outside of the LP position price range, then the position will be singularly concentrated in the less valuable asset. While the price remains outside of the price range, the position will be “inactive”. This means the position will not earn fees until if and when the price comes back in range. We currently plan to leave fees on the contract with most likely use of rolling more liquidly back in or for more CoE proposal uses(nothing set in stone)
