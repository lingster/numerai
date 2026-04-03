---
title: "Feature Selection with BorutaShap"
category: Data Science
url: https://forum.numer.ai/t/feature-selection-with-borutashap/4145
created_at: 2021-09-17T23:04:24.828000+00:00
last_posted_at: 2023-01-17T13:38:40.774000+00:00
posts_count: 17
views: 12777
tags: []
---

# Feature Selection with BorutaShap

---

### Post #1 — **mdo** | 2021-09-17 23:04 UTC

I first read an article on the [BorutaShap](<https://medium.com/analytics-vidhya/is-this-the-best-feature-selection-algorithm-borutashap-8bc238aa1677>) feature selection algorithm a while ago but had never got it to work properly with the Numerai data. I thought with the release of the new data it might be time to try again. After some initial failures, I dug into the [code](<https://github.com/Ekeany/Boruta-Shap>) to see if I could improve things. I found and addressed a couple issues and now I think you all may find it useful:

  1. When set to calculate feature importance SHAP values on the test set, it doesn’t respect era boundaries when splitting the data
  2. It doesn’t actually calculate SHAP values just using the test set, even when set to do so. Rather it uses the whole dataset.



My fixed up version of the code is [here](<https://drive.google.com/file/d/1h3Lhcl4Xtxmp_RKO-zTXzi2eTWOGhQEo/view?usp=sharing>) I’ll try to get a PR into the main branch, but this should work for now. (caveat - the sampling option will not respect eras so I recommend leaving as False)
    
    
    import numpy as np
    import pandas as pd
    from numerapi import NumerAPI
    import sklearn
    import lightgbm
    from BorutaShap import BorutaShap
    
    napi = NumerAPI()
    
    current_round = napi.get_current_round(tournament=8)
    
    # load int8 version of the data
    napi.download_dataset("numerai_training_data_int8.parquet", "numerai_training_data_int8.parquet")
    df = pd.read_parquet('numerai_training_data_int8.parquet')
    
    # create era integer column for convenience
    df["erano"] = df.era.astype(int)
    eras = df.erano
    
    # create model to be used by BorutaShap feature selector
    # changes to the model choice affect the features that are chosen so there's lot's of room to experiment here
    model = lightgbm.LGBMRegressor(n_jobs=-1, colsample_bytree=0.1, learning_rate=0.01, n_estimators=2000, max_depth=5)
    
    # initialize the feature selector
    Feature_Selector = BorutaShap(model=model,
                                        importance_measure='shap',
                                        classification=False)
    
    # here I iterate over the 4 non-overlapping sets of eras and perform feature selection in each, then take the union of the selected features
    # I'm just using standard 'target' for now, but it would be interesting to investigate other targets as well
    # It may also be useful to look at the borderline features that aren't accepted or eliminated
    good_features = []
    for i in range(1,5):
        df_tmp = df[eras.isin(np.arange(i, 575, 4))]
        eras_tmp = eras[eras.isin(np.arange(i, 575, 4))]
        Feature_Selector.fit(X=df_tmp.filter(like='feature'), y=df_tmp['target'], groups=eras_tmp, n_trials=50, sample=False, train_or_test = 'test', normalize=True, verbose=True)
        good_features+=Feature_Selector.accepted
    good_features = list(set(good_features))
    

The features I got out of running the above are:
    
    
    good_features = [
                    'feature_unwonted_trusted_fixative',
                    'feature_introvert_symphysial_assegai',
                    'feature_jerkwater_eustatic_electrocardiograph',
                    'feature_canalicular_peeling_lilienthal',
                    'feature_unvaried_social_bangkok',
                    'feature_crowning_frustrate_kampala',
                    'feature_store_apteral_isocheim',
                    'feature_haziest_lifelike_horseback',
                    'feature_grandmotherly_circumnavigable_homonymity',
                    'feature_assenting_darn_arthropod',
                    'feature_beery_somatologic_elimination',
                    'feature_cambial_bigoted_bacterioid',
                    'feature_unaired_operose_lactoprotein',
                    'feature_moralistic_heartier_typhoid',
                    'feature_twisty_adequate_minutia',
                    'feature_unsealed_suffixal_babar',
                    'feature_planned_superimposed_bend',
                    'feature_winsome_irreproachable_milkfish',
                    'feature_flintier_enslaved_borsch',
                    'feature_agile_unrespited_gaucho',
                    'feature_glare_factional_assessment',
                    'feature_slack_calefacient_tableau',
                    'feature_undivorced_unsatisfying_praetorium',
                    'feature_silver_handworked_scauper',
                    'feature_communicatory_unrecommended_velure',
                    'feature_stylistic_honduran_comprador',
                    'feature_travelled_semipermeable_perruquier',
                    'feature_bhutan_imagism_dolerite',
                    'feature_lofty_acceptable_challenge',
                    'feature_antichristian_slangiest_idyllist',
                    'feature_apomictical_motorized_vaporisation',
                    'feature_buxom_curtained_sienna',
                    'feature_gullable_sanguine_incongruity',
                    'feature_unforbidden_highbrow_kafir',
                    'feature_chuffier_analectic_conchiolin',
                    'feature_branched_dilatory_sunbelt',
                    'feature_univalve_abdicant_distrail',
                    'feature_exorbitant_myeloid_crinkle'
                    ]
    

Making a model using just those 38 features + 80% neutralization, I was able to get a pretty nice model. I’m sure it could be improved further by performing feature selection and training with the alternative targets and then ensembling. Let me know how it goes! Good luck  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/72b620596685661599d54ba25c14bd6ebf25a646.png)image692×498 30.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/72b620596685661599d54ba25c14bd6ebf25a646.png> "image")

