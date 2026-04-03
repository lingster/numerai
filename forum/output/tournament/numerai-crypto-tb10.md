---
title: "Numerai Crypto TB10"
category: Tournament
url: https://forum.numer.ai/t/numerai-crypto-tb10/7828
created_at: 2024-11-01T15:37:23.894000+00:00
last_posted_at: 2024-11-01T15:37:24.011000+00:00
posts_count: 1
views: 450
tags: []
---

# Numerai Crypto TB10

---

### Post #1 — **jefferythewind** | 2024-11-01 15:37 UTC

The release of the Crypto Meta Model delivers a new opportunity to community members, and frankly, anyone in the world. Now we have the power to construct portfolios and allocate capital according to the MM predictions from the tournament.

I just put together this quick notebook to try to get a feel if the predictions were working or not. This is based on the intersection of the tradable universe from the Numerai Crypto Tournament (around 500 each round) and the Yahoo crytpo data available through the API.

This is just a crude first look, but the numbers appear to be inspiring. The process is to only include trades for which we have a full 20 day log return of data to use. The portfolio process simulates buying an equal weight in each of the top 10 and short selling and equal weight of each of the bottom 10 predictions from Numerai’s meta model. The weights are computed in such a way that the leverage of the strategy is 1.

Also we need a `crypto` tag in the forum.

[Here is the code.](<https://gist.github.com/jefferythewind/cfd1a7e750dbee3d14756a136ea92306>)

[![Screenshot 2024-11-01 at 11.23.25 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0c99a6b6b6c2a96156c283cc30a6f0a2759961f2_2_571x500.jpeg)Screenshot 2024-11-01 at 11.23.25 AM1166×1020 65.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c99a6b6b6c2a96156c283cc30a6f0a2759961f2.jpeg> "Screenshot 2024-11-01 at 11.23.25 AM")
