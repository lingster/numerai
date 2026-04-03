---
title: "How to train on the full V4 dataset with 8GB RAM"
category: Data Science
url: https://forum.numer.ai/t/how-to-train-on-the-full-v4-dataset-with-8gb-ram/5734
created_at: 2022-09-29T08:31:17.587000+00:00
last_posted_at: 2022-10-06T20:49:44.708000+00:00
posts_count: 6
views: 1567
tags: []
---

# How to train on the full V4 dataset with 8GB RAM

---

### Post #1 — **nyuton** | 2022-09-29 08:31 UTC

Hi,

I guess I’m not the only one here, who doesn’t have 128GB RAM at hand. So it might be helpful to share, how it is possible to use the full dataset with <8GB RAM.

The basic idea is to split the full dataset into chunks (split by era). Save these chunks as separate parquet files and then load them on the fly in parallel threads.

The result is not a significant compromise on speed. It requires very little RAM and needs only 5 threads to continously read the data from disk. The number of threads might need to be adjusted based on the speed of your disk and the number of CPU cores available, etc

Here you find the code for training.

[github.com](<https://github.com/nemethpeti/numerai/blob/main/TrainOnAllData/torchtrain_alldata.py>)

#### [nemethpeti/numerai/blob/main/TrainOnAllData/torchtrain_alldata.py](<https://github.com/nemethpeti/numerai/blob/main/TrainOnAllData/torchtrain_alldata.py>)
    
    
    import torch
    import pandas as pd
    import numpy as np
    import torchsort
    from torch.functional import F
    import torch.optim as optim
    from torch import nn
    
    import json
    import joblib
    import random
    import math
    
    
    #device = 'cpu'
    device = "cuda" if torch.cuda.is_available() else "cpu"
    #print(f"Using {device} device")
    
    torch.use_deterministic_algorithms(mode=True)
    pd.options.mode.chained_assignment = None  # default='warn'
    

This file has been truncated. [show original](<https://github.com/nemethpeti/numerai/blob/main/TrainOnAllData/torchtrain_alldata.py>)

Have fun!

---

### Post #2 — **nyuton** | 2022-10-03 07:00 UTC

Feedback and ideas on improvement are welcome!

---

### Post #3 — **mundan** | 2022-10-03 20:45 UTC _(reply to #2)_

Maybe saving as `.npy`, `.pkl`, or `.feather` will make loading faster. At least it is the case for big tables. Also casting before saving could be good. What’s your take on this?

Thank you for sharing your work

---

### Post #4 — **nyuton** | 2022-10-04 06:45 UTC _(reply to #3)_

I’m not sure about their load times, please try if you wish.

But load time is not very relevant. Threads run parallel and read a era worth of data in the background. As long as you have enough threads, load speed doesn’t matter much.

---

### Post #5 — **dangerbot** | 2022-10-05 07:54 UTC

I’ve been trying to train some models on Colab, so I’m running into memory issues a lot there even with the int datasets. I found with [Parquet](<https://arrow.apache.org/docs/python/generated/pyarrow.parquet.ParquetFile.html?highlight=iter#pyarrow.parquet.ParquetFile.iter_batches>) there is a way read chunks of data and select features, but doing any filtering based on the rows takes up too much ram.

I wrote a class for Keras streaming data in batches. It keeps the memory foot print low and you can select the number of rows (the batch size.)
    
    
    import pandas as pd
    import pyarrow.parquet as pq
    import numpy as np
    from tensorflow.keras.utils import Sequence
    class TrainDataBatches(Sequence):
        def __init__(self, feature_cols: list, target_cols: list, era_col: str, batch_size: int = 256,
                     file_path: str = 'train.parquet'):
            self.batch_size = batch_size
            self.features = feature_cols
            self.targets = target_cols
            self.era = era_col
            self.file_path = file_path
            self._index = pq.read_table(file_path, columns=["id"]).to_pandas().reset_index()
            self.on_epoch_end()
    
        def __len__(self) -> int:
            m = pq.read_metadata(self.file_path)
            return int(np.ceil(m.num_rows / self.batch_size))
    
        def on_epoch_end(self):
            self.df_train = pq.ParquetFile(self.file_path).iter_batches(
                self.batch_size,
                columns=self.features + self.targets + self.era)
            # self._index = self._index.loc[np.random.shuffle(self._index.index)]
    
        def __getitem__(self, idx) -> pd.DataFrame:
            return self.return_data()
    
        def shuffle_data(self, idx: int):
            """
            Shuffles training data out of core
            """
            # takes up too much ram
            ID = list(self._index.iloc[idx * self.batch_size:(idx + 1) * self.batch_size]['id'])
            df = pq.read_table(self.file_path,
                               columns=self.features + self.targets + self.era,
                               filters=[('id', 'in', ID)]).to_pandas()
            df[self.features] = df[self.features].astype(float) / 4.
            df[self.era] = df[self.era].astype(float)
            return (df[self.features + self.targets], df[self.era]), df[self.features + self.targets]
    
        def return_data(self):
            """
            reads data in batches  as is.
            """
            try:
                chunk = next(self.df_train)
                ch = chunk.to_pandas()
                ch[self.features] = ch[self.features].astype(float) / 4.
                ch[self.era] = ch[self.era].astype(float)
                return (ch[self.features + self.targets].values, ch[self.era]), ch[self.features + self.targets].values
            except StopIteration:
                self.on_epoch_end()
                return self.return_data()

---

### Post #6 — **dzheng1887** | 2022-10-06 20:49 UTC

I have never tried it, but I just had to replicate several of my coworker’s virtual environment/processing scripts and one used dask to train and predict on his models.

I am not sure how it works, and I have failed to make it myself when messing around one day, but I have noticed that his RAM usage when making predictions was much lower than my other 3 coworkers and they all used XGBoost to model the same thing.
