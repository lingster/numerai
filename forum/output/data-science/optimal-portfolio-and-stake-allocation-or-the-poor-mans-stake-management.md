---
title: "Optimal Portfolio and Stake Allocation (or the poor man's stake management)"
category: Data Science
url: https://forum.numer.ai/t/optimal-portfolio-and-stake-allocation-or-the-poor-mans-stake-management/6520
created_at: 2023-07-02T21:35:35.791000+00:00
last_posted_at: 2023-07-09T18:06:08.115000+00:00
posts_count: 5
views: 1191
tags: []
---

# Optimal Portfolio and Stake Allocation (or the poor man's stake management)

---

### Post #1 — **degerhan** | 2023-07-02 21:35 UTC

I was generally happy with my model fleet. Some with consistent corr20, others with top decile TC. Then came the burn of Q2’23.

Seeing red round after round and getting to a 15% drawdown in a few weeks sharpens the mind. Hat tip to [@bor1](</u/bor1>) and eses-wk for their discord messages and code, I finally got the incentive to work on the “portfolio optimization thingy”.

I wanted a system to:

  * go long or short any model,
  * treat TC and corr separately,
  * not only calculate the optimal portfolio weights,
  * but also solve for its implementation within existing staking slots,
  * using nothing but stake types and model assignments (because no stake-management after all these years) [@slyfox](</u/slyfox>),
  * and do it in a self-contained notebook.



I found the final solver part helps make this a pseudo stake management tool, allowing an approximate implementation of your stake goals without moving NMR among your slots,

Let’s walk through [Optimal Portfolio and Stake Allocation](<https://gist.github.com/degerhan/92033750f0fb65fb698115f0a1a12a4c>) notebook with the degerhan fleet:

  * source models are defined in MODELS (my models plus those that can be purchased on numerbay or replicated from examples), plug in yours,

  * performance figures are downloaded via the API and four sub-models (model_tc, model_corr20V2, short_model_tc, short_model_corr20V2) are generated, quadrupling the list of instruments,

  * Hierarchical Risk Parity (Marcos López de Prado) is used to calculate the weights of the optimal portfolio. MLDP claims HRP performs better than mean-variance analysis in out-of-sample data,

  * given the recent bizarro markets, and using a lookback window of 100 rounds, no wonder today’s solution points towards shorting:

| weights  
---|---  
short_degerhan_r1_03_tc | 0.325226  
short_degerhan_r1_04b_tc | 0.150286  
short_degerhan_r1_04_tc | 0.148127  
short_degerhan_r4_04_tc | 0.107129  
short_degerhan_r1_03_corr20V2 | 0.104179  
paul_the_0ct0pus_corr20V2 | 0.101152  
short_degerhan_r1_06_tc | 0.0638998  
  
  * staking slots are defined in SLOTS, I have 9, plug in yours,

  * current stakes of the slots are retrieved via API, and multiplied with the desired LEVERAGE and optimal portfolio weights, yielding our target allocation:

short_degerhan_r1_03: (1333.5, 4163.1),  
short_degerhan_r1_04: (0.0, 1896.1),  
short_degerhan_r1_04b: (0.0, 1923.7),  
short_degerhan_r1_06: (0.0, 817.9),  
short_degerhan_r4_04: (0.0, 1371.3),  
paul_the_0ct0pus: (1294.8, 0.0)

  * To implement the above goal, the linear programming optimizer assigns a reference model and stake type for each staking slot:

(‘slot:(degerhan_s_01)’, ‘short_degerhan_r1_03’, ‘1x Corr’, ‘3x TC’)  
(‘slot:(degerhan_s_05)’, ‘short_degerhan_r1_03’, ‘0.5x Corr’, ‘1.5x TC’)  
(‘slot:(degerhan_s_03)’, ‘short_degerhan_r1_04’, ‘0x Corr’, ‘2.5x TC’)  
(‘slot:(degerhan_p_01)’, ‘short_degerhan_r1_04’, ‘0x Corr’, ‘3x TC’)  
(‘slot:(degerhan_s_02)’, ‘short_degerhan_r1_04b’, ‘0x Corr’, ‘2.5x TC’)  
(‘slot:(degerhan_s_07)’, ‘short_degerhan_r1_06’, ‘0x Corr’, ‘2x TC’)  
(‘slot:(degerhan_s_08)’, ‘short_degerhan_r4_04’, ‘0x Corr’, ‘3x TC’)  
(‘slot:(degerhan_s_04)’, ‘paul_the_0ct0pus’, ‘0.5x Corr’, ‘0x TC’)  
(‘slot:(degerhan_s_06)’, ‘paul_the_0ct0pus’, ‘1x Corr’, ‘0x TC’)

  * which results in the following actual allocations:

short_degerhan_r1_03: (1412.0, 4236.1)  
short_degerhan_r1_04: (0.0, 1917.9)  
short_degerhan_r1_04b: (0.0, 2010.6)  
short_degerhan_r1_06: (0.0, 849.8)  
short_degerhan_r4_04: (0.0, 1379.7)  
paul_the_0ct0pus: (1330.5, 0.0)

  * These are not exact, but close enough to our desired allocation, and without any manual excel jockeying. Where we started with a desired LEVERAGE of 2.0, today’s solution required actual leverage of 2.05.




I started using this allocation system with round 479, and portfolio returns have been more positive than not. Definitely much better results (thanks to the shorts) than if had kept staking my trusted models as before.

I imagine the portfolio optimizer will take many weeks to switch from shorting models to going long when the markets become rational again, so I will likely be burning when everyone else is partying – so even if you like what you see here, know that it comes with a different set of risks.

---

### Post #2 — **objectscience** | 2023-07-03 01:35 UTC

Amazing stuff as always.

---

### Post #3 — **dzheng1887** | 2023-07-07 17:45 UTC

. (nevermind, I see you wrote it in your post)

---

### Post #4 — **tb1** | 2023-07-09 10:52 UTC

Very interesting, so going down the rabbit hole somewhat… did some sensitivity analysis wrt to the risk measures. Used your data/code and got the following insample performance metrics (with full look ahead bias), so take it with a pinch of salt, but interesting results on a relative basis at least. Seems clear to stay away from volatility as a risk measure.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b38d6eef634ce050ab35c538a6f2b5d3f0016875.png)image445×758 24.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b38d6eef634ce050ab35c538a6f2b5d3f0016875.png> "image")

---

### Post #5 — **degerhan** | 2023-07-09 18:06 UTC _(reply to #4)_

Very nice. I intuitively feel more comfortable with drawdown and downside risk measures, great to see they outperform symmetric volatility measures (at least in the current sample). Thank you for sharing.
