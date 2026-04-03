---
title: "Era batches for trainning Keras NN"
category: Data Science
url: https://forum.numer.ai/t/era-batches-for-trainning-keras-nn/4050
created_at: 2021-09-08T12:17:15.942000+00:00
last_posted_at: 2021-09-08T13:12:13.301000+00:00
posts_count: 4
views: 1364
tags: []
---

# Era batches for trainning Keras NN

---

### Post #1 — **javiermoral** | 2021-09-08 12:17 UTC

I am trying to train a NN with era batches using Keras data generators. I am not familiar with data generators but I have found them very easy to understand after a couple of tutorials. Still, I can’t get it to work and I can’t find where I’m going wrong; the class is very simple and has all the methods required for the Keras model to work.
    
    
    class EraDataGenerator(tf.keras.utils.Sequence):
    'Generates data for Keras'
    
    def __init__(self, X, y, shuffle=True):
        'Initialization'
        self.X = X
        self.y = y
        self.dim = len(X.columns)
        self.eras = X.era.unique()
        self.shuffle = shuffle
        
        if self.shuffle == True:
            np.random.shuffle(self.eras)
    
        self.on_epoch_end()
    
    def __len__(self):
        'Num of batches per epoch'
        return len(self.eras)
    
    def __getitem__(self, idx):
    
        myEras = [idx]
        
        X = self.X.loc[self.X.era.isin(myEras), self.features].values
        y = self.y.loc[self.X.era.isin(myEras), 'target'].values
        
        return X, y
    
    def on_epoch_end(self):
        'Mixes eras order after each epoch'
        if self.shuffle == True:
            np.random.shuffle(self.eras)
    

The error that occurs is as follows:
    
    
    ValueError: Failed to find data adapter that can handle input: <class '__main__.EraDataGenerator'>, <class 'NoneType'>
    

Has anyone used Data Generators for the same case and managed to implement it without problems?

---

### Post #2 — **nyuton** | 2021-09-08 12:32 UTC

__getitem() should return an X,y tuple

---

### Post #3 — **javiermoral** | 2021-09-08 12:35 UTC _(reply to #2)_

still getting the same error

---

### Post #4 — **nyuton** | 2021-09-08 13:12 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) [Feature reversing input noise](<http://forum.numer.ai/t/feature-reversing-input-noise/1416/17>) [Data Science](</c/data-science/5>)

> class DataSequence(tf.keras.utils.Sequence): def __init__(self, df, features, erasPerBatch=1, shuffle=True): self.df = df self.features = features self.shuffle = shuffle self.eras = df.era.unique() if self.shuffle == True: np.random.shuffle(self.eras) self.erasPerBatch = erasPerBatch self.df['target_aux'] = self.df[target] def __len__(self): return len(self.eras) // sel…
