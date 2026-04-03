---
title: "Which Model is Better?"
category: Tournament
url: https://forum.numer.ai/t/which-model-is-better/4841
created_at: 2022-01-23T03:56:33.062000+00:00
last_posted_at: 2022-01-27T21:41:45.751000+00:00
posts_count: 45
views: 3063
tags: []
---

# Which Model is Better?

---

### Post #1 — **dzheng1887** | 2022-01-23 03:56 UTC

I am curious what others think, I have two models. One where I optimized for correlation, and the other I optimized for risk. Based on the validation numbers, which one would you prefer to stake? I didn’t do the cross validation, so I do not have that info on hand as I see that seems more popular on this forum.

I like how the max draw down is not that much over two weeks in the second one. On the other hand, I am only putting a small percentage of my assets on these models so perhaps I should go for the higher risk?

Thanks for feedback

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/556b05f97f457cef096cb5ef1aef91a7350b8c40_2_690x445.png)image735×475 29.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/556b05f97f457cef096cb5ef1aef91a7350b8c40.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5db04a5198ed6aaebbd9440175c0748a1ef333f1_2_690x442.png)image742×476 30.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5db04a5198ed6aaebbd9440175c0748a1ef333f1.png> "image")

---

### Post #2 — **wigglemuse** | 2022-01-23 04:06 UTC

I’d stake 'em both. Then I’d keep generating more, hopefully with significantly lower corr to examples.

---

### Post #3 — **dzheng1887** | 2022-01-23 04:11 UTC _(reply to #2)_

Sorry, I don’t understand. What do you mean by “significantly lower corr to examples”?

Thanks for the feedback

---

### Post #4 — **wigglemuse** | 2022-01-23 04:39 UTC _(reply to #3)_

meta model corr (ex preds corr here) – you’ve got .71 & .66. In other words, I’d be trying to make some models that are both good and more original. That’s going to be more valuable in the future.

---

### Post #5 — **dzheng1887** | 2022-01-23 15:50 UTC _(reply to #4)_

Yes I have been reading about some of these things briefly, but didn’t really understand. Wanted to try to put something on the board first.

Then perhaps will want to try to work on Signals and MMC. FNC might also be coming to stake on?

---

### Post #6 — **johnnywhippet** | 2022-01-23 19:35 UTC

what type of model is it? Tree, NN, something else?

---

### Post #7 — **dzheng1887** | 2022-01-23 20:46 UTC

Standard tree like everything else. Not too different from examples they gave honestly. I want to try some more advanced stuff later, but will probably be a while til I get to it.

---

### Post #8 — **johnnywhippet** | 2022-01-23 22:53 UTC _(reply to #7)_

how long have the models been running? whats the corrmmc for these models?

---

### Post #9 — **maxchu** | 2022-01-23 23:21 UTC

As mentioned by most experienced participants, don’t put too much focus on the validation set. A cross-validation score is a much better indicator for future performance. You can start with the advanced example script.

---

### Post #10 — **dzheng1887** | 2022-01-23 23:46 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/johnnywhippet/48/2803_2.png) johnnywhippet:

> corrmmc

Sorry I don’t know what corrmmc is for the model. I just started.

For the cross validation, do you put the training and validation data together and cross validation, say k=5 folds? I was thinking similarly, but often find the training/test split is just as good (in other applications) as cross validation and doesn’t take as long to run. Mostly because of the correlation of the models due to them sharing a lot of the same data.

One thing I do not like is using the same validation set all the time. I usually avoid this by changing a random seed number every now and then (and if I really want a CV esque like result, do 100 random seeds), but it’s not as simple here. Need to worry about overlapping eras and I really don’t understand the gap between the train and validation eras. Feel I should maintain that as it was given. /shrug

---

### Post #11 — **dzheng1887** | 2022-01-23 23:47 UTC _(reply to #10)_

Well, are there models out there on this forum that show the CV result, the validation result, and the actual future results? I also remember seeing the more experienced participants say such things, but did not see the evidence

---

### Post #12 — **maxchu** | 2022-01-24 04:58 UTC _(reply to #11)_

You are right that not many ppl show their CV result. Maybe it is because there are multiple ways to do CV and the validation periods is not the same for everyone. But it is quite obvious and common sense that CV score is more important than validation set as in CV you basically test your model on multiple CV test set and CV validation set (depends on how to select your fold the validation set can be a part of your CV fold, so your canonical validation set is just one part of your CV scores).

---

### Post #14 — **maxchu** | 2022-01-24 05:00 UTC _(reply to #13)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) [Diagnostics for #39](<http://forum.numer.ai/t/diagnostics-for-39/4155>) [Data Science](</c/data-science/5>)

