---
title: "Eejits guide to Numer.ai"
category: Data Science
url: https://forum.numer.ai/t/eejits-guide-to-numer-ai/4023
created_at: 2021-09-01T13:11:15.046000+00:00
last_posted_at: 2021-09-19T21:52:51.622000+00:00
posts_count: 3
views: 1266
tags: []
---

# Eejits guide to Numer.ai

---

### Post #1 — **pheasantstilly** | 2021-09-01 13:11 UTC

Along my starting journey with of Machine learning was with Kaggle data. but it just wasn’t giving the correct understanding of long term aspirations of building AI that would take over the Universe and destroy the Borg.

Upon hearing of this magical tournament of computer wielding smart arses, where models battle amongst the silicone burning RTX 3090’s. But a retro gaming machine may never compete against these power houses. But fear not because you can use Colabs.

But going through the Numer.ai tutorial and given a basic XGBRegressor model that works surprisingly well. Setup an automated system that allows me to download, run. But I needed time to go through the code fully and understand the full process. Over time the model did ok. but knowing everyone has mostly the same model. I knew I’d have to go back.

So my latest project was to demystify some of this, mainly for myself.  
SO without any further creditability.

Here is my early work on [GitHub - gnellany/numerai: Stuff I'm working on](<https://github.com/gnellany/numerai>)

If you are using the model that numer.ai supplies and running in python  
"  
model = XGBRegressor(n_estimators=10000,learning_rate=0.01,subsample=0.3,colsample_bytree=0.1,max_depth=5,  
booster=‘gbtree’,tree_method=‘gpu_hist’,predictor=‘gpu_predictor’,  
reg_lambda=0.0009,reg_alpha=23,random_state=42)  
"  
To you new users, remember if using the starting code to delete the example_model.xgb

After building a few different models with this. I decided to automate a little more to find the best variables to use with this code. If you kept reading this far the code you are looking for is called Long_train

The current results with the model trainings can be found:

[docs.google.com](<https://docs.google.com/spreadsheets/d/1Lr0ai8sUiePRx0-jftL3CBv09hjgBzMbEL08btBT3e4/edit?usp=sharing>) [](<https://docs.google.com/spreadsheets/d/1Lr0ai8sUiePRx0-jftL3CBv09hjgBzMbEL08btBT3e4/edit?usp=sharing>)

### [Model_stats](<https://docs.google.com/spreadsheets/d/1Lr0ai8sUiePRx0-jftL3CBv09hjgBzMbEL08btBT3e4/edit?usp=sharing>)

Sheet1 Estimators,learning_rate,subsample,colsample,Depth,Lambda,alpha,mmc_mean,mmc_sharpe,mmc_diff,corr_preds 10000,0.01,0.3,0.01,5,0.0009,23,-0.003251714,0.485043681,-0.194173275,0.896079509 10000,0.007,0.4,0.01,5,0.0009,23,-0.003644807,0.44146663...

The future Issue I face is What is the MMC and what is a target for these?

---

### Post #2 — **autratec** | 2021-09-02 02:58 UTC

Thanks for sharing the code. MMC definition was well explained in the tournament introduction documents. Basically, it is the performance indicator with your peers.

---

### Post #4 — **pheasantstilly** | 2021-09-19 21:52 UTC _(reply to #3)_

Update to now legacy model code with 97%

model = XGBRegressor(n_estimators=100000, learning_rate=0.0029815, subsample=0.9, colsample_bytree=0.06576536,  
max_depth=5,  
booster=‘gbtree’, tree_method=‘gpu_hist’, predictor=‘gpu_predictor’,  
reg_lambda=0.1, reg_alpha=24, random_state=42)
