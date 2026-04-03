---
title: "Signal Miner: Find Unique Alpha & Beat the Benchmark"
category: Tournament
url: https://forum.numer.ai/t/signal-miner-find-unique-alpha-beat-the-benchmark/7922
created_at: 2025-01-29T20:18:44.457000+00:00
last_posted_at: 2025-04-16T13:48:31.692000+00:00
posts_count: 19
views: 2370
tags: []
---

# Signal Miner: Find Unique Alpha & Beat the Benchmark

---

### Post #1 — **jefferythewind** | 2025-01-29 20:18 UTC

# ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) Signal Miner: Find Unique Alpha & Beat the Benchmark

> **Revolutionizing Staking:** Aligning users and the fund through unique models.

## ![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=15) What is [Signal Miner](<https://github.com/jefferythewind/signal_miner/tree/main#installation--setup>)?

Signal Miner is a **fully automated model mining framework** designed to generate models that **outperform Numerai’s benchmark models** in terms of correlation and Sharpe ratio. Instead of staking on **pre-existing models** , this tool helps you **discover your own unique alpha** , which has a better chance of producing **positive MMC (Meta Model Contribution).**

![:bulb:](https://emoji.discourse-cdn.com/twitter/bulb.png?v=15) **Why use Signal Miner?**

  * **Unique Alpha:** Avoids the trap of staking on common, overused models.
  * **Better Payouts:** Unique signals **increase your expected returns** compared to generic staking.
  * **Automated Discovery:** Efficiently scans a search space for **high-performance models** using a scalable, asynchronous approach.



* * *

## ![:inbox_tray:](https://emoji.discourse-cdn.com/twitter/inbox_tray.png?v=15) Quick Start: Install & Run

Clone the repo and set up your environment. [Instructions available at Github project.](<https://github.com/jefferythewind/signal_miner/tree/main#installation--setup>)

* * *

## ![:fire:](https://emoji.discourse-cdn.com/twitter/fire.png?v=15) How It Works

![:bulb:](https://emoji.discourse-cdn.com/twitter/bulb.png?v=15) **The core workflow:**

  1. **Define a Benchmark Model** : This is what your models will aim to outperform.
  2. **Launch Model Mining** : Explore a grid of hyperparameters asynchronously.
  3. **Monitor Performance** : Track model evaluations across cross-validation folds.
  4. **Compare to the Benchmark** : Identify models that exceed performance thresholds.
  5. **Export Winning Models** : Save the best models for staking or further tuning.



### ![:trophy:](https://emoji.discourse-cdn.com/twitter/trophy.png?v=15) Defining a Benchmark Model
    
    
    benchmark_cfg = {
        "colsample_bytree": 0.1,
        "max_bin": 5,
        "max_depth": 5,
        "num_leaves": 15,
        "min_child_samples": 20,
        "n_estimators": 2000,
        "reg_lambda": 0.0,
        "learning_rate": 0.01,
        "target": 'target'  # Using the first target for simplicity
    }
    

### ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) Launch Mining

`start_mining()`

Once mining is started, models will be **trained and evaluated** in the background.

**Check Progress Anytime:**

`check_progress()`

> Progress: 122.0/2002 (6.09%)

### ![:bar_chart:](https://emoji.discourse-cdn.com/twitter/bar_chart.png?v=15) Visualizing Cross-Validation Splits

To **ensure proper evaluation** , the framework implements **time-series cross-validation with an embargo period** :

[![output](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/76db081941e77d5163ee7e55f9d476da073036a0_2_690x398.png)output1515×875 19.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/76db081941e77d5163ee7e55f9d476da073036a0.png> "output")

Here, training and test sets are **sequentially split** to mimic **live trading conditions** —a crucial step for avoiding data leakage.

* * *

## ![:chart_with_upwards_trend:](https://emoji.discourse-cdn.com/twitter/chart_with_upwards_trend.png?v=15) Mining Results: Past vs. Future Performance

Since yesterday, I’ve been running Signal Miner to evaluate **70+ models out of 1000** , and we already see **many models outperforming the benchmark** on both **validation and test** datasets. ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15)

Below is a **scatter plot** showing how models that performed well in validation (past) also tended to do well in test (future).

![:bar_chart:](https://emoji.discourse-cdn.com/twitter/bar_chart.png?v=15) **Sharpe Ratio: Validation vs. Test**

[![sharpe_scatter](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ce6d7923e04eb5f46d971023f7565f93628d30c6_2_677x500.jpeg)sharpe_scatter1766×1304 154 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ce6d7923e04eb5f46d971023f7565f93628d30c6.jpeg> "sharpe_scatter")

![:mag_right:](https://emoji.discourse-cdn.com/twitter/mag_right.png?v=15) **Key Insights:**

  * The **red dot** represents the benchmark model.
  * While **the top validation model wasn’t the best in test** , we found **several models that outperformed the benchmark in both.**
  * **Positive Correlation** : The best validation models _tended_ to be among the best in test as well.
  * If the scatter plot **looked random (a cloud of points), it would suggest the model selection process is noise** —but instead, we see a clear **upward trend**.



![:loudspeaker:](https://emoji.discourse-cdn.com/twitter/loudspeaker.png?v=15) **Goal:** Find a model that beats the benchmark in **both correlation & Sharpe ratio.** Still mining! ![:pick:](https://emoji.discourse-cdn.com/twitter/pick.png?v=15) ![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=15)

* * *

## ![:chart_with_upwards_trend:](https://emoji.discourse-cdn.com/twitter/chart_with_upwards_trend.png?v=15) Scaling Behavior

This entire process can be **viewed as a function of the number of trees in the search space**.  
For this experiment, I set n_estimators=2000—but **early results suggest that increasing this value improves overall performance**.

This hints at a **scaling law** , an idea that has come up in community discussions before.

* * *

## ![:handshake:](https://emoji.discourse-cdn.com/twitter/handshake.png?v=15) Join the Experiment!

This is an **open-source** project, and everyone is welcome to:  
![:heavy_check_mark:](https://emoji.discourse-cdn.com/twitter/heavy_check_mark.png?v=15) **Run their own mining experiments**  
![:heavy_check_mark:](https://emoji.discourse-cdn.com/twitter/heavy_check_mark.png?v=15) **Contribute improvements** (PRs welcome!)  
![:heavy_check_mark:](https://emoji.discourse-cdn.com/twitter/heavy_check_mark.png?v=15) **Share results & insights**

![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) **Ready to try?** Head over to **[Signal Miner on GitHub](<https://github.com/jefferythewind/signal_miner>)** and start **mining unique alpha** today!

![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=15) ![:pick:](https://emoji.discourse-cdn.com/twitter/pick.png?v=15) **Let’s Make Staking Great Again!** ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15)

---

### Post #2 — **joakim** | 2025-01-29 20:53 UTC

Consider me thoroughly impressed (though still a bit skeptical—hopefully I’m wrong as is often the case). I’ll definitely give it a try. Thanks for sharing and for the excellent write-up, readme, and model miner notebook!

---

### Post #3 — **jefferythewind** | 2025-01-30 13:59 UTC _(reply to #2)_

Thank you [@joakim](</u/joakim>) !

![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=13) Alright party people, day 2 of mining and I have currently processed a total of 112 models (not that many!) now I have a model that objectively beats the benchmark on both corr and Sharpe.

[![Screenshot 2025-01-30 at 8.45.12 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4dcc4d4d668d69aeb99c45867078622bf608353d.png)Screenshot 2025-01-30 at 8.45.12 AM848×148 7.14 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4dcc4d4d668d69aeb99c45867078622bf608353d.png> "Screenshot 2025-01-30 at 8.45.12 AM")

  


[![Screenshot 2025-01-30 at 8.45.20 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4824096899424747e707f9170cc9f9c7fdb3cfbf.png)Screenshot 2025-01-30 at 8.45.20 AM850×146 7.62 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4824096899424747e707f9170cc9f9c7fdb3cfbf.png> "Screenshot 2025-01-30 at 8.45.20 AM")

Also and interesting thing has emerged on this plot.

[![Screenshot 2025-01-30 at 8.50.07 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e007bc08a8be3422c346b6bc32c679b07b0e1fc9_2_675x500.jpeg)Screenshot 2025-01-30 at 8.50.07 AM1760×1302 159 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e007bc08a8be3422c346b6bc32c679b07b0e1fc9.jpeg> "Screenshot 2025-01-30 at 8.50.07 AM")

The benchmark model has arguably **the largest generalization error** out of any of my field of random models. This means that, for some reason, this model showed very good performance in the validation and considerably less good in the test set. The generalization error here is worse than for a randomly selected model. Why?

One way to understand it is to say this benchmark model is overfit to the validation set. High validation sharpe corresponds to lower test sharpe compared to any of the randomized models so far. You would have to be very unlucky to have picked that model. ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=13) ![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=13)

---

### Post #4 — **taori** | 2025-01-30 16:15 UTC

Very nice work, thanks for sharing

---

### Post #5 — **foolish_observer** | 2025-01-30 17:16 UTC _(reply to #3)_

I have to say very nice work indeed and props for providing the code so swiftly! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)  
I would still be interested in some comparison of “discovered” model predictions to benchmark model predictions (for uniqueness). This could be a simple correlation of the two or MMC calc. Maybe someone else has an even better idea? Because my hunch is that the new models performance is still highly correlated with the benchmark model. And the new model is just better at exploiting the same patterns.

---

### Post #6 — **jefferythewind** | 2025-01-30 18:58 UTC _(reply to #5)_

Yes certainly it seems a requested feature is more metrics to compare. It is straight forward to put any metric you like in there. Thanks for the support! The code for this actually grew out of a project I did for my doctoral work. It went into a small part of one chapter of my thesis, but I thought the conclusion was profound. I applied the logic to numerai’s data and it helped me to start seeing the problem in a new light.

Unfortunately, what happened in a previous project was that the validation vs. test scatter plot was like a round ball, zero correlation, and indeed OOS live performance was very spotty and random. Of course I didn’t produce this scatter plot until at the end of the project.

What is awesome about Numerai’s data set is that we can usually get a nice positive correlation here, which we see. Of course it depends on the model and what you’re doing with feature selection, etc.

Here is a snapshot of the best model so far…

[![Screenshot 2025-01-30 at 1.57.46 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3943a91eebb2aa4402c22ced9d426a237726275f_2_690x65.png)Screenshot 2025-01-30 at 1.57.46 PM2104×200 15.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3943a91eebb2aa4402c22ced9d426a237726275f.png> "Screenshot 2025-01-30 at 1.57.46 PM")

---

### Post #7 — **jefferythewind** | 2025-01-31 15:40 UTC

Just checking in on day 2 of mining. So far I still haven’t unearthed a better model than my previous, in terms of both corr and Sharpe, but there are now many models which beat the benchmark Sharpe on **both validation and test**. What does this mean? They scored better on validation (so we would have chosen them over the benchmark, based on validation metrics, and then they also ended up scored better on test set (OOS, in the future).

I’ve exported my best model, so far, and uploaded it to my first mining spot here.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9876d03bddb05081b19599937ae12cad96152e1.png) [numer.ai](<https://numer.ai/signalminer_1>)

### [Numerai](<https://numer.ai/signalminer_1>)

![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=13)  


[![Screenshot 2025-01-31 at 10.53.19 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/909852591094b02a4c589cf16941d46523711d30_2_682x500.jpeg)Screenshot 2025-01-31 at 10.53.19 AM1752×1284 165 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/909852591094b02a4c589cf16941d46523711d30.jpeg> "Screenshot 2025-01-31 at 10.53.19 AM")

![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=13)

Also, I added a section to the Readme about hardware, with some tips for smashing large data sets: [GitHub - jefferythewind/signal_miner: Numerai Signal Miner](<https://github.com/jefferythewind/signal_miner/tree/main?tab=readme-ov-file#hardware--resource-considerations>)

---

### Post #8 — **joakim** | 2025-02-01 04:29 UTC _(reply to #7)_

I don’t think the notebook will run without errors on Windows or MacOS due to how they handle multiprocessing differently from Linux. At least I wasn’t able to run it on my MacBook without changing it to a .py script with a main function running everything, and the multiprocessing functions at top level. And then when I run it I always run out of memory (64GB) :). My desktop is similar to yours (PopOS 22.04 with AMD Threadripper 2 and 128GB or RAM) and I plan to try it with double the swap file. I’m assuming you use CPU when mining?

---

### Post #9 — **jefferythewind** | 2025-02-01 16:00 UTC _(reply to #8)_

Thank you, [@joakim](</u/joakim>) . I am not surprised to hear that. On my system I had tried to package this whole thing into its own module. For some reason just putting all the variables that are currently in the global scope in Jupyter notebook into a class messes up how the multiprocessing and data exchange works between the processes and the memory mapped files.

I will put an emphasis somewhere that right now this only works in its current form, running it from the jupyter notebook (on Linux).

And, yes I use a CPU for this currently. This whole thing should hopefully be extended to use more model types and more architectures so I welcome you to give your best/fastest model a try. In a previous version I had tried to get this working with Murky’s GPU code. It did not work in a straightforward manner. Had to abandoned multiprocessing, I think.

---

### Post #10 — **joakim** | 2025-02-02 06:01 UTC

[![Screenshot from 2025-02-02 15-40-02](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3dc235094fb29ddb6e92f22823eb63d354818c14_2_658x500.png)Screenshot from 2025-02-02 15-40-021053×800 84.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3dc235094fb29ddb6e92f22823eb63d354818c14.png> "Screenshot from 2025-02-02 15-40-02")

  
Finally started mining, woohoo!

Have you tried to implement saving progress e.g. in an SQLite DB, with what models were found, and performance on validation and test, etc? If not, I might try to see if I can add that so one could stop mining and restart where left off, as it’s difficult to do anything else while mining. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #11 — **jefferythewind** | 2025-02-03 12:48 UTC _(reply to #10)_

Hi [@joakim](</u/joakim>) . Great progress!

So if you notice, this line will control how many concurrent processes are run at the same time in the job pool.

`pool = Pool(processes=2)`

So the reason you’re seeing all the jobs taken up on your computer is because LightGBM is designed to use as many processors as are available. I order to use less resources, you can pass the `n_jobs` parameter to the LightGBM model to give a maximum number of CPU processors that the model will use. Currently that code is in `signal_miner.py`. I will work on a way to pipe that parameter through from the notebook.

About starting/stopping mining. Currently all results are saved to the 2 memory-mapped files, so that is already working like data base.
    
    
    # Prepare memory-mapped files
    os.makedirs("results", exist_ok=True)
    mmapped_array = np.memmap(
        os.path.join("results", "test_mmapped_array.dat"),
        dtype='float16', mode='w+', shape=(len(data), len(configurations))
    )
    done_splits = np.memmap(
        os.path.join("results", "test_done_splits.dat"),
        dtype='float16', mode='w+', shape=(len(all_splits) * len(configurations))
    )
    

In a previous version I also saved the configurations locally, so you could restart from a previously unfinished program. Besides the results you also need the list of configurations specific to a particular run. I noticed I forgot to carry this over to the new version. I will put that back in.

The trick there is use a unique name for each mining run, and make the code so it doesn’t over-write past work.

Great recommendations, look for an update coming later today.

---

### Post #12 — **jefferythewind** | 2025-02-03 15:01 UTC

Signal miner update, now I’ve processed over **310 randomized** configurations, and now we have 3 models that are beating the benchmark on both corr and Sharpe.

[![Screenshot 2025-02-03 at 9.57.26 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/da658cb042a8240b10317c5f37d0228a345ac11f_2_690x61.png)Screenshot 2025-02-03 at 9.57.26 AM2464×220 18.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/da658cb042a8240b10317c5f37d0228a345ac11f.png> "Screenshot 2025-02-03 at 9.57.26 AM")

[![Screenshot 2025-02-03 at 9.58.04 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/55be8076aafd3a8b4e5eb10af216ca56c22d61fa_2_689x97.png)Screenshot 2025-02-03 at 9.58.04 AM2446×346 36.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55be8076aafd3a8b4e5eb10af216ca56c22d61fa.png> "Screenshot 2025-02-03 at 9.58.04 AM")

Seriously interesting looking alpha here, with 3 different targets.

This plot is starting to fill out, burying the benchmark deeper in the field.

[![Screenshot 2025-02-03 at 9.59.36 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fd26e9ac4eaacc4edef941aa792e89ce5384d2cb_2_670x500.jpeg)Screenshot 2025-02-03 at 9.59.36 AM1740×1298 175 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fd26e9ac4eaacc4edef941aa792e89ce5384d2cb.jpeg> "Screenshot 2025-02-03 at 9.59.36 AM")

---

### Post #13 — **joakim** | 2025-02-07 08:49 UTC

Extremely slow progress here (I’m searching a wider space) but at least I have a decent benchmark model it looks like.

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6327df14be144213b6790fe1621170648194c373.png)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/84720ac02f6590ece6f53febdc8ddfd540a75082_2_673x500.png)image1039×771 56.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/84720ac02f6590ece6f53febdc8ddfd540a75082.png> "image")

---

### Post #14 — **jefferythewind** | 2025-02-10 14:19 UTC _(reply to #13)_

Hi [@joakim](</u/joakim>) , that’s great but something appears to not be working correctly if you’re not getting more blue dots on your scatter plot. If you are still just using 2 splits, you should have 36/2 = 18 completed models, and so there should be 18 additional blue dots showing up on your scatter plot.

---

### Post #15 — **joakim** | 2025-02-11 02:22 UTC _(reply to #14)_

Thanks. You might have to push an update to the notebook, as [the one on GitHub](<https://github.com/jefferythewind/signal_miner/blob/main/Model%20Miner.ipynb>) shows it had mined 4 models, but they also don’t show up on the scatter plot.

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1354b6e10c27762e17d9ffcd528d5adab2701bef.png)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/586cab8c6867c1c7122ac8ce232d0c12c84c1cc9_2_685x500.png)image802×585 22.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/586cab8c6867c1c7122ac8ce232d0c12c84c1cc9.png> "image")

Also, ‘eval_shp’ and ‘train_shp’ I think should be ‘test_shp’ and ‘validation_shp’ respectively.

My res_df only contains the benchmark model unfortunately so I’ll stop mining for now, hoping that you’ll push an update soon. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #16 — **jefferythewind** | 2025-02-27 16:50 UTC _(reply to #13)_

[![Screenshot 2025-02-27 at 11.59.56 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c97da71fd77c202b307d7802fa9204eef318bf34_2_690x389.jpeg)Screenshot 2025-02-27 at 11.59.56 AM1920×1084 277 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c97da71fd77c202b307d7802fa9204eef318bf34.jpeg> "Screenshot 2025-02-27 at 11.59.56 AM")

# ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) Signal Miner Update: Beating the High-Bar Benchmark ![:trophy:](https://emoji.discourse-cdn.com/twitter/trophy.png?v=15)

Hey everyone,

It’s time for a **major** update on **Signal Miner**! We’ve been hard at work refining our approach, running massive models, and pushing our computational limits to uncover **optimal signal mining parameters**.

## ![:fire:](https://emoji.discourse-cdn.com/twitter/fire.png?v=15) What’s New?

### ![:heavy_check_mark:](https://emoji.discourse-cdn.com/twitter/heavy_check_mark.png?v=15) Fixed Scatter Plot Bug

The **Validation vs. Test Sharpe Scatter Plot** is one of the most important visualizations for evaluating parameter performance. However, we discovered that the **validation axis was actually displaying the whole Sharpe score** instead of the correct validation Sharpe. **This has been fixed** —so now you can fully trust this critical plot!

### ![:bar_chart:](https://emoji.discourse-cdn.com/twitter/bar_chart.png?v=15) Introducing the High-Bar Benchmark

We’ve added a **benchmark reference model** , which represents the **real challenge to beat**. This model has **seriously strong performance** :

  * **Validation Sharpe:** 2.44
  * **Test Sharpe:** 1.69



Here are its parameters:
    
    
    benchmark_cfg = {
        "colsample_bytree": 0.1,
        "max_bin": 5,
        "max_depth": 10,
        "num_leaves": 2**10,
        "min_child_samples": 10000,
        "n_estimators": 30_000,
        "reg_lambda": 0.0,
        "learning_rate": 0.001
    }
    

### ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) Expanded Search Grid

We’re pushing the search space further, with models now going up to:

  * **30K trees** ![:deciduous_tree:](https://emoji.discourse-cdn.com/twitter/deciduous_tree.png?v=15)
  * **Max depth: 16**
  * **Up to 2048 leaves** ![:leaves:](https://emoji.discourse-cdn.com/twitter/leaves.png?v=15)
  * **Min child samples: 15,000**



These are **BIG MODELS** —the kind of setups that can only be explored **with time and patience**.

### ![:checkered_flag:](https://emoji.discourse-cdn.com/twitter/checkered_flag.png?v=15) The Race to Beat the Benchmark

I’ve been running configurations **non-stop for over a week (or two?)** —only 20 configurations fully evaluated so far. **BUT** , I **already** found **one model** that **outperforms** the benchmark on **test Sharpe** , and **several others** in the same ballpark.

**With just 20 models tested, we’re already close to beating the benchmark.** At this rate, my estimate is that by **100 models** , we’ll have a **clear winner** —a setup that dominates on **both validation and test Sharpe**.

[![Screenshot 2025-02-27 at 11.48.57 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/660bd4307d142e358422b19f539a70580d339fc1_2_672x500.jpeg)Screenshot 2025-02-27 at 11.48.57 AM1600×1190 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/660bd4307d142e358422b19f539a70580d339fc1.jpeg> "Screenshot 2025-02-27 at 11.48.57 AM")

Stay tuned for more updates as this scatter plot fills out and we beat the benchmark!

Get all the latest code at the **Github Project** : [GitHub - jefferythewind/signal_miner: Numerai Signal Miner](<https://github.com/jefferythewind/signal_miner>)

---

### Post #17 — **f58c** | 2025-04-12 19:52 UTC _(reply to #12)_

That’s really cool! Have you staked any of the models? I’m finding that some of my models that perform well don’t do well on live data. But, some models that don’t perform well on the validation set have done well on live data. So far, I haven’t found a consistent way to develop models that beat the benchmark models- although some do: [Numerai](<https://numer.ai/~f58c>)

---

### Post #18 — **jefferythewind** | 2025-04-12 21:41 UTC _(reply to #17)_

All of my models use this technique to some extent, from signals, to crypto to the main tournament. Recently I have been mining for deep models, up to 30K trees, and progress has been slow. I updated the slot below slot with a pretty competitive model a few weeks ago that took between 1 and 2 months to find, you can see the inflection point in the results from when I switched to the newer model. It was a pretty obvious upgrade from the first model, which was just mined in about a week or so. So the longer you mine, the better your models will be. That’s what this framework is all about: **How to decide what will work in live?**

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ab14bca3f9cc38f9e616fde3e2e6f6599d91979c.png) [numer.ai](<https://numer.ai/signalminer_1>)

### [Numerai](<https://numer.ai/signalminer_1>)

---

### Post #19 — **jefferythewind** | 2025-04-16 13:48 UTC _(reply to #18)_

Signal Miner Update. ![:snake:](https://emoji.discourse-cdn.com/twitter/snake.png?v=14)

So its time to retire my current run, which has been going for 2 months now, and using the CPU LightGBM model, I was only able to mine 93 models according to this big grid of parameters.
    
    
    param_dict = {
        'colsample_bytree': list(np.linspace(0.001, 1, 100)), 
        'reg_lambda': list(np.linspace(0, 100_000, 10000)),
        'learning_rate': list( np.linspace(.00001, 0.3, 1000, dtype='float') ),
        'max_bin' : list(np.linspace(2, 5, 4, dtype='int')),
        'max_depth': list(np.linspace(5, 16, 12, dtype='int')),# [5, 10, 15, 20, 25, 50, 100],
        'num_leaves': list(np.linspace(4, 2048, 2044, dtype='int')),#, 4112],#, 8192, 32768],
        'min_child_samples': list( np.linspace(1,15000,15000,dtype='int') ),
        'n_estimators': list( np.linspace(10,max_trees,max_trees-10,dtype='int') ),#,75,100,150,200],#, 500, 700, 900, 1200], 
        'target':targets,
    }
    

We plot these on the Sharpe ratio plot, comparing past to future performance, and indicate the benchmark model with a red star.

[![Screenshot 2025-04-16 at 9.35.29 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5ef4197b5ed261c5738123d8bebe5afff2f1bf20_2_682x500.jpeg)Screenshot 2025-04-16 at 9.35.29 AM1782×1306 155 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5ef4197b5ed261c5738123d8bebe5afff2f1bf20.jpeg> "Screenshot 2025-04-16 at 9.35.29 AM")

**Evaluation**

An interesting to notice, which is very common, is that the best performing model from the validation set is **not** the best performing model from the test set. Even the benchmark outperforms on validation (past), while there were other models that end up performing better in the future.

The overall objective was to find a model that outperformed on both folds of the data. The speed I was running here was just too slow, I don’t have that much time. 93 models? We should be doing this in a day or less. However, even these models are producing MMC. A few weeks ago I put a small ensemble of these models online, and they have have been doing well. In the signal miner code, you can export ensembles easy with this line.

`to_export = res_df.sort_values('whole_shp').iloc[-10:].index.tolist() #can be a list to ensemble`

Here I export an ensemble of 10 models, based on which performed best in Sharpe on the whole data set.

**Next Iteration**

I’ve recently learned that a lot of progress has been made in GPU-based GBMs that run super fast compared the CPU-based LGBM, which in the past had been more competitive. CatBoost runs super fast, and I will spin up a new version of the signal miner with CatBoost on GPU. As always, we will get fresh new alpha.

I’ve also developed a fresh new GPU-powered GBM called **WarpGBM** , in collaboration with [@fraulty](</u/fraulty>). It is already comparable in speed to LightGBM, XGBoost and CatBoost on the GPU, but we are aiming for the #1 position in that category. The simplicity of our code is going to enable next-level customization and warp-speed domain generalization.

Stay tuned.

[github.com](<https://github.com/jefferythewind/warpgbm>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4a70830b29ce7212f400fb2a924c1b6d45f346e2_2_690x344.png)

### [GitHub - jefferythewind/warpgbm: WarpGBM: High-Speed Gradient Boosting](<https://github.com/jefferythewind/warpgbm>)

WarpGBM: High-Speed Gradient Boosting
