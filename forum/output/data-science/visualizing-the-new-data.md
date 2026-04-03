---
title: "Visualizing the New Data"
category: Data Science
url: https://forum.numer.ai/t/visualizing-the-new-data/4067
created_at: 2021-09-10T02:53:22.374000+00:00
last_posted_at: 2021-09-10T14:37:09.558000+00:00
posts_count: 4
views: 1039
tags: []
---

# Visualizing the New Data

---

### Post #1 — **gammarat** | 2021-09-10 02:53 UTC

So I’ve started looking at the new data, first by looking at the correlations between the features and the targets for the training set. There’s some interesting patterns showing up.

By way of process, what I did was take each era, Spearman correlate it with all the available targets. A small percentage of the targets, ~0.25%, had to be cooked (replaced with 0.5) as they were showing up as NaNs. There’s better ways, but that’ll do for now.

There’s 21 targets for each era, two of which (“target” and “target_nomi_20”)) are the same, so that gets double counted. Then, for each era, along each variable, the RMS value of the correlations is taken, and normalized to its median value across the 1050 variables, with values <1 set to one. It’s a bit of a hack, but quite useful for detecting patterns in data. The results are plotted on a log10 scale, from 0 to about 0.7.

The vertical coordinates are era (from top to bottom) and variable (left to right).

So here’s a jpeg of that:  


[![FullCorrsTrainData](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/abce38c411adbe19e405b8700dad1dbd8dc798e6_2_690x346.jpeg)FullCorrsTrainData1920×963 330 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/abce38c411adbe19e405b8700dad1dbd8dc798e6.jpeg> "FullCorrsTrainData")

Now I don’t know how clearly that plot will show up for the reader, but there’s some interesting artifacts. First off is the repeated patterns separated by about 210 bins horizontally. Those are clearest, at least for me, in the 5 thin vertical lines pretty much running continuously from top to bottom.

Here’s a blown up view:  


[![PartialCorrsTrainData](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/17301ba7a34f4575e2d8d91079bfef59cc4f8fad_2_690x346.jpeg)PartialCorrsTrainData1920×963 224 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/17301ba7a34f4575e2d8d91079bfef59cc4f8fad.jpeg> "PartialCorrsTrainData")

  
which brings into focus more the way the peak correlation moves a bit from bin to bin – particularly in the area slightly to the right of centre, and the way it spreads, forming blocks or pulses. Maybe it’s time to resurrect my trackers ![:male_detective:](https://emoji.discourse-cdn.com/twitter/male_detective.png?v=13)

What’s it mean? ![:thinking:](https://emoji.discourse-cdn.com/twitter/thinking.png?v=13)

Tomorrow maybe I’ll try the same for the Validation data.

---

### Post #2 — **jacob_stahl** | 2021-09-10 03:15 UTC

Maybe you could try k-means clustering on the columns. It would be interesting to see how these features group together.

---

### Post #3 — **rigrog** | 2021-09-10 03:25 UTC

“…repeated patterns separated by about 210 bins horizontally.”

See also: cell “Out[7]”, of analysis_and_tips.ipynb. It’s a colored plot of C[i, j] = (correlation of feature i, with feature j).

That plot looks for all the world, as if feature[i] = feature[i + 210] = feature[i + 420] = feature[i + 630] = feature[i + 840], for 0 <= i < 210\. It’s close enough, that I can’t tell any difference by eyeball.

---

### Post #4 — **gammarat** | 2021-09-10 14:37 UTC _(reply to #3)_

I agree [@rigrog](</u/rigrog>), the modulo 210 pattern repetition is really quite interesting. It does appear as well in the Validation correlation plot:  


[![ValCorrs](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bba30781b87d91830b56e39f6b90345fc70a4ba8_2_690x346.jpeg)ValCorrs1920×963 211 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bba30781b87d91830b56e39f6b90345fc70a4ba8.jpeg> "ValCorrs")

though maybe not as clearly as, having fewer files, the image is more smeared.

The images are also floored (to the median response in each era). For completeness, here’s plots of those for the Train data:  


[![NoiseFloorTrain](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/08abe708639b4dd0dcc1cd51bae03aced0009810.jpeg)NoiseFloorTrain560×420 20.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/08abe708639b4dd0dcc1cd51bae03aced0009810.jpeg> "NoiseFloorTrain")

and then the Val data:  


[![NoiseFloorVal](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6913701c360d55b7e503d218a7cb050ef8e4cac7.jpeg)NoiseFloorVal560×420 16.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6913701c360d55b7e503d218a7cb050ef8e4cac7.jpeg> "NoiseFloorVal")

Anyway, I think the next step for me is to look at the 210 bin cycle, and what one can derive from that.
