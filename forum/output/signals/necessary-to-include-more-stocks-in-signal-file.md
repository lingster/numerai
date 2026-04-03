---
title: "Necessary to include more stocks in signal file?"
category: Signals
url: https://forum.numer.ai/t/necessary-to-include-more-stocks-in-signal-file/3670
created_at: 2021-06-27T11:40:35.026000+00:00
last_posted_at: 2021-07-21T02:47:14.914000+00:00
posts_count: 17
views: 1101
tags: []
---

# Necessary to include more stocks in signal file?

---

### Post #1 — **autratec** | 2021-06-27 11:40 UTC

Hi all, currently, due to some setup and data source issues, I am only submit prediction of 10 random selected stocks. Just wondering, if I increase stock quantity to 50 or 100, using same prediction method, will the overall performance be improved ?

---

### Post #2 — **gammarat** | 2021-06-27 14:15 UTC

Probably but not necessarily.  
Stocks for which you do not submit a prediction are filled in at a median value. This pushes your predictions to the extreme ends, with half going to the high end, and half going to the low. What effect the neutralization has though on the results is undetermined from the user point of view.

If you work through the [sample program](<https://github.com/numerai/example-scripts/blob/master/SignalsScoringExample.ipynb>) it helps understand what happens to your submission.

---

### Post #3 — **mattiasl** | 2021-06-27 14:24 UTC

Because stocks that you don’t submit automatically get assigned a value of 0.5, submitting fewer stocks will mean that your overall spearman rank correlation will be closer to 0 on average than if you had a submission with many more stocks.

Furthermore, we are in the business of creating predictions which have only have a very small information edge (best average correlations with ground truth are between 1% and 2%) so by submitting more stocks the spearman rank correlation will be less volatile than if you submit fewer stocks.

---

### Post #4 — **gammarat** | 2021-06-27 15:02 UTC _(reply to #3)_

Except that Numerai doesn’t seem to use a full Spearman correlation in that tied ranks are effectively assigned values according to the order in which they appear in the filled in submission prior to applying the Pearson correlation. This makes any specific submission sensitive to the order in which the missing stocks are added, though the expected effect (over a large number of submissions) would still be zero.

Re. the information edge–that’s an interesting problem because the scoring is also dependent on the neutralization. The effect of neutralization can be seen by correlating your base results (your results prior to submission) to the market as versus your final score.

---

### Post #5 — **wigglemuse** | 2021-06-27 18:19 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> This makes any specific submission sensitive to the order in which the missing stocks are added

But in Signals, your predictions are then neutralized before scoring, and so all those 0.5s would end up with different values (and not all the same value). That’s assuming they do in fact do the final correlation the same way as in the main tournament but I don’t know if they do. (Is there open code for that?) And it turns out for the MMC calculation in the main tournament they don’t break those ties like they do with CORR score because the neutralization does it for them – they may use that method as well for Signals.

---

### Post #6 — **gammarat** | 2021-06-27 20:56 UTC _(reply to #5)_

But how order preserving is that neutralization? After all if you were to submit a prediction on all of the full set that was, in a sense of the ordering, absolutely perfect, you would expect a positive score.

It’s one of the things I hope to look into later in the summer (but right now the weather’s too nice ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) )

Mind you I’m not trying to _call out_ Numerai or anything like that. I just like to know before I put _skin in the game_ whether I’m dealing with a gentle massage or a meat grinder.

---

### Post #7 — **wigglemuse** | 2021-06-27 21:16 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> But how order preserving is that neutralization? After all if you were to submit a prediction on all of the full set that was, in a sense of the ordering, absolutely perfect, you would expect a positive score.

Possibly not at all. There are your predictions and then an unknown set of predictions you are being neutralized against – essentially a subtraction. So if the unknown set has little to no ties in it (which is what I would expect), then subtracting a constant (a bunch of 0.5s) against them would preserve the order of the unknown set, not of your 0.5s. So as long as the unknown set has little to no ties, then breaking your ties by row order is sort of pointless and counter-productive (for Numerai to be doing as pre-processing on your signal).

---

### Post #8 — **gammarat** | 2021-06-28 00:42 UTC _(reply to #7)_

