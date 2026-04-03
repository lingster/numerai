---
title: "16GB Intermediate solution: XGB Era Boosting"
category: Tournament
url: https://forum.numer.ai/t/16gb-intermediate-solution-xgb-era-boosting/4421
created_at: 2021-10-29T18:14:20.102000+00:00
last_posted_at: 2022-04-01T02:49:45.071000+00:00
posts_count: 55
views: 5915
tags: []
---

# 16GB Intermediate solution: XGB Era Boosting

---

### Post #1 — **objectscience** | 2021-10-29 18:14 UTC

I’ve combined the example script with the era boosting script to create a low memory, “high performance” [solution](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/example_intermediate_16GB.py>). I’ve tested it several times and total memory usage is around 13GB (edit: 16GB on data load, see post below). On an 8 core machine (no threads), it takes a little over an hour for the initial run.

Data is “int8”  
The feature set is “medium”  
Training Era = every 4th.

The era boosting portion saves each iteration as a model for additional testing and analysis. Parameters here are random, you’ll want to do additional testing

Results from one of the iterative models.  


[![lowMem](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c273963d6ecf040dd8104cbea1c18cb76a626467.png)lowMem704×545 35.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c273963d6ecf040dd8104cbea1c18cb76a626467.png> "lowMem")

[![lowMem2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/587b5bae0c0af160ad56f6315c558c9073cb5081_2_638x500.png)lowMem2699×547 34.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/587b5bae0c0af160ad56f6315c558c9073cb5081.png> "lowMem2")

[![lowMem3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dc4508086a52cf7df8aac0e7834b6f194a693301.png)lowMem3700×540 35.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dc4508086a52cf7df8aac0e7834b6f194a693301.png> "lowMem3")

[![lowMem4](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/de37c90cc4482d99b471b9c45d69af90e414ccd5_2_633x500.png)lowMem4697×550 35.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de37c90cc4482d99b471b9c45d69af90e414ccd5.png> "lowMem4")

---

### Post #2 — **objectscience** | 2021-10-30 14:22 UTC

I’ll be cleaning the code up this weekend. Moving things off to utils where they belong etc.

---

### Post #3 — **objectscience** | 2021-10-30 16:02 UTC

Just tested the script again on the bigger box which has some better diagnostics.

Using the “medium” feature set, this will just touch 100% of 16GB when reading the training data. It drops off to 13 and then creeps back to 15.4 during the run. If people run into issues we can create a slightly smaller feature set to avoid topping out.

Using the “small” feature set, you’ll see just under 10GB of mem utilization during a run.

medium feature run  


[![itsClose](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8389e4c3fe8dfb9f1d2731c3a9df95e07028c87b_2_690x163.png)itsClose1908×451 74.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8389e4c3fe8dfb9f1d2731c3a9df95e07028c87b.png> "itsClose")

small feature run (cleaned up the output a little…)  


[![small](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6db62e0c1a849dec47c71d7f58f69213a217d26c_2_690x163.png)small1914×454 21.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6db62e0c1a849dec47c71d7f58f69213a217d26c.png> "small")

---

### Post #4 — **objectscience** | 2021-10-31 16:38 UTC

I’ve cleaned up the code a little, put things where they belong. Still have one thing I need to sort out and will get to that this week.

I’ve started working on an optimized feature set that will target around 15GB, leaving a little more headroom when loading the data. I’m using MDO’s BorutaShap code for this, it’s going to take a while. Estimating around 250 hours to process all the targets. I’m going to publish all the results from this as I feel like the community at large will benefit from the knowledge, it also prevents us from doing parallel work, which I’m not a fan of. No reason to be wasting compute cycles on the same stuff when we should be focusing on original/different ensembles. I’ll drop the first half this week and the balance next.

I’ll make this a priority the first of the year when the new data drops, so we can hit the ground running.

~ OS, a.k.a ‘feature_baldish_cognitional_naha’

---