> Diagnostics are built to help us, but they can be very misleading. My most successfull model, which stands at #39 at the time of writing (nyuton_test8) has so bad diagnostics, that I almost threw it out at the beginning and I haven’t started staking on it until recently. Trust you CV! I’m writing this post partly for myself as a reminder, when I see similar results with the new dataset. To be frank, this model uses an ensemble of models from CV folds. Data also includes validation set. This …

---

### Post #15 — **dzheng1887** | 2022-01-24 05:45 UTC _(reply to #14)_

Thanks maxchu, yes I believe it was these posts that I saw. It’s crazy how poorly they performed but still earned some medals in live rounds. I also did want to start including the validation data in my training examples as well and just trust the model fit on 20% more data.

I know CV sounds pretty cool. All the DS people I know prefer it to training test split. You get to use all the data points twice, once for training and another for validation. I don’t feel it’s worth the Kx time in training for k fold CV. If so, I think seeing some analysis that shows training/test split is bias but CV is not would change my mind. Or if there’s some other argument out there besides using all the data twice.

And if you want to understand the volatility of your metrics or you feel you are abusing the validation set too much or you feel the random draw of the validation set is off, then I’ll just find another validation set or deeply bootstrap some things instead. That is an altogether different idea though

---

### Post #16 — **maxchu** | 2022-01-24 05:53 UTC _(reply to #15)_

I come from a background of deep learning research and CV is not a common practice due to the nature of the problem where deep learning does well. Usually, problems with lots of data require lots of computing, and in that case, CV is not feasible. But for numerai data, it is completely different from the usual deep learning dataset. Signal to noise is very high, data set is non-iid. I would say in a problem like numerai, CV is the most important thing. All I can say is that you will learn your lesson in the future if you don’t use CV. I actually think that numerai should stop labeling the canonical validation set and simply tell users to do their own validation split, ideally in CV.

---

### Post #17 — **maxchu** | 2022-01-24 05:58 UTC _(reply to #15)_

Also, it takes a long time only if you are training deep NN. But from my own experience and experience shared by other users, you dont need a very deep NN to have good results (checkout the autoencoder post about Jane Street Kaggle competition), i actually think it will hurt if your model is too deep. If you train a shallow autoencoder-like network, it is actually much faster than tree-models as it can easily fully utilize multiple GPUs, you can train multiple targets at once. I also like NN as it is more flexible and you can model very complex ideas easily (for example like global era-wise feature, multiple output head, … etc).

---

### Post #18 — **dzheng1887** | 2022-01-24 07:06 UTC

Thanks for your feedback. I have learned 4 PhD classes in Stats and they all more or less gloss over this point. When asked about it, no proof is given, just general heuristics that CV uses data more efficiently because the points are used for training and testing. I have also tried looking this up in papers too. I guess most people accept it is true so I don’t find what I’m looking for.

My also not rigorous reasoning is this. Let k is 4. One train test split is just one fold of the k == 4 CV. Have you ever seen one fold do so drastically worse than 4 folds most of the time? And then if the model did accidentally generalized well on the one fold, I would expect another model fit with 66% same data/33% test data would also by chance generalize well to the new held out (old training) data. If the dataset is small, say 4 observations, I can see how only looking at one fold would be too volatile by outlier chance. Not so much for millions though.

Do people see that in their CV results? If you accidentally just used one of your folds, would you have made a mistake according to what you find looking at all your folds aggregated in some way? I think that would be interesting to see and would definitely convince me to use more CV. I will probably even try myself for curiosity one day, but in all my other projects, I have not seen it besides in the very small sample case. As such, I find the extra amount of modeling fitting not very worthwhile.

I totally agree though, I’ve been using this one validation set too much. And there is a question if there is some bias in the validation set. For reasons like you mention if there is a very strong non iid correlation and it persists through the 100 validation eras. I do think it’s time to train/test a different group of data. But I also don’t hyperparameter tune my models very precisely, only to general heuristics after seeing how the model/data behaves.

I do have two questions for those who use CV. I was thinking to block split the eras because they are overlapping (not iid). So eras 1-4 go to the same fold. But I didn’t know if era 1 coincided with week 1 of a month. Or should I be block splitting eras 2-5 if era 1 was the 4th week of another month? Second, how do you deal with multiple observations of the same firm throughout all the folds in your dataset? Surely the data is also not IID in this way too. I assume the given validation period is far away from the training period to not have this issue (but I have no idea if the gap in the eras actually mean anything). I also found my validation data taken from the training period to also be overly optimistic compared to the given validation data. I assumed it was for this reason.

