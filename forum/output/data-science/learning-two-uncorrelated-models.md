---
title: "Learning Two Uncorrelated Models"
category: Data Science
url: https://forum.numer.ai/t/learning-two-uncorrelated-models/400
created_at: 2020-05-14T22:13:02.599000+00:00
last_posted_at: 2020-09-09T13:14:09.930000+00:00
posts_count: 17
views: 6674
tags: []
---

# Learning Two Uncorrelated Models

---

### Post #1 — **richai** | 2020-05-14 22:13 UTC

Numerai is really just about finding some function (a model) that maps the features to a vector of predictions.

Imagine instead Numerai posed the following problem: learn a function that maps the features to _two_ prediction vectors such both prediction vectors have equal performance but have a correlation of zero with each other.

How would you learn two such predictions at the same time? If your two models have zero correlation with each other over the training data, how do you feel confident that they will have zero correlation out of sample?

Since by construction, your two models are uncorrelated, they are likely to have very different feature exposures eg one might heavily weight the intelligence group of features and the other might heavily weight the charisma features. Therefore the two models are likely to combine very well together. In fact, you might take both your models and sum them together and use that as your model. Does this combination of the two uncorrelated predictions outperform your best model? It might have lower mean but does it have higher Sharpe and better consistency and stationarity?

Numerai’s new Meta Model Contribution payouts launching soon opens up the value of models which aren’t simply good at mapping from the features to predictions but are also uncorrelated with the meta model. Trying to build two models that are both good but perfectly uncorrelated out of sample is a worthwhile exercise to get good at MMC. Perhaps one of the two or both of the two models you build in this way will have strong MMC.

---

### Post #2 — **jrb** | 2020-05-14 22:54 UTC

This isn’t quite what you’re suggesting, but tangentially related. In my attempt at an MMC maximizing model, I have a penalty term in my loss function for correlation with example predictions. I got a reasonably low correlation (0.4243) with example predictions, which could’ve perhaps be pushed lower if it wasn’t for early stopping.

---

### Post #3 — **richai** | 2020-05-15 00:48 UTC _(reply to #2)_

That’s a great idea.

How did you implement the loss function against correlation with example predictions? Would you care to share that code? If you are training to maximize MMC in sample, does it end up staying uncorrelated with example predictions out of sample when cross validated?

---

### Post #4 — **jrb** | 2020-05-15 09:35 UTC

Thanks! I wasn’t trying to directly maximise MMC, only to minimize correlation with example predictions and to maximize rank correlation with the labels. My first attempt was to try to use JAX’s version of `np.corrcoef`, but it isn’t differentiable. As it turned out, the formula for Pearson’s correlation coefficient translates directly into simple differentiable code.
    
    
    import jax.numpy as jnp
    
    def correlation(x, y, axis=-1):
        mx = jnp.mean(x, axis=axis)
        my = jnp.mean(y, axis=axis)
        xm, ym = x - mx, y - my
        r_num = jnp.mean(xm * ym, axis=axis)
        r_den = jnp.std(xm, axis=axis) * jnp.std(ym, axis=axis)
        return r_num / (r_den + jnp.finfo(float).eps)
    

This can be directly dropped into the loss function as a weighted term. Maximizing rank correlation builds on this, but needs a differentiable ranking function (which is a big ball of hair). The final loss function is a weighted sum of a regression loss (MSE), ranking loss and the aforementioned penalty for correlation with example predictions.

I’ve also tried minimizing feature correlations directly with this, but it’s excruciatingly slow and it’s easier and far more efficient to enforce feature sparsity with L1 regularization.

And yes, once the loss weights are properly tuned, the decorrelation with example predictions transfers fairly well, out of sample.

---

### Post #5 — **no_formal_agreement** | 2020-05-17 07:34 UTC

**Edit made a mistake in the code, its fixed now**

