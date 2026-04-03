---
title: "NMR price hedging: 2026 edition"
category: Numeraire
url: https://forum.numer.ai/t/nmr-price-hedging-2026-edition/8213
created_at: 2025-12-27T17:00:11.760000+00:00
last_posted_at: 2026-01-13T16:09:57.183000+00:00
posts_count: 3
views: 473
tags: []
---

# NMR price hedging: 2026 edition

---

### Post #1 — **correlator** | 2025-12-27 17:00 UTC

**Purpose** :

Suggest a way for NMR stakers in the Numerai tournament to hedge the NMR price risk.

It answers the question: As a DS in the Numerai tournament, I want to be exposed to the alpha of my model submissions, not the beta of the NMR price movements. How do I trim the beta, but retain the alpha.

(This post is borderline related to the stable staking discussion, as the end goal of both the approaches is same i.e. reduce/remove NMR price exposure)

**Overview** :

  * The method suggested here involves taking a short position on NMR in an exchange of choice (where NMR perpetuals are listed).
  * The NMR short is balanced by an equal amount of a participants’ stake of NMR in the tournament.
  * Taking a long position (stake in tournament) and short position (perps) of equal amount of NMR makes this strategy effectively neutral to NMR price fluctuation



**Prerequistes** :

  * Some basic understanding of how Perpetual futures (also called perps) work will be beneficial.
  * Nevertheless, the details will try to be broken down in simple to understand language as much as possible.



