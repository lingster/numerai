---
title: "Rnumerai - R Interface to the Numerai Machine Learning Tournament API"
category: Data Science
url: https://forum.numer.ai/t/rnumerai-r-interface-to-the-numerai-machine-learning-tournament-api/214
created_at: 2020-04-21T15:24:01.978000+00:00
last_posted_at: 2020-05-18T12:12:16.021000+00:00
posts_count: 12
views: 1917
tags: []
---

# Rnumerai - R Interface to the Numerai Machine Learning Tournament API

---

### Post #1 — **theomniacs** | 2020-04-21 15:24 UTC

**Rnumerai -** R Interface to the Numerai Machine Learning Tournament API

[github.com](<https://github.com/OmniacsDAO/Rnumerai>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8d0a87e5593e7087923e0afd542d21d812065b1e_2_690x344.png)

### [GitHub - OmniacsDAO/Rnumerai: R Interface to the Numerai Machine Learning...](<https://github.com/OmniacsDAO/Rnumerai>)

R Interface to the Numerai Machine Learning Tournament API

Hi everyone! This post is to introduce Rnumerai, an R Interface for the Numerai Machine Learning Tournament API. After you’ve spent your time pulling every ounce of performance out of your model, this package steps in to help automate the submission process. Let’s walk through some of the functionality in the Readme.

# Installation

  * For the latest stable release: `install.packages("Rnumerai")`
  * For the latest development release: `devtools::install_github("Omni-Analytics-Group/Rnumerai")`



# Automatic submission using this package

### 1\. Load the package.

  * `library(Rnumerai)`



### 2\. Set working directory where data will be downloaded and submission files would be kept.

Use current working directory

`data_dir <- getwd()`

Or use temporary directory

`data_dir <- tempdir()`

Or use a user specific directory

`data_dir <- "~/OAG/numerai"`

### 3\. Set Public Key and Secret API key variables.

Get your public key and api key by going to numer.ai and then going to `Custom API Keys` section under your `Account` Tab. Select appropriate scopes to generate the key or select all scopes to use the full functionality of this package.

  * `set_public_id("public_id_here")`
  * `set_api_key("api_key_here")`



Optional: If we choose not to setup the credentials here the terminal will interactively prompt us to type the values when we make an API call.

### 4\. Download data set for the current round and split it into training data and tournament data

  * `data <- download_data(data_dir)`
  * `data_train <- data$data_train`
  * `data_tournament <- data$data_tournament`



### 5\. Generate predictions

A user can put his/her own custom model code to generate the predictions here. For demonstration purposes, we will generate random predictions.

  * `submission <- data.frame(id=data_tournament$id,prediction_kazutsugi = sample(seq(.35,.65,by=.1),nrow(data_tournament),replace=TRUE))`



### 6\. Submit predictions for tournament and get submission id

The submission object should have two columns (id & prediction_kazutsugi) only.

  * `submission_id <- submit_predictions(submission,data_dir,tournament="Kazutsugi")`



### 7\. Check the status of the submission (Wait for a few seconds to get the submission evaluated)

  * `Sys.sleep(10) ## 10 Seconds wait period`
  * `status_submission_by_id(submission_id)`



### 8\. Stake submission on submission and get transaction hash for it.

  * `stake_tx_hash <- stake_nmr(value = 1)`
  * `stake_tx_hash`



### 9\. Release Stake and get transaction hash for it.

  * `release_tx_hash <- release_nmr(value = 1)`
  * `release_tx_hash`



# Performance

In our newest release, we’ve added functionality to graphically assess the performance of a single model or collection of models across time. The current performance metrics supported are:

`Reputation`  
`Rank`  
`NMR_Staked`  
`Leaderboard_Bonus`  
`Payout_NMR`  
`Average_Daily_Correlation`  
`Round_Correlation`  
`MMC`  
`Correlation_With_MM`

These metrics are used within three main functions:

`performance_distribution(username, metric, merge = FALSE, round_aggregate = TRUE)`

`performance_over_time(username, metric, merge = FALSE, outlier_cutoff = if (round_aggregate) 0 else 0.0125, round_aggregate = TRUE)`

`summary_statistics(username, dates = NULL, round_aggregate = TRUE)`

Here are some samples:

### 1\. Display performance distributions

`performance_distribution(c("objectscience"), "Average_Daily_Correlation")`

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e6c95e64c03ce789cf035b4f24aaa0cb87644f2d_2_690x470.png)image758×517 29.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e6c95e64c03ce789cf035b4f24aaa0cb87644f2d.png> "image")

`performance_distribution(c("objectscience", "uuazed","arbitrage"), "MMC")`

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/7bfa1e4bdd43c73655ba807dfabdafda6e5c8961_2_609x500.png)image763×626 35.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7bfa1e4bdd43c73655ba807dfabdafda6e5c8961.png> "image")

### 2\. Display performance over time

performance_over_time(c(“objectscience”), “Correlation_With_MM”)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/301358ca368177525ea68d318f4f3e1fdc5e2e29_2_603x499.png)image747×619 38.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/301358ca368177525ea68d318f4f3e1fdc5e2e29.png> "image")

performance_over_time(c(“objectscience”, “uuazed”,“arbitrage”), “Correlation_With_MM”)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/8f9412fd0f9cc62b85bbf1381cb1355ed165497d_2_594x500.png)image750×631 51.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8f9412fd0f9cc62b85bbf1381cb1355ed165497d.png> "image")

