---
title: "Super Massive Data Release: Deep Dive"
category: Data Science
url: https://forum.numer.ai/t/super-massive-data-release-deep-dive/4053
created_at: 2021-09-08T22:40:55.011000+00:00
last_posted_at: 2021-11-22T15:13:03.023000+00:00
posts_count: 82
views: 21799
tags: []
---

# Super Massive Data Release: Deep Dive

---

### Post #1 — **master_key** | 2021-09-08 22:40 UTC

## Highlights

  * We have just released the biggest upgrade to Numerai’s dataset ever.
  * The new dataset has 4x the number of rows, more than 3x the number of features, and 20 optional targets.
  * The fastest way to get started with the new dataset is to run through the [new example scripts](<https://github.com/numerai/example-scripts>)
  * You can continue to use the old dataset in the same way but models on the new dataset have much higher scores in historical tests.
  * The website’s “Download Data” button will only download new data. The legacy data can still be downloaded via the API (GraphQL or NumerAPI)
  * The website’s “Upload Predictions” button will only work for predictions made on the new data. Submissions using the legacy data can still be made via the API



## New Data

The new data has both more features and more eras. There are now 1050 features instead of 310, and a total of 679 training and validation eras with targets provided instead of 142.

The eras are now weekly instead of monthly. This means that eras match the tournament more precisely, however they are now “overlapping”. This means that nearby eras are correlated with one another because their targets are generated from stock market performance from a shared, or “overlapping”, period of time.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/14575921af2a961265f91da174b42b10e6140cf9_2_522x321.png)1054×650 9.55 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/14575921af2a961265f91da174b42b10e6140cf9.png>)

The new “training” period covers the same time period as eras #1-132 in the old data, but is now weekly rather than monthly.

The new “test” period is the same as the previous “test” period.

The new “validation” period covers the same time period as eras #197-212 in the old data plus an additional time period, and is now weekly rather than monthly.

The new “live” period functions just like the “live” period in the old data.

  * training_data 
    * One continuous period of historical data
    * Has targets provided
  * tournament_data 
    * Consists of “test” and “live”
    * All of these rows must be predicted for a submission to be valid
    * No targets provided
    * Test is used for internal testing, but is not part of the tournament scoring and payouts
    * Live is what users stake on and are scored on in the tournament
  * validation_data 
    * A separate file. Predictions on these rows are not required for submission
    * It can be submitted at any time to receive diagnostics on your predictions
    * Has targets provided
    * This is the most recent data that we provide, far removed from training data. This makes it particularly useful for seeing how your models’ performance declines over time, and how it would have been performing lately.



**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8560ca6e9bae62e50952c2f5e9a0be49e91e4d3c_2_178x428.png)568×1372 24.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8560ca6e9bae62e50952c2f5e9a0be49e91e4d3c.png>)

**

## New Targets

The final major change is that there are now many different targets in the dataset. The tournament target, which is the one you are scored on, is always called “target”. Currently “target” corresponds to “target_nomi_20”, but this may change in the future. However you will also find 20 more targets which are not scored on, but you may find useful for training. The 20 targets consist of 10 different types of targets constructed using 2 different time periods, 20 and 60 days. Additional targets may also be added in the future.

Be aware that some of the new targets have different binning distributions than what you see with Nomi, i.e. 7 bins rather than 5, with less rigid constraints on samples per bin. Training models to be good at multiple targets and/or ensembling models trained on different targets is a great way to improve generalization performance and increase the uniqueness of your model.

The new targets are regularized in different ways and exhibit a range of correlations with each other from around ~0.3 to ~0.9. Due to this regularization you may find that models trained on some of the new targets generalize to predict “target” better than models trained on “target”. Other targets may yield models that appear to generalize poorly to “target” but end up helping in an ensemble.

You may also find that training on the 60 day targets, e.g. “target_nomi_60” yields more stable models when scored on the 20 day “target”. But beware: the eras are even more overlapped when using 60 day targets! You need to sample every 4th era to get non-overlapping eras with the 20 day targets, but every 12th era to get non-overlapping eras with the 60 day targets. If you choose not to subsample in this way, you instead need to be very careful about purging overlapping eras from your cross-validation folds. With great power comes great responsibility!

Finally, be careful about just selecting a target that does well on Validation. Target selection is yet another way to overfit. When in doubt, cross-validate!

## API

The new data can be accessed either through the “Download Data” button in the leaderboard sidebar or through s3 links returned by the dataset API using the filename argument; a list of valid filenames can be retrieved through the new list_datasets API query. The new training_data and validation_data files will be the same every week, while the tournament_data file will be updated with the latest live era. Parquet and CSV versions of these files will be available at the start of the round each Saturday; you may retrieve data for past rounds using the round argument of the dataset and list_datasets APIs.