**Overview of Perps** :

  * Although perps are generic and consistent market derivatives across exchanges, here the example of [* Lighter](<https://app.lighter.xyz/trade/NMR>) dex will be used. At the time of writing, Lighter is a reputed perp dex which lists NMR perps.
  * Users deposit a collateral asset (USDC) which is used to open long or short positions.
  * As a derivative product, perps provide exposure to price movements of the underlying asset (NMR in this case). Buying (going long) an asset which increases in price results in a positive PnL. Similarly, selling (going short) an asset which decreases in price also results in a positive PnL. This allows users to take a stance on price going up or the price going down.
  * The collateral asset (USDC) is a solvency measure of the exchange, using which the exchange can recover assets if the user’s position goes underwater.
  * A key term here is **Liquidations.** For a short position on NMR, if the price of NMR rises above a certain value (liquidation threshold), then the user’s short position will be closed by the exchange and it might result in complete loss of the collateral asset (usdc)
  * Liquidation is the key risk in this approach. Bulk of the analysis/calculations done subsequently cater to mitigating this risk.
  * Another, slightly less important from risk pov, aspect is the funding fees. This is the fees paid by one side of the position holders to the other (either longs pay shorts or shorts pay longs). The purpose of these fees is to maintain the trading price (NMR) on exchange closer to what it’s being traded at on other exchanges. The fees act as an incentive/disincentive mechanism for market participants to maintain the “actual” trading price (of NMR).



**Terminologies** :

  * Oracle price: “Actual” price of the asset (NMR) sourced from reputable external sources (like other exchanges where the asset is traded)
  * Funding fees: Positive implies longs pay (shorts); Negative means shorts (pay). They are calculated and applied on an hourly basis. If the funding fees are say +0.001% per hour, this implies that the short position will earn 0.001% for that hour.
  * Liquidation threshold: The price of the asset (NMR) which triggers a force closure of the short position. This usually results in complete loss of collateral supplied.



**Accounting for Liquidation risk:**

A rational user will try to mitigate the possibility of a liquidation event.

This means ensuring sufficient buffer of usdc collateral to cover for any NMR price spikes.

A typical short position on the Lighter dex looks as shown in image.

[![Screenshot 2025-12-27 at 9.08.01 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3359630885e523855eb37c219a63cdbd384f8599_2_690x104.png)Screenshot 2025-12-27 at 9.08.01 PM1578×240 28.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3359630885e523855eb37c219a63cdbd384f8599.png> "Screenshot 2025-12-27 at 9.08.01 PM")

[![Screenshot 2025-12-27 at 9.13.52 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/929841701e76c09f9c46f9a6e7a01177a4bb0684_2_690x101.png)Screenshot 2025-12-27 at 9.13.52 PM1384×204 20.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/929841701e76c09f9c46f9a6e7a01177a4bb0684.png> "Screenshot 2025-12-27 at 9.13.52 PM")

The calculation below depicts the amount of collateral, i.e. “Total balance”, needed to safeguard against this risk:

  * T: Total balance when short opened.
  * T_s: Total balance at a future time. (_s stands for under stress)
  * q: Amount of NMR sold (shorted)
  * P: Price at which position opened.
  * P_s: Price at a future time.
  * g: Price multiple i.e P_s / P. This is the factor by which the price increased from the time the position was opened.
  * alpha: self incorporated safety buffer. Typical value = 1.1
  * M: Margin fraction required. (Fraction of T). This is 0.2 for NMR perps on Lighter.



T_s = T + q*(P - P_s) ; (Decrease in future price increases future balance and vice versa)

Margin requirement (to avoid liquidation): 20% of Notional NMR short i.e.: 0.2 * q * P_s.

To avoid liquidation, the user has to ensure: T_s > alpha * Margin requirement

Solving the above equation for T (i.e usdc balance/collateral as of now)

`=> T > q * P [ (g - 1) + alpha * g * M)]`

Refer to the above as _Formula 1_

The value **g** depends on how much the price could increase in the future time period, and is a key element to model the value of T.

For calculating worst case liquidation risk, ‘g’ should be computed on a worst case basis from past NMR price data.

The calculation methodology of ‘g’ is described in **Appendix A**.

The value of ‘g’ from past data is _3.06_

`=> T > 2.73 *` _`(`_`q `_`*`_` P)`

“q * P” is the notional value of NMR short at time of opening the position.

**Final Takeaway for Total balance estimation:**

The collateral supplied has to be 2.73 times the value of NMR shorted.

Example:

  * Amount of NMR to short: 10 NMR
  * NMR Price: $8
  * Notional value of NMR short = 10 * 8 = $80
  * Safe T: 2.73 * 80 = $219
  * This value of T safeguards from liquidation risk as long as the future NMR price < 3.06 * current NMR price.



**Rebalancing**

  * Rebalancing or re-assessing is a key aspect to maintain a “safe" value of T.
  * The rebalancing frequency will also affect the value ‘g’; which takes into account the worst case price increase in that time frame.
  * Here, rebalancing frequency of 1 month has been considered.
  * An additional benefit of rebalancing is that it would allow the user to take out excess capital if during a time period, the NMR price decreases. This excess capital can be used to buy spot NMR and stake in the tournament.
  * At rebalance: 
    * Adjust the total balance according to _Formula 1_
    * This could mean either supplying more collateral (usdc) if the NMR price has risen in the previous period. It could also mean taking out excess capital (to maintain efficiency), if the price of NMR has fallen in the previous period.



**Funding fees of NMR**

  * Each perp position has an associated funding fees.
  * Funding fees are calculated and applied hourly.
  * Historical funding rates on Lighter can be fetched for a period going back 30 days.
  * For this exercise, funding rate of NMR for 30 days prior was fetched.
  * This gives a distribution of funding rates across each hour for the past 30 days.
  * The summary stats of the funding rate for NMR (in basis points per day) are: 
    * Mean: -12.7
    * Std: 16.6
    * APY: -37%
    * i.e. Shorts would have payed longs at the rate of 46% annualized
    * Note: This seems bad on surface, but can be improved.
    * Daily funding rate of NMR for the past 30 days is shown below. It has huge negative spikes, which implies shorters would have payed more during these times.
    * [![Screenshot 2025-12-27 at 10.10.24 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/182508fdb5dd1711bc04c2b0e1c608616e961f18_2_556x500.png)Screenshot 2025-12-27 at 10.10.24 PM1552×1394 184 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/182508fdb5dd1711bc04c2b0e1c608616e961f18.png> "Screenshot 2025-12-27 at 10.10.24 PM")




Contrast this with the funding rate for ETH:

  * Mean rate: 2.4
  * std: 0.6
  * i.e. 9% annualized where longs pay shorts (opposite that of NMR)
  * and much tighter spreads of rates (low std)



The funding rates are usually low for most coins with decent trading volumes. Another example is that of the UNI token with mean rate of 1.5 and std of 3.2.

Funding rates for NMR are all over the place due to low volumes and liquidity as seen here

[![Screenshot 2025-12-27 at 10.17.29 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a87580a31fcb0712a54ce27e60f078ecd5dac966_2_690x170.png)Screenshot 2025-12-27 at 10.17.29 PM1742×430 56.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a87580a31fcb0712a54ce27e60f078ecd5dac966.png> "Screenshot 2025-12-27 at 10.17.29 PM")

NMR is the asset with least volume on Lighter. This implies low participation by market makers etc which is not good for maintaining NMR price same as the ‘oracle price’. This ultimately leads to high and fluctuating funding rates.

The good news is that this is very much fixable. But will need Numerai’s help.

Numerai already has tie ups with reputed market makers. Numerai can point them to participate in market making activities on Lighter. This would significantly improve volumes. (fyi [@richai](</u/richai>) )

This will be good for low slippage as well as low funding rates.

**Miscellaneous** :

  * If more than one asset is being held/traded in the account, opening an isolated margin (instead of the default cross-margin) position for nmr short may be explored. Isolated margin position ensures that, in the case of adverse drawdown event, only that position is liquidated without bleeding into other assets in the account. This would be reflected in the ‘Liquidation price’.



**Appendix A**

Calculation of ‘g’.

  * Fetch ohlcv NMR 5 minute price data from binance for the past year
  * Maintain a window size of 30 days (rebalancing frequency) and step size of 7 days for overlapping calculation.
  * Compute worst case price jumps. From start of window to max of ‘high’ price within each window.
  * The worst case price percent increases are shown below
  * [![Screenshot 2025-12-27 at 10.26.06 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/774803118f7aa9da88d4bff4203f479c199dc639_2_690x185.png)Screenshot 2025-12-27 at 10.26.06 PM2400×644 61.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/774803118f7aa9da88d4bff4203f479c199dc639.png> "Screenshot 2025-12-27 at 10.26.06 PM")

  * The worst case increase is 206%.
  * Therefore the value of g = 1 + 2.06 = 3.06



* * *

Disclaimer: NFA. DYOR.

Disclosure: As of writing, I stake NMR. I do not hedge the stake.

---

### Post #2 — **correlator** | 2025-12-28 07:53 UTC

**Extension** :

Someone could manage this NMR short strategy as a “Public Pool” in Lighter. So, this could be run by a single operator and others can just deposit usdc into the Pool. Since “Public Pools” is a primitive in Lighter, there’s no additional trust factor apart from Lighter. The operator’s role is limited to managing the positions (NMR short) as a proportion of total capital in the pool. Depositors can withdraw funds at any time (after accounting for PnL).

This does require proper managament of the Pool including periodic rebalancing and active programmatic oversight and adjustment of the positions in the Pool to cater to deposits and withdrawals (which could occur at any time)

CoE could support this initiative. (fyi [@ia_ai](</u/ia_ai>))

---

### Post #3 — **correlator** | 2026-01-13 16:09 UTC

**Update** (15 days after the post)

The Funding rate has become much more favourable on Lighter.

The recent stats are as follows (bps per day for the last 30 days)

  * Mean: -2.0

  * Std: 6.3

  * APY: -7%




The downward spikes are still prevalent, albeit with lesser intensity.

[![Screenshot 2026-01-13 at 9.37.35 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/45e0375c50a3b43574bcfadc52d658d457aa7d98_2_549x499.jpeg)Screenshot 2026-01-13 at 9.37.35 PM1452×1322 130 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/45e0375c50a3b43574bcfadc52d658d457aa7d98.jpeg> "Screenshot 2026-01-13 at 9.37.35 PM")
