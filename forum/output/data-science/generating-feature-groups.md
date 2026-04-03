---
title: "Generating Feature Groups"
category: Data Science
url: https://forum.numer.ai/t/generating-feature-groups/4744
created_at: 2022-01-08T04:43:19.424000+00:00
last_posted_at: 2022-09-16T03:38:47.336000+00:00
posts_count: 20
views: 3340
tags: []
---

# Generating Feature Groups

---

### Post #1 — **jacob_stahl** | 2022-01-08 04:43 UTC

I’ve been working on a method to group features together like the old dataset  
by making a correlation matrix with the training set, and clustering the columns together with k-means. This groups features together if they have similar behavior. I also tried doing this recursively by repeating the process with each new group to find sub groups.

The full experiment is in this [notebook](<https://jacob-stahl.github.io/numerai_feature_grouping/>)

Csv with feature groups [here](<https://github.com/Jacob-Stahl/numerai_feature_grouping/blob/main/feature_groups.csv>)

I haven’t made any models that use these groups yet, but I’m curious if any of you would find  
this useful.

---

### Post #2 — **slowmoe** | 2022-01-11 17:58 UTC

I like the idea and I’ve been playing with that too. I never tried clustering features using kmeans of the corr matrix though. Any motivation for kmeans of the corr matrix?  
I did try clustering with some homegrown methods though. When I add mean, std, etc per group as additional features, the resulting models always show improvements OOS. What I did to cluster features was something like:

  1. two features that correlate above some threshold are defined as neighbors
  2. features groups are neighborhoods



You could also try linear regression coefficients instead of corr values to define neighbors, seems to give interesting results as well.

---

### Post #3 — **jacob_stahl** | 2022-01-12 21:56 UTC _(reply to #2)_

When I first looked at the dataset’s correlation matrix I noticed a repeating diagonal pattern that suggested every ~200 features were similar in some way. I wanted find a way to rearrange the columns to make that pattern go away. Initially I looked at it as a kind of sorting problem and it evolved from there.

---

### Post #4 — **gammarat** | 2022-01-13 17:17 UTC _(reply to #3)_

It seems to be 210, and as that’s 1/5 of 1050, as a first guess I assume Numerai is collecting 210 features for each stock each day, and then gluing 5 days of those together to form a single row.

---

### Post #5 — **slowmoe** | 2022-01-15 10:03 UTC

Yes, 210 by my count too, the corr matrix seems to be very periodic. I like gammarat’s interpretation, at least that would make sense.

---

### Post #6 — **gammarat** | 2022-08-13 15:59 UTC _(reply to #5)_

Belated thanks! But I do believe I was wrong. Right now I’m leaning towards the idea that (in the original 1050) each set of 5 represents the posterior distribution of a 5 component Gaussian Mixture composed for each of their basic indicators. Or something along those lines, as once you factor an indicator into GMs, there’s multiple ways to play with the posterior distributions to generate new signals.

Of course I could be quite wrong, that’s happened many times before. ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12)

---

### Post #7 — **kenfus** | 2022-08-18 21:09 UTC _(reply to #6)_

I did group them together by correlation, but the result was meh. Since then, I went more the route of feature selection, neutralization and model stacking.

---

### Post #8 — **taori** | 2022-08-19 10:46 UTC

This is interesting, but I would rather use [Hierarchical clustering](<https://stackoverflow.com/questions/34940808/hierarchical-clustering-of-time-series-in-python-scipy-numpy-pandas>) over k-means as you don’t know how many groups you end up finding.

---

### Post #9 — **gammarat** | 2022-08-19 19:54 UTC _(reply to #7)_

I’m still using a fairly simple genetic algorithm, but even in that there’s a lot to play with and test. But the idea struck me (that the feature sets are based on posterior probabilities) because awhile back I started using that in Signals as it seems a relatively clean way to look at high and low performers, and it seems to do ok (well, sometimes ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12)).

---

### Post #10 — **jacob_stahl** | 2022-08-21 02:56 UTC _(reply to #6)_

I wonder if this means the dataset is really derived from 210 features, but averages them out over 5 different time windows. For example, maybe there is “volatility 10 day mean”, “volatility 30 day mean”, “volatility quarterly mean” and “volatility yearly mean”.

---

### Post #11 — **gammarat** | 2022-08-21 06:54 UTC _(reply to #10)_

Maybe, but I think that overall would be complicated to implement and keep consistent from week to week, while maintaining scale relationships between different tickers. One of the aspects that draws me to using Gaussian mixture type posteriors is that they will always be between 0 and 1, so it’s just a question of binning w/r to the tournament.

Of course a big drawback to my idea is that would require a slowly evolving mixture process; an idea I want to start playing with in Signals in the next few weeks.

---

### Post #12 — **gammarat** | 2022-08-22 21:42 UTC

I got curious about the relationships between the various targets, so I have been playing around a bit with those. FWIW, I only use the last 350 or so eras, and rather than using those complicated names I just use numbers 1 to 21.

I thought this plot might be of interest; it’s the correlation between the primary target and the whole set:  


[![TargetCorrelations](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b2f8919b895c1679fb3044048c87b39158dd00ee_2_690x238.jpeg)TargetCorrelations1217×420 91.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b2f8919b895c1679fb3044048c87b39158dd00ee.jpeg> "TargetCorrelations")

1 and 2 really aren’t visible (they’re just ones after all), but what was curious was the somewhat periodic nature of the correlation between the first target and 60 day targets, all in the lower group.

Interesting as well is the best correlation, aside from the 2 perfect ones, occurs for Target 20, which is shown in light blue. Target 20 is a 7 bin target.

---

### Post #13 — **gammarat** | 2022-08-25 02:29 UTC

I got a bit of time today to look at the last 141 features in v4. It’s interesting; it appears that they they are generated in a number of groups. As before, I’m just using the last 350 eras (excluding the final ones that still have nans).  
First the correlations among the raw data, not separated by era:  


[![Last141x350Corr](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d4195cb99ca1024becb66a098a42e0712e2371fa_2_441x375.jpeg)Last141x350Corr1059×898 80.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d4195cb99ca1024becb66a098a42e0712e2371fa.jpeg> "Last141x350Corr")

  
Next:  
The correlations between the correlations of the raw features with target 01:  


[![Last141x350CorrTarg01](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/682c8a4a545cf965abec793ed13a74f7ac1e5443_2_441x375.jpeg)Last141x350CorrTarg011059×898 96.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/682c8a4a545cf965abec793ed13a74f7ac1e5443.jpeg> "Last141x350CorrTarg01")

next, a plot of the cumulative sum of the correlations over the 350 eras, which shows interesting behaviour:  


[![Last141x350CorrTarg01sum](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/75a9c91011945df25036eda294b6566e2e73da5b_2_517x281.jpeg)Last141x350CorrTarg01sum771×420 49.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/75a9c91011945df25036eda294b6566e2e73da5b.jpeg> "Last141x350CorrTarg01sum")

  
particularly the 5 that appear at the top right of the plot

And finally a plot of the mean correlation of each of those features with the target.  


[![Last141x350CorrTarg01means](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ae490cc9656277c954e7d94182d0744ce18b78ff.jpeg)Last141x350CorrTarg01means560×420 13.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ae490cc9656277c954e7d94182d0744ce18b78ff.jpeg> "Last141x350CorrTarg01means")

There’s some interesting clustering going on!

**Added, 16 days later. Apparently Discourse won’t allow more than 3 consecutive posts in a row, so I’ve added what’s below as an edit.** I really am not trying to spam this board, I just found these results interesting and hopefully of some use to others. But I’ll desist if that’s preferable.

On the topic of clustering:  
I’ve taken a first pass at breaking the raw features into pretty simple clusters, resulting in about 235 of them. Right now it’s hit and miss and by hand, so I don’t expect much.

But I was also curious about the different targets as well. So for this ‘experiment’ (using the term loosely ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)) I ran the 235 clusters against all 10 of the 20 day targets (those with an __20_ in their names, or for those of us more numerically minded, the evenly numbered target columns from 2 to 20, with all targets being 1 to 21). I only use the most recently completed 350 or so eras.

