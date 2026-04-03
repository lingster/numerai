---
title: "Preview: NumerBlox 1.0"
category: Data Science
url: https://forum.numer.ai/t/preview-numerblox-1-0/6696
created_at: 2023-10-02T12:57:42.822000+00:00
last_posted_at: 2023-11-15T15:01:39.682000+00:00
posts_count: 12
views: 1208
tags: []
---

# Preview: NumerBlox 1.0

---

### Post #1 — **perfect_fit** | 2023-10-02 12:57 UTC

About 1.5 years ago [@jrai](</u/jrai>) and I created an open source library called [NumerBlox](<https://github.com/crowdcent/numerblox/tree/master>) to simplify the software engineering around Numerai inference pipelines. After hearing your feedback and using it internally for all [CrowdCent](<https://crowdcent.com/>) models we had many insights and integrated everything we have learned into NumerBlox 1.0. We invite you to try out this [preview version](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1>) and give feedback before we merge it.

**Quickstart (v4.2. data):** <https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#3-quick-start>

**Overview of NumerBlox functionality:** <https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/index.md>

**Advanced new features for end-to-end pipelines:** <https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/end_to_end.md>

# Why a new version of NumerBlox?

After working with NumerBlox for almost 2 years we decided to focus more on going towards end-to-end pipelines to improve reproducibility and robustness. For NumerBlox 1.0 we focused on the following topics:

## 1\. End-to-end pipelines and full [scikit-learn](<https://scikit-learn.org/stable/>) compatibility

  * Every component can now be used with scikit-learn pipelines. We even developed [meta-estimators](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/meta.md>) so ensembling and feature neutralization can be fitted end to end in one pipeline.
  * All components can be used standalone, but we believe the most robust models are fully reproducible and can be saved and loaded as one (cloudpickle) file. They should accept raw input and output fully processed predictions. NumerBlox v1 allows for this end-to-end modelling, even if you have a cross-validation setup, are ensembling multiple models and doing feature neutralization.
  * An additional benefit is that NumerBlox components now integrate with not only scikit-learn, but also extension libraries like [scikit-lego](<https://github.com/koaning/scikit-lego>), [scikit-llm](<https://github.com/iryna-kondr/scikit-llm/>) and [@jefferythewind’s Era Splitting models](<https://github.com/jefferythewind/scikit-learn-erasplit>).



Below is an example of what you could build with the new NumerBlox setup. Here multiple cross validation schemes are fitted with an underlying estimator (`XGBRegressor` in this case). These models are ensembled and the final prediction is neutralized. An implementation of this example can be found in [this example notebook (Section 3)](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/examples/end_to_end.ipynb>).

[![meta_pipeline](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0b1191938b5b7dab9eb3c28f3feeee597589985e.png)meta_pipeline912×230 23.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0b1191938b5b7dab9eb3c28f3feeee597589985e.png> "meta_pipeline")

NOTE: This is also a heads-up for people currently using NumerBlox 0.x. The new version will have some breaking changes for current NumerBlox 0.x pipelines. The old system of `Model` and `ModelPipeline` objects will be deprecated in favor of full compatibility with `scikit-learn`.

## 2\. Simplify!

  * We’ve greatly simplified the package structure and reduced the number of mandatory dependencies. Bulky dependencies like Tensorflow are now optional and only needed if you use specific components like [Feature Penalization](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/penalization.md>). Our custom DataFrame structure, [NumerFrame](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/numerframe.md>), is now completely optional and no processors depend on using NumerFrame.
  * An additional benefit of these simplifications to the library is that it allowed us to build a more robust test suite to make sure all components behave as expected.



## 3\. Leverage new v4.2 data to the fullest

  * After deprecation of v2/v3 data was announced we moved quickly to update our pipelines. The downloaders we refined make it easy to pull the newest data and auxiliary data like feature groups and meta model predictions to make the transition to v4 data easier.
  * The [new v4.2 data](<https://numer.ai/data/v4.2>) reintroduced feature groups. We added functionality to `NumerFrame` that allows you to retrieve feature groups with one line of code to prepare your data for training and inference.



**NumerFrame Examples**
    
    
    import pandas as pd
    from numerblox.download import NumeraiClassicDownloader
    from numerblox.numerframe import NumerFrame
    from numerblox.prediction_loaders import ExamplePredictions
    downloader = NumeraiClassicDownloader("data")
    # Training and validation data
    downloader.download_training_data("train_val", version="4.2", int8=True)
    df = NumerFrame(pd.read_parquet("data/train_val/train_int8.parquet"))
    # Era column
    eras = df.get_era_data
    # Get small feature set
    small_df = df.get_small_feature_data
    # Get last 100 eras of rain features
    rain_df = df.get_last_n_eras(100).get_feature_group("rain")
    # Get v3 equivalent features
    v3_df = df.get_v3_equivalent_features
    # FNCv3 features
    fncv3 = df.get_fncv3_feature_data
    

  * The feature groups allow for new feature engineering techniques like creating aggregate statistics of the groups. [GroupStatsPreProcessor](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/preprocessing.md#groupstatspreprocessor>) implements this and integrates with scikit-learn pipelines.



# Installation of Preview

## Library

The new NumerBlox version will work with Python 3.9+. Because we are still in development you can clone NumerBlox v1 from the dev branch using the code below.
    
    
    git clone --single-branch --branch rewrite/numerbloxv1 https://github.com/crowdcent/numerblox.git
    pip install poetry 
    cd numerblox
    poetry install
    

As an alternative to Poetry it is possible to run `pip install .` after you cloned the library.

## Documentation

The new documentation will eventually be on a Github Pages website. For now docs can be found [here](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1/docs>) or can be build locally with `mkdocs`:
    
    
    pip install mkdocs
    mkdocs build
    mkdocs serve
    

# Contributing

I always welcome new contributions and feature suggestions. If you are eager to contribute check out the [new contributing docs](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/contributing.md>) and create a PR that merges to the `rewrite/numerbloxv1` branch.

Looking forward to hear your feedback and to refine NumerBlox before release! Very grateful for any suggestions on how we can improve this library and simplify competing in both Numerai Classic and Signals for all levels.

---

### Post #2 — **jeremy_berros** | 2023-10-05 14:27 UTC

Thanks for sharing Carlo. Can’t wait to use it. I’ve successfully installed Numerblox however I am having issues importing some subpackages like **misc** or **prediction_loaders** . For example I get `ImportError: cannot import name 'Key' from 'numerblox.misc'` and even `ModuleNotFoundError: No module named 'numerblox.prediction_loaders'`. Any idea what could be the culprit?

---

### Post #3 — **perfect_fit** | 2023-10-05 17:11 UTC _(reply to #2)_

Hey Jeremy, thank you so much for checking it out!

This sounds like you’ve installed the `master` branch instead of the `rewrite/numerbloxv1` branch. The new NumerBlox is not merged to `master` yet, but in `rewrite/numerbloxv1`.

Have you followed these installation instructions?
    
    
    git clone --single-branch --branch rewrite/numerbloxv1 https://github.com/crowdcent/numerblox.git
    pip install poetry 
    cd numerblox
    poetry install

---

### Post #4 — **jeremy_berros** | 2023-10-05 17:50 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/perfect_fit/48/2527_2.png) perfect_fit:

> 
>     poetry install
>     

Yes I did and I ran into `RuntimeError: Unable to find installation candidates for tensorflow-io-gcs-filesystem (0.34.0)`

EDIT:

I’ve bypassed the problem by removing `tensorflow = "^2.13.0"` from `pyproject.toml` and the poetry installed `numerblox==0.5.14` without any problem.

However, I still have `ImportError: cannot import name 'Key' from 'numerblox.misc' (C:\Users\pubbe\anaconda3\lib\site-packages\numerblox\misc.py)`

---

### Post #5 — **perfect_fit** | 2023-10-05 18:35 UTC _(reply to #4)_

Interesting, haven’t encountered that `poetry` Tensorflow error before.

The version that you need is `numerblox==1.0`, which is not released on Pypi yet (pip) so thats why we have this poetry installation.

Tensorflow is part of the dev dependencies so not needed per se to test the library.

Could you try running
    
    
    poetry install --no-dev
    

Make sure you are in the newly cloned `numerblox` directory.

If that doesn’t work I would do `pip install .` while being in the newly cloned `numerblox` directory.

`0.5.14` is the current release so not the new version. In Numerblox 1.0 we moved `Key` to `misc` so that why you get the ImportError with an older Numerblox version.

---

### Post #6 — **jeremy_berros** | 2023-10-05 19:56 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/perfect_fit/48/2527_2.png) perfect_fit:

> pip install .

`poetry install --no-dev` didn’t work but `pip install .` did.

Thanks for your support Carlo!

---

### Post #7 — **perfect_fit** | 2023-10-05 20:45 UTC _(reply to #6)_

Good to hear! What error did `poetry install --no-dev` give? it shouldn’t give any Tensorflow related dependency errors.

---

### Post #8 — **jeremy_berros** | 2023-10-05 21:06 UTC _(reply to #7)_

I got `The --no-dev option is deprecated, use the --only main notation instead. Installing dependencies from lock file. Warning: poetry.lock is not consistent with pyproject.toml. You may be getting improper dependencies. Run poetry lock [--no-update] to fix it.`

As expected, running `poetry lock [--no-update]` didn’t fix, anything so I went with `pip install .` instead

Btw, how much RAM do you need to run the end to end pipeline?

---

### Post #9 — **perfect_fit** | 2023-10-05 21:59 UTC _(reply to #8)_

Ok, thanks for letting me know! Will check if `poetry install --only main` works for me.

If you can normally fit the full new v4.2. dataset with your models you should be able to fit the example pipelines. The most intensive step I think is the feature neutralization. You can always run the neutralization on a subset of the features if there is not sufficient memory for the full feature set.

---

### Post #10 — **jeremy_berros** | 2023-10-06 14:07 UTC _(reply to #9)_

Troubleshooting the Advanced Numerblox Modeling Notebook.

When training with `full_pipe.fit(X.values, y_int.values, numeraiensemble__eras=eras, featureneutralizer__eras=eras, featureneutralizer__features=features)` I get `TypeError: Provided variable X is not of type pandas.DataFrame` even though it’s clearly a dataframe .`isinstance(X, pd.DataFrame) True` ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=12)

---

### Post #11 — **perfect_fit** | 2023-10-06 14:30 UTC _(reply to #10)_

Thanks for the feedback! Must have happened when I changed to the XGBoost model.

It should now work with these changes:

![](https://github.githubassets.com/favicons/favicon.svg) [github.com](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#32-advanced-numerblox-modeling>)

### [GitHub - crowdcent/numerblox at rewrite/numerbloxv1](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#32-advanced-numerblox-modeling>)

[rewrite/numerbloxv1](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#32-advanced-numerblox-modeling>)

Solid Numerai pipelines. Contribute to crowdcent/numerblox development by creating an account on GitHub.

---

### Post #12 — **perfect_fit** | 2023-11-15 15:01 UTC _(reply to #11)_

UPDATE: NumerBlox v1 has been merged and uploaded to PyPi.

From now on you can install the new NumerBlox version with

`pip install -U numerblox`