We’ve updated our create_submission API to accept predictions on the new live and test data. Set the optional parameter version to 2 to upload predictions on the new data. If unspecified, version will default to 1 for legacy submissions. Existing pipelines that upload submissions via the API won’t break.

Version 2 of the endpoint is now used by the website when you press “Upload Predictions”. This means that predictions made using the old data will not be accepted via the Numerai website, you will instead have to set version to 1 in create_submission to upload predictions on the old data.

The new version of the submission endpoint does not accept predictions on validation and does not generate diagnostics, instead these will be provided through a new set of diagnostics APIs. You can find a new section for these diagnostics under a model’s “More” dropdown in the [numer.ai/models](<http://numer.ai/models>) page. The APIs work much like submissions, call diagnostics_upload_auth to get a url to which you can upload your file, then call create_diagnostics to run diagnostics on your upload. You can use the diagnostics API either to list diagnostics for a given model or to retrieve diagnostics for a specific upload.

All of these new API features can be used via the [GraphQL API](<https://api-tournament.numer.ai/>), or through [NumerAPI](<https://github.com/uuazed/numerapi>).

## Performance

The most important thing about the new data is that it helps models predict the targets more accurately!

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/626b69c4bc59625ca68f198cd07e37735415f3fe_2_466x383.png)952×782 94.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/626b69c4bc59625ca68f198cd07e37735415f3fe.png>)

**

Here’s a comparison of two large XGBoost models, one built on the old data and one on the new data, and tested on the validation period.

The mean correlation increases from 0.0209 to 0.0234, the Sharpe increases from 0.576 to 0.692, and the worst drawdown drastically improves from -25.5% to only -14.6%.

One interesting thing is how a feature-neutral model looks. With so many more features to neutralize to, it actually hurts the mean score, but dramatically improves the consistency and Sharpe - the worst drawdown is only -0.7%!

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/091a4ebff37fbd77e9ab08e268321f76bcdfdbb0_2_468x386.png)914×754 87.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/091a4ebff37fbd77e9ab08e268321f76bcdfdbb0.png>)

**

Another option is to only neutralize to the features whose correlation to the target changes the most over the training set. The theory being “these are the features that we think might be the most risky, so let’s just neutralize to them, but keep our exposure to the rest of the features.” This gives an especially nice looking result.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c5b070b80e05839b9518e4c60d7144de55b82c43_2_463x383.jpeg)1618×1340 154 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c5b070b80e05839b9518e4c60d7144de55b82c43.jpeg>)

This simple modeling improvement shows the power of having so many more features. With this model, the mean goes all the way up to 0.0284, the Sharpe up to 1.142, and the worst drawdown only -4.93%.

Another characteristic of the new data is that there are many different targets which you can train with. The example below shows that when measuring correlation on target_nomi_20, an ensemble of 3 models each trained on a different target outperforms a model trained on only target_nomi_20.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d3c37942fa1d4ea3c82542cf5ab29317b2487468_2_492x404.png)1318×1084 107 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d3c37942fa1d4ea3c82542cf5ab29317b2487468.png>)

