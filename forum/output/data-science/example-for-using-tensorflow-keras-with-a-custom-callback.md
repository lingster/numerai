---
title: "Example for using Tensorflow / Keras with a custom callback"
category: Data Science
url: https://forum.numer.ai/t/example-for-using-tensorflow-keras-with-a-custom-callback/855
created_at: 2020-08-27T11:45:00.484000+00:00
last_posted_at: 2020-11-03T15:57:16.881000+00:00
posts_count: 8
views: 3177
tags: []
---

# Example for using Tensorflow / Keras with a custom callback

---

### Post #1 — **bcb** | 2020-08-27 11:45 UTC

Lately i switched from using XGBoost to using Tensorflow / Keras for my models in the tournament, but still wanted to have the metric output like in the era boosting example. Additionally, the callback saves the best model based on these metrics.

So i created a custom callback to show the metrics after each epoch while training. If you want to take a look, i shared it on Github:

![](https://github.githubassets.com/favicons/favicon.svg) [github.com](<https://github.com/chricke/Numerai-Keras/tree/master>)

### [GitHub - chricke/Numerai-Keras: Examples to use Tensorflow / Keras](<https://github.com/chricke/Numerai-Keras/tree/master>)

[master](<https://github.com/chricke/Numerai-Keras/tree/master>)

Examples to use Tensorflow / Keras. Contribute to chricke/Numerai-Keras development by creating an account on GitHub.

If you have any comments or improvements please let me know.

---

### Post #2 — **jorijnsmit** | 2020-08-29 09:59 UTC

What is your reasoning behind switching from XGBoost to a neural net?

---

### Post #3 — **bcb** | 2020-08-29 11:38 UTC

Short answer: results ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #4 — **olivepossum** | 2020-10-24 22:49 UTC

I’m not a NN expert but would it be possible to use, instead a custom callback, a custom loss function to optimize on CORR?

---

### Post #5 — **surajp** | 2020-10-25 03:40 UTC _(reply to #4)_

Absolutely. That’s where NNs really shine
    
    
    def my_loss_fn(y_true, y_pred):
        squared_difference = tf.square(y_true - y_pred)
        return tf.reduce_mean(squared_difference, axis=-1)  # Note the `axis=-1`
    
    model.compile(optimizer='adam', loss=my_loss_fn)
    

<https://keras.io/api/losses/#creating-custom-losses>

---

### Post #6 — **bcb** | 2020-10-25 17:47 UTC

The custom callback was only to show how the metrics can be calculated during training like in the example we have in the forum for XGBoost (as a kind of reporting overview).

If you want to really want to optimize for a specific metric the custom loss is the way to go.

---

### Post #7 — **olivepossum** | 2020-10-25 20:52 UTC _(reply to #6)_

Thanks a lot for you answers and for sharing this code. I’ve learned a lot with it. By the way [@bcb](</u/bcb>), I was playing a bit with it and calculateScores class is using global variables inside it’s functions (model, features and sometimes train_df and val_df). For it to work not depending on the global variables (I was having errors because in my code, outside the class those variables were named differently), I’ve added them as class variables so have to be passed in the constructor.
    
    
    class calculateScores(tf.keras.callbacks.Callback):
        def __init__(self, train_df, val_df, save_file, model, features):
            self.max_score = 0.0
            self.max_score_round = 0
            self.train_df = train_df
            self.val_df = val_df
            self.save_file = save_file
            self.model = model
            self.features = features
    
        def on_epoch_end(self, epoch, logs=None):
            # score each era
            print("")
            print("="*20)    
            print("predicting on train")
            preds = self.model.predict(self.train_df[self.features])
            self.train_df["pred"] = preds
            era_scores = pd.Series(index=self.train_df["era"].unique(), dtype='float64')
            print("getting per era scores")
            for era in self.train_df["era"].unique():
                era_df = self.train_df[self.train_df["era"] == era].copy()
                era_scores[era] = spearmanr(era_df["target_nomi"], era_df["pred"])
            era_scores.plot(kind="bar")
            print("performance over time")
            plt.show()
            print("="*20)
            print("autocorrelation")
            print(ar1(era_scores))
            print("mean correlation")
            print(np.mean(era_scores))
            print("sharpe")
            print(np.mean(era_scores)/np.std(era_scores))
            print("numerai sharpe")
            print(numerai_sharpe(era_scores))    
            print("smart sharpe")
            print(smart_sharpe(era_scores))
            print("="*20)
            print("predicting on validation")
            preds_val = self.model.predict(self.val_df[self.features])
            self.val_df["pred"] = preds_val
            val_era_scores = pd.Series(index=self.val_df["era"].unique(), dtype='float64')    
            print("getting per val_era scores")
            for era in self.val_df["era"].unique():
                val_era_df = self.val_df[self.val_df["era"] == era].copy()
                val_era_scores[era] = spearmanr(val_era_df["target_nomi"], val_era_df["pred"])
            val_era_scores.plot(kind="bar")
            print("performance over time")
            plt.show()        
            print("val_autocorrelation")
            print(ar1(val_era_scores))
            print("val_mean correlation")
            print(np.mean(val_era_scores))
            print("val_sharpe")
            print(np.mean(val_era_scores)/np.std(val_era_scores))
            print("val numerai sharpe")
            print(numerai_sharpe(val_era_scores))    
            print("val_smart sharpe")
            print(smart_sharpe(val_era_scores))  
            
            new_score = smart_sharpe(val_era_scores) + numerai_sharpe(val_era_scores) + (np.mean(val_era_scores)/np.std(val_era_scores)) + np.mean(val_era_scores)*2
            if new_score > self.max_score:
                print("saving best scored model...")
                self.model.save(self.save_file)
                self.max_score = new_score
                self.max_score_round = epoch
                print(f"new max_score: {self.max_score}")
            else:
                print(f"current score {new_score} did not improve from max score {self.max_score} on round {self.max_score_round}")
            print("="*20)

---

### Post #8 — **estevees** | 2020-11-03 15:57 UTC

Thanks for posting the custom callback. Very interesting approach to improve the NN results.

One newbie question. To avoid over fitting wouldn’t it be best to treat the tournament_file as a blind data set ? Splitting training_file into train and test, and use the custom callback on that.

Otherwise we aren’t we effectively training on the tournament_file ?