Well might as well start off with the obvious solution: PCA features. Given the outputs of PCA must by definition be uncorrelated with each other, a set of linear models trained on different principal components should have low correlation to one another. Below is the sample code to test this hypothesis:
    
    
    
    import pandas as pd
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LinearRegression
    from scipy import stats
    
    
    def get_spearman_by_era(p,target,eras):
        
        df = pd.DataFrame(columns = ('p','target','eras'))
        df.loc[:,'p'] = p
        df.loc[:,'target'] = target
        df.loc[:,'eras'] = eras
        era_names = df.eras.unique()
        output_dict = dict()
        for i in era_names:
            p0 = df.loc[df.eras == i,'p']
            target0 = df.loc[df.eras == i,'target']
            output_dict[i] = stats.spearmanr(p0,target0)
        return output_dict
    
    def get_sharpe_ratio(spearmans):
        output = np.zeros((len(spearmans)))
        j = 0
        for i in spearmans:
            output[j] = spearmans[i][0]
            j = j + 1
        return np.mean(output)/np.std(output)
    
    
    print('loading files')
    numerai_training_data = pd.read_csv("Input/numerai_training_data.csv")
    numerai_tournament_data = pd.read_csv("Input/numerai_tournament_data.csv")
    numerai_validation_data = numerai_tournament_data.loc[numerai_tournament_data.data_type == "validation"]
    
    eras_train = numerai_training_data.loc[:,'era']
    eras_valid = numerai_validation_data.loc[:,'era']
    
    print('transforming data')
    X_train = numerai_training_data.loc[:,'feature_intelligence1':'feature_wisdom46'].values
    X_valid = numerai_validation_data.loc[:,'feature_intelligence1':'feature_wisdom46'].values
    
    
    Y_train = numerai_training_data.loc[:,'target_kazutsugi'].values
    Y_valid = numerai_validation_data.loc[:,'target_kazutsugi'].values
    
    
    pca = PCA(svd_solver='full')
    pca.fit(X_train)
    
    X_train_pca = pca.transform(X_train)
    X_valid_pca = pca.transform(X_valid)
    
    
    models = list()
    p_train = list()
    p_valid = list()
    
    num_models = 5
    
    for i in range(num_models):
    
        X = np.c_[X_train_pca[:,i],X_train_pca[:,i+num_models],X_train_pca[:,i+num_models*2],X_train_pca[:,i+num_models*3],X_train_pca[:,i+num_models*4]]
        models.append(LinearRegression().fit(X,Y_train))
        p_train.append(models[i].predict(X))
        p_valid.append(models[i].predict(np.c_[X_valid_pca[:,i],X_valid_pca[:,i+num_models],X_valid_pca[:,i+num_models*2],X_valid_pca[:,i+num_models*3],X_valid_pca[:,i+num_models*4]]))
        
        spearman_by_era = get_spearman_by_era(p_train[i],Y_train,eras_train)
        spearman_by_era_valid = get_spearman_by_era(p_valid[i],Y_valid,eras_valid.reset_index(drop =True))
        print('Spearmans')
        print(stats.spearmanr(p_train[i],Y_train))
        print(stats.spearmanr(p_valid[i],Y_valid))
        print('Sharpe Ratios')
        print(get_sharpe_ratio(spearman_by_era))
        print(get_sharpe_ratio(spearman_by_era_valid))
        print('')
        
    corr_train = np.corrcoef(p_train)
    corr_valid = np.corrcoef(p_valid)
    
    print('Correlation Coeficients')
    print(np.corrcoef(p_train))
    print(corr_train)
    print(corr_valid)
    
    
    

With the resulting output being:

loading files  
transforming data  
Spearmans  
SpearmanrResult(correlation=0.01497619233887175, pvalue=2.6928745376728484e-26)  
SpearmanrResult(correlation=0.013284837628533032, pvalue=1.4017169427249316e-05)  
Sharpe Ratios  
0.6599993421219399  
0.48983802341438826

Spearmans  
SpearmanrResult(correlation=0.010373654196207392, pvalue=2.0012757690323247e-13)  
SpearmanrResult(correlation=0.012355041163440845, pvalue=5.355087706273797e-05)  
Sharpe Ratios  
0.5710633677918008  
0.5557453873478579

Spearmans  
SpearmanrResult(correlation=0.020850179835250258, pvalue=2.2366481230283833e-49)  
SpearmanrResult(correlation=0.006082960200549018, pvalue=0.046722525083223526)  
Sharpe Ratios  
0.6798675967774218  
0.20818493808291985

Spearmans  
SpearmanrResult(correlation=0.012221942605479852, pvalue=4.795609428680984e-18)  
SpearmanrResult(correlation=0.00434274497569329, pvalue=0.1556537105563265)  
Sharpe Ratios  
0.4294696314411901  
0.2230339401171146

Spearmans  
SpearmanrResult(correlation=0.01383767783987328, pvalue=1.094686955408993e-22)  
SpearmanrResult(correlation=0.00010391446593068246, pvalue=0.9728976999576355)  
Sharpe Ratios  
0.5734665431860216  
0.008617590297056693

