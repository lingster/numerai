---
title: "Return Calculus"
category: Tournament
url: https://forum.numer.ai/t/return-calculus/5357
created_at: 2022-05-06T15:13:43.083000+00:00
last_posted_at: 2022-11-15T01:10:03.452000+00:00
posts_count: 4
views: 1058
tags: []
---

# Return Calculus

---

### Post #1 — **slowmoe** | 2022-05-06 15:13 UTC

So I’ve been trying to reproduce the 3M and 1Y return numbers that are given on numer.ai. Using numerapi in python. This is what I came up with:
    
    
    modelname = "slowmoe"
    rmp = napi.round_model_performances(modelname)
    df = pd.DataFrame(rmp).set_index("roundNumber").sort_index()
    df["payout_rel"] = df["payout"] / df["selectedStakeValue"]
    cumprod = (df["payout_rel"].fillna(0)+1).cumprod()
    gain_1Y = cumprod.iloc[-1] / cumprod.iloc[-52]
    
    print(f"1 Year Return on Stake: {100*(gain_1Y-1):.1f}%")
    

which as of today gives me:

> 1 Year Return on Stake: 114.3%

while the [website](<https://numer.ai/slowmoe#>) reports 109.5%. Pretty close, but something is missing. Any thoughts?

---

### Post #2 — **taori** | 2022-05-06 16:09 UTC

I might be wrong, but just give it a try with:
    
    
    # 52 weeks of compounding minus 3 for stake compounding lag
    gain_1Y = cumprod.iloc[-1] / cumprod.iloc[-49]
    

[Source](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L242>)

---

### Post #3 — **slowmoe** | 2022-05-07 09:19 UTC _(reply to #2)_

I tried that and all sorts of other values, 51,50,48,… no dice

---

### Post #4 — **pschork** | 2022-11-15 01:10 UTC _(reply to #3)_

See [Reproducing 1d, 3mo, 12mo returns the hard way](<http://forum.numer.ai/t/reproducing-1d-3mo-12mo-returns-the-hard-way/5850>)
