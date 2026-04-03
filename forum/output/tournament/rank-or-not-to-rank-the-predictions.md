---
title: "Rank or not to rank the predictions?"
category: Tournament
url: https://forum.numer.ai/t/rank-or-not-to-rank-the-predictions/5643
created_at: 2022-08-12T22:00:49.560000+00:00
last_posted_at: 2022-08-16T16:28:26.545000+00:00
posts_count: 4
views: 902
tags: []
---

# Rank or not to rank the predictions?

---

### Post #1 — **taori** | 2022-08-12 22:00 UTC

While the [example script](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/example_model.py#L143>) ranks the predictions and also states that it is a requirement , the [official numerai documentation](<https://docs.numer.ai/tournament/learn#modeling>) doesn’t rank the predictions but it doesn’t event document the format. So I now wonder what is the official submission format. Any idea?The ranking doesn’t affect the corr but I don’t know about TC.

---

### Post #2 — **restrading** | 2022-08-13 12:03 UTC

They rank your predictions after submission, so it does not matter if you do it or not.

---

### Post #3 — **jrb** | 2022-08-13 14:08 UTC

Ranking isn’t required. Also, if you do rank, do it on a per-era basis. The only requirement is that the predictions are in [0, 1). The [comment](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/example_model.py#L142-L143>) above the line you’d linked to, from the example script indirectly explains it. The intent of the line you cite in the example model, isn’t to rank, but to perform [MinMax scaling](<https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html>) in a one liner.

---

### Post #4 — **taori** | 2022-08-16 16:28 UTC

Thanks both [@restrading](</u/restrading>) and [@jrb](</u/jrb>). I hope [@restrading](</u/restrading>) is right though, otherwise the official documentation would be providing a wrong example.
