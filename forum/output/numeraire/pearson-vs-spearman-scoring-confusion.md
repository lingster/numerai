---
title: "Pearson vs. Spearman scoring confusion"
category: Numeraire
url: https://forum.numer.ai/t/pearson-vs-spearman-scoring-confusion/2559
created_at: 2021-03-27T18:23:50.048000+00:00
last_posted_at: 2021-03-28T15:50:38.204000+00:00
posts_count: 5
views: 3523
tags: []
---

# Pearson vs. Spearman scoring confusion

---

### Post #1 — **oiboy** | 2021-03-27 18:23 UTC

Hey all, newbie here.

I keep seeing posts which state that Numerai scores are based on the Spearman correlation coefficient. The [comment in the example](<https://github.com/numerai/example-scripts/blob/59d82639b11b67e51c4b8e7eee08ac38455dfc81/example_model.py#L20>) seems to agree with this. However, [the same example](<https://github.com/numerai/example-scripts/blob/59d82639b11b67e51c4b8e7eee08ac38455dfc81/example_model.py#L22-L23>) and [the documentation](<https://docs.numer.ai/tournament/learn#scoring>) state that the correlation for scoring is calculated using:
    
    
    ranked_preds = predictions.rank(pct=True, method="first")
    return np.corrcoef(ranked_preds, targets)[0, 1]
    

which returns the Pearson’s correlation coefficient, according to [numpy’s documentation](<https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html>).

Which is actually used by Numerai to evaluate correlation for scoring, Spearman’s or Pearson’s? Is ranking the predictions enough for `np.corrcoeff()` to return the Spearman correlation?

---

### Post #2 — **quantized** | 2021-03-28 11:34 UTC

The second line in the code above does indeed calculate Pearson. However, the line above, which ranks the predictions, means that Spearman is in fact calculated. You can think of this:  
**Spearman = Ranking + Pearson**

---

### Post #3 — **wigglemuse** | 2021-03-28 14:41 UTC _(reply to #2)_

Not quite – only the predictions are ranked (and ties broken), not the targets (ties remain). So it isn’t fully Spearman.

---

### Post #4 — **oiboy** | 2021-03-28 15:42 UTC _(reply to #3)_

So is this code accurate for how Numerai calculates corr for scoring? Or should I rank the targets as well?

scipy also offers [scipy.stats.spearmanr](<https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.spearmanr.html>), I’m wondering if that’s the easier option.

---

### Post #5 — **wigglemuse** | 2021-03-28 15:50 UTC _(reply to #4)_

It’s accurate, yes. The difference from actual spearman is slight, though.