---

### Post #19 — **maxchu** | 2022-01-24 10:11 UTC _(reply to #18)_

I will first answer your first question as i found it a little bit confusing for me. When you do the CV, your K-fold validation sets should cover most of your original train+val set. In the simplest case, you can just use the average of all corr of all folds as your CV score. Say you have N models (different methods or just different hyperparameters), each model will have its own CV score. You can just pick one with the highest score. In this example, the risk of overfitting is much less compared to just using the canonical validation set provided by numerai because your selected model performs the best among all validation sets rather than just one. Does that make sense to you?

---

### Post #20 — **dzheng1887** | 2022-01-24 16:22 UTC _(reply to #19)_

Yes, I understand what you are mentioning. But the risk is in expectation. For the CV to make a material difference from the training test split, the sample sizes would need to be small.

I would think a sufficiently large training test split would be approximately close enough. But I will test it myself. I’ll bootstrap the metrics with various 80/20 splits and see it’s volatility. Perhaps for reasons you state, low signal to noise ratio and just crazy volatility and non iid observations in both time and asset, so millions of observations are not sufficient.

It is possible, but my prior belief is that it is unlikely in this circumstance. Regardless, thank you for this discussion. I can report back results from the bootstrap later this week.

---

### Post #21 — **maxchu** | 2022-01-24 23:42 UTC _(reply to #20)_

So, correct me if I am wrong, you are saying that the sample size for numerai is too large so CV will not be worth it as it wastes a lot of compute?

---

### Post #22 — **dzheng1887** | 2022-01-25 00:27 UTC

Perhaps, that is my initial reaction. Do you find otherwise? I will see soon with the bootstrap.

Not just that it’s too big to compute, but how do you handle the panel data correlations (era and firms) in the training data when you split it up? (two questions earlier) I couldn’t work that out either and have found that my validation using the training data was always more optimistic than my validation using the given validation data.

---

### Post #23 — **johnnywhippet** | 2022-01-25 13:35 UTC

have you tried stacking them?

---

### Post #24 — **dzheng1887** | 2022-01-25 14:15 UTC _(reply to #23)_

Not sure how stacking them would help. Do you guys understand why having repeated observations in different folds is weird?

---

### Post #25 — **dzheng1887** | 2022-01-25 15:48 UTC

Here are the results from the bootstrap. The min/max difference from one fold compared to all folds combined is +/- 0.007 corr, which is not small. (all numbers are corr)

The mean/stds for all folds combined (100 trials) is 0.04646 and 0.0004. The mean/stds for the 500 individual folds is 0.04655 and 0.0026.

The 2 std range for all folds combined [0.04564, 0.04728]. The 2 std range for 500 individual folds [0.04128, 0.0518].

Here is the code if anyone would want to try with another model to compare results. I don’t want to keep running this (and I only have one main model right now), but I would be curious how often the decision choice for the model varies with these metrics over the bootstrap. I posted the data in the next message.
    
    
    from numerapi import NumerAPI
    import pandas as pd
    import numpy as np
    import xgboost as xgb 
    import json 
    from utils import get_latest_round_data, load_data, numerai_score
    import time
    import random
    
    napi = NumerAPI()
    current_round = napi.get_current_round(tournament=8)  
    folder_path = 'round'+str(current_round)
    get_latest_round_data(folder_path)
    
    train_data = load_data(folder_path, 'training')
    valid_data = load_data(folder_path, 'validation')
    
    targets = [i for i in train_data.columns if i[0:7] == 'target_']
    with open(folder_path+"/features.json", "r") as f:
        feature_metadata = json.load(f)
    features = feature_metadata['feature_sets']
    features['all'] = [i for i in train_data.columns if i[0:7] == 'feature']
    
    train_data = pd.concat((train_data,valid_data))
    train_data['erano'] = train_data['era'].astype(int)
    
    eras = np.unique(train_data['erano'])
    keep_eras = [i for i in range(max(eras)) if (i-1) % 4 == 0]
    eras = list(set(eras).intersection(set(keep_eras)))
    eras.sort()
    
    train_data = train_data.loc[train_data['erano'].isin(eras)]
    
    param = {}
    target = 
    feature_set = 
    num_round =
        
    ii = 100
    jj = 5
    results = np.ndarray((ii,1+jj+1))
    for i in range(ii):
        
        start = time.time()
        
        random.seed(i)
        fold_ids = [int(random.random()*5) for i in range(train_data.shape[0])]
        
        all_preds = pd.DataFrame()
        
        for j in range(jj):
            
            train_fold_data = train_data.loc[[ids != j for ids in fold_ids]]
            valid_fold_data = train_data.loc[[ids == j for ids in fold_ids]]
            
            dtrain = xgb.DMatrix(train_fold_data.loc[:,features[feature_set]], 
                                 label = train_fold_data.loc[:,target])
            dvalid = xgb.DMatrix(valid_fold_data.loc[:,features[feature_set]], 
                                 label = valid_fold_data.loc[:,target])
            
            bst = xgb.train()
        
            preds = bst.predict(dvalid)
            preds = pd.DataFrame(preds, index=valid_fold_data.index)
            corr = numerai_score(valid_fold_data['target'], 
                                 preds, 
                                 valid_fold_data['era'])
    
            results[i,0] = i
            results[i,1+j] = corr
                  
            all_preds = pd.concat((all_preds,preds))
                
        all_preds['target'] = train_data['target']
        all_preds['era'] = train_data['era']
        corr = numerai_score(all_preds['target'], all_preds[0],all_preds['era'])
        
        results[i,1+jj] = corr
    
        # print(i,
        #       " ".join(results[i,:].round(4).astype(str)), 
        #       round((time.time()-start)/60))
    
    

