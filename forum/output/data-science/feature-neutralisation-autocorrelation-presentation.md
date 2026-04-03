---
title: "Feature Neutralisation & Autocorrelation Presentation"
category: Data Science
url: https://forum.numer.ai/t/feature-neutralisation-autocorrelation-presentation/2341
created_at: 2021-03-13T18:48:15.720000+00:00
last_posted_at: 2022-06-15T13:55:56.216000+00:00
posts_count: 6
views: 3282
tags: []
---

# Feature Neutralisation & Autocorrelation Presentation

---

### Post #1 — **rsmillie94** | 2021-03-13 18:48 UTC

Hello! Just making a post to go along with the OHwA interview.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/75fe2466497db3804444db4c3eefea3e7b2a1679_2_690x426.png)image1164×720 85.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/75fe2466497db3804444db4c3eefea3e7b2a1679.png> "image")

First I wanted to talk about feature neutralisation. In the picture above the X axis represents the value of a dummy feature and the Y axis represents the predicted value, the blue line represents the original unmodified model fitted to this data. You can see that the original prediction is heavily modified when performing feature neutralisation; the prediction changes from a strictly monotonically increasing function to a function which is decreasing for 80% of the values. To me this is something which we would not want in our modelling.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e446a3ab2950fddd20c75504668ac103061e1afc_2_690x426.png)image1164×720 91 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e446a3ab2950fddd20c75504668ac103061e1afc.png> "image")

In the next image we see a symmetric prediction. For this kind of prediction feature neutralisation changes nothing about the rank of the predictions for the values of the dummy feature and so does not perform any kind of risk avoidance. I see no reason why this kind of prediction would be deemed less risky than the first and yet feature neutralisation does nothing to address this.

To address both of these concerns I propose a new method, I will call this one hot exposure clipping (not very catchy so I’m very open to new names). The idea behind this is to make new features which represent the non linear predictions of particular features we deem ourselves to be overexposed to and neutralise based on these rather than the original features. I’m working on a prototype for this and will explain further in a future post.

Lastly I want to briefly mention autocorrelation, or how to predict when a feature will perform well. Below you see two histograms, the left represents the autocorrelations of 310 random number sequences, the right represents the autocorrelations of sequences derived by calculating the correlation of each of the 310 Numerai feature columns with the target for each training round. As you can see there is not much difference, this is presented to warn against assuming you have found a particular feature to be autocorrelated just because you have a statistically significant result. I still believe there may be some way to predict when a feature is going to do well but there is much more work to do.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/21d35ae42f6661993313250347981c94ff9c813b_2_690x392.png)image1188×675 49.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/21d35ae42f6661993313250347981c94ff9c813b.png> "image")

Thanks for reading and happy modelling!

---

### Post #2 — **one5hot76** | 2021-05-14 22:38 UTC

Can you clarify what you mean by “feature neutralization”? At first I thought you were talking about normalizing data, but then I remembered that NumerAI data is already between 0 and 1.

---

### Post #3 — **themicon** | 2021-05-15 03:36 UTC

