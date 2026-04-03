---
title: "Are the new data more noisy?"
category: Tournament
url: https://forum.numer.ai/t/are-the-new-data-more-noisy/4196
created_at: 2021-09-25T10:27:54.411000+00:00
last_posted_at: 2021-10-04T17:52:31.726000+00:00
posts_count: 6
views: 983
tags: []
---

# Are the new data more noisy?

---

### Post #1 — **eleven_sigma** | 2021-09-25 10:27 UTC

I’m finding new data more noisy as they require more regularization. I have not done feature selection so far, it is the next step, but the impression is that to get the value of new data a strong work of selection / regularization / neutralization will be necessary.  
At this point the question is, are the new data really NEW? That is, is there any data different in source or nature? or only is a change in the dimensionality reduction / offuscation.  
In other words, are we working now with 1050 principal components of the same data that we worked with 310? If so that could explain the presence of more noisy features.  
The patterns detected by [@rigrog](</u/rigrog>) in [About the new dataset and RAM usage - #3 by rigrog](<http://forum.numer.ai/t/about-the-new-dataset-and-ram-usage/4176/3>) could confirm this.  
What do you think?

---

### Post #2 — **maxchu** | 2021-09-26 05:49 UTC

Good question, i would also love to know the answer. I tend to think it is additional data rather than increasing dimensionality of dimensionality reduction/obfuscation as the improvement is quite significant. You can try to do pca to reduce the new features to 310 features and i think the result will still be better than the old model.

---

### Post #3 — **eleven_sigma** | 2021-09-29 08:13 UTC _(reply to #2)_

Yes this makes sense (new data) but why exactly 5 * 310 features and not 1100 or 1000 new features?

---

### Post #4 — **maxchu** | 2021-09-29 12:02 UTC _(reply to #3)_

The number 310 is already quite “ugly” to me, maybe it is related to the time series length, I am not sure. But I think 310 is the final dimension after the reduction of old data. So, the new data set after reduction is a multiple of 310 is not so surprising. After all, i think 310 is more magical here than the multiplier 5.

---

### Post #5 — **wigglemuse** | 2021-09-29 13:19 UTC

310 is the number of features in the old data. Key number in the new data seems to be 210 (x5).

---

### Post #6 — **gammarat** | 2021-10-04 17:52 UTC

I submitted my first full runs of the new data last week. As of this moment–which is really rather early to make any absolute decision–my twenty models built on the new data are all significantly outscoring my thirty models built on the old data. So I’m happy (for now) with the new data, it seems it’s possible to extract more signal from the noise than previously.

I’m also considering moving my Signals models to a similar architecture, especially as they aren’t doing all that well anyway.