Details on the techniques above can be found in the [example scripts repo](<https://github.com/numerai/example-scripts/>), which has been updated with:

  * An analysis and tips notebook for the new data
  * Two new example model scripts: simple and advanced



Updates:  
There has been lots of concern about comparing old models to new models, as well as general difficulty with data size. There have been a few updates to address these:

  1. There’s a new file accessible via api called `old_data_new_val.parquet`  
using the utils in the new example scripts you can run `download_data(napi, 'old_data_new_val.parquet', 'old_data_new_val.parquet', round=280)`. This will give you the old data, but over the exact same period as the new validation. You will then be able to run your existing models and submit the predictions to diagnostics to get a 1 to 1 comparison against models built on the new data.
  2. I’ve placed new files called `numerai_{validation/training/tournament}_data_int8.parquet/csv`. These have features as integers 0 to 4, which result in DataFrames about 30% as large.
  3. I’ve also added `numerai_live_data.parquet` and `numerai_live_data_int8.parquet` which only contain the live era each week.



## The Future

There are a couple of other long-term considerations that we need users to begin preparing for.

More data may be added from time to time. These releases will always be announced, but it still has some effect on automation. We haven’t added new features often before now, but we want to be able to add new features regularly without it causing hiccups for users.

For example, simply getting all columns that start with “feature_” won’t work, as your model will receive unexpected columns (unless you are retraining). So your scripts should be explicit about which columns you want to use in order to ensure that they are always able to run even when new data is added. The new example script considers this already.

Features may be unavailable in some weeks. We don’t expect this to happen any time with this current data, but as we add more and more features, it is inevitable that some week, one of the features won’t be available at all in time for the round start. We don’t want to hold up the entire tournament for one feature, so we may put out that feature with NaNs. The new example script will implement the simple practice of filling missing data with 0.5, which you are encouraged to copy or improve upon.

---

### Post #2 — **rigrog** | 2021-09-08 23:41 UTC

Of those 1050 features: are there 310 of them, which are identical to the legacy features?

In other words, if I “continue to use the old dataset in the same way”, does that correspond to using some subset of the 1050 features, and also some subset of “4x the number of rows”?

I’d like to use the same 310 columns, but more rows, _especially_ validation rows. Please advise.

---

### Post #3 — **mdo** | 2021-09-09 00:00 UTC _(reply to #2)_

Sorry, but there is not a 1-to-1 mapping between the old features and new.

---

### Post #4 — **rigrog** | 2021-09-09 00:06 UTC _(reply to #3)_

If 310 old features are _not_ a subset of the 1050 features: then there are actually 1050 + 310 = 1360 features available, by downloading both datasets.

The legacy 310 wouldn’t be given for _all_ the rows, only 1/4 or 1/5 of them… but that would _have_ to include the live rows, or else the legacy modelers and new-data modelers couldn’t even be in the same tournament.

---

### Post #5 — **mdo** | 2021-09-09 00:31 UTC _(reply to #4)_

Nearly all the information of the old features is included in the new features plus a lot of new information. The old features were constructed in a way that wasn’t extensible and so a 1-to-1 mapping with the new system isn’t feasible.

---

### Post #6 — **mic** | 2021-09-09 02:06 UTC

Thanks for the release to you all at Numerai, huge effort and big ups for designing for future change!

Are there any plans to stop supplying the legacy style features? Rough timeframe?

Is the target unchanged? I read here it is nomi_20 today, was it nomi_20 last week?

---

### Post #7 — **gammarat** | 2021-09-09 04:31 UTC _(reply to #6)_

[@mic](</u/mic>), I was asking so what similar questions over on RC, so a kind person posted this link: <https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>

The same file comes with the release, but if (like me) you don’t use Jupyter Notebook (whatever that is) it’s rather unreadable. The GitHub link otoh is relatively well presented.

FWIW, the target to submit on for the competition is still labelled target, and it looks much the same. There just also a bunch of other targets to play with.

FWIW, I’ve just been playing with the training data a bit. Taking the latest era, about 35% of the data is linearly dependent on the rest; when I took the last four eras together, about 70% is linearly dependent. There’s some interesting exploring to do there.

---

### Post #8 — **aininja** | 2021-09-09 12:10 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> The website’s “Upload Predictions” button will only work for predictions made on the new data. Submissions using the legacy data can still be made via the API

Don’t understand this point. I thought that legacy data and new data predict the same time interval so there should be not difference in the file format or id numbers. What are differences in submission file between legacy and new data?

---

### Post #9 — **andy_shaps** | 2021-09-09 15:12 UTC _(reply to #8)_

the tournament file will be different between legacy/new and given that you need to submit a complete prediction list for the whole tournament, they must be separate. Don’t forget, the legacy tournament dataset included; test, val and live and had a mix of monthly/weekly eras. new tournament dataset only has test and live and is all in weekly, thus the difference in formats. Hopefully that helps

---

### Post #10 — **johnnywhippet** | 2021-09-09 16:38 UTC _(reply to #9)_

I’m out. too much for my humble laptop. Any takers on a 3rd-hand laptop?

---

### Post #11 — **richai** | 2021-09-10 00:12 UTC _(reply to #10)_

To train faster, you can drop 3/4ths of the rows (to turn the training data back into monthly instead of weekly).

Many good models can be built by downsampling like this.

---

### Post #12 — **rigrog** | 2021-09-10 00:34 UTC _(reply to #11)_

Do you mean, go drop-drop-drop-keep, by eras? Or is it by rows?  
And only train, or train and val?

Maybe a better idea: drop 4/5 of the _columns_ (i.e. features). Looking at the plot in “Out[7]” of analysis_and_tips.ipynb, it looks like columns 0-209 are just repeated five times consecutively.

---

### Post #13 — **autratec** | 2021-09-10 07:37 UTC

i like current numerai tournament. 2.5G data set is just nice for my current machine learning environment. Moving from 2.5G to 10G is over my current limit. I might put this journey on hold and more focus on signal which the data collect is still under my control.

---

### Post #14 — **kamikaza26** | 2021-09-10 07:46 UTC

I see big down side to this… since you need a lot more compute power… so you are basicly making it harder and harder to enter tournament.

if you scale data again you are making it impossible to compete with no major investment into equipment… at least 2000$ machine (computer) … and then you also need to invest in NMR to try to get that investment back…

I thought you want as much diversity as possible, but its starts to look more and more big guys taking all … hope you are also thinking in about problem like this.

On other hand its exciting to get more data to analise and dive deeper …

---

### Post #15 — **mic** | 2021-09-10 07:55 UTC _(reply to #14)_

You can always use just some of the data.

---

### Post #16 — **mdo** | 2021-09-10 08:01 UTC _(reply to #12)_

He means dropping 3/4ths of the eras (which will drop 3/4ths of the rows), e.g. training on eras 1,5,9…  
You could make four such models with different starting points (e.g. using eras 2,6,10…, etc) and ensemble them. Heck you could combine that with your idea of using the each of the blocks of 210 features and make 20 models to ensemble. Each individual training would use less memory than the previous dataset and I’d bet such a thing would perform very well. There are lots of memory efficient ways to use all the data. I really don’t think anyone needs to upgrade their hardware unless they really need an excuse to ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #17 — **mic** | 2021-09-10 08:04 UTC

In the tournament data file, will the live eras be the only thing that changes week to week?

---

### Post #18 — **mdo** | 2021-09-10 08:07 UTC _(reply to #17)_

Yes, and as per the recent announcement in RocketChat you can now download only the live if you so choose, so you can easily generate live predictions to append to previously generated test predictions for upload.

---

### Post #19 — **sunkay** | 2021-09-10 08:14 UTC

[![屏幕快照 2021-09-10 下午3.57.46](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b6526d5a56820a3eec5ccc9b7533a66eec718982_2_690x414.jpeg)屏幕快照 2021-09-10 下午3.57.461306×784 145 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b6526d5a56820a3eec5ccc9b7533a66eec718982.jpeg> "屏幕快照 2021-09-10 下午3.57.46")

  
I droped 3/4 of rows and start training on my new machine ![:grinning:](https://emoji.discourse-cdn.com/twitter/grinning.png?v=13)

---

### Post #20 — **autratec** | 2021-09-10 08:16 UTC _(reply to #11)_

in order to get more people continue participating in the numer.ai tournament, may i request organizer to continue providing old data set as they did before ? BTW, providing a separate live data set for submission is a good idea and should continue.

---

### Post #21 — **mdo** | 2021-09-10 08:27 UTC _(reply to #20)_

If you were using Numerapi to download the dataset previously, it will continue to download the old dataset. With Numerapi you need to actively switch to using the new data. This was done to not break people’s compute pipelines.

---

### Post #22 — **autratec** | 2021-09-10 08:54 UTC _(reply to #21)_

thanks for the clarification. it might solve my problem in the short term as i am using colab to download and submit some predictions. But my another route will be impacted as i also download the data, unzip them and upload to Azure Machine Learning (studio) for prediction. The whole space Azure offer on cloud is 10G ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=9)

---

### Post #23 — **bvmcheckking** | 2021-09-10 09:22 UTC

Looking at the number of eras, do I understand correctly that the old train and validation1 (eras 121-132) become the current train period (but now with weekly data instead of monthly) and the the old validation 2 became the current validation (but again upsampled) and another year of data is added to the dataset.

Also can we know to what dates the eras match to?

---

### Post #24 — **foolish_observer** | 2021-09-10 11:45 UTC

I have some problems running the new scripts. I might be missing something but I cannot find the download_dataset method for numerapi. There is a download_current_dataset and a download_latest_data but both are missing the round argument. What is the difference between those two? Many thanks in advance

---

### Post #25 — **mic** | 2021-09-10 12:09 UTC _(reply to #24)_

[@foolish_observer](</u/foolish_observer>) It was added recently. Maybe you need to upgrade to the latest version. It looks like the functions you named will be deprecated in the future.

---

### Post #26 — **gigikone** | 2021-09-10 13:51 UTC _(reply to #16)_

I’m still pretty new to coding, but I would like to try the dividing the features into blocks of 210. How could you do that? Is there a specific pandas function that can be used?

---

### Post #27 — **yxbot** | 2021-09-10 14:08 UTC _(reply to #26)_

check out this cheatsheet:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eaca02cdf82a3d73af573f1e3648595263a78367.png) [blog.finxter.com](<https://blog.finxter.com/pandas-cheat-sheets/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eea25643a56248ab8decc325294451d295fcc590.png)

### [[PDF Collection] 7 Beautiful Pandas Cheat Sheets — Post Them to Your Wall –...](<https://blog.finxter.com/pandas-cheat-sheets/>)

---

### Post #28 — **amiga43ver** | 2021-09-10 14:41 UTC

Would it be possible to provide training data in CSV format? I’m stuck with 16 gigs of RAM for now and it is simply impossible to work with so large parquet file. I would like to play with new data and as CSV I could split the training dataset into multiple chunks to fit it into memory…

Or I’m just dumb and there is some simple way to split/partition file even if it is in parquet format?

---

### Post #29 — **rigrog** | 2021-09-10 16:26 UTC _(reply to #28)_

If the parquet file is too big, then the CSV will be way, way too big. [edit] Oops, I forgot that those formats are only _on disk_ , not in RAM. They’ll be the same in RAM (in numpy/pandas).

Soon you’ll be able download an int8 version of the training data (features are 0, 1, 2, 3, & 4). Pandas + 16 Gb can read that parquet file. For further work, you could compress it by:  
for i in range(210): (cooked feature)[i:] = sum( (raw feature)[i : : 210] )

---

### Post #30 — **chaotician** | 2021-09-10 17:15 UTC

I have Colab Pro with 35.25G RAM and both example codes crashes due to lack of RAM! How much RAM is needed to run the example codes? Or do you have any tips / tools to lessen RAM consumption?

---

### Post #31 — **mdo** | 2021-09-10 17:20 UTC _(reply to #30)_

from RocketChat [#announcements](</c/announcements/8>)  
Ok I have heard your primary feedback:

  1. How do we compare our old model performance to our new model performance?
  2. Data too big



Addressing both of these:

  1. There’s a new file accessible via api called `old_data_new_val.parquet`  
using the utils in the new example scripts you can run `download_data(napi, 'old_data_new_val.parquet', 'old_data_new_val.parquet', round=280)`. This will give you the old data, but over the exact same period as the new validation. You will then be able to run your existing models and submit the predictions to diagnostics to get a 1 to 1 comparison against models built on the new data.

  2. I’ve placed new files called `numerai_validation_data_int8.parquet`, `numerai_training_data_int8.csv`, etc. These have features as integers 0 to 4, which result in DataFrames about 30% as large.  
I’ve also added `numerai_live_data.parquet` and `numerai_live_data_int8.parquet` which only contain the live era each week.




The int8 files will be available for each round so you can make your pipelines expect those if you’re having RAM issues.

Cheers

---

### Post #32 — **mdo** | 2021-09-10 17:27 UTC _(reply to #22)_

You can use the old api call like you have in colab on your local machine to download the old zip locally and then you should be set for your Azure upload path. You can also try the int8 version of the new data as it is quite small

---

### Post #33 — **habakan** | 2021-09-11 05:43 UTC

Thank you for releasing new dataset.  
Using int8 dataset, I think some of the memory issues will be resolved, but I’ve published a Kaggle Notebook that train sample 1/4 of the era discussed in this topic, and I’ll share it.  
[https://www.kaggle.com/kansukehabano/numerai-training-new-data-for-low-ram ](<https://www.kaggle.com/kansukehabano/numerai-training-new-data-for-low-ram>)  
Using DuckDB, I was able to read and train only specific eras even with a float dataset.  
But now, thanks to the int8 dataset, we can map all training data into memory and still train without DuckDB.

---

### Post #34 — **sunkay** | 2021-09-11 08:52 UTC

anyone run example_model_advanced.py without error?

---

### Post #35 — **eleven_sigma** | 2021-09-11 10:03 UTC _(reply to #34)_

Someone more think that this change should be produced releasing the new data format and giving two-three weeks for adjusting and test models before use in production?  
I don’t understand why after several months using old data you need to go live with the new in three days…  
Still you have 8 hours to reconsider this and delay a bit the new data challenge.  
Release old data for this and next weeks and give time to test and adjust our work,  
Giving only a few days you are understimating the effort people are doing. Some people only can work on this in weekends. I haven’t time to check the new data and for sure more people are in same situation.

---

### Post #36 — **mic** | 2021-09-11 12:14 UTC _(reply to #35)_

[@eleven_sigma](</u/eleven_sigma>) the team at Numerai have said the legacy format data will be continuing, it is not stopping right now, so you can continue with it and move over to the new data format when convenient for you.

---

### Post #37 — **eleven_sigma** | 2021-09-11 12:20 UTC _(reply to #36)_

Yes but you need to use the API. I haven’t time this weekend to adjust it. I think announcing it a Thursday to begin in the same week is absolutely unfair.

---

### Post #38 — **autratec** | 2021-09-11 12:29 UTC

I feel numerai is under estimate the imapct to those part time “data scientist”, using their own computer resource and time and try to meet the weekly commitment.

If old API is still working, why we just continue providing old dataset as download files ?get two processes running parallelly can minimise the change impact.

---

### Post #39 — **halsmith99** | 2021-09-11 12:32 UTC _(reply to #37)_

thought there was some talk in rocketchat about adding a button for submitting old data

---

### Post #40 — **autratec** | 2021-09-11 12:48 UTC _(reply to #39)_

Yes. I just checked the chat room and looks like legacy data download and submission will still be provided. I suggest the COE should conduct a post mortem review of this event. It is a good intention to provide better quality data from scientist perspective. But the whole change impact was under estimated. The response from technical team is fast. Hope we can manage it better next time.

---

### Post #41 — **master_key** | 2021-09-11 14:35 UTC _(reply to #37)_

We added an old data download/upload version back to the website

---

### Post #42 — **master_key** | 2021-09-11 14:40 UTC _(reply to #34)_

Sorry about that. I’ve made some updates to it since the original drop, if you pull the latest changes it should work. You can reach out to me in RocketChat if you keep having issues

---

### Post #43 — **gammarat** | 2021-09-11 15:29 UTC _(reply to #37)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> Yes but you need to use the API.

No you don’t. If you look under the “Download Data” and “Upload Predictions” buttons, you’ll see a link the says “legacy data”. Click on that and you’ll get the buttons for the old data downloads and uploads. (Thanks [@master_key](</u/master_key>)!)

---

### Post #44 — **muppetshow** | 2021-09-11 18:37 UTC

Been just about coping with old format with 32GB ram, but seems I need an upgrade. Is feeding this in chunks to a GPU (12gb?) practical?

---

### Post #45 — **bob_watson** | 2021-09-11 18:45 UTC

I’m trying to submit and getting “PermissionError Forbidden”  
Same trying diagnostics on a validation set which worked yesterday!

Just started working! OK now!

---

### Post #46 — **objectscience** | 2021-09-11 20:00 UTC _(reply to #34)_

I ran a partial stress test on it yesterday. Set downsampling to 1 and n_estimators to 40k. I let it get into the second split of the CV before killing it. No issues up to that point. Where did it fail?

---

### Post #47 — **donk** | 2021-09-12 05:55 UTC

Deep dives come with risk of drowning…  
Hopefully all will manage to surface with good results!

---

### Post #48 — **jefferythewind** | 2021-09-12 10:16 UTC

Hi, Can anyone tell me how to download the new data with `numerapi`? I can confirm that my legacy code continues working by downloading the legacy data, but what changes do I need to make the numerapi code to get the new data in my pipeline. I didn’t see it mentioned anywhere yet or on the numerapi docs. Thanks!

EDIT: I see how this is explained in the github repo, for anyone else looking.

---

### Post #49 — **fwaris** | 2021-09-12 17:39 UTC

Parquet format suggestions / issues;

a) There should be multiple small partitions instead of a single huge partition. Presently you have to load the entire set into memory to do something with it. Smaller partitions will allow streaming data processing - useful for many scenarios such as simple transforms or serving data in chunks.

b) The the ‘thrift’ schema in the parquet files shows “target…” columns to be nullable single (32bit float values) but in actuality the data is nullable double values for those columns. This issue probably does not show up in Python (which is not statically typed) but does cause problems in other languages/platforms. Ideally the data should conform to the schema.

---

### Post #50 — **gammarat** | 2021-09-12 18:38 UTC _(reply to #49)_

Or you could write a simple routine to break the parquet data up into whatever format is most convenient for your routines and save the output locally? That’s what I do, and I break it into separate, directly loadable files listed by era, with the Id column kept in a separate file for each data_type. When it comes to processing, I then can load only the era data I’m looking for, and if it’s already in the appropriate binary format, one doesn’t have to slow down for translation.

Getting it broken down quickly is a function of efficient memory and reducing file calls. So right now I take in ~50 feature columns to assemble 200 eras at a time, and save those separately. On my home box that takes about 30 minutes for the full data set. I can probably reduce that more (it would have been multi-hours doing one feature column to assemble on era at a time, for example), but this does for now.

I find the Parquet files mush easier to work with than CSV.

---

### Post #51 — **taori** | 2021-09-13 19:36 UTC

> The new targets are regularized in different ways and exhibit a range of correlations with each other from around ~0.3 to ~0.9. Due to this regularization you may find that models trained on some of the new targets generalize to predict “target” better than models trained on “target”. Other targets may yield models that appear to generalize poorly to “target” but end up helping in an ensemble.

Can someone explain the rationale behind this approach? Why using a “wrong” target for training would help the real target? Is this technique specific to finance data (more noise than signal) or is this a general idea in ML?

---

### Post #52 — **restrading** | 2021-09-14 01:47 UTC _(reply to #51)_

I think this is more related to the concept of generalization in ML where uncorrelated ensemble (in this case as a result of training on different targets) reduces variance in out of sample data at a slight cost of bias.

---

### Post #53 — **lothlorien** | 2021-09-14 07:44 UTC

So how do I download the supermassive dataset via GraphiQL? It seems I should pass the round number for the NEW dataset, like this?

{dataset(tournament:8,round:281)}

but the resulting data is the old set.

---

### Post #54 — **lothlorien** | 2021-09-15 09:46 UTC _(reply to #53)_

I figured it out:  
query { listDatasets }  
will give you a list of file names available.  
To get the download link for the legacy data, you do NOT specify a filename:  
query { dataset ( tournament:8, round:281 ) }  
To get the new, supermassive data as a .zip file containing .parquet files:  
query { dataset ( tournament:8, round:281, filename:“numerai_datasets.zip” ) }  
To get the new, supermassive data as .csv or the int8 versions, you need to specify which file you want, e.g.:  
query { dataset ( tournament:8, round:281, filename:“numerai_training_data.csv” ) }

---

### Post #55 — **johnnywhippet** | 2021-09-16 20:31 UTC _(reply to #29)_

yeah but i find csv files easier to manipulate than parquet files.

---

### Post #56 — **testnet666** | 2021-09-19 22:55 UTC

Getting a 403 Client Error: Forbidden when trying to download the ‘old_data_new_val.parquet’ file in either parquet or CSV versions. Anyone have a solution for this?

---

### Post #57 — **thekizoch** | 2021-09-20 18:53 UTC

Is there a timeline estimation for when the legacy dataset will be deprecated?

---

### Post #58 — **taori** | 2021-09-21 18:09 UTC _(reply to #57)_

> Is there a timeline estimation for when the legacy dataset will be deprecated?

Same here, I would like to know how much time I have to migrate my code to the new dataset.

---

### Post #59 — **maxchu** | 2021-09-22 05:15 UTC

I found out that some targets has “nan” values, like “target_arthur_60” has 20599 nans in the “numerai_training_data.parquet”. Is it normal?

---

### Post #60 — **gammarat** | 2021-09-22 06:02 UTC _(reply to #59)_

Yes. I don’t remember the exact number offhand though, and I don’t think there were any in the primary target.

---

### Post #61 — **pyr395410** | 2021-09-25 08:38 UTC _(reply to #56)_

seems that this may be accessed via GraphiQL using { dataset ( tournament:8, round:280, filename:“old_data_new_val.parquet” ) }

---

### Post #62 — **thekizoch** | 2021-10-01 15:28 UTC _(reply to #58)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/thekizoch/48/1403_2.png) thekizoch:

> Is there a timeline estimation for when the legacy dataset will be deprecated?

I’ll make a new thread about it, unless you already have an answer?

---

### Post #63 — **wigglemuse** | 2021-10-01 17:53 UTC _(reply to #62)_

No firm timeline – many months at least. (Maybe even never.)

---

### Post #64 — **eses** | 2021-10-07 16:35 UTC _(reply to #31)_

Thanks for uploading the validation data for the old model. However, I got these errors when I ran the ‘download_data’ function:

> TypeError: download_data() got an unexpected keyword argument ‘round’`

when I delete the “round=280” input, I got the following error:

> HTTPError: 403 Client Error: Forbidden for url: [https://numerai-datasets.s3.amazonaws.com/284/v3/old_data_new_val.parquet?](<https://numerai-datasets.s3.amazonaws.com/284/v3/old_data_new_val.parquet?X-Amz-Algorithm=.......................................>)

---

### Post #65 — **bundushathur** | 2021-10-08 11:05 UTC _(reply to #64)_

As [pyr395410](<http://forum.numer.ai/u/pyr395410>) pointed out you can get the old features data over the new validation eras like this:

query = “”"  
query{  
dataset(tournament: 8, filename: “old_data_new_val.parquet”, round: 280)  
}  
“”"  
old_data_new_val_df = pd.read_parquet(napi.raw_query(query)[‘data’][‘dataset’])

---

### Post #66 — **bob_watson** | 2021-10-09 18:27 UTC

Trying to upload 285 and getting:  
Runtime.ImportModuleError Unable to import module ‘tournament_validate’: No module named ‘pydantic’

---

### Post #67 — **taori** | 2021-10-15 14:01 UTC

Out of curiosity, why isn’t the tournament data released automatically for training once the tournament ends (so every week we should have new training data)?

---

### Post #68 — **vurehout66** | 2021-10-17 11:12 UTC

In my eyes very sloppy how the new dataset and the old exist and get retreived. I have not seen a clear example of the dataset being loaded. Also now not able to participate for 3 weeks because of that. The example notebook download_data does not work. Terrible…reverting back to:  
napi.download_current_dataset(dest_path="…/286/", dest_filename=None,  
unzip=True, tournament=8)  
The above code only gives the CSV  
How would I download the parquet with new data?

---

### Post #69 — **oliveoil** | 2021-10-17 11:29 UTC _(reply to #68)_

from numerapi import NumerAPI
    # NumerAPI
    napi = NumerAPI()
    # (file, filename)
    datasets = [('numerai_training_data_int8.parquet', 'training_data.parquet'),
                ('numerai_tournament_data_int8.parquet', 'tournament_data.parquet'),
                ('numerai_validation_data_int8.parquet', 'validation_data.parquet'),
                ('numerai_live_data_int8.parquet', 'live_data.parquet'),
                ('example_validation_predictions.parquet', 'example_val_pred.parquet'),
               ]
    # Download datasets
    for dataset in datasets:
        napi.download_dataset(*dataset)

---

### Post #70 — **vurehout66** | 2021-10-17 11:31 UTC _(reply to #69)_

Not sure how you get that to work, it throws:  
AttributeError: ‘NumerAPI’ object has no attribute ‘download_dataset’

---

### Post #71 — **oliveoil** | 2021-10-17 11:33 UTC _(reply to #70)_

Did you update to the most recent version? The command was first added in version 2.8.0 according to the changelog:

<https://numerapi.readthedocs.io/en/stable/changelog.html>

---

### Post #72 — **vurehout66** | 2021-10-17 11:40 UTC _(reply to #71)_

I don’t know how, just use pip install numerapi each time, but it does not seem to be updated then.  
Ok managed to uninstall and install, thanks

---

### Post #73 — **jeremy_berros** | 2021-10-17 19:54 UTC _(reply to #72)_

`pip install --upgrade numerapi`

---

### Post #74 — **luee** | 2021-11-08 16:58 UTC

Quick question on the data, as of right now the training data includes the era 1 to 574 and the validation data include the era 857 to 961 while the unlabeled tournament data include the missing 300 or so eras between 574 and 857. If I understand it correctly we are in essence missing roughly 6 recent years of data, and if so what is the reasoning behind this? It seems that including that data in the training set could yield much better performances

---

### Post #75 — **wigglemuse** | 2021-11-08 17:20 UTC _(reply to #74)_

They’ve needed it for backtests and such – testing our models on eras we don’t have the targets for over a significant period. In the past they’ve said this is important for their own planning/optimization and also to show potential investors. However, recently they’ve indicated that they are going to release the targets for the test set also – I think they said probably in December. (Apparently the test set is no longer needed in this way internally?) Anyway, in a another month or so we should have that data too. (Of course sometimes plans change, we’ll see if it happens.)

---

### Post #76 — **luee** | 2021-11-08 17:24 UTC _(reply to #75)_

Awesome thanks for the reply, that should give a healthy boost in performance to everyone

---

### Post #77 — **jaca_ml** | 2021-11-14 12:07 UTC

Hi, I have couple of questions that I have been thinking for a time and I didn’t find an answer to them.

Is it possible to know which number era is the live era? So that we can use the temporal information to make temporal features like: the mean of the targets when feature_1 is less than 0.5 in last era.

Another question that I have is: How is it possible that the validation data is more recent than the live data? It doesn’t make sense to me because we are predicting the next week in live

Thank you in beforehand mates ![:smiley:](//forum.numer.ai/images/emoji/twitter/smiley.png?v=9)

---

### Post #78 — **wigglemuse** | 2021-11-14 17:50 UTC _(reply to #77)_

The live era is the final era in the tournament dataset each week. It doesn’t even have a number. Under the old system we’ve just left (before this massive data release), each week last week’s live era would simply be added to the test set. However, with the new data, that’s not happening anymore (the test set is remaining static), so you if you want last week’s live data you’d now have to save it each week yourself (or get it from somebody that has done that).

As far as the validation data being more recent than the live data, it isn’t, because as you say, that wouldn’t make sense.

---

### Post #79 — **jaca_ml** | 2021-11-14 21:22 UTC _(reply to #78)_

Thank you very much! That was super helpful.

Last thing, we can save the live data but is there a way to save also the targets at the end of the week in the live data?

---

### Post #80 — **wigglemuse** | 2021-11-14 21:29 UTC _(reply to #79)_

No – we never get the live targets under current scheme. This may change at some point though, they’ve been talking about it. (They have said already we are going to get the existing test set targets soon though.)

---

### Post #81 — **mindyoself** | 2021-11-21 01:08 UTC

Does the new dataset have an s3 bucket link?

---

### Post #82 — **rigrog** | 2021-11-22 15:13 UTC _(reply to #78)_

It’s also possible to download no-longer-live data through the API.
