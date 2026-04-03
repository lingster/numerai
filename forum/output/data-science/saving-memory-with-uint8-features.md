---
title: "Saving memory with uint8 features"
category: Data Science
url: https://forum.numer.ai/t/saving-memory-with-uint8-features/254
created_at: 2020-04-23T21:14:54.588000+00:00
last_posted_at: 2022-12-20T03:33:33.424000+00:00
posts_count: 2
views: 2797
tags: []
---

# Saving memory with uint8 features

---

### Post #1 — **jrb** | 2020-04-23 21:14 UTC

I’ve noticed that there have been quite a few complaints in the chat rooms about memory usage on compute since the test set got bigger. I’d originally contributed the float16 patch to `example_model.py` to help alleviate this, a couple of months ago. I just realized that there’s a simple way improve on this and to nearly halve the memory usage in your inference pipeline if you’re using a tree based classifier (Xgboost, Catboost, Lightgbm, etc).

We just need to rescale the features and cast them to `uint8`. This further halves the memory usage for feature columns. Note that trick won’t work on the target column because that’s still a floating point value.  
The intuition is that with tree based models like XGBoost, rescaling the inputs (and training the model with the rescaled) won’t affect the model’s performance.

I’ve tested this on `example_model.py` and verified that it generates the same predictions with and without the change. To try this for yourself, simply replace the `read_csv` function in `example_predictions.py` (or your derivative thereof) with the following function:
    
    
    def read_csv(file_path):
        to_uint8 = lambda x: np.uint8(float(x) * 4)
        with open(file_path) as f:
            column_names = next(csv.reader(f))
        dtypes = {TOURNAMENT_NAME: np.float16}
        converters = {x: to_uint8 for x in column_names if x.startswith('feature')}
        return pd.read_csv(file_path, dtype=dtypes, converters=converters).set_index("id")

---

### Post #3 — **anakin_sky_walker** | 2022-12-20 03:33 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) jrb:

> `np.uint8`

Can I ask, is this working on the training process? It seems to me 32GB RAM still not sufficient for the full datasets.