[@one5hot76](</u/one5hot76>) You can find the answers here: [What exactly is neutralization?](<http://forum.numer.ai/t/what-exactly-is-neutralization/2016>)

---

### Post #4 — **kideacreat012** | 2021-05-17 02:32 UTC

Ah an excellent notion that imposes much inquisitiveness which helps drive discussion. I am impressed by the connotations. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #5 — **lingzhou125** | 2021-05-17 03:59 UTC

In your first example, are you neutralizing 1 feature out of 310 and then training the model? If so, the result is not surprising especially if it’s a heavily exposed feature. If you have 2 features, one that causes the target to go up and another that causes the target to go proportionally down. ‘neutralizing’ one of the features would cause the target to flip right? A bit more detail about that first graph is needed.

---

### Post #6 — **bor1** | 2022-06-15 13:55 UTC

I have been using a variant based on [@rsmillie94](</u/rsmillie94>) 's original script, that I can share here. It does the conversion to one-hot encoding and then sequentially neutralizes the predictions for the all features in feature_cols.

My current incarnation is highly inefficient, but time is cheap.

Here is how I use it to get to a fully neutralized version. The idea of the ever-increasing neutralization is to first neutralize the most-exposed features (above 0.15 here), then the less-exposed features (0.14, 0.13), all the way down to whatever level you want. There is probably better ways to do this, as some of [@mdo](</u/mdo>) 's and [@jrb](</u/jrb>) 's code probably does the transformation at once.

put the following in a batch file, adapt to your situation and run it:

> python.exe onehot_neut_shuffle.py …/results/BOR_onehotmonkey_geoburn.csv …/data/tournament_int8.parquet 0.15 BOR_ONEHOTMONKEY_OHN_15.csv
> 
> python.exe onehot_neut_shuffle.py BOR_ONEHOTMONKEY_OHN_15.csv …/data/tournament_int8.parquet 0.14 BOR_ONEHOTMONKEY_OHN_14.csv
> 
> python.exe onehot_neut_shuffle.py BOR_ONEHOTMONKEY_OHN_14.csv …/data/tournament_int8.parquet 0.13 BOR_ONEHOTMONKEY_OHN_13.csv
> 
> python.exe onehot_neut_shuffle.py BOR_ONEHOTMONKEY_OHN_13.csv …/data/tournament_int8.parquet 0.12 BOR_ONEHOTMONKEY_OHN_12.csv

etc…

The actual code for onehot_neut_shuffle.py is as follows:

> def onehot_neut(preds, tournament_data, cutoff):  
>  preds = (preds-preds.min())/(preds.max()-preds.min())  
>  feature_cols = tournament_data.columns[tournament_data.columns.str.startswith(‘feature’)]
>     
>     
>     shuffledlist = list(range(len(feature_cols)))
>     random.shuffle(shuffledlist) 
>     for i in shuffledlist:  # Added a seed-defined random shuffle of the order in which the columns are processed.
>         feat = feature_cols[i]
>         feat_col = tournament_data[feat]
>         feat_onehot = np.empty((len(tournament_data),5))
>         for j in range(5):
>             feat_onehot[:,j] = feat_col == j/4
>         
>         lin = LinearRegression().fit(feat_onehot,preds)
>         dummy_input = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
>         dummy_output = lin.predict(dummy_input)
>         diff = max(dummy_output) - min(dummy_output)
>         if diff>cutoff:           
>             mult = 1-cutoff/diff
>             preds = preds - mult*lin.predict(feat_onehot)
>               
>             
>         
>     preds = (preds-preds.min())/(preds.max()-preds.min())        
>     return(preds)
>     
> 
> if **name** == ‘**main** ’:
>     
>     
>     #Import Modules
>     
>     import random
>     import sys
>     import pandas as pd
>     import numpy as np
>     from sklearn.linear_model import LinearRegression
>     
>     #Read in arguments
>     
>     predictions_df_fil = sys.argv[1]
>     tournament_data_fil = sys.argv[2]
>     cutoff = float(sys.argv[3])
>     write_file = sys.argv[4]
>     
>     #Extract Dataframes
>     
>     predictions_df = pd.read_csv(predictions_df_fil)
>     tournament_data = pd.read_parquet(tournament_data_fil)
>     predictions = predictions_df.iloc[:, 1]
>     
>     #Perform Neutralisation
>     
>     neut_preds = onehot_neut(predictions, tournament_data, cutoff)
>     
>     #Write Output to CSV
>     
>     neut_preds_df = predictions_df
>     neut_preds_df["prediction"] = neut_preds
>     
>     neut_preds_df.to_csv(write_file, index = False)
>     

The main adaptations I did compared to [@rsmillie94](</u/rsmillie94>)’s original is to shuffle the order in which the script runs through the feature columns. I didn’t like the idea that features were processed in a fixed order. Another thing I did might have been running the script multiple times, with a high feature exposure threshold first, and lower feature exposure thresholds later, rather than go for a low threshold immediately. The idea behind that (I am repeating myself) is that I want to get the high feature exposures out of the way first, and only then adapt the now-changed-because-more-neutral predictions to whatever feature exposure is still in it.