In here, I even divided up the eras into 4 to avoid that overlapping weekly-month era problem. So if you want to train on all data with CV, it’ll even be 20 models with k=5 fold. The 0.045 corr is about what I was getting before when I was looking at training validation numbers and is always higher than my 0.02 to 0.03 diagnostic validation metric. I assume it is because of autocorrelation in the assets over time which I am unable to identify and handle in the cross validation with the data given. But regardless of the metric inflation, perhaps the model choice decision would be consistent even if we were able to properly cross validate across different assets as well.

---

### Post #26 — **dzheng1887** | 2022-01-25 15:57 UTC _(reply to #25)_

trail,fold1,fold2,fold3,fold4,fold5,all
    0,0.0454512,0.0463021,0.0481612,0.0475084,0.046036,0.0465768
    1,0.0461641,0.0426798,0.0488758,0.0466342,0.0485836,0.046368
    2,0.0481643,0.0473197,0.0450287,0.0465363,0.046393,0.0466854
    3,0.0467998,0.0498067,0.0473212,0.0443931,0.0456131,0.0465906
    4,0.0454342,0.0471746,0.0467139,0.0508233,0.0451697,0.0470217
    5,0.0430922,0.042396,0.0483958,0.047381,0.0513269,0.0464404
    6,0.0494867,0.0431321,0.0475262,0.0469005,0.0448159,0.0461766
    7,0.0479359,0.0458342,0.0472137,0.0416656,0.0514214,0.0466997
    8,0.0490363,0.0501262,0.0415602,0.0432651,0.0507932,0.0469314
    9,0.0526103,0.0439338,0.0447898,0.0456008,0.0463078,0.0466632
    10,0.0478756,0.0439681,0.0475459,0.0455541,0.0466427,0.0461699
    11,0.0453465,0.0463051,0.0492987,0.0449121,0.0424048,0.0455972
    12,0.0486342,0.0460027,0.0459584,0.0411065,0.0522588,0.0467448
    13,0.0468255,0.0491371,0.0439315,0.0444841,0.0478756,0.0464577
    14,0.0470846,0.0489082,0.0488789,0.0463103,0.0433617,0.046888
    15,0.048792,0.0433608,0.0462839,0.0492664,0.047397,0.0469982
    16,0.046701,0.0435104,0.049601,0.0505646,0.0423483,0.0464501
    17,0.046993,0.0455555,0.0433257,0.0480617,0.0459516,0.0459497
    18,0.0474933,0.0456222,0.0480716,0.0471274,0.0445115,0.0465076
    19,0.0444521,0.0450144,0.0467531,0.0478124,0.0470413,0.0461556
    20,0.0493849,0.0441109,0.0487016,0.047246,0.0450537,0.0468194
    21,0.049017,0.0482838,0.0446609,0.0440899,0.0440323,0.0459504
    22,0.0480687,0.0507559,0.0459764,0.0435936,0.0483386,0.0472242
    23,0.0417204,0.0477246,0.0448494,0.052641,0.0459125,0.0464731
    24,0.0409186,0.0485285,0.0479908,0.0513518,0.0453517,0.0467985
    25,0.0483,0.0482696,0.0511694,0.0442082,0.0418532,0.0466986
    26,0.0510052,0.046943,0.0444164,0.0424078,0.0437092,0.0455664
    27,0.0484662,0.0475047,0.0442272,0.0450285,0.0475818,0.0465954
    28,0.0473677,0.0469808,0.0442228,0.0471263,0.0457046,0.0462523
    29,0.0470475,0.0424258,0.0441187,0.0494812,0.048361,0.0462131
    30,0.0450089,0.0481456,0.0483964,0.0430841,0.0467578,0.0462786
    31,0.044192,0.0468426,0.0470397,0.0469078,0.0470955,0.0464195
    32,0.0498815,0.0471341,0.0424716,0.0479667,0.045624,0.0465243
    33,0.0407067,0.0484569,0.0473392,0.0475696,0.0462711,0.0458958
    34,0.0505618,0.0470625,0.0443338,0.0482,0.0453517,0.0471104
    35,0.0483278,0.0494009,0.0426818,0.0481715,0.0442333,0.0465486
    36,0.0472073,0.0481577,0.0446825,0.044485,0.0467739,0.0461266
    37,0.043594,0.0463735,0.0477529,0.0479444,0.0445199,0.046037
    38,0.0446921,0.0461256,0.0466182,0.0446218,0.0487841,0.0461291
    39,0.0458596,0.045189,0.0473348,0.0474093,0.0493812,0.0471188
    40,0.0477954,0.0431284,0.0492554,0.0464612,0.0459006,0.0462556
    41,0.0435226,0.0465053,0.04756,0.0447214,0.0473549,0.0459075
    42,0.045941,0.0433099,0.0459535,0.0446809,0.0532554,0.0463989
    43,0.047135,0.0436759,0.0438512,0.0480062,0.049624,0.0464179
    44,0.0492976,0.0492129,0.0436938,0.0452712,0.0456339,0.046624
    45,0.0516194,0.0471187,0.0473453,0.041776,0.047129,0.046929
    46,0.0433419,0.0480354,0.0495389,0.0470666,0.0476467,0.0469895
    47,0.0465759,0.0481465,0.0505586,0.0451065,0.0456455,0.0472998
    48,0.0465002,0.051564,0.0451451,0.0474905,0.0424634,0.0465274
    49,0.0468831,0.0457768,0.0450393,0.0490985,0.0487772,0.0469825
    50,0.0417888,0.0455056,0.0509021,0.047003,0.0454096,0.0460697
    51,0.0442714,0.0478697,0.0424965,0.0521136,0.0460873,0.0465415
    52,0.0495826,0.0458567,0.0497032,0.0459093,0.0432857,0.0467512
    53,0.0408756,0.0462859,0.0507189,0.0445478,0.0495572,0.0462834
    54,0.0519681,0.0425537,0.0494473,0.0458247,0.0441632,0.0466197
    55,0.0459439,0.042358,0.0503978,0.0500509,0.0442735,0.0465332
    56,0.0462911,0.044802,0.0478479,0.0460618,0.0455183,0.0459834
    57,0.0472916,0.0513738,0.0505625,0.0415692,0.044628,0.0469703
    58,0.048421,0.0464198,0.0467036,0.0431291,0.0459133,0.0461762
    59,0.0466142,0.0460279,0.045562,0.0396132,0.0483752,0.0451058
    60,0.0485735,0.0397927,0.0538569,0.0487737,0.0444589,0.0469261
    61,0.0491468,0.0451239,0.0462121,0.0419088,0.0477186,0.0459002
    62,0.0430902,0.04388,0.0505072,0.0450501,0.0479288,0.0460039
    63,0.0464864,0.0484427,0.0474004,0.0460825,0.0419726,0.046067
    64,0.0448574,0.0442045,0.0498019,0.0502939,0.0467484,0.0469565
    65,0.0487501,0.0436807,0.047649,0.0479983,0.0451955,0.0466779
    66,0.0472595,0.0457648,0.0502793,0.0445404,0.0450672,0.0465302
    67,0.0466916,0.0491404,0.0446774,0.0429084,0.0483207,0.0460811
    68,0.049345,0.0484095,0.0444826,0.0479081,0.0453472,0.0468229
    69,0.0465495,0.0487521,0.0448203,0.0447768,0.0458559,0.0459055
    70,0.0449307,0.049067,0.0444911,0.04666,0.0428952,0.0455729
    71,0.0497617,0.0482966,0.0451918,0.0450548,0.0460682,0.0466547
    72,0.0421529,0.0503088,0.0455051,0.0466188,0.0480857,0.0465094
    73,0.0477716,0.0497149,0.0470153,0.0430442,0.0419668,0.0459256
    74,0.0400881,0.0487076,0.0455716,0.0499832,0.0498025,0.0467876
    75,0.0521937,0.0469653,0.0440891,0.041514,0.0477371,0.0463776
    76,0.0506272,0.0501738,0.0410215,0.0441536,0.0476548,0.0466554
    77,0.0480731,0.0473878,0.0502569,0.0424778,0.0466857,0.0468076
    78,0.0443044,0.0454224,0.0450349,0.0455673,0.0494592,0.0458684
    79,0.0509537,0.0440325,0.043193,0.0495951,0.0446791,0.0463975
    80,0.0457146,0.0482137,0.0431033,0.0463431,0.0503114,0.0465895
    81,0.0444321,0.0542167,0.0484362,0.0419455,0.0445467,0.0466185
    82,0.0463462,0.0444241,0.0520595,0.0444156,0.044644,0.0464431
    83,0.0443932,0.0497169,0.0458551,0.0443577,0.0497161,0.0466788
    84,0.0497253,0.0410755,0.0491929,0.0506663,0.0423233,0.0464948
    85,0.0461457,0.0457695,0.0468747,0.0484608,0.048471,0.0471038
    86,0.0434023,0.0473817,0.0464394,0.0480758,0.0493162,0.0469385
    87,0.0440076,0.0410904,0.0478069,0.0508067,0.0483574,0.0462676
    88,0.0469968,0.04731,0.0437514,0.0460746,0.0489373,0.0465023
    89,0.0435701,0.0490209,0.0476565,0.048394,0.0443097,0.0464222
    90,0.0467009,0.0531009,0.0454824,0.0421911,0.0467472,0.046691
    91,0.0447045,0.0481898,0.0485401,0.0447496,0.0465588,0.046507
    92,0.0470614,0.0443226,0.0477666,0.0474712,0.0450678,0.0463706
    93,0.0446403,0.0448446,0.0491012,0.0468921,0.0439495,0.0457443
    94,0.0545186,0.0467705,0.0475951,0.0423732,0.0440008,0.0469763
    95,0.0427576,0.0482073,0.0501902,0.0412603,0.0497724,0.0464288
    96,0.0489274,0.0407707,0.047828,0.0465981,0.0488622,0.0463332
    97,0.046451,0.0492799,0.047756,0.0451662,0.047543,0.0471633
    98,0.0449395,0.0422609,0.0486628,0.0502684,0.0453263,0.0461156
    99,0.0475424,0.0434008,0.0463483,0.0448359,0.0490639,0.0462389