### 3\. Display performance summary statistics

`summary_statistics(c("arbitrage", "objectscience","uuazed"))`

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a620951195ca1a85f578f6c77625690eae780f84.png)image1079×310 15.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a620951195ca1a85f578f6c77625690eae780f84.png> "image")

### 4\. Support for many models and accounts

`performance_distribution(c("objectscience", "uuazed","arbitrage","cryptoquant","phorex","wander","madmin","wilfred","beepboopbeep","no_formal_agreement"), "Round_Correlation")`

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/df3a4fa5ec66d1a376f0b4ccc8b2398b6c6e9007_2_550x500.png)image1894×1719 602 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/df3a4fa5ec66d1a376f0b4ccc8b2398b6c6e9007.png> "image")

`data.frame(summary_statistics(c("objectscience", "uuazed","arbitrage","cryptoquant","phorex","wander","madmin","wilfred","beepboopbeep","no_formal_agreement"))$stats)`

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/24604967de279301a06b7a51f22d47f9cb4714d4.png)image946×443 28.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/24604967de279301a06b7a51f22d47f9cb4714d4.png> "image")

# Further Updates

As the performance metrics and functionality change, stay tuned for the latest updates! We’ve already included the recent changes in support of multiple models under the same account. If you have any questions or suggestions, please feel free to open a Github issue or here in the forum.

---

### Post #2 — **kreator** | 2020-05-15 07:20 UTC

Hi, thanks for developing and maintaining this project. For me as an R user it already saved me days or even weeks ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) in the last years. I really appreciate it. Please keep up the good work!

---

### Post #3 — **javibear** | 2020-05-15 23:28 UTC

Thanks as well. Quick question. how does the submit_predictions() function change with new multimodel functionality? when i enabled it, i was told to use :

submission_id <\- submit_predictions(submission, data_dir, tournament=“Kazutsugi”,  
model_id=models$integration_test)

model_id a new parameter?

---

### Post #4 — **ssh** | 2020-05-16 16:25 UTC _(reply to #3)_

I haven’t used my multi-models submissions yet, but in example provided there is also step when you init variable “models” before you use it at submit_predictions()

`models <- get_models() `  
before using it at:  
submission_id <\- submit_predictions(submission, data_dir, tournament=“Kazutsugi”, model_id=models$YOUR_MODEL_NAME)

if I understand API correctly you could also use:

`submission_id <- submit_predictions(submission, data_dir, tournament="Kazutsugi", model_id="YOUR_MODEL_ID_FROM_WEBSITE")`

where YOUR_MODEL_ID_FROM_WEBSITE provided at website (at <https://numer.ai/models> under earch your model name )

---

### Post #5 — **kreator** | 2020-05-17 20:12 UTC _(reply to #4)_

I tried version 2.1.1 of the package. There seems to be a bug in `get_models` and `submit_predictions`. I contacted the maintainers and they will have a look at it. Unfortunately, in my understanding the upload does not work for multi-model accounts at the moment.

---

### Post #6 — **ssh** | 2020-05-17 20:30 UTC _(reply to #5)_

[@kreator](</u/kreator>) also faced same issue with multi-model submissions. reported it at <https://community.numer.ai/channel/support> (and possible solution to this issue). I believe [@theomniacs](</u/theomniacs>) will update code at github as they are really supportive and quick to react. Or you could apply it locally (which I don’t like as it makes extra code to support)

---

### Post #7 — **ssh** | 2020-05-17 20:41 UTC

[@kreator](</u/kreator>) also had troubles with `get_models` as it didn’t worked with my previuse API_ID. I believe it need extra permission (like “get user info”), not only “submission”. so I went and created other API_ID with this extra permission on site, but it really not nessessary step as you could use model_id from site without calling get_models()

---

### Post #8 — **ssh** | 2020-05-17 20:59 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ssh/48/2729_2.png) ssh:

> submission_id ← submit_predictions(submission, data_dir, tournament=“Kazutsugi”, model_id=models$YOUR_MODEL_NAME)

other minor thing is: get_models() return a vector so one can’t address it with “$” and correct R code example would be:
    
    
    models <- Rnumerai::get_models()
    submission_id <- Rnumerai::submit_predictions(submission, data_dir, 
    tournament=“Kazutsugi”, model_id=models["YOUR_MODEL_NAME"])

---

### Post #9 — **javibear** | 2020-05-18 05:01 UTC

i had issues with get_models() too but figured you had to authenticate yourself first. try adding before get_models:

set_public_id(your_id)  
set_api_key(your_key)

worked fine after this and merely produces a df of your account names and model_ids

---

### Post #10 — **kreator** | 2020-05-18 09:49 UTC _(reply to #6)_

Thank you [@ssh](</u/ssh>) I posted an issue at github too. And right, I agree, they are very supportive. Would be great if they could resolve the issue quickly - especially with your input. Thank you!  
PS: Thank you for the hint on get_models too! And right, it is not necessarily needed as one can just hard code the model ids.

---

### Post #11 — **kreator** | 2020-05-18 09:55 UTC _(reply to #9)_

[@javibear](</u/javibear>) and [@ssh](</u/ssh>) the hint was correct. You have to produce new API keys, then `get_models` works. But it did not work with API keys that were generated before the change to the multi-model support.

---

### Post #12 — **kreator** | 2020-05-18 12:12 UTC

The bug was corrected today. After re-installation from github the submission for multi-model accounts worked for me.