Correlation Coeficients  
[[ 1.00000000e+00 -6.57942828e-16 4.68513837e-16 -5.40879164e-16  
-1.09616316e-15]  
[-6.57942828e-16 1.00000000e+00 -4.43714100e-16 4.01355067e-16  
9.56080427e-16]  
[ 4.68513837e-16 -4.43714100e-16 1.00000000e+00 -9.55135609e-16  
-4.48100911e-16]  
[-5.40879164e-16 4.01355067e-16 -9.55135609e-16 1.00000000e+00  
4.84548276e-16]  
[-1.09616316e-15 9.56080427e-16 -4.48100911e-16 4.84548276e-16  
1.00000000e+00]]  
[[ 1.00000000e+00 -6.57942828e-16 4.68513837e-16 -5.40879164e-16  
-1.09616316e-15]  
[-6.57942828e-16 1.00000000e+00 -4.43714100e-16 4.01355067e-16  
9.56080427e-16]  
[ 4.68513837e-16 -4.43714100e-16 1.00000000e+00 -9.55135609e-16  
-4.48100911e-16]  
[-5.40879164e-16 4.01355067e-16 -9.55135609e-16 1.00000000e+00  
4.84548276e-16]  
[-1.09616316e-15 9.56080427e-16 -4.48100911e-16 4.84548276e-16  
1.00000000e+00]]  
[[ 1.00000000e+00 -3.81042255e-02 3.84405057e-03 -3.95131357e-02  
-5.40280742e-03]  
[-3.81042255e-02 1.00000000e+00 -9.78007427e-04 1.06135805e-02  
-1.03187024e-02]  
[ 3.84405057e-03 -9.78007427e-04 1.00000000e+00 4.45218610e-02  
-7.32469233e-03]  
[-3.95131357e-02 1.06135805e-02 4.45218610e-02 1.00000000e+00  
-4.22985841e-02]  
[-5.40280742e-03 -1.03187024e-02 -7.32469233e-03 -4.22985841e-02  
1.00000000e+00]]

The highest correlation coefficient between any of the five models is ~0.045. The out of sample correlation is also very similar to the in sample correlation. So that answers the question of whether samples generated this way will maintain there orthogonality. None of these models are particularly ‘good’ though so I wouldn’t ever recommend staking on an individual one of them however this does demonstrate that creating multiple positive Sharpe uncorrelated predictions is pretty trivial. Despite the fact that there is probably a way to game MMC with very large numbers of these types of models, I don’t know if there is any benefit to numerai having large numbers of models like this…

---

### Post #6 — **zempe** | 2020-05-17 19:51 UTC _(reply to #2)_

Sorry for the silly question but what do you refer as example predictions? you mean validation data in the tournament df?

---

### Post #7 — **kainsama** | 2020-05-17 20:02 UTC _(reply to #6)_

here: <https://numer.ai/integration_test>

---

### Post #8 — **arbitrage** | 2020-05-18 15:00 UTC _(reply to #6)_

the dataset zip includes training data, tournament data and a csv file of the predictions made from the example model which is also found in the zip.

---

### Post #9 — **richai** | 2020-06-18 18:14 UTC _(reply to #5)_

I played around with your code here and got similar results. Do these models combine well when you add them together?

One thing I found generating models in this way with the PCA features is that although the predictions would be uncorrelated the performance would be very correlated. For example, model1 and model2 could have no prediction correlation but fail or win on the exact same eras meaning they didn’t stack well. I would re-phrase my original question as can you build two models whose era scores are uncorrelated. These models will tend to work very well when combined.