---

### Post #27 — **johnnywhippet** | 2022-01-25 16:21 UTC _(reply to #24)_

You won’t know unless you give it a try. It’s helped some of my models.

---

### Post #28 — **dzheng1887** | 2022-01-25 16:43 UTC _(reply to #27)_

Sorry man, not sure what you are referring to

---

### Post #29 — **adalseno** | 2022-01-25 19:38 UTC _(reply to #25)_

Hi [@dzheng1887](</u/dzheng1887>) , I’m a little bit puzzled about your code.  
You split the dataframe in 1/4 and took one era (and that’s fine, providing you do the training also for the other 3).  
What it’s not clear to me is the split between training and validation data. I mean you made a completely random split of about 80/20 but without taking into account eras so your training and validation data are completely messed up (and, IMHO, it’s not what you’d want for a time series). I think you’d better follow some kind of “era wise kfold” as suggested [here](<http://forum.numer.ai/t/era-wise-time-series-cross-validation/791/24>) in the forum. What do you think?

---

### Post #31 — **maxchu** | 2022-01-25 20:46 UTC _(reply to #26)_

Definitely, the sample size is not large (it will never be enough for this kind of data I guess). When I say not enough, I mean whatever models you use, the training and validation result difference is huge.  
Also, you will notice that the validation result is more or less the same even if you downsample the row for training (say, every 20th row, so the sample size is reduced to only 1/20). I think it is because the era-effect is stronger than individual stock information when it comes to measuring era-wise corr as our tournament goal. So, I would say the “effective sample size” is the number of eras we have in our training set (which is very small). If you tried training a very shallow deep learning before, you will notice that the validation will go up at around after one epoch (reasonably high learning rate), which I haven’t seen in my other deep learning project even with much deeper models.

---

### Post #32 — **dzheng1887** | 2022-01-26 04:58 UTC _(reply to #29)_

Hey adalseno, thank you for the message. That definitely would seem to alleviate some of my concern about any autocorrelation between eras for a given firm. But besides the full training vs validation split, I would think there is still some leakage. I will take a look and give it some more thought.

---

### Post #33 — **dzheng1887** | 2022-01-26 05:07 UTC _(reply to #31)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/dec6dc/48.png) maxchu:

> h row, so the sample size is reduced to only 1/20). I think it is because the era-effect is stronger than individual stock information when it comes to measuring era-wise corr as our tournament goal. So, I would say the “effective sample

