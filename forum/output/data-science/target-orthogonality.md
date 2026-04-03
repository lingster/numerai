---
title: "Target orthogonality"
category: Data Science
url: https://forum.numer.ai/t/target-orthogonality/6574
created_at: 2023-07-21T23:14:19.742000+00:00
last_posted_at: 2023-07-25T22:14:27.797000+00:00
posts_count: 7
views: 1168
tags: []
---

# Target orthogonality

---

### Post #1 — **steelyglint** | 2023-07-21 23:14 UTC

I find this mathematically quite beautiful and wanted to share it.

[![image2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/237d93a519dc0f61dbc3cf6d8adce339c81b78b1_2_515x500.jpeg)image21054×1022 133 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/237d93a519dc0f61dbc3cf6d8adce339c81b78b1.jpeg> "image2")

The plot shows the almost complete orthogonality of two large clusters of targets. The actual ‘target’ is in one of the clusters, I haven’t looked yet, but I’m guessing it’s in the larger of the two.

Why the decay at the North and South corners, and not the East and West corners? That’s quite informative.

Look carefully and you can see striping at 0.25, 0.5, and 0.75, both SW to NE, and NW to SE. Colour depth indicates an anomaly score, light=low.

Look at the target vectors; in each orthogonal direction there are two groups of dominant (longer), and less dominant (shorter) vectors.

I’m not going to say much about how this is derived, except to say that it’s a low rank, accurate representation of the full rank data.

I think there are lots of opportunities here for segmenting and ensembleing.

---

### Post #2 — **steelyglint** | 2023-07-23 23:07 UTC

Follow-up with same analysis for features. (Every 4th era, 412789 rows, 1586 cols)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ce89b25d3db1a39bd51f344dbd16b46ec430b8b5_2_581x500.jpeg)image1174×1010 141 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ce89b25d3db1a39bd51f344dbd16b46ec430b8b5.jpeg> "image")

Labelling only the dominant (longer) feature vectors, looks like some interesting grouping for feature selection. Again the colour depth is an anomaly score but it looks all very normally distributed (nice looking Tukey box-plots not shown.)

---

### Post #3 — **steelyglint** | 2023-07-23 23:59 UTC

A more detailed, side-by-side display showing the associated scree plots and box plots; features on the left, targets on the right.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/671831f30d7da7ac1fd11a133bd6c3969c6687b2_2_690x401.jpeg)image1920×1117 154 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/671831f30d7da7ac1fd11a133bd6c3969c6687b2.jpeg> "image")

---

### Post #4 — **steelyglint** | 2023-07-25 13:33 UTC _(reply to #3)_

You can see the relationships between the targets nicely in this more conventional correlation cluster map; they’re a bit obscured in the biplot.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4647d65d27dd910827066d754e286c34b4d2420a_2_512x500.jpeg)image1030×1005 190 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4647d65d27dd910827066d754e286c34b4d2420a.jpeg> "image")

Doing separate decompositions for the target variants shows the dominant targets (arthur, alan, janet) and their orthogonal relation to the rest.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3c4eedc45797328a47fedd260dd9c0dc80b9ff37_2_568x500.jpeg)image1124×988 136 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c4eedc45797328a47fedd260dd9c0dc80b9ff37.jpeg> "image")

---

### Post #5 — **wigglemuse** | 2023-07-25 20:56 UTC

It makes sense that he 20 day targets and the 60 day targets would be each clustered together, although I wouldn’t really expect them to be super orthogonal to each other since they are the same targets just farther out.

---

### Post #6 — **steelyglint** | 2023-07-25 21:44 UTC _(reply to #5)_

Yes, important to realise that the extreme orthogonality is in the low rank-2 approximation; but also that that is the overwhelmingly dominant sub-space. There is more beyond rank-2; we can either compute the relations in ever more inclusive dimensions (all the way up to exact full rank), or visualise the more subtle relations as they come out in subsets like in the last plot.

What we see in the biplot is an extraction of the most dominant relationships.

---

### Post #7 — **wigglemuse** | 2023-07-25 22:14 UTC _(reply to #6)_

Aha. Then the orthogonality makes sense also when looking at LR2.