Each cluster, fwiw, is used to generate a Gaussian mixture model from 100 eras from the appropriate target, and then run against the last 250 or so eras of the same target.

That generates interesting results, as shown in the next figure:  


[![TargetClusters](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aa71955acdbfe346cee0d44edb1e777258fec484.jpeg)TargetClusters560×420 19.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aa71955acdbfe346cee0d44edb1e777258fec484.jpeg> "TargetClusters")

Each separate color represents the mean correlation of the output from a different target. So the dark blue points are the results from 235 clusters built from 100 eras of Target #2 and then tested on 250 eras of the same target. The next (red) group are the same clusters but using 100 eras of Target#4, and so on.

I had expected them to be roughly the same, but surprise, surprise, they aren’t. Obviously Targets #12 (light blue) and #14 (maroon) respond rather well! But #6, #10, and #18 do not. ![:thinking:](https://emoji.discourse-cdn.com/twitter/thinking.png?v=13)

(Fixed an error in the last sentence, it originally read “…#6, #8, and #10…”. My apologies.)

---

### Post #14 — **bor1** | 2022-09-12 11:55 UTC _(reply to #13)_

Just for those that don’t think in columns - which targets are those light blue and maroon targets?

---

### Post #15 — **gammarat** | 2022-09-12 16:05 UTC _(reply to #14)_

The targets on the chart are, from left to right:

“target_nomi_v4_20” (dark blue)  
“target_jerome_v4_20” (red)  
“target_janet_v4_20” (yellow)  
“target_ben_v4_20” (purple)  
“target_alan_v4_20” (green)  
**“target_paul_v4_20” (light blue)  
“target_george_v4_20” (maroon)**  
“target_william_v4_20” (blue)  
“target_arthur_v4_20” (red)  
“target_thomas_v4_20” (yellow)

I bolded the two you asked about (Targets #12 and #14).

---

### Post #16 — **wigglemuse** | 2022-09-12 17:29 UTC

Targets 11-14 I’ve found to be the most strange and least useful for actually making models, unless I’ve got it backwards and they are somehow the most useful.

---

### Post #17 — **gammarat** | 2022-09-12 18:55 UTC _(reply to #16)_

I’ve not gotten to the point where I can decide yet (which is pretty much the story of my life ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)). But for me, the various 20 day targets seem to be variations of one another in that they correlate to each other reasonably well. Is Numerai simply sliding the break points between the various bins to generate different targets? IDK, that’s one of the things I hope to look at in the near future.

Here’s an example:  
For the 350 eras that I’m using, I took each possible value of Target #1 and looked at the distribution of of values in Target #12:

[![TargetDist\(1-12\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cea46b4fa854a475e246498c5dcacd8cf290eb80_2_360x500.jpeg)TargetDist(1-12)560×776 26.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cea46b4fa854a475e246498c5dcacd8cf290eb80.jpeg> "TargetDist\(1-12\)")

This is going to be slightly affected by the fact that if there are NaNs in Target #12, they get replaced by the corresponding value in Target #1. But there’s very few, so that seems to work for ballparking, for now. How those NaNs are distributed is something else to look at.

---

### Post #18 — **gammarat** | 2022-09-12 20:51 UTC

The next look is at the orderings among just the features themselves. Here, as usual, I’ve taken the last 350 eras that have completed 20 day targets.

For each era, I take the correlation among the features at each era, and then take the mean over the 350 for each correlation. This is a 1191x1191 array, that looks like this:  


[![DCorrsMean](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e58d9553bd55c248ebea6ad3668ea50b1d494ce7_2_636x500.jpeg)DCorrsMean777×610 74 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e58d9553bd55c248ebea6ad3668ea50b1d494ce7.jpeg> "DCorrsMean")

Note the 1050x1050 pattern that covers most of of the plot, the addition of the 141 extra features makes up the bottom and right boundaries.

Now if one takes the mean value down any column (or across any row, the distribution is diagonally symmetric), a pattern should emerge, which we can see in the top plot of the next figure. Note that in that same plot, features 1051 through 1191 are already forming clusters. So they won’t be touched.

but if we rearrange the first 1050 so that points separated by 210 features are gathered together, we get the second plot in the figure.  


[![FeatureCorrs350Eras](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4373c9916bec8cf58128d94516c4ec5b29461ee8_2_587x500.jpeg)FeatureCorrs350Eras1044×889 69 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4373c9916bec8cf58128d94516c4ec5b29461ee8.jpeg> "FeatureCorrs350Eras")

Most of the “blobs” in the lower image are comprised of 5 points, often arranged similarly.

---

### Post #19 — **jacob_stahl** | 2022-09-16 00:20 UTC _(reply to #18)_

Notice that each of those blobs have a similar shape. i wonder what those mean?

---

### Post #20 — **gammarat** | 2022-09-16 03:38 UTC _(reply to #19)_

My guess (and it’s only a guess) is that they use similar feature generating algorithm for each Perhaps a five component Gaussian Mixture Model (GMM), in which case the outputs (before normalizing) would be 5 posterior probability streams (very low, low, medium, high, very high, for example) for each original measurement (like, say, a twenty day profile of closing prices.) They’re pretty easy to create, but the utility of their outputs depend strongly on the predictive quality of the input technical indicators…

Please note: I am highly biased, as I used GMMs a lot in my job before retiring.