Ah, that is an interesting thought. In such a case, would you then expect model degradation if you remove say 300 of the 600 training eras? But there is no model degradation when you remove half of the stocks in each era? And then you do well in the validation period if the eras you have in the training sample is representative of the type of eras in validation?

I have not yet tried a deep learning model yet. I am thinking of implementing somethings Bayes like though. I like Bayes ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) But I do plan to one day try some deeper models and I will look for that as well.

---

### Post #34 — **dzheng1887** | 2022-01-26 06:22 UTC _(reply to #29)_

I like this technique, it will definitely help with the autocorrelation between eras. Not sure optimal gapping though  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/735ac805ebaf1fb78da78ddd7251be579c733d6c_2_690x182.png)image696×184 26 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/735ac805ebaf1fb78da78ddd7251be579c733d6c.png> "image")

---

### Post #35 — **kenfus** | 2022-01-26 08:03 UTC _(reply to #34)_

I have a model with the sliding window and one with the expending window. Currently, it seems the expanding window is better

---

### Post #36 — **adalseno** | 2022-01-26 14:58 UTC _(reply to #33)_

It happened to me that some models do not learn at all and the final score is almost equal as predicting the simple mean, using `rmse` as loss/scoring function. So no wonder that, in such a situation, removing some rows or changing the sample size (or eras distribution) does not affect the performance (and if it does it’s purely by chance). Simply there is no performance at all. Check it out if it’s your case too.