---

### Post #2 — **qeintelligence** | 2021-09-18 15:37 UTC

Wow, very nice and detailed explanation including sample code! Afaik tell thats worth of a bonus. I am curious if this BortuaShap approach is model-agnostic or do you need to re-run for other type of models? The other one I am curious about is if this feature-selection had a (slight) negative performance result when compared to your model when using all features.

Also one of the benefits of feature selection I guess, saves a lot of memory (and thus solves memory issues lol)

---

### Post #3 — **rigrog** | 2021-09-18 17:26 UTC

Please fix the title: s/Bortua/Boruta/

---

### Post #4 — **mdo** | 2021-09-18 18:00 UTC _(reply to #3)_

fixed, that’s embarrassing ![:man_facepalming:](http://forum.numer.ai/images/emoji/twitter/man_facepalming.png?v=9)

---

### Post #5 — **gerardp** | 2021-09-19 13:17 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> 
>     import numpy as np
>     import pandas as pd
>     from numerapi import NumerAPI
>     import sklearn
>     import lightgbm
>     from BorutaShap import BorutaShap
>     
>     napi = NumerAPI()
>     
>     current_round = napi.get_current_round(tournament=8)
>     
>     # load int8 version of the data
>     napi.download_dataset("numerai_training_data_int8.parquet", "numerai_training_data_int8.parquet")
>     df = pd.read_parquet('numerai_training_data_int8.parquet')
>     
>     # create era integer column for convenience
>     df["erano"] = df.era.astype(int)
>     eras = df.erano
>     
>     # create model to be used by BorutaShap feature selector
>     # changes to the model choice affect the features that are chosen so there's lot's of room to experiment here
>     model = lightgbm.LGBMRegressor(n_jobs=-1, colsample_bytree=0.1, learning_rate=0.01, n_estimators=2000, max_depth=5)
>     
>     # initialize the feature selector
>     Feature_Selector = BorutaShap(model=model,
>                                         importance_measure='shap',
>                                         classification=False)
>     
>     # here I iterate over the 4 non-overlapping sets of eras and perform feature selection in each, then take the union of the selected features
>     # I'm just using standard 'target' for now, but it would be interesting to investigate other targets as well
>     # It may also be useful to look at the borderline features that aren't accepted or eliminated
>     good_features = []
>     for i in range(1,5):
>         df_tmp = df[eras.isin(np.arange(i, 575, 4))]
>         eras_tmp = eras[eras.isin(np.arange(i, 575, 4))]
>         Feature_Selector.fit(X=df_tmp.filter(like='feature'), y=df_tmp['target'], groups=eras_tmp, n_trials=50, sample=False, train_or_test = 'test', normalize=True, verbose=True)
>         good_features+=Feature_Selector.accepted
>     good_features = list(set(good_features))
>     

On what machine have you tried it?  
I tried it on google colab with 25gb of ram and it crashed due to lack of ram.

---

### Post #6 — **themicon** | 2021-09-22 12:53 UTC _(reply to #2)_

Except that you need to be able to load the entire dataset into memory first and be able to run LightGBM at least a few times before you can actually get the “good features”.

---

### Post #7 — **gbrecht** | 2021-09-28 06:00 UTC

Does anyone also get gbm warnings about the max leaf size with the code provided?
    
    
    [LightGBM] [Warning] Accuracy may be bad since you didn't explicitly set num_leaves OR 2^max_depth > num_leaves. (num_leaves=31).

---

### Post #8 — **gbrecht** | 2021-09-28 06:18 UTC

When I compare feature importance to their standard deviation, the std is often higher than the importance (which is the mean). Do you experience the same? Does it make sense to view this like some sort of sharpe of the feature?

---

### Post #9 — **adalseno** | 2021-12-05 18:26 UTC

Hi, thank you very much for sharing your code [@mdo](</u/mdo>)  
I have an issue with it, though (the modified Boruta-Shap class I mean). Using `GroupShuffleSplit` with groups option, train and test eras won’t overlap, but the order is not preserved. I made some test and, for example I got:
    
    
    Number of overlapping eras: 0
    Min era for train: 2 and max era for train: 572
    Min era for test: 1 and max era for test: 574
    

I would expect the test set to be at the end of train one. With `GroupShuffleSplit` this is not granted.

I mean, even when one does Cross Validation (and Boruta-Shap does not), one splits the series in chunks and for every chunk will use the first part for training and the last part for testing.  
Am I missing something?

---

### Post #10 — **autratec** | 2021-12-05 23:21 UTC

[@mdo](</u/mdo>) hi, how is the live submission result after the feature filtering algo being used ? What’s the model name ?

---

### Post #11 — **objectscience** | 2021-12-06 20:20 UTC _(reply to #9)_

Might be worth noting that it’s possible to get:  
Min era for train = 1  
Min era for test = 2

But the eras will still be shuffled to something like this:  
train = [1, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 20, 23, …, 573, 574]  
test = [2, 3, 12, 13, 16, 18, 21, 22, 25, …, 564, 568]

So we’re effectively training on data that occurs after eras in the test set. I don’t know how big of an issue it is for feature selection, but forcing a proper time series split doesn’t seem like a bad idea here.

I know [@mdo](</u/mdo>) created a custom splitter [here](<http://forum.numer.ai/t/era-wise-time-series-cross-validation/791>), maybe we can use that again with a little tuning.

---

### Post #12 — **mdo** | 2021-12-07 02:13 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/adalseno/48/1476_2.png) adalseno:

> I mean, even when one does Cross Validation (and Boruta-Shap does not), one splits the series in chunks and for every chunk will use the first part for training and the last part for testing.

This is not true for standard CV, but is for walk forward CV. A era-wise walk forward/time series split could also be used here as you point out [@objectscience](</u/objectscience>) and could be worth checking out. You could probably use the splitter from the walk forward/time series CV post.

---

### Post #13 — **adalseno** | 2021-12-14 14:38 UTC _(reply to #9)_

Hi [@mdo](</u/mdo>) , thank you for your reply. Yes of course, I was referring to TimeSeries cross validation (otherwise there wouldn’t be any issue). I will give a look to the code mentioned by [@objectscience](</u/objectscience>) .

I made a subclass of BorutaShap that should be era wise and split the time series correctly. It runs, but I’m not sure of the results that seem not too consistent over time (unfortunately running the selection on the whole dataset, without sampling, takes too long on my machine to test it deeply; I expect the results to be the same over multiple runs. With sampling it’s not granted given the random process). I changed the original code as little as possible, but added early stopping to gradient descent models to improve reliability and speed (and fixed an issue in sampling that could lead to infinite loop; I made a PR for it). If someone wants to try it, here is the code:
    
    
    from BorutaShap import BorutaShap
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm
    from scipy.stats import ks_2samp
    from sklearn.ensemble import IsolationForest
    
    
    
    
    class BorutaShapNumerai(BorutaShap):
        """
            Subclass of BorutaShap to be used in Numerai tournament
            It will split the data era wise.
            To be used with train_or_test = 'test' (no matter what you choose, it will always be 'test')
            Sampling should work fine, era wise, and is highly recommended 
            given the time and RAM needed for full training
    
        """
        
        
        def Check_if_chose_train_or_test_and_train_model(self):
    
            """
            Decides to fit the model to either the training data or the test/unseen data a great discussion on the
            differences can be found here.
    
            https://compstat-lmu.github.io/iml_methods_limitations/pfi-data.html#introduction-to-test-vs.training-data
    
            """
            if self.stratify is not None and not self.classification:
                raise ValueError('Cannot take a strtified sample from continuous variable please bucket the variable and try again !')
    
    
            if self.train_or_test.lower() == 'test':
                # keeping the same naming convenetion as to not add complexit later on
                self.X_boruta_train, self.X_boruta_test, self.y_train, self.y_test, self.w_train, self.w_test = self.train_test_split(self.X_boruta,
                                                                                                                                    self.y,
                                                                                                                                    self.sample_weight,
                                                                                                                                    test_size=0.3,
                                                                                                                                    random_state=self.random_state)
                # Pass also X_test and y_test to allow early stopping
                self.Train_model(X=self.X_boruta_train, y=self.y_train, sample_weight = self.w_train, 
                                 X_test=self.X_boruta_test, y_test=self.y_test, eval_sample_weight=self.w_test)
    
            elif self.train_or_test.lower() == 'train':
                # model will be trained and evaluated on the same data
                self.Train_model(self.X_boruta, self.y, sample_weight = self.sample_weight)
                self.X_boruta_test = self.X_boruta
    
            else:
                raise ValueError('The train_or_test parameter can only be "train" or "test"')
    
        def train_test_split(self, X, y, sample_weight=None, test_size=0.3, random_state=None):
            X_boruta_train = X[self.cutoff]
            X_boruta_test = X[~self.cutoff]
            y_train = y[self.cutoff]
            y_test = y[~self.cutoff]
            w_train = None
            w_test = None
           
            return X_boruta_train, X_boruta_test, y_train, y_test, w_train, w_test
    
        def Train_model(self, X, y, sample_weight = None, X_test=None, y_test=None, eval_sample_weight=None):
    
            """
            Trains Model also checks to see if the model is an instance of catboost as it needs extra parameters
            also the try except is for models with a verbose statement
    
            Parameters
            ----------
            X: Dataframe
                A pandas dataframe of the features.
    
            y: Series/ndarray
                A pandas series or numpy ndarray of the target
    
            sample_weight: Series/ndarray
                A pandas series or numpy ndarray of the sample weights
    
            Returns
            ----------
            fitted model object
    
            """
            # Use early stopping when possible (that is in test mode; in train mode early stopping is not available)
            if 'catboost' in str(type(self.model)).lower():
                if X_test is not None and y_test is not None:
                    self.model.fit(X, y, sample_weight = sample_weight,  
                                   eval_set=[(X_test, y_test)], early_stopping_rounds=100,  verbose=False)
                else:
                    self.model.fit(X, y, sample_weight = sample_weight, cat_features = self.X_categorical,  verbose=False)
                    
            elif 'lightgbm' in str(type(self.model)).lower():
                if X_test is not None and y_test is not None:
                    self.model.fit(X, y, sample_weight = sample_weight, 
                                   eval_set=[(X_test, y_test)], early_stopping_rounds=100,eval_sample_weight = [eval_sample_weight], verbose=False)
                else:                
                    self.model.fit(X, y, sample_weight = sample_weight, verbose=False)
           
            elif 'xgboost' in str(type(self.model)).lower():
                if X_test is not None and y_test is not None:
                    self.model.fit(X, y, sample_weight = sample_weight,  
                                   eval_set=[(X_test, y_test)], early_stopping_rounds=100, eval_sample_weight = [eval_sample_weight], verbose=False)
                else:                
                    self.model.fit(X, y, sample_weight = sample_weight, verbose=False)
    
            else:
    
                try:
                    self.model.fit(X, y, sample_weight = sample_weight, verbose=False)
    
                except:
                    self.model.fit(X, y, sample_weight = sample_weight)
    
    
        @staticmethod
        def create_cutoff(df):
            eras = sorted(df.era.unique())
            # Eras do not have all the same size so to identify the right era we need to find what is the era at the 70% of the index, add 1 and use it as our limit
            cutoff_era = int(df.iloc[int(len(df.index)*0.7)].era+1)
            cutoff = df.era < cutoff_era
            return cutoff
       
        
        def fit(self, X, y, sample_weight = None, n_trials = 20, random_state=0, sample=False,
                train_or_test = 'test', normalize=True, verbose=True, stratify=None):
    
            """
            The main body of the program this method it computes the following
    
            1. Extend the information system by adding copies of all variables (the information system
            is always extended by at least 5 shadow attributes, even if the number of attributes in
            the original set is lower than 5).
    
            2. Shuffle the added attributes to remove their correlations with the response.
    
            3. Run a random forest classifier on the extended information system and gather the
            Z scores computed.
    
            4. Find the maximum Z score among shadow attributes (MZSA), and then assign a hit to
            every attribute that scored better than MZSA.
    
            5. For each attribute with undetermined importance perform a two-sided test of equality
            with the MZSA.
    
            6. Deem the attributes which have importance significantly lower than MZSA as ‘unimportant’
            and permanently remove them from the information system.
    
            7. Deem the attributes which have importance significantly higher than MZSA as ‘important’.
    
            8. Remove all shadow attributes.
    
            9. Repeat the procedure until the importance is assigned for all the attributes, or the
            algorithm has reached the previously set limit of the random forest runs.
    
            10. Stores results.
    
            Parameters
            ----------
            X: Dataframe
                A pandas dataframe of the features.
    
            y: Series/ndarray
                A pandas series or numpy ndarray of the target
    
            sample_weight: Series/ndarray
                A pandas series or numpy ndarray of the sample weight of the observations (optional)
    
            random_state: int
                A random state for reproducibility of results
    
            Sample: Boolean
                if true then a rowise sample of the data will be used to calculate the feature importance values
    
            sample_fraction: float
                The sample fraction of the original data used in calculating the feature importance values only
                used if Sample==True.
    
            train_or_test: string
                Decides whether the feature importance should be calculated on out of sample data see the dicussion here.
                https://compstat-lmu.github.io/iml_methods_limitations/pfi-data.html#introduction-to-test-vs.training-data
    
            normalize: boolean
                if true the importance values will be normalized using the z-score formula
    
            verbose: Boolean
                a flag indicator to print out all the rejected or accepted features.
    
            stratify: array
                allows the train test splits to be stratified based on given values.
    
            """
    
            if sample_weight is None:
                sample_weight = np.ones(len(X))
            np.random.seed(random_state)
            self.starting_X = X.copy()
            self.X = X.copy()
            self.y = y.copy()
            self.cutoff=None
            self.cutoff=self.create_cutoff(self.X)
            self.sample_weight = sample_weight.copy()
            self.n_trials = n_trials
            self.random_state = random_state
            self.ncols = self.X.shape[1]
            self.all_columns = self.X.columns.to_numpy()
            self.rejected_columns = []
            self.accepted_columns = []
            self.check_X()
            self.check_missing_values()
            self.sample = sample
            self.train_or_test = 'test'  # train is not implemented yet
            self.stratify = stratify
    
            self.features_to_remove = []
            self.hits  = np.zeros(self.ncols)
            self.order = self.create_mapping_between_cols_and_indices()
            self.create_importance_history()
    
            if self.sample: self.preds = self.isolation_forest(self.X, self.sample_weight)
    
            for trial in tqdm(range(self.n_trials)):
    
                self.remove_features_if_rejected()
                self.columns = self.X.columns.to_numpy()
                self.create_shadow_features()
    
                # early stopping
                if self.X.shape[1] == 0:
                    break
    
                else:
    
                    self.Check_if_chose_train_or_test_and_train_model()
    
                    self.X_feature_import, self.Shadow_feature_import = self.feature_importance(normalize=normalize)
                    self.update_importance_history()
                    hits = self.calculate_hits()
                    self.hits += hits
                    self.history_hits = np.vstack((self.history_hits, self.hits))
                    self.test_features(iteration=trial+1)
    
            self.store_feature_importance()
            self.calculate_rejected_accepted_tentative(verbose=verbose)
            
            
    
        @staticmethod
        def isolation_forest(df, weights=None):
            '''
            fits isloation forest to the dataset and gives an anomaly score to every sample
            '''
            
            print('Calculating anomaly scores')
            preds = []
            for _,x in tqdm(df.groupby('era', group_keys=False)):
                clf = IsolationForest(n_jobs=-1, random_state=68).fit(x)
                preds.append(clf.score_samples(x))
            preds = pd.Series(np.hstack(preds), index=df.index, name='preds').to_frame()
            preds['era'] = df.era
            return preds   
        
        
        
        def find_sample(self):
            '''
            Finds a sample by comparing the distributions of the anomaly scores between the sample and the original
            distribution using the KS-test. Starts at 5% however will increase to 10% and then 15% etc. if a significant sample can not be found
            '''
            index_for_sample = []
            for _,X in self.preds.groupby('era', group_keys=False):
                loop = True
                iteration = 0
                size = self.get_5_percent_splits(X.shape[0])
                element = 1 # we start at 10%, if you want to start at 5% set it to zero
                while loop:
    
                    sample_indices = np.random.choice(np.arange(X.shape[0]),  size=size[element], replace=False)
                    sample = self.preds.loc[X.iloc[sample_indices].index]['preds']
                    if ks_2samp(X.preds, sample).pvalue > 0.95:
                        index_for_sample.append(X.iloc[sample_indices].index)
                        break
    
                    iteration+=1
    
                    if iteration == 20:
                        element  += 1
                        iteration = 0
    
            index_for_sample = np.hstack(index_for_sample)
            #print(f'Sample size is {len(index_for_sample)} about {(len(index_for_sample)/len(self.preds)*100):.2f}% of the original size')
            
            return self.X_boruta.loc[index_for_sample]
    

Save the code as `BorutaShapNumerai.py` and import as:
    
    
    from BorutaShapNumerai import BorutaShapNumerai as BorutaShap 
    

and you are ready to go.

---

### Post #16 — **matfyzak** | 2022-10-27 18:36 UTC

Hi, I am a newbie in Numerai. I wanted to load only the mentioned features but I don’t see them in the training dataset (v4) that I have just downloaded. Are features renamed after new data releases?

If yes, does anyone have an updated list of features? (I am currently working on a machine with limited RAM to run this myself on a whole dataset.)

---

### Post #17 — **shatteredx** | 2022-10-27 22:55 UTC _(reply to #16)_

Yes, those features are the “small” feature set in features.json:
    
    
    napi = NumerAPI()
    napi.download_dataset("v4/features.json")
    
    # read the feature metadata and get a feature set (or all the features)
    with open("v4/features.json", "r") as f:
        feature_metadata = json.load(f)
    features = feature_metadata["feature_sets"]["small"] # get the small feature set

---

### Post #18 — **matfyzak** | 2022-10-28 09:14 UTC _(reply to #17)_

Thank you for your guidance!

---

### Post #19 — **halsmith99** | 2023-01-17 13:38 UTC

what version of the data was this run on? having problems with missing data in 4.1
