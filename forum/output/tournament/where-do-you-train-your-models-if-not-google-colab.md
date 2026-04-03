---
title: "Where do you train your models (if not Google Colab)"
category: Tournament
url: https://forum.numer.ai/t/where-do-you-train-your-models-if-not-google-colab/7194
created_at: 2024-03-31T19:22:04.566000+00:00
last_posted_at: 2024-09-19T20:21:32.929000+00:00
posts_count: 12
views: 2039
tags: []
---

# Where do you train your models (if not Google Colab)

---

### Post #1 — **nathanganser** | 2024-03-31 19:22 UTC

As I’m starting to work with the larger datasets, my Google Colab functions are taking hours to run and thus disconnecting me in between when I leave my laptop.

Is there another tool out there that can run a jupyter notebook in the background? What are you using?

Thanks!

---

### Post #2 — **svendaj** | 2024-04-05 14:56 UTC

I am using and recommend [Kaggle](<https://www.kaggle.com/>). Not only that you can run for free [jupyter notebooks with 4 CPUs and 30GB RAM (max 12 hours run each, 5 notebooks in parallel)](<https://www.kaggle.com/docs/notebooks#technical-specifications>), but thanks to [Kaggle API](<https://www.kaggle.com/docs/api>) you can fully automatize your pipeline. On top, there is great community and possibility to learn more from competitions.

I have created a few public notebooks and datasets to simplify first steps for Numerai Tournament participants:

  * weekly updated dataset with latest data, so that you do not need to download them each time: 
    * [**V4.3 Midnight**](<https://www.kaggle.com/datasets/svendaj/numerai-v4-3-midnight>) \- latest data, notebook producing the dataset: [numerai data v4.3 Midnight (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-data-v4-3-midnight>)
    * **V4.2 Rain**, notebook producing the dataset: [numerai data v4.2 Rain (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-data-v4-2-rain>)
    * [**Older V4 and V4.1**](<https://www.kaggle.com/datasets/svendaj/numerai-latest-tournament-data>) and notebook producing the dataset: [numerai data (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-data>)
  * Example models - typically forks of Numerai example models with improvements for better results: 
    * [Hello Numerai automated (kaggle.com)](<https://www.kaggle.com/code/svendaj/hello-numerai-automated>), with upload via NumerAPI, model is also staked so you can check its performance on leaderboard ( [JOS_KAGGLE_HELLO - Numerai](<https://numer.ai/jos_kaggle_hello>) and improved version [JOS_KAGGLE_SHATTER - Numerai](<https://numer.ai/jos_kaggle_shatter>))
    * [numerai Feature Neutralization (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-feature-neutralization>) \- example model with feature neutralization, [JOS_KAGGLE_MEDIUM_FN - Numerai](<https://numer.ai/jos_kaggle_medium_fn>)
    * [numerai Target Ensemble (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-target-ensemble>) \- example model of target ensembling, [JOS_KAGGLE_MEDIUM_TE - Numerai](<https://numer.ai/jos_kaggle_medium_te>)
    * [Numerai Example Model Sunshine (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-example-model-sunshine>) \- older more complex example model, [JOS_KAGGLE_SUNSHINE - Numerai](<https://numer.ai/jos_kaggle_sunshine>)
  * Kaggle automation tips: 
    * [Triggering notebook execution by webhook with Flask and Kaggle API | Kaggle](<https://www.kaggle.com/discussions/questions-and-answers/397468>)
    * [Scheduling notebook execution with cron and Kaggle API | Kaggle](<https://www.kaggle.com/discussions/product-feedback/371090>)
    * [Running pipeline of notebooks with Kaggle API](<https://www.kaggle.com/code/svendaj/running-pipeline-of-notebooks-with-kaggle-api>)

---

### Post #3 — **nathanganser** | 2024-04-05 17:24 UTC _(reply to #2)_

Thank you! I’ll review this!!!

---

### Post #4 — **dfrank** | 2024-05-03 07:10 UTC _(reply to #2)_

Thank you! Also a new user exploring ways to train models (turns out my ~10 year old gaming rig can’t handle much past the “small” feature set)

---

### Post #5 — **ambrul11** | 2024-05-07 13:18 UTC

Also using [kaggle.com](<http://kaggle.com>). Highly convenient option

---

### Post #6 — **smilence666** | 2024-05-10 16:44 UTC _(reply to #2)_

I train it on my local computer and use a batch script to submit dailly.

---

### Post #8 — **datahunter** | 2024-08-26 18:51 UTC _(reply to #2)_

This is very useful, thank you so much

---

### Post #9 — **nathanganser** | 2024-08-26 19:04 UTC

Update on my end:

  * I’ve tested many options (including Kaggle, but 30GM of RAM is limiting)
  * I now exclusively use <https://brev.dev/> which has super cheap GPUs and using `screen` you can easily leave your process running in the background for days and and get the model once the process is done.



Highly recommend that!

---

### Post #10 — **svendaj** | 2024-08-27 19:10 UTC

Some guys are using [Rent GPUs | Vast.ai](<https://vast.ai/>) as most price effective GPU option.

---

### Post #11 — **gammarat** | 2024-08-28 13:59 UTC

I found it useful to have my programs periodically save relevant parameters to files. For example with my basic Numerai program I save parameters every 250 iterations to files named by the iteration number (like “XXXXX.mat”, where XXXXX is the iteration number, and “mat” because I use MatLab). In my case 250 iterations represents about 1/2 hour of processing, so there’s not much lost if for some reason or another processing is interrupted.

That also allows you to branch off downstream programs from pretty much where one likes.

FWIW I train my models at home, and the few times (for other projects) I’ve used Colab I used Google Drive for data storage.

---

### Post #12 — **gregbowers** | 2024-09-17 08:29 UTC

This is very useful, thank you so much ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=12)

---

### Post #13 — **shi_luo** | 2024-09-19 20:21 UTC

I’m experimenting with PaperSpace Gradient. It’s like Colab but with ‘unlimited’ GPUs with monthly subscription. I’m currently trying to build the correct virtual environments on Gradient so the pickled model is consistent with Numerai Evaluation. If it do work well, I’m guessing it would be a solid place for high-ram GPU training!
