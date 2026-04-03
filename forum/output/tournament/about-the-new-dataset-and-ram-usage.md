---
title: "About the new dataset and RAM usage"
category: Tournament
url: https://forum.numer.ai/t/about-the-new-dataset-and-ram-usage/4176
created_at: 2021-09-21T11:53:58.412000+00:00
last_posted_at: 2022-02-15T15:37:57.453000+00:00
posts_count: 5
views: 2683
tags: []
---

# About the new dataset and RAM usage

---

### Post #1 — **rngguy** | 2021-09-21 11:53 UTC

Hi everybody,

I saw that some users complained about the RAM usage after the “super massive data” release. I experienced some crashes when trying to fit LightGBM models but finally managed to make it work under 16GB memory. I wanted to share my experience because it might help somebody here, one day…

At first, I was just loading the `int8` Parquet training file with Pandas (so far so good). Then, when passing the DataFrame to the `train` method of LightGBM, the memory usage went above my computer limits. According to issue [#1032](<https://github.com/microsoft/LightGBM/issues/1032>), with the Python package, LightGBM internally converts values to `float32`, hence the memory explosion. A solution to avoid this is to save data to a CSV file and construct a Dataset object from that file.

Now, one might say “ok, that’s easy, Numerai already provides training data in CSV format”. Well, even when set to be ignored, the `id` and `era` columns trigger errors because, as per the documentation: “despite the fact that specified columns will be completely ignored during the training, they still should have a valid format allowing LightGBM to load file successfully”.

So, I simply selected the target and the features from the Parquet file and saved them to CSV using the PyArrow library (which was much faster than using Pandas). However, I am pretty sure there’s a clever way to generate an adequate CSV file by filtering columns from the Numerai CSV file with a Linux command (but I haven’t checked it yet).

And I could finally perform some hyperparameter search.

On a side note, if you want to delete a Dataset object and create a new one, you might encounter some high memory usage because of issue [#4239](<https://github.com/microsoft/LightGBM/issues/4239>): a memory leakage happens since version 3.0.

That’s it!

---

### Post #2 — **autratec** | 2021-09-21 12:51 UTC

I still feel numer.ai moving towards the wrong direction. Providing new mass data set raised bar to get data scientist participate in this game. We should suppose get game easier, and convenient, and attract more participants, which help increase the usage of NMR and its value.

---

### Post #3 — **rigrog** | 2021-09-21 16:53 UTC

I’ll tell how I’m handling “super massive”: I’m collapsing it down to approximately “legacy” size.

The motivation, for the radical surgery that follows, can be seen quite plainly in the graph of inter-feature correlations, displayed in the cell “Out[7]” of analysis_and_tips.ipynb . Take a look at it! It shows 25 visually indistinguishable squares – no speck or squiggle out of place, in any of those 25 squares! Props to Numerai, for putting this redundancy front and center. They could very easily have obfuscated it.

For each “longRow”, of 1,050 int8 features (0, 1, 2, 3, or 4), I do:
    
    
    shortRow = [sum( longRow[j : : 210] ) for j in range(210)]
    

Now I have 210 features, each with a value from 0 to 20 – which still fits in an int8.

Due to the high correlation, I wasn’t much surprised to find almost half the cells (in the 4.4M by 210 feature array) occupied by a whole multiple of 5 (i.e. 0, 5, 10, 15, or 20: what you’d get by adding 5 identical feature values). What did surprise me, was that 0 and 20, which can only be 0+0+0+0+0 or 4+4+4+4+4, each occupy 1/8 of the cells!

So if (like me) you have just a little more than enough RAM for the legacy tourney, you can probably squeeze in this 210 feature version of the super-massive. You won’t get much advantage (over legacy) feature-wise, but you will be in a significantly more “target rich environment” (a greater proportion of the rows are labeled with target values).

If you have abundant RAM, like 64 Gb and up, with a fleet of cores and GPU’s: maybe a 210-feature model could contribute to your grand ensemble.

---

### Post #4 — **adam19** | 2021-12-15 21:13 UTC _(reply to #3)_

Hi there. I’m trying to implement this idea but can’t seem to get the run time down to a useable level. Does anyone have any tips to do this quickly in python?

---

### Post #5 — **bobyfisch** | 2022-02-15 15:37 UTC

hi [@rngguy](</u/rngguy>) !

Could you send us a code snipet for the modifications you introduce to get LGBM to load your .CSV? is it some feature reduction similar to what [@rigrog](</u/rigrog>) proposes?
