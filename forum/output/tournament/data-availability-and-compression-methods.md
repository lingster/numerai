---
title: "Data Availability and Compression Methods"
category: Tournament
url: https://forum.numer.ai/t/data-availability-and-compression-methods/5813
created_at: 2022-11-01T01:30:47.151000+00:00
last_posted_at: 2022-11-01T13:58:30.749000+00:00
posts_count: 2
views: 546
tags: []
---

# Data Availability and Compression Methods

---

### Post #1 — **liborty** | 2022-11-01 01:30 UTC

I am experiencing difficulties using v4 data because the `.csv` data is missing from that set. Why? The .parquet readers waste unreasonable amounts of memory because they (stupidly) insist on reading all of the data instead of reading it in the time-honoured way, row-by-row.

Is the transmission bandwidth the problem?

In that case, may I ask for the `_int8.csv` files to be compressed by some standard method please? In that form, they will be even smaller than the `.parquet` versions. However, crucially, they will be much easier to use.

To back this assertion up, I performed a comparison on v3 version (last available non .parquet data). I used standard lzma compression with default settings.

227501648 Nov 1 12:05 numerai_validation_data.parquet  
107301737 Nov 1 12:17 numerai_validation_data_int8.csv.lzma

As you can see, the `_int8.csv.lzma` version is less than half the size.

---

### Post #2 — **shatteredx** | 2022-11-01 13:58 UTC

You can use Dask dataframes instead of pandas to read the parquet files without loading them into memory.

Example: Read parquet, only keep every 4th era, and compute to pandas
    
    
    import dask.dataframe as dd
    training_data = dd.read_parquet('train.parquet')
    # pare down the number of eras to every 4th era
    every_4th_era = training_data[ERA_COL].unique()[::4].compute()
    training_data = training_data[training_data[ERA_COL].isin(every_4th_era)].compute()
