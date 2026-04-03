---
title: "Error when reading in validation parquet file"
category: Tournament
url: https://forum.numer.ai/t/error-when-reading-in-validation-parquet-file/4581
created_at: 2021-12-05T18:09:14.469000+00:00
last_posted_at: 2021-12-11T05:16:59.861000+00:00
posts_count: 7
views: 7756
tags: []
---

# Error when reading in validation parquet file

---

### Post #1 — **smilence666** | 2021-12-05 18:09 UTC

Hi,

I started to encounter this error recently using the same code. Did anything change for the validation parquet file?

validation_example_preds = pd.read_parquet(‘example_validation_predictions.parquet’)  
PyDev console: starting.  
Traceback (most recent call last):  
File “C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pydev_pydevd_bundle\pydevd_exec2.py”, line 3, in Exec  
exec(exp, global_vars, local_vars)  
File “”, line 1, in   
File “C:\ProgramData\Anaconda3\envs\py38\lib\site-packages\pandas\io\parquet.py”, line 495, in read_parquet  
return impl.read(  
File “C:\ProgramData\Anaconda3\envs\py38\lib\site-packages\pandas\io\parquet.py”, line 239, in read  
result = self.api.parquet.read_table(  
File “C:\ProgramData\Anaconda3\envs\py38\lib\site-packages\pyarrow\parquet.py”, line 1905, in read_table  
dataset = _ParquetDatasetV2(  
File “C:\ProgramData\Anaconda3\envs\py38\lib\site-packages\pyarrow\parquet.py”, line 1711, in **init**  
[fragment], schema=fragment.physical_schema,  
File “pyarrow_dataset.pyx”, line 978, in pyarrow._dataset.Fragment.physical_schema.**get**  
File “pyarrow\error.pxi”, line 143, in pyarrow.lib.pyarrow_internal_check_status  
File “pyarrow\error.pxi”, line 99, in pyarrow.lib.check_status  
pyarrow.lib.ArrowInvalid: Could not open Parquet input source ‘’: Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.

---

### Post #2 — **platemort** | 2021-12-05 18:13 UTC

I get the same error on this weeks training data. I hope someone can fix this before the round closes.

---

### Post #3 — **smilence666** | 2021-12-05 18:29 UTC _(reply to #2)_

a workaround is to comment all lines related to the validation dataset - if there is no change for the model.

But i do wish someone could fix it asap to test any further model changes.

---

### Post #4 — **eleele** | 2021-12-05 18:51 UTC

Remove the files and download them again. After a couple of times, the problem was solved in my case. Maybe a glitch?

---

### Post #5 — **smilence666** | 2021-12-05 20:18 UTC _(reply to #4)_

thanks. it works after repeating this a few times.

---

### Post #6 — **platemort** | 2021-12-06 12:36 UTC

I had the same experience. After deleting the previously downloaded file, re-running the exact same code executed without error. I hope that somebody will look into this, since it could be a significant burden for automatic submission.

---

### Post #7 — **kmtk49** | 2021-12-11 05:16 UTC

I also had same trouble then fixed already. However I experienced from last round.  
Anyone know why happen at last round?
