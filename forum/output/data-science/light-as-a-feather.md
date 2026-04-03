---
title: "Light as a Feather"
category: Data Science
url: https://forum.numer.ai/t/light-as-a-feather/534
created_at: 2020-06-08T20:29:32.950000+00:00
last_posted_at: 2020-06-13T16:07:43.175000+00:00
posts_count: 3
views: 3968
tags: []
---

# Light as a Feather

---

### Post #1 — **arbitrage** | 2020-06-08 20:29 UTC

During S2E1 of OHwA I made a short presentation about the [feather file format](<https://arrow.apache.org/docs/python/feather.html>), which is language agnostic between R and Pandas (Python). Here is the code to store the training and tournament data as feather files, which preserves the float32 dtype for feature columns and significantly reduces memory usage and storage space.

Step 1: create a dictionary of column names and dtypes for pandas’ read_csv to use to import the CSV files in the correct dtype.
    
    
    import pandas as pd
    import numpy as np
    from joblib import dump
    
    #download Numerai training data and load as a pandas dataframe
    TRAINING_DATAPATH = 'https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz'
    df = pd.read_csv(TRAINING_DATAPATH)
    
    #create a list of the feature columns
    features = [c for c in df if c.startswith("feature")]
    
    #create a list of the column names
    col_list = ["id", "era", "data_type"]
    col_list = col_list + features + ["target_kazutsugi"]
    
    #create a list of corresponding data types to match the column name list
    dtype_list_back = [np.float32] * 311
    dtype_list_front = [str, str, str]
    dtype_list = dtype_list_front + dtype_list_back
    
    #use Python's zip function to combine the column name list and the data type list
    dtype_zip = zip(col_list, dtype_list)
    
    #convert the combined list to a dictionary to conform to pandas convention
    dtype_dict = dict(dtype_zip)
    
    #save the dictionary as a joblib file for future use
    dump(dtype_dict, 'dtype_dict.joblib')
    

Step 2: use the newly created dictionary to import both data files and save them as feather format
    
    
    import pandas as pd
    import numpy as np
    from joblib import load
    import pyarrow.feather as feather
    
    #load dictionary to import data in specific data types
    dtype_dict = load('dtype_dict.joblib')
    
    #download Numerai training data and load as a pandas dataframe
    TRAINING_DATAPATH = 'https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz'
    df = pd.read_csv(TRAINING_DATAPATH, dtype=dtype_dict)
    
    #download Numerai tournament data and load as a pandas dataframe
    TOURNAMENT_DATAPATH = 'https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz'
    df_tournament = pd.read_csv(TOURNAMENT_DATAPATH, dtype=dtype_dict)
    
    #save Numerai training data as a compressed feather file
    feather.write_feather(df, 'training_compressed.feather', compression='lz4')
    
    #save Numerai tournament data as a compressed feather file
    feather.write_feather(df_tournament, 'tournament_compressed.feather', compression='lz4')
    

Using the above code in production is very simple:
    
    
    import pandas as pd
    df = pd.read_feather('training_compressed.feather')

---

### Post #2 — **jrb** | 2020-06-13 13:26 UTC

Thanks for posting this [@arbitrage](</u/arbitrage>)! I wasn’t aware of Wes McKinney’s pet file format `feather` before you’d mentioned it. I finally got around trying it today. The load time seems significantly faster than what it takes to load a compressed csv (albeit, `lzma`, the format used by `xz` achieves much higher compression ratios than `lz4` which doesn’t compress as well, but is much faster).

I ran the code you’d posted and some more and got these numbers:

file name | size | comments  
---|---|---  
latest_numerai_training_data.csv.xz | 51M | The original xz compressed csv file  
latest_numerai_training_data.feather | 371M | Feather with no compression  
latest_numerai_training_data.feather.lz4 | 241M | Feather with LZ4 compression  
latest_numerai_training_data.parquet | 64M | Parquet  
  
Curiously enough, the parquet file is smaller than the compressed feather file. It defaults to using `snappy` for compression, which is quite similar to `lz4` in its performance characteristics (high speed, low compression). Also, `parquet` is an older, more widely used format (ask anyone who’s written Spark pipelines) and supports JVM (h/t @bor) and C++, in addition to the few languages that feather supports.

It’s worth noting that the reason why both `feather` and `parquet` seem to load dataframes instantaneously is because they use [mmap](<https://en.wikipedia.org/wiki/Memory-mapped_I/O>), which has better performance, but also the cost of reading the file is amortized over the entire read (i.e although the load call returns instantaneously, the actual data is only loaded lazily from disk, as needed), while `read_csv` has to read the entire file into memory at once. There are [other](<https://linux.die.net/man/2/madvise>) [ways](<http://tldp.org/HOWTO/SCSI-Generic-HOWTO/dio.html>) to make it even faster, but since we’re dealing with interpreted languages like Python and R, it’s probably not worth the effort.

Here’s a code snippet for serializing any Pandas dataframe into a parquet file.
    
    
    import pyarrow as pa
    import pyarrow.parquet as pq
    
    def write_parquet(df, filename="data.parquet"):
        table = pa.Table.from_pandas(df)
        pq.write_table(table, filename)
    

And reading parquet files from pandas is as easy as:
    
    
    df = pd.read_parquet("data.parquet")
    

This makes me wonder: Is there a good reason for the `feather` format to even exist? ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)  
The whole situation is reminiscent of this XKCD [comic](<https://xkcd.com/927/>).  


[![standards](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2728a7282d74170629fc2eb9ecb6a8e405fd1eff.png)standards500×283 22.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2728a7282d74170629fc2eb9ecb6a8e405fd1eff.png> "standards")

---

### Post #3 — **arbitrage** | 2020-06-13 16:07 UTC _(reply to #2)_

[@jrb](</u/jrb>) Thank you for the write-up! Let me expand on my motivation for doing this.

Because I focus on the new users who are more likely hobbyists or are scientists from other fields (in other words, not pure ML folks), I want to streamline all the things. Having taught undergraduates to participate in the tournament for two semesters, I am very aware of how confusing the workflow can be. Further, [@master_key](</u/master_key>) was quoted saying that Pandas and SKLearn encompasses “99%” of the typical user’s needs, and I think he’s right.

I want people to be able to use at most 4 packages and for the data to exist in Pandas dataframes, not as scattered numpy objects throughout their pipeline. I don’t want a new user to have to fiddle with reducing memory usage or converting between various file formats. Additionally, whatever format is used, should be directly plug and play with R, so that those users also have a similar “path to victory” as Python users.

Parquet meets my requirements at first glance. Feather does as well. There are likely other formats, too. What I like most about Feather is that Wes McKinney is the developer of Pandas and Feather, and the collaboration with [Hadley Wickham](<https://blog.rstudio.com/2016/03/29/feather/>) gives me a lot of confidence that a change in Feather will be simultaneously applied to R and Pandas.

Here’s Wes on Feather and Parquet:

[![pq_v_feather](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d3c95aed699a940a2a148a8cb50450535afaa3cf.png)pq_v_feather741×480 36.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d3c95aed699a940a2a148a8cb50450535afaa3cf.png> "pq_v_feather")

What I am not very concerned with is the storage size. I am ambivalent between loading speed and download speed, desiring only that the downloaded file is read into memory as a dataframe with the dtypes preserved. [This write-up](<https://towardsdatascience.com/the-best-format-to-save-pandas-data-414dca023e0d>) shows a concerning memory consumption growth when loading parquet files, which feather does not suffer from.

In the end, either option is significantly better than the CSV files, and now users can choose for themselves. Hopefully someday soon the team will offer the data files in several formats with direct links (and maybe even shortened URLs) ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)
