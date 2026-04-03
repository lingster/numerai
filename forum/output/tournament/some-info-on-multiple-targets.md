---
title: "Some info on multiple targets?"
category: Tournament
url: https://forum.numer.ai/t/some-info-on-multiple-targets/5606
created_at: 2022-07-28T06:30:46.754000+00:00
last_posted_at: 2022-09-20T08:31:56.330000+00:00
posts_count: 11
views: 1643
tags: []
---

# Some info on multiple targets?

---

### Post #1 — **taori** | 2022-07-28 06:30 UTC

I didn’t find much information (nothing at all) regarding the multiple targets in the official documentation. I would like to know in which way they differ (except the 20 vs 60 days difference, which is clear). Does anybody know something on this topic? Thanks.

---

### Post #2 — **wigglemuse** | 2022-07-28 13:21 UTC

Nobody knows! They are neutralized to different things and some such is about all the explanation we’ve gotten. Testing shows that at least several of them are pretty useful though.

---

### Post #3 — **autratec** | 2022-07-29 03:27 UTC

you might come out your own assumption and test whether it aligned with the target they provided. let’s say market moving up more than 1% with 0.75 and move down 1% with 0.25.

---

### Post #4 — **taori** | 2022-08-25 21:37 UTC

[This](<http://forum.numer.ai/t/generating-feature-groups/4744/12>) post made me curious and so here is the correlation matrix between targets and the dendrogram to better highlight relationships.

[![Figure_1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/404b87d1da36118ebc3260966cb8d5c6bccdb96b_2_640x500.png)Figure_11123×876 223 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/404b87d1da36118ebc3260966cb8d5c6bccdb96b.png> "Figure_1")

[![Figure_2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d5de53d8e61894c470ab6e416029f5e1e706db4d_2_511x500.png)Figure_21000×978 66.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d5de53d8e61894c470ab6e416029f5e1e706db4d.png> "Figure_2")

Here is the code.
    
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    
    targets = [
        'target_nomi_v4_20',
        'target_nomi_v4_60',
        'target_jerome_v4_20',
        'target_jerome_v4_60',
        'target_janet_v4_20',
        'target_janet_v4_60',
        'target_ben_v4_20',
        'target_ben_v4_60',
        'target_alan_v4_20',
        'target_alan_v4_60',
        'target_paul_v4_20',
        'target_paul_v4_60',
        'target_george_v4_20',
        'target_george_v4_60',
        'target_william_v4_20',
        'target_william_v4_60',
        'target_arthur_v4_20',
        'target_arthur_v4_60',
        'target_thomas_v4_20',
        'target_thomas_v4_60']
    
    # analyse the validation data, but we could do the same on the training data
    df = pd.read_parquet('v4/validation.parquet', columns=targets + ['era'])
    
    # compute the mean of the era correlation of every target with any other target
    corr = df.groupby('era').corr(method='spearman').mean(axis=0, level=1)
    
    # arrange the order of the columns and rows (for visualization) so that they
    # are sorted by correlation with the target 'target_nomi_v4_20' 
    corr = corr.sort_values(
        'target_nomi_v4_20',
        axis=0,
        ascending=False).sort_values(
            'target_nomi_v4_20',
            axis=1,
        ascending=False)
    
    sns.heatmap(corr, annot=True)
    plt.show()
    
    sns.clustermap(corr)
    plt.show()

---

### Post #5 — **ryo_matsuzaka** | 2022-09-19 22:57 UTC

Sorry, it could be a basic question but I don’t understand why there are multiple targets…  
When doing training and prediction, we need to choose a target.

For example, the example code chooses a “target_nomi_v4_20”.

[github.com](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L10>)

#### [numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L10](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L10>)
    
    
          
    
    
              
        1. import numpy as np
    
              
        2. import pandas as pd
    
              
        3. import scipy
    
              
        4. from halo import Halo
    
              
        5. from pathlib import Path
    
              
        6. import json
    
              
        7. from scipy.stats import skew
    
              
        8. 
                   
    
    
        9. ERA_COL = "era"
    
              
        10. TARGET_COL = "target_nomi_v4_20"
    
              
        11. DATA_TYPE_COL = "data_type"
    
              
        12. EXAMPLE_PREDS_COL = "example_preds"
    
              
        13. 
                   
    
    
        14. spinner = Halo(text='', spinner='dots')
    
              
        15. 
                   
    
    
        16. MODEL_FOLDER = "models"
    
              
        17. MODEL_CONFIGS_FOLDER = "model_configs"
    
              
        18. PREDICTION_FILES_FOLDER = "prediction_files"
    
              
        19. 
                   
    
    
        20. 
               
    
    
    
        

But I don’t understand why “target_nomi_v4_20” is chosen.  
How could it be selected? Is there any rule or a criteria?

---

### Post #6 — **thedarklord** | 2022-09-20 01:38 UTC _(reply to #5)_

As I far as I understand, we are trying to predict the ‘target’. However, the other targets provided can do a better job at the predicting the ‘target’ than the ‘target’ itself. Sounds confusing, right? Basically, it means we can use one of other targets, say ‘target_nomi_v4_20’ to train the model. And them use the trained model, which was trained using ‘target_nomi_v4_20’ as Y, to predict ‘target’.

---

### Post #7 — **ryo_matsuzaka** | 2022-09-20 02:02 UTC _(reply to #6)_

Yes, it is very confusing…  
But now I understood it. I will play with those targets.  
Thank you very much.

---

### Post #8 — **ryo_matsuzaka** | 2022-09-20 02:11 UTC

Sorry, but still I don’t understand the targets.  
Targets consists of the limited sets of discrete numbers.  
So I will use classifier not regresser for predictions.  
But then some targets(`target_brabra`) don’t have the value in the `target`.

---

### Post #9 — **wigglemuse** | 2022-09-20 02:15 UTC

target_nomi_v4_20 actually is the “target” that we are scored on (for correlation). But sounds like they have their sights on jerome_60 for the future maybe. (20 = day targets, 60 = 60 day targets).

And the targets are in buckets just like the features (except the distributions are different). In most cases you’ll find a regression approach working better – at least for getting correlation. (Your submission should be real-valued – not just the 5 buckets. We are scored on ranking/ordering, not actual values.)

It should be pointed out that TC evaluation is based on portfolio returns of your model vs others and so kinda doesn’t have a fixed target. Another reason to mix it up.

---

### Post #10 — **ryo_matsuzaka** | 2022-09-20 02:24 UTC _(reply to #9)_

[@wigglemuse](</u/wigglemuse>)  
Thank you very much for the information and advice.  
I completely understand it.

> In most cases you’ll find a regression approach working better – at least for getting correlation. (Your submission should be real-valued – not just the 5 buckets. We are scored on ranking/ordering, not actual values.)

I agree with you.

---

### Post #11 — **taori** | 2022-09-20 08:31 UTC _(reply to #10)_

[@ryo_matsuzaka](</u/ryo_matsuzaka>) Just to make your life easier, train your model multiple times, each time with a different target. Then create one model slot in your numer.ai account for each target so that you can submit the predictions coming from models trained on different targets to different slot. Then observe which target gives you better results and stake on it.