This is one of the things I found really interesting when I first started looking into this. You’re right, of course, that even an excellent user prediction might not do well after the Numerai feature neutralization (that was a point I made in an earlier thread). But some numerical estimate of that effect has to be made if it’s to be of any use. Designing tests for that and then deploying such to probe Numerai’s structure is, for me at least, entertaining. ![:male_detective:](http://forum.numer.ai/images/emoji/twitter/male_detective.png?v=9)

---

### Post #9 — **mattiasl** | 2021-06-28 05:45 UTC _(reply to #8)_

I agree that having Numerai apply feature neutralization without our knowing exactly what this neutralization does is somewhat disconcerting. Yes, the smaller the number of submitted stocks, the larger the amount of stocks whose ranks are completely fixed by the neutralization process. Also it would be interesting to know how sensitive this neutralization is. For example, are all the 0.5 scores altered to be in a 0.52 to 0.48 range or are they altered to be in a 0.6 to 0.4 range? This is quite important in terms of how the targets are calibrated on the main model. Will my model work better if I submit only 25% of the Numerai universe if the targets are all in a 0.4 to 0.6 range or will it work better with a higher dispersion in the 0.8 to 0.2 range?

Hard questions which can only be resolved through trial and error optimization!

---

### Post #10 — **autratec** | 2021-06-28 06:52 UTC

those are interesting discussion. looks like i need to continue submitting my 10 stock prediction for a while, and see how it perform comparing with rest of traders.

---

### Post #11 — **wigglemuse** | 2021-06-28 12:49 UTC

I would assume that post-neutralization that just like on classic the only thing that matters for scoring is the resulting order, not what range the values end up at.

---

### Post #12 — **liz** | 2021-06-28 13:40 UTC

has anybody submitted all 0.5s?

---

### Post #13 — **mugamma** | 2021-06-28 20:55 UTC _(reply to #12)_

Wouldn’t all 0.5s result in zero exposure to the neutralized features? So still all 0.5 and zero correlation after neutralization?

---

### Post #14 — **gammarat** | 2021-06-29 00:39 UTC _(reply to #13)_

You’ll get a low correlation to the features, but the resultant data set will not be all 0.5’s.

You can see this by taking the feature set from a Tournament era, like _era121_validation_. Treat that like the [feature set mentioned in the docs](<https://github.com/numerai/example-scripts/blob/master/SignalsScoringExample.ipynb>), and create a “prediction” the same size as the targets, but all 0.5’s.

Then go step by step through the documentation example, repeating what is done there, but with your predictions and features.

After the Gaussianization step, your originally flat predictions should look like this:  


[![Gaussianized](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/34490492d2fee919cecc190a0a442c3f2306178b.jpeg)Gaussianized560×420 11.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/34490492d2fee919cecc190a0a442c3f2306178b.jpeg> "Gaussianized")

and after the neutralization, like this:  


[![Neutralized](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5aefae13e85157d3115596dd504e4bb993438e53.jpeg)Neutralized560×420 18.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5aefae13e85157d3115596dd504e4bb993438e53.jpeg> "Neutralized")

That result will be fairly independent of the actual features: if you plot out the Spearman correlation of that with the features, it will look like this:  


[![Correlation](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/29cc2a7398aefb4e0b5ad4c3a97674ccd5ad0e05.jpeg)Correlation560×420 26.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/29cc2a7398aefb4e0b5ad4c3a97674ccd5ad0e05.jpeg> "Correlation")

  
(note the y-axis max is less than 0.01).

and if you compute the Spearman correlation of the result with the original target data, it’s about -0.004. You can’t get a correlation off the original, all 0.5 data (no variance), but for the ranked version against the targets, it comes out to -0.0034.

Providing of course I have done this correctly, please feel free to correct me or try your own!

---

### Post #15 — **mugamma** | 2021-06-29 03:00 UTC _(reply to #14)_

I modified a copy of the notebook that you linked and made all the data 0.5, and it worked as I expected. I forgot about the Gaussianization step, but since the inputs there are a constant, only zeros come out. Additionally, I forgot the neutralization would remove the constant 0.5 making it all zeros, but the Gaussianization step already did that. Constant inputs is a degenerate case in a lot of ways. Random predictions between 0.4999 and 0.5001 would be as you described.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/efdb6b0f40f1b9fbdeac29ce39278548787f47df_2_690x159.png)image1666×386 15.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/efdb6b0f40f1b9fbdeac29ce39278548787f47df.png> "image")

After that, the correlation calculations get wonky from dividing by standard deviations of zero.

The final correlation was actually 0.6 in that toy example, but that’s just because the toy target happened to be somewhat close to sorted.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5423bc77e62188d38fe9bc2f0da6c43c32f7c37c_2_690x334.png)image1548×750 83 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5423bc77e62188d38fe9bc2f0da6c43c32f7c37c.png> "image")

I suppose the equivalent in live signals scoring would be the neutralized targets being somewhat close to lexicographical order or however the file is really sorted when the ranks are computed.

---

### Post #16 — **gammarat** | 2021-06-29 03:46 UTC _(reply to #15)_

Thanks, I see where one of my problems lies. Pandas defaults to average rankings in the case of ties, MatLab defaults to ‘first’. I’ll run this tomorrow again if I get the chance.

---

### Post #17 — **autratec** | 2021-07-21 02:47 UTC

just quick update using my live case in signal submissions. i started from 10 stocks to 72 stocks to 360 stocks. the performance of those submissions, using same ML model, being improved a lot. i will continue observe. But it is pretty sure, based on gut feeling that, less stock submission will leads to more noise (un-expected price movement in observation window) and more stocks submission will provide pretty good noise cancellation function and result could be more aligned with expected target.
