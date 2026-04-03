---
title: "Feature selection by Marcos Lopez de Prado"
category: Data Science
url: https://forum.numer.ai/t/feature-selection-by-marcos-lopez-de-prado/3170
created_at: 2021-05-02T17:52:44.622000+00:00
last_posted_at: 2024-04-03T03:16:21.468000+00:00
posts_count: 35
views: 8423
tags: []
---

# Feature selection by Marcos Lopez de Prado

---

### Post #1 — **nyuton** | 2021-05-02 17:52 UTC

Hi,

my experiments shows, that there is a hugh potential in reducing the numer of features I use for training. Gains can be as high as +0.5% CORR on the validation set. (Or higher if you do better that I do ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) )

Marcos Lopez de Prado describes the “Mean Descreas Accuracy” algorithm in his book “Advances in Financial Machine Learning”. Here is my code snippet that implements that algorithm.
    
    
    > def MDA(model, features, testSet):
    >     
    >     testSet['pred'] = model.predict(testSet[features])   # predict with a pre-fitted model on an OOS validation set
    >     corr, std = num.numerai_score(testSet)  # save base scores
    >     print("Base corr: ", corr)
    >     diff = []
    >     np.random.seed(42)
    >     for col in features:   # iterate through each features
    > 
    >         X = testSet.copy()
    >         np.random.shuffle(X[col].values)    # shuffle the a selected feature column, while maintaining the distribution of the feature
    >         testSet['pred'] = model.predict(X[features]) # run prediction with the same pre-fitted model, with one shuffled feature
    >         corrX, stdX = num.numerai_score(testSet)  # compare scores...
    >         print(col, corrX-corr)
    >         diff.append((col, corrX-corr))
    >         
    >     return diff
    

Simple, fast, elegant and it improves your models!  
Have fun!

---

### Post #2 — **mrquantsalot** | 2021-05-03 01:17 UTC

I’m confused, it looks like after running this you have list of:

FeatureName  
How much better or worse randomly shuffling FeatureName affects CORR

How do you go about interpreting the results? Do you say something like: “Well, when I randomly shuffle FeatureWisdom13 my CORR on the validation set gets better. Therefore I should exclude it from my final model.”

I think I’m missing something because it seems to me that randomly shuffling an entire column would just make the overall model worse since it’s just adding in random noise.

---

### Post #3 — **nyuton** | 2021-05-03 06:39 UTC _(reply to #2)_

As I understand it, the question is, what happens if you “remove” one feature.  
Shuffling is kind of a “remove”. It doesn’t require re-training, so it’s much faster.  
An shuffling keeps the distribution of that feature.

---

### Post #4 — **paulito** | 2021-05-03 06:48 UTC

Maybe you want to do random sampling, not shuffling?

---

### Post #5 — **nyuton** | 2021-05-03 06:50 UTC _(reply to #4)_

Nope, it’s shuffling!  
Reading the book is highly recommended. I’ve learnt a lot from it.

But obviously this is my interpretation and implementation of what’s in the book…

---

### Post #6 — **paulito** | 2021-05-03 07:26 UTC _(reply to #5)_

