---
title: "Signals time series modeling with targets--no external data"
category: Signals
url: https://forum.numer.ai/t/signals-time-series-modeling-with-targets-no-external-data/5917
created_at: 2022-12-07T18:55:03.826000+00:00
last_posted_at: 2023-04-06T20:10:11.540000+00:00
posts_count: 8
views: 2456
tags: []
---

# Signals time series modeling with targets--no external data

---

### Post #1 — **jrai** | 2022-12-07 18:55 UTC

In Signals, we have

  1. the ability to track targets on a per ticker basis through time
  2. new targets updated every week for recently resolved eras



This allows us to use time series methods that aren’t possible in the Classic Tournament. In fact, this means we can even predict future targets and participate in Signals without having to use any external data at all–using only a ticker’s previous targets. To be sure, we shouldn’t expect to get great scores, but it’s a fun exercise and what we learn can likely be applied to modeling paired with other external data. Since targets are bucketed measures of transformed returns, you can also think of this as a type of momentum or reversal prediction model.

# Targets exploration

First, let’s pick a random ticker and plot its targets over time. As we know, targets only take on 5 possible values: [0, 0.25, 0.5, 0.75, 1], so the plot doesn’t seem to contain all that much information:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/afa4b50b3afb82ba1b7e376e4c59d01ac1babd82_2_690x263.png)image826×316 97.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/afa4b50b3afb82ba1b7e376e4c59d01ac1babd82.png> "image")

But if we take a rolling mean, we can start to see some patterns and trends potentially emerge. Indeed, maybe we see how this can be treated as a pure time series problem:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/528c0b29dc8979ef0a096dd41f6b97214187c9af_2_690x261.png)image835×316 87 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/528c0b29dc8979ef0a096dd41f6b97214187c9af.png> "image")

Let’s look at some autocorrelation plots to see if there are any overall relationships in the time series data. Autocorrelation plots are important in time series analysis because they show the relationship between a variable and itself at different time intervals. This can help identify patterns and trends in the data that can be used for forecasting. For example, if a time series has a strong positive autocorrelation at a lag of 2, it indicates that the current value is likely to be similar to the value 2 time periods ago. This information can be used to build better predictive models.

Since we have 10s of thousands of tickers in the dataset, we have to compute each ticker’s autocorrelation separately. Then, we can plot the distributions of those autocorrelations for each lag:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dcc11be7bd0041979ef2ec4d936783ca70e652e1.png)image840×297 22.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dcc11be7bd0041979ef2ec4d936783ca70e652e1.png> "image")

In our case it’s no surprise that we have significant autocorrelation up until lag_4. That’s because each era starts weekly, but has a duration of one month. For the same reason that we need to make sure our train/test set splits have at least a four week gap in Classic, we need to make sure that we’re using fully resolved targets as data for this exercise.

There may also be a hint of negative autocorrelation at lag_5 so this might suggest the targets start to trend in the opposite direction (reversal or mean reversion) after a month.

Now that we have some sense of what the targets look like, we can try some forecasting methods, starting simple and getting progressively more fancy.

# Baseline lag prediction

For the most naive possible baseline, our predictions will be a ticker’s target as of 5 lags ago (this is also the most recent available target in the weekly validation data updated by Numerai at round open). But, since the autocorrelation plot suggests there may be negative autocorrelation at lag_5, we’re going to flip the sign so that our predictions are: \hat{Y_t} = 1 - Y_{t-5}

To visualize and try to gain an intuition of what’s going on, this chart shows a random ticker’s rolling target over time, it’s lagged target (as of 5 eras ago), and the inverse of that lag, which we’ll use as our predictions. For visualization purposes, this is the rolling mean of this ticker’s targets, but our actual values for all modeling are the discrete target values for that era.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0351dc0fa1993652c512f83f51f9fbd07459d0e4.png)image595×225 75.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0351dc0fa1993652c512f83f51f9fbd07459d0e4.png> "image")

Now that we have baseline predictions, let’s see if this can actually translate into any scoring. Nothing particularly great, but also looks like we may be on to something–it’s certainly not random:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a12375c2b658831d6ac321d3429fdba3b73cd55b_2_690x468.png)image739×502 38.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a12375c2b658831d6ac321d3429fdba3b73cd55b.png> "image")

