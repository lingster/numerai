---
title: "Which is the current dataset?"
category: Tournament
url: https://forum.numer.ai/t/which-is-the-current-dataset/5810
created_at: 2022-10-30T05:15:18.897000+00:00
last_posted_at: 2022-11-09T06:21:52.820000+00:00
posts_count: 23
views: 1970
tags: []
---

# Which is the current dataset?

---

### Post #1 — **liborty** | 2022-10-30 05:15 UTC

There seem to be at least four different versions of datasets now and new ones are being added without warning. I may have been using an old version to my cost.  
Anyway, I have only just updated to v3 and the diagnostics have improved.  
What about v4? Is there any notice anywhere that would say at all times which is currently the latest data to use and explain its properties?

Or can at least someone tell me here now? Should I have gone straight to v4?

---

### Post #2 — **taori** | 2022-10-30 10:00 UTC

Did you miss this old announcement? <http://forum.numer.ai/t/super-massive-data-release-deep-dive/>

---

### Post #3 — **taori** | 2022-10-30 10:05 UTC

And this might help too [Numerai](<https://numer.ai/data/v4>)

---

### Post #4 — **wigglemuse** | 2022-10-30 14:04 UTC

The above posted link to [Numerai](<https://numer.ai/data/>) has tabs for all the dataset versions.

Also see this post: [Removing Dangerous Features](<http://forum.numer.ai/t/removing-dangerous-features/5627>)

---

### Post #5 — **liborty** | 2022-10-31 06:09 UTC _(reply to #3)_

Thanks. I guess I should be using v4 then but I can not read .parquet files.  
Are there .int8.csv versions still available somewhere, as for the previous versions?

What I mean is I can not convert .parquet because most converters try to stupidly read the entire file all at once and I do not have enough memory for that.  
I need to be able to read this data line by line, removing the nonsensical ‘feature names’ and converting to plain .csv.

---

### Post #6 — **kayeffnumeraitor** | 2022-10-31 10:54 UTC _(reply to #5)_

I had the same memory issues, for that I wrote a script that reads the parquet file once and splits it up into single era csv files. With csv files you can explicitly force the column data types at readout to be `float16` , which I really wish would be available for parquet as well. However there is the `"v4/train_int8.parquet"` file, this file should be more manageable but I haven’t tried it

---

### Post #7 — **liborty** | 2022-10-31 11:04 UTC _(reply to #6)_

`"v4/train_int8.parquet"` \- yes, those are the files I am trying to use but they are still too big for the parquet readers.

---

### Post #8 — **liborty** | 2022-11-01 03:13 UTC _(reply to #2)_

I did not miss the original supermassive announcement and I did reprogram everything to work with it. That data is now called `v3`, I believe. I was downloading automatically _int8 files. I did miss any announcements that there may have been later about the labelling and v4. Since _int8 files were for some reason discontinued in v4, `numerapi` downloader just kept on getting v3. I was totally unaware that anything was amiss, apart from the fact that my model started performing badly and I lost money. Not an edifying experience.

As a result, my opinion of `numerai` is currently very low.

---

### Post #9 — **wigglemuse** | 2022-11-01 14:07 UTC _(reply to #8)_

int8 files were not discontinued, but csv files were for the newer data set.

In any case, none of the data updates have anything to do with your model performance going down – that’s just the market vs your model. Plenty of people are still running models based on both v3 & v2 data.

---

### Post #10 — **liborty** | 2022-11-02 00:29 UTC

But why were the `csv` files terminated? There is no good reason for it. See my more recent post entitled ‘Data Availability and Compression Methods’.

Changing data formats like this is not at all user friendly. Some of us have our own processing implementations which rely on the original format.

---

### Post #11 — **wigglemuse** | 2022-11-02 00:50 UTC _(reply to #10)_

Too big, I guess. What was _supposed_ to happen with the parquet files and/or api was the ability to pick and choose which eras (and even which columns) you wanted to download (and apparently parquet files are capable of that if you set it up properly). But that was never implemented. (Unless there is some magic there that actually does work that nobody knows about?)

The trouble is really only with the val set because it is a big file and changes every week. For submissions, we can download the live set only, and we only need to submit the live era now as well so that’s become much nicer and a lot faster.

The training file is huge but you only ever have to process once since it doesn’t change. I know there are those that download the training file every week, but frankly that is just a very poor way to do things so I’m going to put the blame on the user if they do that because doing that is silly – just save the data.

But with the validation set the feature data never changes but does get added to with new eras and targets as they become available. It is somewhat smaller than the training file (talking v4 here) but of course growing all the time. So that’s the one that has to be dealt with if you want those updates regularly, and they really should break it up or fix the api so we can just download the new stuff.

---

### Post #12 — **liborty** | 2022-11-02 02:09 UTC

That is all true, except that .csv is not “too big” but rather the opposite, when you apply some standard no-nonsense compression to it. I did an experiment on v3 data in the other thread, which proves that it is, in fact, less than half the size of your chosen format:

227501648 Nov 1 12:05 numerai_validation_data.parquet  
107301737 Nov 1 12:17 numerai_validation_data_int8.csv.lzma

PS. I understand that the training data does not change. However, that is the problem. Given that it was collected in some remote past, when the market conditions were very different, its validity is questionable at best. I think `numerai` is falling here into the trap of making the same comfortable assumptions as most ‘investment advisors’. They all subsist on the assumption that markets are always going up and up and are happy to cash in on it. Frankly, as long as that assumption holds, it takes zero skill anyway. When the markets inevitably turn sour, then it is: “sorry buddy, not my fault”.

---

### Post #13 — **dzheng1887** | 2022-11-02 03:32 UTC

Man, does anyone else feel the quality of the numerai operations have gone downhill the past few months? It just seems I have been noticing more bugs and weird things. I don’t know if I was just not paying attention before or something. Nothing major, but makes me feel a bit anxious on the stability of the system.

---

### Post #14 — **wigglemuse** | 2022-11-02 03:40 UTC _(reply to #12)_

So…then use the newest data instead? Or do Signals. Nobody is forcing anything on you.

btw, there is an int8 parquet val file which is currently about ~1GB

---

### Post #15 — **joakim** | 2022-11-02 08:02 UTC _(reply to #13)_

I’m quite worried too. Don’t think we’re quite at the ‘99.99% sure everything’s correct’ level yet that [@slyfox](</u/slyfox>) spoke about in the last FSC. Difficult to tell from the outside but there appears to be plenty of opportunity to strengthen controls around change and incident management.

---

### Post #16 — **lowvolmeanreversion** | 2022-11-05 01:08 UTC _(reply to #13)_

Yeah, I recently had a pretty large drop suspiciously around the same time that the daily uploading started. Definitely makes me feel a bit anxious about staking on dailies now, as now I’m uncertain whether the drop is related to a bug in the daily pipeline, but could be coincidence.

Roughly a 20% drop in 1 day on my model: [Numerai](<https://numer.ai/tap_ai>)

By far the largest drop since the inception of my model. I might have to lower my TC stake until I can feel more confident that things are working as intended.

---

### Post #17 — **kayeffnumeraitor** | 2022-11-05 10:00 UTC _(reply to #12)_

The non changing training data was actually one of the reasons I quit numerai some time ago. I came back once I saw that numerai now uploads an updated file containing the latest eras with targets. This means you can choose your own train/test split up until the newest eras. I guess the reason why the “vanilla” train/test split exists is to protect newcomers from being overconfident in their models.

Regarding your issues with parquet files: I am a little bit confused where your memory bottleneck is, is it your disk space or your RAM that is constraining you? To me it sounds like you are trying to train your model in a very disk and RAM constrained environment.  
Because parquet files are column oriented as opposed to row oriented csv files, what you can do is read only a few columns of a parquet file, read them at the specfic row, clear your RAM from the parquet file and read the next columns. Obviously this is very slow, but you can use this technique to at least split up the data into single eras which are more handy.

Another tip: you don’t have to read all columns, columns 210 - 1050 are almost identical copies of columns 0-209 (see [correlation matrix here in cell 12](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>)), so you can save memory by just reading columns 0-209 and columns 1050-1191, leaving you with 351 features that have almost the same information content.

---

### Post #18 — **liborty** | 2022-11-07 09:33 UTC

I am now totally confused. I am trying to change to v4 dataset but the tournament file is missing from it. However, the data description on the web says that it is the only one that changes weekly and must be used to generate the predictions. But the tournament files before v4 have different number of features and thus are incompatible with v4.  
I can generate live predictions based on v4 training and v4 live data files but where do I get the test predictions from?

---

### Post #19 — **wigglemuse** | 2022-11-07 13:33 UTC

You only need to submit the live era. (Now true no matter which dataset you use – just submit live, it is way faster.) In v4 the validation set grows each week – new eras with targets added as they become available. (You can use these for training as well, or even exclusively.) There are still a few “test” eras at the end of the validation file – these are the most recent eras that don’t have targets yet.

---

### Post #20 — **liborty** | 2022-11-08 01:11 UTC _(reply to #19)_

Thanks! I wish this kind of crucial information would be posted somewhere prominently instead of misleading outdated instructions.  
I notice that the v4 validation file is all clean now, with the new features.  
However, the v4 training set is useless and conflicting, as it still contains the old feature set.

---

### Post #21 — **kayeffnumeraitor** | 2022-11-08 07:30 UTC _(reply to #20)_

I think there might be still some misunderstanding. Both files `v4/train.parquet` and `v4/validation.parquet` have the same feature set, that is, they all cointain the same columns named with “feature_XXX…”. If not, then most probably something in your downloading/preprocessing pipeline is broken.  
Because they share the same featureset, the files `train.parquet` and `validation.parquet` can be concatenated together to form the entire Numerai dataset.  
This combined dataset represents a time series dataset containing at this time of writing 1035 eras, where each era is one week apart. Since ~1000 samples is a rather low count for time series data (no matter how much information there is per sample), every additional era has a very high value in the data set, so I wouldn’t call any of the data “useless”.

---

### Post #22 — **wigglemuse** | 2022-11-08 12:34 UTC

Yes, you should be seeing the same features for all v4 files, and yes the validation set is just a continuation of the training set with an arbitrary break point.

---

### Post #23 — **liborty** | 2022-11-09 06:21 UTC

Thank you for that reassurance, [@kayeffnumeraitor](</u/kayeffnumeraitor>) and [@wigglemuse](</u/wigglemuse>). It turns out I was indeed still picking up v3 of the train data by a mistake.
