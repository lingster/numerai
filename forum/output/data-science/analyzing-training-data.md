---
title: "Analyzing Training Data"
category: Data Science
url: https://forum.numer.ai/t/analyzing-training-data/3143
created_at: 2021-05-01T05:56:03.677000+00:00
last_posted_at: 2021-05-02T03:52:06.935000+00:00
posts_count: 3
views: 1429
tags: []
---

# Analyzing Training Data

---

### Post #1 — **gammarat** | 2021-05-01 05:56 UTC

I’ve been playing around with the feature groups a bit, and two things popped out having to do with the standard deviations of the features. Referring to these plots:  


[![RawDataVariances](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c075c83bf685b69c53cb6bfc3f6967c9f66548ed_2_690x416.jpeg)RawDataVariances1083×653 50.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c075c83bf685b69c53cb6bfc3f6967c9f66548ed.jpeg> "RawDataVariances")

  
The numbers down the side of the first plot are feature numbers, down the side of the second plot they are simply levels. Sorry about the mess.  
Across the bottom are file numbers from 1 to 148. 1 to 120 are training data era, 121 to 148 are validation.  
In the first plot, I just took the standard deviation of each feature in each file, and plotted it, shaded according to relative level. Some aspects are rather striking, such as how the standard deviations are low (dark) in the Strength and Charisma feature groups, especially in the early training data files, and how they rise in the later eras.

These things have implications for me (as I largely work with pretty standard tools), perhaps they do for others as well. When I get a chance I’ll look at the Tournament data as well.

---

### Post #2 — **gammarat** | 2021-05-01 18:13 UTC

So here are some plots for the validation, test and live eras. Again, sorry for the mess in the first plot w/r to the labelling/ But going down the side of that are the features, labelled from 1 to 310, and across the bottom (of all 3) are file numbers.  


[![VTLDataSTD](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b843252f0399080cffff582adfd093168f6e9328_2_469x500.jpeg)VTLDataSTD869×925 57.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b843252f0399080cffff582adfd093168f6e9328.jpeg> "VTLDataSTD")

I added a second line plot so that the mean of the standard deviations from the Tournament data could be seen on the same scale as the previous Training data.

---

### Post #3 — **gammarat** | 2021-05-02 03:52 UTC

So trying to get some notion of what’s going on within these eras, I thought it might be useful to look at all the eras together.

This next covers all the eras in the Training and Tournament groups, with the same messy labels ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) (I really have to do something about that) The dashed vertical line in the second plot marks the end of the training and validation eras.

[![TVTLDataSTD](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2db53aea2fd939e1c25fba80b12a7f531cf3d29f_2_690x400.jpeg)TVTLDataSTD1152×668 53.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2db53aea2fd939e1c25fba80b12a7f531cf3d29f.jpeg> "TVTLDataSTD")

It’s interesting (to me at least) how the mean STD changes in behaviour…

To look a little more closely at that, I thought to bring out my (t)rusty [principal components](<https://builtin.com/data-science/step-step-explanation-principal-component-analysis>) (PCA) tools One of the handy things about PCA is that it concentrates variance in the first few columns of its output matrix (often referred to as _scores_), and packs the means into vectors I’m happy to forget about for now.

What I next did was PCA every feature group in each era, and then packed the results back into an array of Nx310 elements, where N is the the number of eras. This is the result:

[![TVTLGram](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/aa7e43fb50fdf5ea2906afa2c3c05580ca4c854f_2_452x500.jpeg)TVTLGram837×925 57.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/aa7e43fb50fdf5ea2906afa2c3c05580ca4c854f.jpeg> "TVTLGram")

On the left is the column means of the PCA scores (all on the order of 10-16; on the right are the standard deviations of each era for each each set of features. Note how the large values appear now in the first column (leftmost) of each feature group.

So with those I thought to see what those first columns look like when plotted out, and here’s the result:  


[![LeadingPCA](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e17153c37cf923be883cc79684e3032f51252a98_2_690x231.jpeg)LeadingPCA1251×420 48.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e17153c37cf923be883cc79684e3032f51252a98.jpeg> "LeadingPCA")

Whether those are enough to strongly associate separate eras in a Numerai useful way, I really don’t know; maybe they are, and maybe they aren’t. But in any case, I do find them interesting.

Next I took the leading columns of each of the feature group scores for the first 148 eras (ok, I cheat, and didn’t stick to just training data), and used them to build a Gaussian Mixture model. This one has 5 components, though I think four may be better for dependence on the Training models only, and one can use a lot more if we look for associations across the whole set of eras.

[![ForJane](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/1a465d3bae14f82b610aca09fc2260de99ddab09_2_690x158.jpeg)ForJane1830×420 47.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1a465d3bae14f82b610aca09fc2260de99ddab09.jpeg> "ForJane")

The plot is a bit hard to read. Given an era, the mixture model gives you posterior probabilities for that era relative to each of the mixture components, so that the sum of the probabilities for any given era across the five components is one. Now whether that can be used in analysing the likelihood of good scores remains to be seen, but I’ll leave that to next week. I’ve got to get my Tournament stuff done (but this is more fun.)