### Post #5 — **objectscience** | 2021-10-31 19:16 UTC

Speaking of ensembles, it’s never too early to begin to think about the possibilities. Between the current number of targets and the growing feature set, we should be able to generate a large number of “unique” submissions. They’ll still be correlated to some degree or another, but the opportunity here to generate “true contribution” should be high (once we know what it is of course.)

This code was ripped from [codegrepper.com](<https://www.codegrepper.com/code-examples/python/python+all+possible+combinations+of+list+items+of+given+length>) I remain little more than a python sneak-thief. ![:slight_smile:](//forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)
    
    
    from itertools import combinations
    
    # targets
    
    targets = [
    "target",
    "target_jerome_20",
    "target_janet_20",
    "target_ben_20",
    "target_alan_20",
    "target_paul_20",
    "target_george_20",
    "target_william_20",
    "target_arthur_20",
    "target_thomas_20",
    "target_nomi_60",
    "target_jerome_60",
    "target_janet_60",
    "target_ben_60",
    "target_alan_60",
    "target_paul_60",
    "target_george_60",
    "target_william_60",
    "target_arthur_60",
    "target_thomas_60"
    ]
    
    ensembleLength = 6 # pick any number here from 1 to 20
    for i in combinations(targets, ensembleLength):
      print(i)

---

### Post #6 — **objectscience** | 2021-11-01 05:14 UTC

Boruta classifies features as ‘confirmed important’, ‘confirmed unimportant’, and ‘tentative’. I grabbed 400 random features from the 1015 ‘confirmed unimportant’ group on nomi_20 and generated a model with decent results. Unimportant isn’t the same as useless.

[![unimportant](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5c5f4c7ebb896b46c8fc79d9b0eb51dae1ce6f82.png)unimportant711×552 34.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5c5f4c7ebb896b46c8fc79d9b0eb51dae1ce6f82.png> "unimportant")

---

### Post #7 — **objectscience** | 2021-11-02 23:49 UTC

Started pushing some of the raw output to [git](<https://github.com/johnputmanii/numerai_xgb_eb/tree/main/borutashap_results/raw_results>).

There have been a couple of targets where the actual features weren’t more predictive than the shadow features, so there are no “important” features in those (Paul, Janet). Seven targets down, 13 to go.

As of right now, there are just over 300 features that fall into the “strong” and “weak” Boruta classification.

---

### Post #8 — **objectscience** | 2021-11-03 19:59 UTC

I’ve just updated the repo with a new feature file that contains 300 features from the Boruta run. These features should work on a 16GB machine and leave headroom in the commit charge on a Windows machine.

From “features2.json” use “xlsmall” for the 16GB feature set.

I’ll continue to add alternative target output from the Boruta run as it drops. This feature set should get you going though.

---

### Post #9 — **objectscience** | 2021-11-03 20:09 UTC

An example of the 16GB feature set ran through the XGB EB script. It is of course cherry-picked to look good-ish.

[![16GBFeatureSet](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2f14550e0a5582009e5ad0cad8934c6e6ea92dd7.png)16GBFeatureSet705×544 35.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2f14550e0a5582009e5ad0cad8934c6e6ea92dd7.png> "16GBFeatureSet")

---

### Post #10 — **bguberfain** | 2021-11-04 11:47 UTC _(reply to #9)_

When working with int8 data you should fill nan with 2, not 0.5

[github.com](<https://github.com/johnputmanii/numerai_xgb_eb/blob/5416c86aff7070b2c02045e788640e1344c38c66/example_intermediate_16GB.py#L123>)

#### [johnputmanii/numerai_xgb_eb/blob/5416c86aff7070b2c02045e788640e1344c38c66/example_intermediate_16GB.py#L123](<https://github.com/johnputmanii/numerai_xgb_eb/blob/5416c86aff7070b2c02045e788640e1344c38c66/example_intermediate_16GB.py#L123>)
    
    
        113. tournament_data = pd.read_parquet(f'tournament_data_int8_{current_round}.parquet',
         
    
    
        114.                                   columns=read_columns)
         
    
    
        115. nans_per_col = tournament_data[tournament_data["data_type"] == "live"].isna().sum()
         
    
    
        116. 
         
    
    
        117. # check for nans and fill nans
         
    
    
        118. if nans_per_col.any():
         
    
    
        119.     total_rows = len(tournament_data[tournament_data["data_type"] == "live"])
         
    
    
        120.     print(f"Number of nans per column this week: {nans_per_col[nans_per_col > 0]}")
         
    
    
        121.     print(f"out of {total_rows} total rows")
         
    
    
        122.     print(f"filling nans with 0.5")
         
    
    
        123.     tournament_data.loc[:, features].fillna(0.5, inplace=True)
         
    
    
        124. else:
         
    
    
        125.     print("No nans in the features this week!")
         
    
    
        126. 
         
    
    
        127. spinner.start('Predicting on validation and tournament data')
         
    
    
        128. # double check the feature that the model expects vs what is available to prevent our
         
    
    
        129. # pipeline from failing if Numerai adds more data and we don't have time to retrain!
         
    
    
        130. model_expected_features = model.get_booster().feature_names
         
    
    
        131. if set(model_expected_features) != set(features):
         
    
    
        132.     print(f"New features are available! Might want to retrain model {model_name}.")
         
    
    
        133. validation_data.loc[:, f"preds_{model_name}"] = model.predict(

---

### Post #11 — **objectscience** | 2021-11-04 16:17 UTC

got ya… fixing right now  
thanks for the catch

---

### Post #12 — **objectscience** | 2021-11-04 22:23 UTC

84 Model Dump

I generated a small batch of nomi_20 models last night with the intermediate script and the new feature set. I’ve pushed these up to a public S3 bucket for anyone to grab and investigate. They will run from extremely under-fit to (probably) extremely over-fit and should give deeper insight into the Boruta optimized feature set and the characteristics of this modeling approach.

This should help reduce some of the initial time spent creating and researching the models and get you closer to generating your own work, interesting ensembles, and alternative target modeling.

Models developed with:

  * Max Depth of 3, 4, 5 & 6
  * Num Estimators at 500*
  * Col Sample at 0.1
  * Learning Rate of 0.001
  * Num of Iterations at 22*


  * These are completely random, there are likely better parameters.



Each file follows a naming convention of  
Max Depth as md  
Num Estimators as ne  
Num of Iterations as ni  
Target name Ex. md3_ne500_ni0_target_nomi_20

Files range in size from 5MB to almost 500MB

File URLs:  
<https://numermodels.s3.us-west-1.amazonaws.com/md3_ne500_ni0_target_nomi_20.pkl>  
<https://numermodels.s3.us-west-1.amazonaws.com/md3_ne500_ni1_target_nomi_20.pkl>  
<https://numermodels.s3.us-west-1.amazonaws.com/md3_ne500_ni2_target_nomi_20.pkl>  
.  
.  
.

<https://numermodels.s3.us-west-1.amazonaws.com/md3_ne500_ni20_target_nomi_20.pkl>  
.  
.  
.  
<https://numermodels.s3.us-west-1.amazonaws.com/md6_ne500_ni20_target_nomi_20.pkl>

Use these at your own risk, nothing here is financial advice and no recommendations are being made.  
These are strictly for research purposes.

---

### Post #13 — **gbrecht** | 2021-11-05 06:40 UTC

Thank you very much for your work.  
The URL listing is truncated. I am sure it is possible to construct them all (semi) manually, but is there a way to bulk download them all (one file) or have the URLs listed sequentially?

---

### Post #14 — **objectscience** | 2021-11-05 13:48 UTC _(reply to #13)_

I’m not aware of a way to bulk dl the files outside of the CLI/console, that doesn’t mean they can’t be scraped though, I’m just not sure how.

Here is a [list](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/link_list.txt>) of all the current models. If this is beneficial, I’ll do a deeper dive and push some more of these out.

---

### Post #15 — **gbrecht** | 2021-11-05 17:22 UTC

That list works very well. Thanks again!

---

### Post #16 — **jefferythewind** | 2021-11-05 20:15 UTC

This is really cool, and a lot of great work. One thing that stands out to me is the trial you posted above that attains almost 5% average correlation, that is huge, right?

---

### Post #17 — **objectscience** | 2021-11-05 22:08 UTC _(reply to #16)_

That was part of the TB200 diagnostics, those are always pretty high.

---

### Post #18 — **objectscience** | 2021-11-06 00:56 UTC

Creating a Feature Neutral Ensemble

I’ve been playing around with feature neutralization in my own work and wanted to pass along some ideas that will work with our sample models. These aren’t recommendations, just random outtakes to get you thinking in new directions.

From our models I grabbed:

  * ni20_target_nomi_20
  * ni15_target_nomi_20
  * ni10_target_nomi_20
  * ni5_target_nomi_20



I ran each of these models through a series of neutralizations:

  * 100% of the features neutralized by a factor of 1.0
  * 100% of the features neutralized by a factor of 0.75
  * 100% of the features neutralized by a factor of 0.5
  * 100% of the features neutralized by a factor of 0.25  
I repeated this process for 75%, 50%, and 25% of the features for all of the selected models.  
You can see sample results for each model [here](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/nuetralization.txt>).



From here I selected a single iteration (ni) from each modeling group, based on its highest APY with a minimum Sharpe of +1.0. These selections are noted by an " * " in the linked table.

The only exception to this is the selection as at " ** ". When I reviewed the choices, I had two from “Neutralize 0.25 features…” and none from “Neutralize all features…” The OCD in me insisted at that point I must have one from each group and " ** " was used instead… ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

Those results were ensembled and this is the result:  


[![fn_ensemble](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/22da7c980918d7b39309fee3dc7407433847840e.png)fn_ensemble703×550 35.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/22da7c980918d7b39309fee3dc7407433847840e.png> "fn_ensemble")

---

### Post #19 — **hellozml** | 2021-11-06 05:10 UTC _(reply to #18)_

Wow. Thanks for sharing.  
You save me tons of man hours and avoided kernel restarts since working with the new massive data_set. Almost gave up.

Eventually, i will need to invest on more ram soon, heard some new massive^2 coming our way.

Cheers

---

### Post #20 — **objectscience** | 2021-11-06 13:55 UTC _(reply to #19)_

I hope there will be room for models like this in the competition for a long-time. When the new data drops and I get my initial work finished, I plan on duplicating this if at all possible. In a perfect world, we can generate two or three 16GB feature sets and corresponding model sets. This will allow for a lot of creative ensembling.

---

### Post #21 — **objectscience** | 2021-11-07 18:46 UTC

Just a heads up. Using the current script on alternate targets results in an “empty dataset error” with xgb. I’ll try to get this sorted as soon as I can, I’ve just got some other stuff on the plate I need to jump on once the Boruta run is finished.

---

### Post #22 — **objectscience** | 2021-11-08 23:42 UTC

Boruta Shap has wrapped up. You can find the raw results [here](<https://github.com/johnputmanii/numerai_xgb_eb/tree/main/borutashap/raw_results>), and the best features [here](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/borutashap/best_all_targets.csv>).

---

### Post #23 — **objectscience** | 2021-11-09 18:51 UTC

Working on some plug-and-play feature [sets](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/borutashap/feature_sets.txt>). You’ll be able to drop these right in your features.json file.

---

### Post #24 — **objectscience** | 2021-11-09 23:55 UTC

[This](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/borutashap/best_plus_all_targets.csv>) is probably the list most of us need. It includes all of the “important” and “tentative” features for all targets. This should work on a 32GM machine as well (I’m fixin’ to find out).

It’s also in the “feature_sets.txt” file, ready to drop into features.json

---

### Post #25 — **objectscience** | 2021-11-10 02:36 UTC

I’ve tested and added a 32GB [script](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/example_intermediate_32GB.py>) to the repo. This uses the “bestplus” feature set, int8 data, and no era paring. It hits a 90% commit charge while processing.

Baseline using minimal parameters compared to the 16GB “xlsmall” features.  
md: 3  
ne: 500  
lr: 0.001  
cs: 0.1  
ni: 3

| mean | sharpe  
---|---|---  
16GB using “xlsmall” feature set | 0.0170511 | 0.482840  
32GB using “bestplus” feature set | 0.0146597 | 0.610938

---

### Post #26 — **objectscience** | 2021-11-13 15:32 UTC

Sharing the results from an advanced script run this week. These were the initially recommended parameters by MDO and should get everyone on the same page. Big box participants can use this as a baseline to explore different params and the small box crew can, hopefully, steer their efforts more effectively when using the example/eb scripts and creating ensembles.

NE: 20,000  
LR: 0.001  
MD: 6  
NL: 2**6  
CB: 0.1  
Cross Val Downsample = 1  
Full Train Downsample = 1

Validation metrics for out of sample training | mean | sharpe  
---|---|---  
preds_model_target_neutral_riskiest_50 | 0.0494102 | 2.09365  
preds_model_target_jerome_20_neutral_riskiest_50 | 0.048734 | 2.06158  
preds_model_target_thomas_20_neutral_riskiest_50 | 0.047007 | 2.04556  
preds_model_target_william_20_neutral_riskiest_50 | 0.0489308 | 2.03005  
preds_model_target_arthur_20_neutral_riskiest_50 | 0.0495472 | 2.01925  
preds_model_target | 0.0599232 | 2.01545  
preds_model_target_ben_20_neutral_riskiest_50 | 0.046293 | 2.00648  
ensemble_all | 0.0532359 | 1.97708  
preds_model_target_thomas_20 | 0.054444 | 1.96829  
ensemble_neutral_riskiest_50 | 0.0467554 | 1.93253  
preds_model_target_ben_20 | 0.0540396 | 1.92106  
ensemble_not_neutral | 0.0555182 | 1.9054  
preds_model_target_william_20 | 0.0567741 | 1.8844  
preds_model_target_nomi_60 | 0.054169 | 1.87865  
preds_model_target_jerome_20 | 0.0570743 | 1.86585  
preds_model_target_arthur_20 | 0.0578719 | 1.86147  
preds_model_target_alan_20 | 0.0432463 | 1.81026  
preds_model_target_thomas_60 | 0.047932 | 1.75095  
preds_model_target_nomi_60_neutral_riskiest_50 | 0.0425226 | 1.73909  
preds_model_target_ben_60 | 0.0480247 | 1.73496  
preds_model_target_jerome_60 | 0.0506499 | 1.71836  
preds_model_target_william_60 | 0.0493479 | 1.71613  
preds_model_target_arthur_60 | 0.050831 | 1.71575  
preds_model_target_janet_20 | 0.0437985 | 1.7139  
preds_model_target_paul_20_neutral_riskiest_50 | 0.0310498 | 1.70455  
preds_model_target_jerome_60_neutral_riskiest_50 | 0.0413955 | 1.67698  
preds_model_target_thomas_60_neutral_riskiest_50 | 0.0394446 | 1.66946  
preds_model_target_george_20_neutral_riskiest_50 | 0.0324472 | 1.66639  
preds_model_target_ben_60_neutral_riskiest_50 | 0.0392669 | 1.66213  
preds_model_target_alan_20_neutral_riskiest_50 | 0.0358959 | 1.65524  
preds_model_target_george_20 | 0.0312737 | 1.64467  
preds_model_target_arthur_60_neutral_riskiest_50 | 0.0413451 | 1.64148  
preds_model_target_janet_20_neutral_riskiest_50 | 0.0358536 | 1.63857  
preds_model_target_william_60_neutral_riskiest_50 | 0.0406023 | 1.63626  
preds_model_target_paul_20 | 0.0269739 | 1.57079  
preds_model_target_paul_60_neutral_riskiest_50 | 0.0278925 | 1.51302  
preds_model_target_paul_60 | 0.0254812 | 1.48692  
preds_model_target_alan_60 | 0.03706 | 1.46467  
preds_model_target_george_60 | 0.0261036 | 1.42696  
preds_model_target_george_60_neutral_riskiest_50 | 0.0271003 | 1.38735  
preds_model_target_janet_60 | 0.0366974 | 1.37472  
preds_model_target_alan_60_neutral_riskiest_50 | 0.030381 | 1.35703  
preds_model_target_janet_60_neutral_riskiest_50 | 0.0295743 | 1.25600

---

### Post #27 — **gbrecht** | 2021-11-13 17:24 UTC

NE is number of estimators and 20k is not a typo?

---

### Post #28 — **objectscience** | 2021-11-13 18:10 UTC _(reply to #27)_

[@gbrecht](</u/gbrecht>) Correct. If you take a peek at the official “example_model_advanced.py” file in Numerai’s example scripts, you’ll see the “ideal” params listed which is what I used for that run. Truthfully, those are probably just starter params. I know some of us were using much higher estimators in older versions of the tourney with good results.

I’ll try to get some plug-and-play versions of these ready so people can focus more on creative ensembles and less on duplicate processes.

---

### Post #29 — **gbrecht** | 2021-11-13 18:56 UTC

I was just curios about the number of trees becasue I remember the example predictions used 2k trees, not 20k.  
Just now because of your comment I saw the comment in the official file listing these parameters … thx!

---

### Post #30 — **mesomachukwu12** | 2021-11-21 19:58 UTC

Getting the error below when using python example_advanced_32GB.py

Entering model selection loop. This may take awhile.  
loading model config for advanced_example_model  
Traceback (most recent call last):  
File “example_advanced_32GB.py”, line 189, in   
feature_cols = model_config[“feature_cols”]  
TypeError: ‘bool’ object is not subscriptable

---

### Post #31 — **adalseno** | 2021-11-24 21:21 UTC

Hi [@mesomachukwu12](</u/mesomachukwu12>) , it looks like the model config was not loaded so False is returned. See utils.py:
    
    
        def load_model_config(model_name):
            path_str = f"{MODEL_CONFIGS_FOLDER}/{model_name}.json"
            path = Path(path_str)
            if path.is_file():
                with open(path_str, 'r') as fp:
                    model_config = json.load(fp)
            else:
                model_config = False
            return model_config

---

### Post #32 — **mesomachukwu12** | 2021-11-25 14:18 UTC _(reply to #31)_

So how can it be addressed

---

### Post #33 — **adalseno** | 2021-11-27 21:01 UTC

Hi [@mesomachukwu12](</u/mesomachukwu12>) , I apologise for the late reply but I’ve been busy during the week.  
If you have already trained a model you should have a models and model_configs folder. If not, you need to train your model.  
In the file `example_advanced_32GB.py` on line 40 set `model_selection_loop` = True. Then on line 199 add `exit(0)` and run the script. After that you should have your model and the configuration file in the right directories (the program will create them if they do not exist). Switch back `model_selection_loop` = False and remove `exit(0)` from line 199 then run the script again. It should work. Let me know.

You may also want to download one of the pre-trained models listed in link_list.csv (they use xgboost) and try one of those for predictions. You will need to tweak the code a little bit to make it working with xgboost though but not that much.

---

### Post #34 — **adalseno** | 2021-11-27 21:59 UTC _(reply to #33)_

here you are a very very simple way to use the pre-trained model(s). Please check that you have created and activated a virtual environment with at least python 3.8 and the required packages in the right version

### You need to have xgboost 1.4.2 installed! pip install xgboost==1.4.2 (1.5.1 won’t work)
    
    
    import pickle # you need at least python 3.8
    
    from numerapi import NumerAPI
    
    import pandas as pd
    
    # Create a folder named pre_trained_models and download and save md3_ne500_ni0_target_nomi_20.pkl there https://numermodels.s3.us-west-1.amazonaws.com/md3_ne500_ni0_target_nomi_20.pkl
    
    # Load Numerai API
    
    napi = NumerAPI()
    
    # Get current tournament round
    
    current_round = napi.get_current_round(tournament=8)
    
    # if you have an old pickle version you will get an error Unsupported Pickle Protocol 5
    
    model = pickle.load(open('pre_trained_models/md3_ne500_ni0_target_nomi_20.pkl', 'rb'))
    
    print("downloading tournament_data")
    
    napi.download_dataset( "numerai_tournament_data_int8.parquet", f"numerai_tournament_data_int8_{current_round}.parquet")
    
    tournament_data = pd.read_parquet(f"numerai_tournament_data_int8_{current_round}.parquet")
    
    # Check that everything is fine
    
    tournament_data.head()
    
    # Get the feature names from the model
    
    feature_names = model.get_booster().feature_names
    
    # create predictions
    
    predictions = model.predict(tournament_data[feature_names])
    
    # Save to file
    
    predictions = pd.DataFrame(predictions, index = tournament_data.index)
    
    predictions.to_csv("predictions.csv") # use a more meaningful name if you want
    

It should work fine but it’s bare basic. You can build up using different models, neutralisation, ensemble and so on. Good luck (and remember to thank [@objectscience](</u/objectscience>) for his work).

---

### Post #35 — **mesomachukwu12** | 2021-11-28 12:24 UTC

Yes, that fix the issue  
Thanks

---

### Post #36 — **mesomachukwu12** | 2021-11-28 12:25 UTC _(reply to #26)_

Had the error below when I used the parameters  
NE: 20,000  
LR: 0.001  
MD: 6  
NL: 2**6  
CB: 0.1  
Cross Val Downsample = 1  
Full Train Downsample = 1

KeyError: ‘preds_model_target_neutral_riskiest_50’

preds_model_target_neutral_riskiest_50 is the highest performing model

---

### Post #37 — **mesomachukwu12** | 2021-11-28 12:50 UTC _(reply to #36)_

I fixed this issue when preds_model_target_neutral_riskiest_50 is included in the validation statistics

---

### Post #38 — **objectscience** | 2021-11-29 19:20 UTC

[@adalseno](</u/adalseno>) Thank you for all your help! I’ve been buried the last couple of weeks and completely missed all this.

---

### Post #39 — **objectscience** | 2021-12-01 17:59 UTC

[@adalseno](</u/adalseno>) put together a function that will allow you to create unique features sets based on the number of times they appear in the raw results. You can find it [here](<https://github.com/johnputmanii/numerai_xgb_eb/blob/main/utils.py>), “create_features_dict()”.

(Really appreciate the addition, Thank you!)

---

### Post #40 — **br1** | 2022-01-03 06:33 UTC _(reply to #37)_

could you point me in the direction of your fix? I’m having the exact same issue and can’t see where it’s hanging up

---

### Post #41 — **mesomachukwu12** | 2022-01-03 23:17 UTC _(reply to #40)_

I modified example_advanced_32GB.py as follows;

# do ensembles
    
    
        training_data["ensemble_neutral_riskiest_50"] = sum(
            [training_data[pred_col] for pred_col in pred_cols if pred_col.endswith("neutral_riskiest_50")]).rank(
            pct=True)
        training_data["ensemble_not_neutral"] = sum(
            [training_data[pred_col] for pred_col in pred_cols if "neutral" not in pred_col]).rank(pct=True)
        training_data["ensemble_all"] = sum([training_data[pred_col] for pred_col in pred_cols]).rank(pct=True)
        training_data["preds_model_target_neutral_riskiest_50"] = sum([training_data[pred_col] for pred_col in pred_cols]).rank(pct=True)
    
        ensemble_cols.add("ensemble_neutral_riskiest_50")
        ensemble_cols.add("ensemble_not_neutral")
        ensemble_cols.add("ensemble_all")
        ensemble_cols.add("preds_model_target_neutral_riskiest_50")

---

### Post #42 — **br1** | 2022-01-07 22:33 UTC _(reply to #41)_

much appreciated, resolved it. I was off chasing the error in utils thinking it was spitting it out when it was calling validation_metrics

---

### Post #43 — **mesomachukwu12** | 2022-01-09 14:53 UTC _(reply to #15)_

[@gbrecht](</u/gbrecht>) which model do you use example_advanced_32GB.py or the intermediate?

---

### Post #44 — **objectscience** | 2022-01-10 17:42 UTC

I’m just getting caught up on all of this, I’ll try to get all of this updated in the next week or so. Holidays have me way behind. [@mesomachukwu12](</u/mesomachukwu12>) appreciate your help here. Thank you!

---

### Post #45 — **gbrecht** | 2022-01-10 20:35 UTC _(reply to #43)_

I have a different way of constructing my models from the way the example model is built. But I am using all available information on feature groupings (I really miss feature groups!)

---

### Post #46 — **mesomachukwu12** | 2022-01-15 16:36 UTC _(reply to #45)_

[@gbrecht](</u/gbrecht>), I will appreciate if you can share with me [matany58@yahoo.com](<mailto:matany58@yahoo.com>)

---

### Post #47 — **objectscience** | 2022-01-15 17:40 UTC _(reply to #46)_

I’ve been giving this a lot of thought since yesterday’s TC announcement: I’m not sure I’m going to be able to reproduce the boruta output when the new classic data drops. The initial run took a little over a week and when the data 3x’s, that could obviously push out much further. This is being further complicated by my new signals pipeline which is turning into a compute black hole.

I just wanted to give you all a heads up and time to prepare for the next data drop. GL!

---

### Post #48 — **mesomachukwu12** | 2022-01-15 18:07 UTC _(reply to #47)_

Thanks for the heads up. The challenge is good

---

### Post #49 — **gbrecht** | 2022-01-15 22:08 UTC _(reply to #47)_

No worries your work is highly appreciated!

---

### Post #50 — **gcotti** | 2022-01-22 23:16 UTC _(reply to #10)_

Hey, can you explain why exactly you need to fill int8 with 2 instead of 0.5 in this case? Been trying to find the answer myself and can’ seem to sort it out

---

### Post #51 — **wigglemuse** | 2022-01-22 23:21 UTC _(reply to #50)_

int8 = integers only, so instead of values 0,0.25,0.5,0.75,1.0, you have 0,1,2,3,4. So 2 is the middle/neutral value instead of 0.5.

---

### Post #52 — **gcotti** | 2022-01-22 23:25 UTC _(reply to #51)_

Ahhhh yeah how embarrassing… here I was thinking it was something to do with the pandas fillna method.

Thanks!

---

### Post #53 — **objectscience** | 2022-01-22 23:58 UTC _(reply to #52)_

I actually made the exact same mistake, don’t think anything of it.

---

### Post #54 — **joakim** | 2022-03-31 09:56 UTC

Hey [@objectscience](</u/objectscience>), I’m not able to access the repo anymore. ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=10)

---

### Post #55 — **objectscience** | 2022-04-01 02:49 UTC _(reply to #54)_

Almost sent you a message the other day, haven’t seen you on the forum in a minute. Hope all is well.

Things on this end have gotten a little dicey since the first of the year and I’ve largely had to pull away from the comp. I was having a really hard time staying on top of the things that needed addressed with the repo and with TC and the new data-set coming thought it was best to pull it, so people didn’t waste time trying to use something that is out of date.

I still have some of the output from the run though, can paste it here if it will help.