Ok I think I get why shuffling could actually work here. The idea is that by shuffling you remove any signal from that feature and observe, whether the optimization metric suffers from that. If not, the feature might be irrelevant. If it does suffer, this feature should be important. You could also do np.random.random or any other method, I guess. It reminds me a lot of [shap · PyPI](<https://pypi.org/project/shap/>).

---

### Post #7 — **lingzhou125** | 2021-05-03 15:34 UTC _(reply to #6)_

my concern with feature engineering in this tournament is that we have no idea what the features are. during a burn, one of the features you’re removing could be the difference between a -20% loss and a -5% loss.

---

### Post #8 — **greenprophet** | 2021-05-03 18:11 UTC

I get this now. Going to be a great idea when the feature list explodes. I was able to just drop one feature and make 310 models and evaluate in less than a day. So that seems better for now. There are some features that really help a lot but almost half the features (150) made corr better when dropped individually. Going to try to make a model dropping the top N worst features. The hurting features don’t lower corr nearly as much as the important features help though. So maybe this is insignificant. But I definitely want to be able to drop or combine features when the expanded set comes out.

---

### Post #9 — **olivepossum** | 2021-05-03 19:07 UTC

Thanks for sharing [@nyuton](</u/nyuton>), really interesting!  
I read that part of the book and had some doubts:

  * At the end of the exercise, I assume you could end up with several shuffled features (all those that make corrX-corr negative)?
  * At first I thought this could lead to higher feature exposure but after thinking it twice, I guess it shouldn’t, as you are just sort of removing (shuffling) features that do not add to corr. Right?
  * Have you tested how consistent it is across eras?



Btw it’s great to have a community to discuss these kind of things! It’s easy to end up with doubts when reading the book.

---

### Post #10 — **nyuton** | 2021-05-03 19:30 UTC _(reply to #9)_

Cross validation looks great.  
Forward testing is in progress…

---

### Post #12 — **javiermoral** | 2021-05-04 06:54 UTC

I implemented this method some time ago and confirm that it slightly improves the boosting models. In my case, I use MDA based on clustering variables to account for multicollinearity.

---

### Post #13 — **minou** | 2021-05-04 08:54 UTC

If I’ve read correctly, this is the “permutation feature importance” method. There’s an implementation in sklearn.
    
    
    from sklearn.inspection import permutation_importance
    

Would be interesting to compare results, and worth trying as dropping even one or two features can make a marked improvement depending on the model.

---

### Post #14 — **jay1100** | 2021-05-04 16:07 UTC

I guess you are doing the following:

  1. select best features based on your validation set with MDA
  2. retrain your model only with the good features
  3. eval the performance on the validation (the same that was used in MDA)



I am wondering if this is leaking information from the validation set into the training and thereby the gain in validation CORR is an overestimation?

---

### Post #15 — **nyuton** | 2021-05-04 16:59 UTC

Hi Jay,

good point, this would be an information leakage.  
But I do this process with all the models of my cross validation set.  
It’s safer that way.

---

### Post #16 — **jay1100** | 2021-05-05 10:50 UTC

Thank you for the clarification.  
So you average the importance scores across all folds, only selecting features which perform well on all folds?  
This will reduce the information leakage but it will not eliminate the leakage completely.

---

### Post #17 — **rpica** | 2021-05-05 10:57 UTC _(reply to #16)_

How about doing this procedure on the training set? Yes, running predictions with training data, but only to check if the performance drops from the starting one (with no shuffling).

If the model is really using the feature, the performance will drop when shuffling that feature. That way there is no leakage.

Is there something obviously wrong with that thought?

---

### Post #18 — **nyuton** | 2021-05-06 20:07 UTC _(reply to #16)_

Yes, I avearage the importance scores across all folds.  
How does it have information leakage?

I’m interested in other points of views!  
It produces such great results, that it’s too good to be true.  
But I don’t see how I leak information…

---

### Post #19 — **nyuton** | 2021-05-06 20:22 UTC _(reply to #13)_

Thanks, for pointing it out. I didn’t know about the sklearn implementation.

---

### Post #20 — **jimmy_woodford** | 2021-05-06 20:25 UTC _(reply to #18)_

If you delete features on training CV and only after that check on val, you should be fine. As long as you check the final performance on a sample you have not optimised the feature selection on.

---

### Post #21 — **jay1100** | 2021-05-07 09:19 UTC

Just to make sure we are talking about the same things. I assume we have a dataset which we split into 5 folds and then we train on 4 folds and validate on 1 fold. We rotate this 5 times to have an entire cross validation.  
If you have information leakage from validation into training in each of the 5 folds, then by averaging your importance scores you are diluting the information leakage, but you do not remove it completely.

I get the following results for 3 different experiments:

  1. Use validation data to get feature importance scores with MDA. Select most important features and retrain. Do this for each fold. Result: corr increases by 0.7% (a lot of leakage)
  2. Use validation data to get feature importance scores with MDA. Average the importance score across all 5 folds. Then select most important features and retrain. Do this for each fold. Result: corr increases by 0.5% (leakage is a bit diluted)
  3. Use training data to get feature importance scores with MDA. Average the importance score across all 5 folds. Then select most important features and retrain. Do this for each fold. Result: corr increases by 0.025% (no leakage for sure)



For these reasons I guess there is still leakage even if you average cross folds.

One thing I did not try is to split the training data into 2 sets. Train on the first set and do MDA on the second set. Then you still have your validation set for a validation without any leakage. Would be interesting to see the results of this.

---

### Post #22 — **jimmy_woodford** | 2021-05-08 07:48 UTC _(reply to #18)_

How do you decide which features to drop? Just the “worst” one and start from the start? Or all negative ones after one loop? Do you check for some sort of significance (possibly corrected for multiple hypotheses testing)? Otherwise, I guess you’ll always find negative results just by chance.

---

### Post #23 — **nyuton** | 2021-05-08 07:59 UTC _(reply to #21)_

Good point! I’ve used the second version so far. I’ll try the 3rd as well!

---

### Post #24 — **jamesjoyce** | 2021-05-08 11:23 UTC

Hi,  
thx for the article.  
Just a question: what would be a good contender for “num.numerai_score”?  
Is there a line of code/github-reference I could use?

---

### Post #25 — **jay1100** | 2021-05-10 07:15 UTC _(reply to #24)_

When you download the example data, there is a file analysis_and_tips.ipynb. It contains a numerai_score method if I remember correctly. You might have to adapt it a bit to fit into the code of nyuton.

---

### Post #26 — **jay1100** | 2021-05-10 07:17 UTC _(reply to #22)_

I simply order the features by importance and then for example drop the lowest 30%. Very straight forward.

---

### Post #27 — **nyuton** | 2021-05-10 07:45 UTC _(reply to #24)_

It’s just the standard correlation score.  
You can get the code here: [GitHub - nemethpeti/numerai](<https://github.com/nemethpeti/numerai>)

---

### Post #28 — **minou** | 2021-05-10 15:50 UTC _(reply to #27)_

Have you compared results of permutation importance with xgboost’s reporting of feature importance? i.e.  
`feature_importances_` or `get_booster().get_score(importance_type=)` Wondering if there’s correlation with any of XGB’s importance types.

---

### Post #29 — **nyuton** | 2021-05-24 18:47 UTC _(reply to #28)_

There should be some correlation, but it’s not the same thing.

---

### Post #31 — **sneaky** | 2021-06-06 18:06 UTC

Thank you for sharing!  
I am a huge believer in peer review that is why I would like to share my take on your feature selection.

I’m currently using following algorithm that was derived from the chat feedback:
    
    
    * split data to 5 folds CV (sequentially)
    * for each split:
       o find optimal parameters for a model using another 5 fold CV
       o train model with the found parameters on all features and measure the "base correlation" with the target
       o mark all features as non-selected
       o for each non-selected feature repeat X (X=5) times:
           * shuffle the feature's column and measure a correlation with the target
           * if the correlation is greater than the "base correlation" break the repeat
       o all features that pass the repeated test are marked as selected features
       
    * return the selected features
    

The idea is that CV should prevent overfitting to validation data and the repeated test should mitigate the effects of chance.

IMHO (not based on any research or math):

  * If at least one split of the CV uses a feature then the feature should be included.
  * If the test fails at least once (the correlation is higher) the model does not rely on the feature.



Aside from that, I’ve tried non-iterative approach particle swarm optimization (PSO) to make a feature selection faster. It did not work well. The computation was a little bit faster, but the performance was much worse. Did anybody has better experience?

Thank you for any feedback!

---

### Post #34 — **neliz** | 2021-07-08 07:35 UTC

thank m8, going to give it a try!

---

### Post #35 — **neliz** | 2021-07-08 09:11 UTC

Noob question: how can you implement this before doing a hyper parameter sweep?

If you do a model.predict, than your hyper parameters should already be defined correct?

---

### Post #37 — **johnnywhippet** | 2021-07-24 18:09 UTC _(reply to #13)_

Good spot. I’m just about to get cracking with  
This.

<https://scikit-learn.org/stable/modules/permutation_importance.html>

---

### Post #38 — **halsmith99** | 2021-07-29 05:17 UTC

hi nyuton,

looking to try this with the new data set coming.

have your live results backed up the experimental results?

---

### Post #39 — **nyuton** | 2021-08-20 10:00 UTC

Hi!

If you liked this post and would like to buy actual good performing models, you can do it now at NumerBay.ai!  
Two of my models are [available here.](<https://numerbay.ai/c/numerai-predictions>)

---

### Post #40 — **kedoink** | 2024-04-03 03:16 UTC

are you able to add this to the pickle or are you running and uploading manually or via webhook?
