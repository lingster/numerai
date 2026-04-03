---
title: "Missing values in targets"
category: Tournament
url: https://forum.numer.ai/t/missing-values-in-targets/6245
created_at: 2023-03-28T08:57:53.657000+00:00
last_posted_at: 2023-03-28T16:22:08.413000+00:00
posts_count: 5
views: 589
tags: []
---

# Missing values in targets

---

### Post #1 — **d4rk5id3** | 2023-03-28 08:57 UTC

Hi all,

Just wanted to let you know that, at the moment, there are apparently missing values in nearly all targets, both in the training as well as in the validation data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3a776f4689663f6d9ae2aa44ef4e8792b059d764_2_311x500.png)image738×1184 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3a776f4689663f6d9ae2aa44ef4e8792b059d764.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f0ea3962607dda25f1d85fe047e950da060a31da_2_311x500.png)image738×1184 117 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f0ea3962607dda25f1d85fe047e950da060a31da.png> "image")

Furthermore, the symmetry is not any longer warranted for many of the targets.

So please be careful if you have a model that’s re-trained (semi-)automatically.

---

### Post #2 — **wigglemuse** | 2023-03-28 15:12 UTC

What do you mean exactly? There are always some missing targets (in the non-nomi targets). Nothing new there – unless targets that used to be there for some rows disappeared or there was just a massive amount of targets missing. I update weekly to get the new eras from the validation set that have had their targets added (I only am interested in eras with both 20d & 60d targets). As part of this process, I double-check that no previous era that I’ve already saved/processed has any changes. The data has always passed this check – no row has ever changed, no target (once added) has ever disappeared, and no missing target (once all the targets around it have been filled-in) has ever gotten filled-in later. But some targets are just missing, yeah. (But it was known and announced that some would be when they started generating multiple targets.)

And I just re-checked the training set – nothing has changed.

---

### Post #3 — **d4rk5id3** | 2023-03-28 15:39 UTC _(reply to #2)_

Hi wigglemuse,

For some targets I see 29K missing in the training set, which represents around 1%. And for the validation set it’s just shy of 79K, representing around 3.2%. This is not a massive amount, but also not negligible.

It’s the first time I notice it, but then you seem to have more sophisticated checks in place than me. I might have raised the alarm bells too quickly, in which case I apologize.

---

### Post #4 — **wigglemuse** | 2023-03-28 15:59 UTC

Yes, so that’s normal. For whatever reason they can’t generate some targets for some rows (probably companies going out of business, mergers, splits, whatever). It is possible (I’m just guessing) that some of the nomi targets actually _should_ be missing, but they fill them in anyway with 0.5s (maybe) just because we are scored on nomi and that’s supposed to be the “main” target. (for now)

And I’m sure you’ve also noticed that with the newest datasets and going forward, some features are also missing, but not with individual rows in an era (which should not happen I’m told), but whole columns for an era with features missing. And that could potentially happen even in new live data. If it ever does, I expect many people to not submit that day as it will screw up many models…

---

### Post #5 — **d4rk5id3** | 2023-03-28 16:22 UTC _(reply to #4)_

Thanks a lot for confirming. This is nice - no need for major concerns and I can go ahead as planned ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)