Era boosting ([Era Boosted Models](<http://forum.numer.ai/t/era-boosted-models/189>)) works in some ways by building many of these performance uncorrelated models.

I think era boosting approaches outperform example predictions and the median staking Numerai user isn’t beating example predictions so I think many users could benefit from these techniques.

---

### Post #10 — **no_formal_agreement** | 2020-06-22 01:56 UTC _(reply to #9)_

These are linear models built on subsections of the data so combining them is just equivalent to building a linear model on the combination of those subsections (ie better yes, but not in a way that is interesting).

Regarding the era performance correlation I ran the code again and compared the per era performance and got the following values on the validation set:

[[ 1. 0.13931771 0.4381523 0.36801614 0.16611012]  
[ 0.13931771 1. 0.0349692 0.39319796 0.38475242]  
[ 0.4381523 0.0349692 1. 0.33687555 -0.09129374]  
[ 0.36801614 0.39319796 0.33687555 1. 0.05083306]  
[ 0.16611012 0.38475242 -0.09129374 0.05083306 1. ]]

So although the model predictions have almost no significant correlation on an individual prediction to individual prediction basis, they do have significant correlation (as high as ~0.438) on an era performance basis. This is not a trivial observation and certainly not intuitive. I have heard of people saying they use correlation to example predictions as a metric to train against, however this might not necessary be preventing what they want to prevent (correlation to era performance of example predictions).

---

### Post #11 — **richai** | 2020-06-23 00:11 UTC _(reply to #10)_

Great. Exactly.

I agree. Being uncorrelated in prediction space is quite easy to do compared to building two models which have uncorrelated era scores out of sample. It makes me wonder if the MMC formulation should be about building models that do well in eras where the meta model does badly.

---

### Post #12 — **of_s** | 2020-06-23 03:08 UTC _(reply to #11)_

I also think Numerai would benefit from MMC as an insurance policy for the meta model, whereby a low volatility low (or ideally negative) correlated model to the meta model should be rewarded for positive performance CORR.

Right now, Numerai is not paying for performance insurance since MMC is 0 when meta model has great era and the MMC model is not as good (yet still positive CORR. Looking on the leaderboard `hb` round 215 is exhibiting this scenario); while essentially overpaying for example predictions.

If there is no incentive to build and maintain those MMC models during good eras to bail out the meta model in bad eras, then they will not be there when the meta model needs them most. Further, MMC should reward lower volatility in its derivation.

---

### Post #13 — **arbitrage** | 2020-06-23 14:49 UTC _(reply to #11)_

100% agree. I have been pondering whether I should tell people that we’re modeling regimes rather than stock performance, since kazutsugi has enough signal to perform well in any regime. If I were given a path to be compensated for modeling different regimes then I would be providing a highly diversified signal for the meta model to learn from. OF_S’ reply above is in that line of thinking as well.

What if there were some kind of score that considered the regime diversity provided across a user’s models, and we could stake separately on the aggregate signal of all the models rather than individual submissions? That would be very interesting indeed.

---

### Post #14 — **quantverse** | 2020-06-24 17:55 UTC _(reply to #13)_

> What if there were some kind of score that considered the regime diversity provided across a user’s models, and we could stake separately on the aggregate signal of all the models rather than individual submissions? That would be very interesting indeed.

I really like this idea.

---

### Post #15 — **bcb** | 2020-09-08 15:45 UTC _(reply to #4)_

Here is a version for Tensorflow based on the code of [@jrb](</u/jrb>) which can be used for a custom loss:
    
    
    import tensorflow as tf
    import tensorflow_probability as tfp
    
    def correlation(x,y):
        mx = tf.math.reduce_mean(x)
        my = tf.math.reduce_mean(y)
        xm, ym = x - mx, y - my
        r_num = tf.math.reduce_mean(xm * ym)
        r_den = tfp.stats.stddev(xm) * tfp.stats.stddev(ym)
        return r_num / (r_den + tf.constant(0.00001, dtype=x.dtype))

---

### Post #16 — **jrb** | 2020-09-09 13:06 UTC _(reply to #15)_

[@bcb](</u/bcb>) Thanks for posting this! I’ve been looking forward to playing with the tf 2.4 nightlies lately, ever since [@surajp](</u/surajp>) told me about its numpy emulation layer. Perhaps this weekend, if I can make some time for it. I also use tf at work, but that’s in an entirely different subfield of ML (vision). I haven’t tried to run your snippet yet, but I believe it could be simplified further and the `tensorflow_probability` dep removed.
    
    
    import tensorflow as tf
    
    def correlation(x,y):
        mx = tf.math.reduce_mean(x)
        my = tf.math.reduce_mean(y)
        xm, ym = x - mx, y - my
        r_num = tf.math.reduce_mean(xm * ym)
        r_den = tf.math.reduce_std(xm) * tf.math.reduce_std(xm)
        return r_num / (r_den + tf.keras.backend.epsilon())

---

### Post #17 — **bcb** | 2020-09-09 13:14 UTC _(reply to #16)_

You are right, tensorflow probability is not needed - guess was a leftover because i also used other modules from the tfp stats package ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)