---

### Post #37 — **restrading** | 2022-01-26 15:57 UTC _(reply to #36)_

Predictions are ranked first before scored, it does not matter in absolute value how much they deviate from 0.5.

---

### Post #38 — **adalseno** | 2022-01-26 17:23 UTC _(reply to #37)_

You may be right, but what I saw is that the model does not converge (it does not learn) so it’s simply not working (at least using `rmse` as loss/metric). In such a situation the more you train the more you overift. You may get decent scores with ensemble (especially using different targets), but essentially you are just getting there by chance not because the model has learnt (you are averaging a bunch of simple means, if the models are not learning).

I tried also to use Spearman as metric/loss but the results, for now, are not encouraging.

On the other hand, as far as I could see, the dataset is a Time Series (from eras point of view), but actually it’s NOT a Time Series since every id is unique so we don’t really have different values over time (therefore no trend, seasonality and so on). A big dilemma, isn’t it?

---

### Post #39 — **dzheng1887** | 2022-01-26 18:01 UTC _(reply to #37)_

Yes I was thinking similarly, the metric is the within era asset raking

---

### Post #40 — **dzheng1887** | 2022-01-26 18:03 UTC _(reply to #38)_

Yes, that is what I was perplexed about too. The era wise CV may correct for it, but we just don’t know how much leakage is occuring if we don’t understand the firm’s autocorrelation between eras. Don’t know how much gap you need to be comfortable no leakage occurs. It’s really a panel dataset but the asset ids are mixed

I imagine a year is probably enough for momentum?

---

### Post #41 — **restrading** | 2022-01-27 01:28 UTC _(reply to #38)_

The term “almost equal as simple mean” does not apply because predictions are ranked, so long as they are not actually a constant, there will be a ranking and the model learns if it produces reasonable ranking performance.

The tournament by design prevents users from modeling time series. Time series info is embedded in the features given to you.

---

### Post #42 — **adalseno** | 2022-01-27 17:17 UTC _(reply to #41)_

Yes, the tournament is designed to prevent you from modelling time series, that’s why I said that it’s actually NOT a time series.

From my point of view, time series features (lag, rolling, expanding and so on so forth) have a meaning as long as you can sort them (and learn from them), otherwise they have little use.

I’m not saying one can’t find decent models but, in my opinion, the models are not learning enough to be reliable (for a reasonable long time at least).

This one, for example, doesn’t look bad, but it’s not based enough on learning IMHO! So I don’t like it.  


[![Schermata 2022-01-27 alle 18.09.33](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26fdaa2696eb2dc7178a93a05c576e549f09db6f_2_690x368.png)Schermata 2022-01-27 alle 18.09.331338×714 63.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/26fdaa2696eb2dc7178a93a05c576e549f09db6f.png> "Schermata 2022-01-27 alle 18.09.33")

PS Don’t look at color codes (they are based on old values found here on the forum and they are not up to date), nor to autocorrelation score (I haven’t yet found a way to properly calculate it; any hint is more than welcome).

