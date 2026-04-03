---
title: "Reducing Memory"
category: Data Science
url: https://forum.numer.ai/t/reducing-memory/313
created_at: 2020-05-03T07:22:10.716000+00:00
last_posted_at: 2021-01-19T16:09:32.714000+00:00
posts_count: 11
views: 3990
tags: []
---

# Reducing Memory

---

### Post #1 — **kainsama** | 2020-05-03 07:22 UTC

When we read the tournament train and test data into memory it takes a lot of memory that could be a problem even if we have a beefy machine. In order to reduce the following function (a popular function from Kaggle notebooks):
    
    
    import pandas as pd
    
    def reduce_mem_usage(df, verbose=True):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        start_mem = df.memory_usage().sum() / 1024**2
        for col in df.columns:
            col_type = df[col].dtypes
            if col_type in numerics:
                c_min = df[col].min()
                c_max = df[col].max()
                if str(col_type)[:3] == 'int':
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)
                else:
                    if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                        df[col] = df[col].astype(np.float16)
                    elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        df[col] = df[col].astype(np.float32)
                    else:
                        df[col] = df[col].astype(np.float64)
    
        end_mem = df.memory_usage().sum() / 1024**2
        print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
        print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    
        return df
    
    training_data = reduce_mem_usage(pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz"))
    training_data.head()
    

Although reducing the precision of the features may hurt the performance of the models but here we are dealing with sets of numerical features with low cardinality so the loss will be negligible.

---

### Post #2 — **jrb** | 2020-05-03 13:19 UTC

Interesting! I tried to solve this problem a bit differently, as outlined [here](<http://forum.numer.ai/t/saving-memory-with-uint8-features/254>). The problem with the approach you’ve outlined is that `pd.read_csv` will have to load the entire dataset into memory at full precision. Although you do get a reduction in memory usage after the transform in `reduce_mem_usage`, the peak memory usage remains the same. Which means that you’re still bottlenecked on memory (and glacially slow swap, if the machine has it enabled). My approach around that problem is to use converters to ensure that the data is converted to the more succinct dtype at load time. It isn’t entirely free, the load time goes up by about a bit, but the memory usage never peaks.

---

### Post #3 — **randperson** | 2020-07-12 16:09 UTC

Thanks for sharing, nice solution! Another approach could be using [dask dataframe](<https://docs.dask.org/en/latest/dataframe.solutionhtml>) instead of pd.

---

### Post #4 — **perfect_fit** | 2020-11-05 12:39 UTC

Nice discussion! Indeed that function works very well for Kaggle competitions, but seems a bit too elaborate for Numerai. It may still be helpful for Numerai Signals, though. Here is a nice compact way to do the memory reduction. If I remember correctly it is from a function by [@mdo](</u/mdo>) or [@jrb](</u/jrb>).
    
    
    import csv
    import numpy as np
    import pandas as pd
    
    def read_csv(path):
        with open(path, 'r') as f:
            column_names = next(csv.reader(f))
            dtypes = {x: np.float16 for x in column_names if x.startswith(('feature', 'target'))}
        return pd.read_csv(path, dtype=dtypes)
    

Hope it helps!

---

### Post #5 — **oxioxi** | 2020-12-13 12:05 UTC

I get “no such file or directory” for basic paths such as :

training_path = ‘<https://numerai-public-datasets.s3-us-w2.amazonaws.com/latest_numerai_training_data.csv.xz>’

tournament_path = ‘<https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz>’

… same as for jrb’s approach. Any fix?

---

### Post #6 — **restrading** | 2020-12-14 05:47 UTC _(reply to #5)_

Try these:  
<https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz>  
<https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz>

---

### Post #7 — **oxioxi** | 2020-12-14 08:41 UTC _(reply to #6)_

Tried, it’s the same, paths work with Pandas.read_csv(), you can’t really open a _url_ path with a regular _open_ , but I don’t have need or time to refactor the method, kainsama’s one is working, at least up until the point I need to train my Catboost model :).

---

### Post #8 — **restrading** | 2020-12-14 08:56 UTC _(reply to #7)_

If someone is using plain open(), it’s implied the file has already been downloaded prior.

---

### Post #9 — **jrb** | 2020-12-15 12:27 UTC _(reply to #7)_

Try this:
    
    
    import csv
    import lzma
    from pathlib import Path
    from typing import IO, Union
    
    import numpy as np
    import pandas as pd
    
    
    def open_file(file_path: Path, mode: str = "rt") -> IO:
        if file_path.suffix == '.xz':
            return lzma.open(file_path, mode)
        else:
            return open(file_path, mode)
    
    
    def read_csv(file_path: Union[Path, str], dtype=np.float16) -> pd.DataFrame:
        if isinstance(file_path, str) and file_path.startswith("https://"):
            column_names = list(pd.read_csv(file_path, nrows=1).columns)
        else:
            if isinstance(file_path, str):
                file_path = Path(file_path)
            with open_file(file_path) as f:
                column_names = next(csv.reader(f))
        dtypes = {x: dtype for x in column_names if
                  x.startswith(('feature', 'target'))}
        return pd.read_csv(file_path, dtype=dtypes, index_col=0)

---

### Post #10 — **oxioxi** | 2020-12-15 13:04 UTC _(reply to #9)_

Thanks, appreciate it. It will be friendly to all the other “hackers” I’m sure.

---

### Post #11 — **goldnumberone** | 2021-01-19 16:09 UTC

Pandas has a section on loading large datasets: <https://pandas.pydata.org/docs/user_guide/scale.html>

They suggest using more efficient datatypes by checking the existing data types and the memory usage:
    
    
    print(training_set.dtypes)
    print(training_set.memory_usage(deep=True))
    

And setting the data type to something smaller by downcasting:
    
    
    training_set['feature_whatever'] = pd.to_numeric(training_set['feature_whatever'], downcast='unsigned')
    print(training_set.memory_usage(deep=True))
    

Another option that’s mentioned is using Dask: <https://docs.dask.org/en/latest/dataframe.html>
