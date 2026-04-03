---
title: "Faster data loading with datatable"
category: Data Science
url: https://forum.numer.ai/t/faster-data-loading-with-datatable/1804
created_at: 2021-02-14T20:38:18.747000+00:00
last_posted_at: 2021-04-09T14:07:01.160000+00:00
posts_count: 7
views: 1865
tags: []
---

# Faster data loading with datatable

---

### Post #1 — **mundan** | 2021-02-14 20:38 UTC

Hey. I’m just starting, and I thought sharing this was something useful.  
**Here is the code of an enhanced** `read_csv` **function, which is a lot faster when** `memory='high'` **is set.**  
The top consumption for both training and tournament data was almost 9GiB (including my system).
    
    
    import csv
    import datatable
    import numpy as np
    import pandas as pd
    import psutil
    
    # Read the csv file into a pandas Dataframe as float16 to save space
    def read_csv(file_path, memory="high"):
        if memory == "high":
            csv_datatable = datatable.fread(file_path)
            dtypes = {
                x: np.float16
                for x in csv_datatable.names
                if x.startswith(("feature", "target"))
            }
            df = csv_datatable.to_pandas().astype(dtypes)
            print('Top used RAM')
            print_used_ram()
            del csv_datatable
        else:
            with open(file_path, "r") as f:
                column_names = next(csv.reader(f))
            if memory == "medium":
                dtypes = {
                    x: np.float16
                    for x in column_names
                    if x.startswith(("feature", "target"))
                }
                df = pd.read_csv(file_path, dtype=dtypes, index_col=0)
            elif memory == "low":
                dtypes = {f"target": np.float16}
                to_uint8 = lambda x: np.uint8(float(x) * 4)
                converters = {x: to_uint8 for x in column_names if x.startswith("feature")}
                df = pd.read_csv(file_path, dtype=dtypes, converters=converters)
            else:
                raise ValueError('memory parameter not in ["high", "medium", "low"]')
        return df
    
    def print_used_ram():
        vm = psutil.virtual_memory()
        used = (vm.total - vm.available) / 1024**3
        print(f'Used RAM: {used} GiB')
        return used 
    
    
    def main():
        u1 = print_used_ram()
        print("Loading data...")
        # The training data is used to train your model how to predict the targets.
        training_data = read_csv("numerai_training_data.csv")
        print('Loaded training data')
        u2 = print_used_ram()
        # The tournament data is the data that Numerai uses to evaluate your model.
        tournament_data = read_csv("numerai_tournament_data.csv")
        print('Loaded tournament data')
        u3 = print_used_ram()
    
        feature_names = [f for f in training_data.columns if f.startswith("feature")]
        print(f"Loaded {len(feature_names)} features")
    
    
    if __name__ == "__main__":
        main()
    

I want to create a pretty serious pipeline, so I can iterate properly. I’ve seen many great posts, but any github repo with that pipeline would be appreciated. If you don’t have one, I’ll share it soon. Hopefully we can improve the pipeline together and focus on modeling. Cheers

---

### Post #2 — **minou** | 2021-02-24 14:56 UTC

Thanks for this. I had errors with `high` when the datatable was used, which turned out to be because `to_pandas()` was adding its own id column, giving 314 columns rather than 313. I found a `set_index()` method that solves this, so the relevant line becomes:

`df = csv_datatable.to_pandas().astype(dtypes).set_index("id")`

Placement before `astype()` will also work.

---

### Post #3 — **krm** | 2021-02-28 03:41 UTC

I use `cudf` for this:
    
    
    import cudf as cd
    
    cd.read_csv('').to_pandas()
    

you need a gpu though

---

### Post #4 — **minou** | 2021-03-12 17:28 UTC

I recommend pickling as well if using a modern python. My csv reader checks for a pickled version first, and creates one if none exists. Once pickled, loading the training and tournament data only takes around 5 seconds total off a fast SSD, giving a welcome saving over other methods.

---

### Post #5 — **mundan** | 2021-04-02 11:19 UTC _(reply to #2)_

You’re right! thanks for the enhancing

---

### Post #6 — **dliden** | 2021-04-09 13:51 UTC _(reply to #4)_

The advice to pickle instead of saving as a CSV was super helpful and shaved a lot of time off my data processing pipeline.

I’ve also found that using the `dask` package for initial reading and processing of the CSVs (I like to make a single dataset with the training and validation eras combined) is considerably faster than trying to use `pd.read_csv` as an iterable (my earlier approach).
    
    
    import dask.dataframe as dd
    tourn_iter_csv = dd.read_csv(tourn_file)
    tmp_df_tourn = tourn_iter_csv[tourn_iter_csv['data_type'] == 'validation']
    tmp_df_train = dd.read_csv(train_file)
    training_data = dd.concat([tmp_df_train, tmp_df_tourn])
    training_data = training_data.compute()
    training_data.reset_index(drop=True, inplace=True)
    
    training_data.to_pickle(processed_train_pickle_path)

---

### Post #7 — **minou** | 2021-04-09 14:07 UTC _(reply to #6)_

Glad that helped. joblib is also popular so I tried that too, but files were twice the size so loading took twice as long. For cases where there wasn’t already a `to_pickle()` style function, I added these functions to a helper file for an easy interface. Path is from pathlib.
    
    
    def has_pickle(path):
        return Path(path).is_file()
    
    def read_pickle(path, default=None):
        res = default
    
        if has_pickle(path):
            with open(path, 'rb') as f:
                res = pickle.load(f)
    
        return res
    
    def write_pickle(data, path):
        with open(path, 'wb') as f:
            pickle.dump(data, f)