---

### Post #43 — **wigglemuse** | 2022-01-27 18:58 UTC _(reply to #42)_

Not quite following this “the model isn’t learning” stuff – the final result is the same as the simple mean of what?

---

### Post #44 — **adalseno** | 2022-01-27 21:01 UTC _(reply to #43)_

I’m referring to the fact that using `rmse` the loss (the validation loss) does not converge or improves significantly as compared to the loss using the simple mean as prediction: `rmse(y_true, model_predictions)` ≈` rmse(y_true, [y_mean]*len(y_true))`

For the model to learn, you’d expect the loss to decrease (with few or more swings, towards zero, the ideal point) but it does not. It just floats around.

Here an example of what I mean:
    
    
    [LightGBM] [Info] Start training from score 0.500017
    [1]	valid_0's l2: 0.0499796
    Training until validation scores don't improve for 100 rounds
    [2]	valid_0's l2: 0.0499781
    [3]	valid_0's l2: 0.0499767
    [4]	valid_0's l2: 0.0499762
    [5]	valid_0's l2: 0.0499784
    [6]	valid_0's l2: 0.0499737
    [7]	valid_0's l2: 0.0499731
    [8]	valid_0's l2: 0.0499751
    [9]	valid_0's l2: 0.0499735
    [10]	valid_0's l2: 0.0499729
    [11]	valid_0's l2: 0.0499721
    [12]	valid_0's l2: 0.0499703
    [13]	valid_0's l2: 0.0499686
    [14]	valid_0's l2: 0.0499695
    [15]	valid_0's l2: 0.0499722
    [16]	valid_0's l2: 0.0499722
    [17]	valid_0's l2: 0.0499715
    [18]	valid_0's l2: 0.0499683
    [19]	valid_0's l2: 0.0499679
    [20]	valid_0's l2: 0.0499659
    [21]	valid_0's l2: 0.0499662
    [22]	valid_0's l2: 0.0499669
    [23]	valid_0's l2: 0.0499665
    [24]	valid_0's l2: 0.0499663
    [25]	valid_0's l2: 0.0499652
    ...
    [124]	valid_0's l2: 0.0500266
    [125]	valid_0's l2: 0.0500285
    Early stopping, best iteration is:
    [25]	valid_0's l2: 0.0499652
    

Get the simple mean error, score it and find the difference with the model:
    
    
    simple_mean = validation_data[target].mean()
    simple_preds = [simple_mean]*len(validation_data)
    simple_rmse = mean_squared_error(validation_data[target], simple_preds)
    print(f"simple_rmse: {simple_rmse}")
    model_rmse = mean_squared_error(validation_data[target],sel_preds)
    print(f"model_rmse: {model_rmse}")
    print('Difference:', "{:.2%}".format((simple_rmse-model_rmse)/simple_rmse))
    
    simple_rmse: 0.04998767748475075
    model_rmse: 0.04997043677304045
    Difference 0.03%

---

### Post #45 — **wigglemuse** | 2022-01-27 21:21 UTC _(reply to #44)_

Ok, so you’re saying the results you get loss-wise are pretty much the same as if the model just outputted nothing but 0.5 for every row, eh? Got it. Although ranking those same results may tell a different story, i.e. couldn’t it be that it is ranking ok (keeping in mind +0.03 corr on val is very good) but with just a very small spread? (If you see no changes in training then probably not, but ranking is the game after all.)

---

### Post #46 — **dzheng1887** | 2022-01-27 21:33 UTC _(reply to #44)_

I think that is perhaps because a large percentage of the stocks are at the 0.5 target level which does very well with a mean guess. I didn’t gave it too much consideration yet, but was thinking of removing that group of neutral stocks to see how well it does on the tails instead.

---

### Post #47 — **adalseno** | 2022-01-27 21:41 UTC _(reply to #45)_

yes, the actual score of the model, after ranking, is way better than the average one, but usually you’d expect to have a decent decrease in the loss for a reasonable number of rounds (the model is learning) and then an increase (it’s overfitting). This is one of the metric plot (validation; as you see the model starts overfitting almost immediately):  


[![Schermata 2022-01-27 alle 22.34.20](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ad4e11f81fa8a3d322d47120f48d3c76054257f2.png)Schermata 2022-01-27 alle 22.34.20461×299 14.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ad4e11f81fa8a3d322d47120f48d3c76054257f2.png> "Schermata 2022-01-27 alle 22.34.20")

It is also true that the target has “just” five values: [0.0, 0.25, 0.5, 0.75, 1.0] in fact I’ve also tried a couple of classification models, but without great results ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=13)
