---
title: "A more clear understanding of the Ranked Correlation"
category: Data Science
url: https://forum.numer.ai/t/a-more-clear-understanding-of-the-ranked-correlation/1387
created_at: 2020-12-27T18:11:00.346000+00:00
last_posted_at: 2021-04-01T19:58:54.193000+00:00
posts_count: 6
views: 2922
tags: []
---

# A more clear understanding of the Ranked Correlation

---

### Post #1 — **pumplerod** | 2020-12-27 18:11 UTC

I’m trying to get a better understanding of the spearman ranked correlation as it relates to our target and predictions.

I went down this rabbit hole trying to build the spearman correlation function to use within TensorFlow, and cannot seem to get the values to correspond with results from scipy.stats.spearmanr()

  1. since our target data is segmented into values which will tie (0.0, 0.25, 0.5, 0.75, 1.0), how is the rank calculated for the target values?
  2. why is the rank on so many ties useful?
  3. has anyone recreated spearman rank correlation with TensorFlow? I have found a few examples out there, none of which provide results matching scipy.stats.spearmanr()
  4. am I correct in my understanding that this should be a matter of A: rank predictions, B: rank targets, C: generate a pearson correlation value from these ranked sets?

---

### Post #2 — **jrb** | 2020-12-27 22:02 UTC

The targets are already ranked, all you need to do is rank your predictions and then compute Pearson’s correlation coefficient between your ranked predictions and the targets. It might be instructive to look at [this block](<https://github.com/numerai/example-scripts/blob/master/example_model.py#L20-L28>) of code in the example model. Here’s a quick and dirty snippet of code that does the same thing with Tensorflow.
    
    
    import tensorflow as tf
    import numpy as np
    import pandas as pd
    
    def correlation(predictions, targets):
        """
        From:
        https://github.com/numerai/example-scripts/blob/master/example_model.py#L21
        """
        if not isinstance(predictions, pd.Series):
            predictions = pd.Series(predictions)
        ranked_preds = predictions.rank(pct=True, method="first")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    
    def corrcoef(x, y):
        """
        np.corrcoef() implemented with tf primitives
        """
        mx = tf.math.reduce_mean(x)
        my = tf.math.reduce_mean(y)
        xm, ym = x - mx, y - my
        r_num = tf.math.reduce_sum(xm * ym)
        r_den = tf.norm(xm) * tf.norm(ym)
        return r_num / (r_den + tf.keras.backend.epsilon())
    
    def tf_correlation(predictions, targets):
        ranked_preds = tf.cast(tf.argsort(tf.argsort(predictions, stable=True)), targets.dtype)
        return corrcoef(ranked_preds, targets)
    
    targets = np.array([0.0, 0.25, 0.5, 0.75, 1.0], dtype=np.float32)
    predictions = np.random.rand(targets.shape[0])
    
    print(correlation(predictions, targets))
    print(tf_correlation(tf.convert_to_tensor(predictions), tf.convert_to_tensor(targets)))
    

One more thing: The `tf_correlation` function isn’t differentiable, which makes it rather useless if you want to use it in a loss function. Also, the code above was quite hastily written in response to your post (although, I did run it in a notebook to verify that `np` and `tf` return the same number), so you might want to review it a couple of times before using it.

---

### Post #3 — **pumplerod** | 2020-12-28 19:10 UTC _(reply to #2)_

This is a huge help. Thank you! I was missing the critical tf.norm() which, to be honest, I don’t fully understand. It looks like you have these in place of a standard deviation call. And I’m not entirely sure what calling the nested argsort() is doing.

I guess it’s the argsort() that prevents the function from being differentiable, but at least I can use it for a metric, which will help. I think I can use standard pearson correlation for the loss function as I’m not likely to get to a full 1.0 correlation in either case.

---

### Post #4 — **jrb** | 2020-12-29 08:06 UTC _(reply to #3)_

`tf.norm()` computes the euclidean norm of a vector. The `corrcoef` function corresponds to _Eq.3_ on the [wikipedia page](<https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>) for Pearson’s correlation coefficient. And yes, `argsort()` isn’t differentiable. Calling `argsort(argsort(x))` on a sequence `x`, returns a sequence of its ranks.

---

### Post #5 — **ccc513** | 2021-03-29 04:33 UTC

[@jrb](</u/jrb>) When you say “the targets are already ranked”, is that the same as saying they’re on a percentile scale 0 < target <= 1? If so, what about the target values which are identically zero?

---

### Post #6 — **factorsparsity** | 2021-04-01 19:58 UTC _(reply to #5)_

Have a look at [this thread](<http://forum.numer.ai/t/are-predictions-discrete-or-continuous/1157>). It gives a good explanation of how the ranking works.