# Averaged lag predictions (rolling mean)

Instead of just taking lag_5, maybe we can do slightly better if we average the lag_5, lag_6, and lag_7? Like the simple baseline, we’ll also take the 1-p version assuming a reversal strategy.  
\hat{Y_t} = 1 - \frac{(y_{t-5} + y_{t-6} + y_{t-7})}{3}

# Simple univariate linear model (autoregression)

Now let’s add some modeling in with a simple linear regression. This is sort of a pseudo time-series model because 1) we have not verified many assumptions needed for proper timer series models and/or 2) we’re not taking the order of the lags into account. Instead, we’re using the time series lags to create cross-sectional features. We’ll use the lags and build a very simple linear regression to predict the current time step. Specifically:

\hat{Y_t} = \beta_1Y_{t-5} + \beta_2Y_{t-6} +...+\beta_{16}Y_{t-20}

Ideally, if the assumption we’ve been operating under–that lag_5 should have a negative reversal–is true, we would hope that the linear model learns a negative coefficient for \beta_1. As it turn out, we do:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e2c88bbfa207184c7397b4ed7c01dfc62a6b5844.png)image560×259 5.14 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e2c88bbfa207184c7397b4ed7c01dfc62a6b5844.png> "image")

# Traditional time-series models

At this point you can and probably should use more traditional time series models. The linear model above is a butchered version of VAR and ARMA models, but I skipped them for now because I’d have to use statsmodels or R. These models also tend to require data transformations due to additional assumptions about the nature of your time series. Mostly, I just don’t like them.

# Multivariate non-linear model (xgboost)

Now that we have 4 new targets in Signals, lets add those lags into the equation as if they were just more features. So instead of just using the lagged `target_20d`, we can also use the lagged `target_20d_raw_returns`, `target_20d_factor_feat_neutral`, and `target_20d_factor_neutral`

**Features:** `lag_features = ['target_20d_lag5', 'target_20d_factor_neutral_lag5', 'target_20d_factor_feat_neutral_lag5', 'target_20d_raw_return_lag5', ... , 'target_20d_lag15', 'target_20d_factor_neutral_lag15', 'target_20d_factor_feat_neutral_lag15', 'target_20d_raw_return_lag15',`

**Target:** `target_20d`

Then, we’ll simply train an xgboost regressor as if it were a cross-sectional problem:
    
    
    model = XGBRegressor()
    model.fit(train_df[lag_features], train_df["target_20d"])
    

# LSTM

With the LSTM (RNN), we’re getting into some more heavy duty time series modeling. What’s nice about the LSTM model is that it takes the order/sequence of lags into account, where the model knows which lag follows which lag and, since it’s a neural net, in its latent space it’s computing more features about how the lags interact with one another. Moreover, we can relax a lot of assumptions needed in more classical time series modeling.

In this case, we’ll use 15 lags of all the targets to predict `target_20d`. With a “many to one” RNN modeling approach, our LSTM network looks a bit like this, where Y_t is `target_20d` and X_i, X_j, etc. are other targets (used as more features like in the xgboost example above) like `target_factor_feat_neutral` and `target_raw_returns`:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c6a7c0f7a4c5486df29ebef3c461b758b4e2b4f5_2_465x499.png)image534×574 49.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c6a7c0f7a4c5486df29ebef3c461b758b4e2b4f5.png> "image")

# Evaluation

Now that we have 5-6 good prediction frameworks, ranging in increasing orders of complexity, let’s submit our predictions to Numerai and pull the diagnostics back so we can look at our fully neutralized correlation scores against the target we were trying to optimize: `target_20d`:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26697247c903e8c9dfed24d58ada91a44138f49e_2_690x318.png)image895×413 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/26697247c903e8c9dfed24d58ada91a44138f49e.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fa67cda11a300856a0cba54afab26e9344f8cc9a_2_690x329.png)image864×413 51.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fa67cda11a300856a0cba54afab26e9344f8cc9a.png> "image")

As it turns out, although it rarely does, as we keep getting fancier, our scores keep getting better!

### A note on neutralization

