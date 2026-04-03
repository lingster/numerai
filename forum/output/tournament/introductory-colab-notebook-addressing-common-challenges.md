---
title: "Introductory Colab Notebook Addressing Common Challenges"
category: Tournament
url: https://forum.numer.ai/t/introductory-colab-notebook-addressing-common-challenges/2154
created_at: 2021-03-05T00:40:13.602000+00:00
last_posted_at: 2022-06-14T21:32:01.866000+00:00
posts_count: 8
views: 2325
tags: []
---

# Introductory Colab Notebook Addressing Common Challenges

---

### Post #1 — **dliden** | 2021-03-05 00:40 UTC

Hello,

I’ve put together a google colab notebook covering the following topics:

  * Handling numerapi API keys in colab without _too much_ friction
  * Managing memory (trying to read the tournament dataset all in one go tends to crash colab)
  * Fitting models: the notebook includes a fastai tabular learner and a scikit-learn regression model
  * Evaluating model performance with average per-era correlation and Sharpe score
  * Generating and formatting predictions and submitting them to the competition with numerapi



You can access the notebook from the link below or from the [github repository](<https://github.com/djliden/numerai_starter_kit>).

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github/djliden/numerai_starter_kit/blob/main/Numerai_Starter_Kit.ipynb>)

Any feedback on ways to make this a more useful resource would be appreciated. It mostly focuses on topics I found challenging during my first few weeks of working on numerai.

The intent of this project is twofold:

  1. Walking new users through the whole process of getting the current data, fitting a model, making predictions, and submitting to the competition; and
  2. Helping those who want to take advantage of colab GPUs but have found it inconvenient or difficult to deal with secret keys and/or colab’s memory limitations.

---

### Post #2 — **mrquantsalot** | 2021-03-07 05:34 UTC

I copied and worked through this notebook it all worked for me out of the box. I thought it was a great introduction that went through all of the steps from data to submitting.

Instead of saving the API credentials in a .env I found it easier to save it as a json file and then just add that filename to my .gitignore.

---

### Post #3 — **dliden** | 2021-03-07 21:55 UTC _(reply to #2)_

Thanks for the comment! That’s a good point – that’s what I do with the `.env` file (include in `.gitignore`), but I didn’t mention it in this notebook. I’ll add a note about that; I think it would be a helpful addition.

---

### Post #4 — **feroxolas** | 2021-03-08 15:54 UTC

Thanks for the tips! I also found that I also needed to batch the predictions in order not to crash colab. Currently, I’m training XGBoost on smaller subsets of data (which isn’t ideal) to prevent colab from crashing. Any tips to getting around this, especially if I want to do cross validation without having to use super small training subsets or excessive calculation times?

---

### Post #5 — **dliden** | 2021-03-13 17:07 UTC _(reply to #4)_

Just wanted to say that I did see your question [@feroxolas](</u/feroxolas>) . I haven’t tried XGBoost in colab yet but I will let you know when I do and if I’m able to find a way to run it without crashing colab or compromising on training sample size.

---

### Post #6 — **mrquantsalot** | 2021-03-14 17:48 UTC _(reply to #4)_

I found and ran this notebook [Numerai tournamentベースライン | Kaggle](<https://www.kaggle.com/code1110/numerai-tournament>) in google colab and it worked fine. They do use LGB instead of XGBoost. They cast the features to int8 to save space. They commented out the XGBoost, so I assume it worked since the rest of the code did. The LGMBRegressor worked when I ran it.
    
    
    mapping = {0.0 : 0, 0.25 : 1, 0.5 : 2, 0.75 : 3, 1.0 : 4}
    for c in feature_cols:
        df[c] = df[c].map(mapping).astype(np.uint8)

---

### Post #7 — **dliden** | 2021-04-05 21:00 UTC

Hello,

I’ve made an updated version of the notebook (leaving the old as-is for reference) that incorporates a few improvements in the initial data processing stages. In both notebooks, the “validation” eras from the tournament CSV are concatenated to the training dataset as this format is, in my opinion, easier to use with the common statistics and ML libraries (especially since memory constraints make it impossible to have both datasets loaded in memory in colab at the same time). There are two changes to this process in the new version:

  1. The processed csv (training + validation eras) is saved as a .pkl file instead of as a csv. The saving and loading are much faster after this change.
  2. The processing step – loading the tournament data, extracting validation eras, and concatenating with the training data – is now done using the `dask` library. This results in substantial speed improvements over reading the csv in chunks using pandas.



Overall, this cut the data preprocessing stage down to less than 1.5 minutes from a ridiculous 4.5ish minutes, and it still works within the constraints of Colab’s RAM limits.

A few other modest changes: I commented out the cells for making submissions to prevent accidental submissions when running through the whole notebook. I also changed the metric used by the `fastai` model from Pearson’s to Spearman’s correlation. I added a brief note about putting a `.env` file in the `.gitignore` for those who choose to use `python-dotenv`.

Link to new notebook: [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github/djliden/numerai_starter_kit/blob/main/Numerai_Starter_Kit_V2.ipynb>)

And the [github repository](<https://github.com/djliden/numerai_starter_kit>).

---

### Post #8 — **svendaj** | 2022-06-14 21:32 UTC _(reply to #7)_

Unfortunately with **latest V4 dataset it is not working** in Colab anymore due to RAM limits. I have stopped using Colab at all and most my notebooks now run in [kaggle](<https://www.kaggle.com/>) which have RAM limit at 16GB. Even with that it needs or downcasting or using “_int8” datasets.  
Also [official First submission notebook](<https://numer.ai/notebook>) will not finish in Colab due to RAM. I have created [copy of that notebook](<https://www.kaggle.com/code/svendaj/first-submission-on-numer-ai>) in kaggle with downcasting to fit into 16GB.