This exercise has also been helpful in seeing the effects of Numerai’s scoring process. When we submit our Signals predictions, we are neutralized to a set of blackbox features before our final correlation scores are computed. In many cases using external data as features, I have seen this neutralization process improving correlation scores from local scoring to diagnostic (Numerai) scoring. In this case, neutralization has a large negative impact on correlation scores. This makes some sense since we are only using targets provided by Numerai, which are ostensibly constructed by the very features we are then being neutralized against. My intuition is that this method of time series modeling using only the Numerai provided targets is 1) as close as possible to also using Numerai’s internal features and 2) also would be heavily exposed to a momentum/reversal factor that we are likely already being neutralized against.

Here is an example with an LSTM model that gets a .0159 local correlation score (pre-neutralization) which then gets a .0102 diagnostics correlation score (post-neutralization). We add random predictions as a baseline measure:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cf155c0332ba1764afde9ab5c7fdff61375fefa2_2_690x297.png)image888×383 75.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cf155c0332ba1764afde9ab5c7fdff61375fefa2.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/094702b3cba988a98baf76c116eb695ec294d649_2_690x305.png)image864×383 35.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/094702b3cba988a98baf76c116eb695ec294d649.png> "image")

# Conclusion

We’ve been able to (seemingly) build semi-performant models for Signals without using any data at all! Starting with a simple baseline prediction of using the inverse of a ticker’s most recently resolved target and moving all the way to a recurrent neural net using multiple targets, it seems as though it’s entirely possible to participate in Signals using just the targets alone. While these models may not be able to achieve high scores on their own, they may be able to provide valuable insights when used in conjunction with external data. Overall, this exercise highlights the potential for using time series methods in Signals and the benefits of the new targets available in this tournament.

---

### Post #2 — **dev0n** | 2022-12-07 20:22 UTC

Nice! Any chance you can share some of the code? I’ve wanted to try LSTM and this would be a great baseline to start from.

---

### Post #3 — **jefferythewind** | 2022-12-07 20:46 UTC

Inspiring work for sure. RNN is very impressive. Just one idea, might we try the RNN to take input and produce output at every time step, so we could process the entire dataset in one pass.

---

### Post #4 — **jrai** | 2022-12-10 13:24 UTC _(reply to #2)_

Assuming you already have train/test sets with lags added to the dataframe, here is some boilerplate to get you started with a univariate LSTM:
    
    
    from keras.models import Sequential
    from keras.layers import LSTM
    from keras.layers import Dense
    
    def prep_data(dataf, num_lags=15):
        X = dataf[
            [f"target_20d_lag{lag}" for lag in range(4 + num_lags, 4, -1)]
        ].values.reshape(-1, 1, num_lags)
        y = dataf["target_20d"].values
    
        return X, y
    
    num_lags = 15
    train_X, train_y = prep_data(train, num_lags=num_lags)
    valid_X, valid_y = prep_data(valid, num_lags=num_lags)
    
    model = Sequential()
    model.add(LSTM(50, activation="relu", return_sequences=True, input_shape=(1, num_lags)))
    model.add(LSTM(50, activation="relu"))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")
    
    model.fit(train_X, train_y, validation_data=(valid_X, valid_y), batch_size=512, epochs=5, verbose=1)
    

You can then add additional lag features along a dimension, experiment with era batching, adding/reducing number of lags, changing the loss function, etc etc

---

### Post #5 — **dev0n** | 2022-12-10 14:42 UTC

Thanks!

Will try this code later

---

### Post #6 — **k1111** | 2023-04-05 12:37 UTC

Can we use lag_5?  
I think that we can use lag_6~.

For example, as of 3/31, can we only use target_20d until 2/17 (lag 6)?

---

### Post #7 — **jrai** | 2023-04-06 15:09 UTC _(reply to #6)_

I think you’re right. [@ark](</u/ark>) I think you may have mentioned in the past that it would be possible to get lag_5 into the signals weekly dataset. Is that still the case or possible any time soon?

---

### Post #8 — **ark** | 2023-04-06 20:10 UTC _(reply to #7)_

Yes this is still on our to-do list! Unfortunately not super high priority given that the Rain dataset is coming very soon and we have some big new tournament features in the works, so will have to wait until we have some down time to do some of these minor improvements.
