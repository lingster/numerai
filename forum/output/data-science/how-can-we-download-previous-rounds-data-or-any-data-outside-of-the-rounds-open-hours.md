---
title: "How can we download previous rounds' data or any data outside of the rounds' open hours?"
category: Data Science
url: https://forum.numer.ai/t/how-can-we-download-previous-rounds-data-or-any-data-outside-of-the-rounds-open-hours/5821
created_at: 2022-11-05T16:46:19.206000+00:00
last_posted_at: 2022-11-06T01:46:14.987000+00:00
posts_count: 4
views: 639
tags: []
---

# How can we download previous rounds' data or any data outside of the rounds' open hours?

---

### Post #1 — **sentientai** | 2022-11-05 16:46 UTC

It seems like numerapi won’t allow downloading of any data outside of when a round is “open”, is this correct? I want to be able to get some data to work on developing code but it seems like numerapi won’t download data from any round outside of the “open” hours. For example, I tried things like:
    
    
    from pathlib import Path
    Path("./v4").mkdir(parents=False, exist_ok=True)
    napi.download_dataset("v4/train.parquet", round_num=344)
    

With different data files and different rounds. I also tried downgrading numerapi in case it was a bug from recent releases, to no avail. The error it returns is something like:
    
    
    2022-11-05 17:38:01,943 ERROR numerapi.utils: Http Error: 500 Server Error: Internal Server Error for url: https://api-tournament.numer.ai/
    2022-11-05 17:38:01,944 ERROR numerapi.utils: Did not receive a valid JSON: Expecting value: line 1 column 1 (char 0)
    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)
    Cell In [10], line 3
          1 from pathlib import Path
          2 Path("./v4").mkdir(parents=False, exist_ok=True)
    ----> 3 napi.download_dataset("v4/train.parquet", round_num=323)
    
    File c:\Users\words\miniforge3\envs\numerai\lib\site-packages\numerapi\numerapi.py:107, in NumerAPI.download_dataset(self, filename, dest_path, round_num)
         98 query = """
         99 query ($filename: String!
        100        $round: Int) {
       (...)
        103 }
        104 """
        105 args = {'filename': filename, "round": round_num}
    --> 107 dataset_url = self.raw_query(query, args)['data']['dataset']
        108 utils.download_file(dataset_url, dest_path, self.show_progress_bars)
    
    KeyError: 'data'
    

Is this expected behavior, or is this just bad luck and things are not working when I’ve been trying it today?

As someone new here it’s super frustrating that the examples don’t work except during the “open” hours, if this is intended, and there’s no way to get old data with the api. It means we have to go to somewhere like Kaggle to get some datasets to start developing with, unless we happen to download it during the exact right time. And then one more question - if we aren’t supposed to be able to dowload previous datasets with the api, then why are they even visible with `napi.list_datasets(245)` and why is round_num even an arg for some of the napi functions?

---

### Post #2 — **shatteredx** | 2022-11-05 17:17 UTC

Remove the round_num argument and train.parquet will download successfully. Train.parquet does not change from round to round.

Validation.parquet gets new eras appended every week at the start of the round.

EDIT: Nevermind, you’re right, numerapi and/or Numerai itself seems to be broken right now. This is definitely not expected behavior. Hopefully there is a fix soon.

---

### Post #3 — **wigglemuse** | 2022-11-05 19:33 UTC

It seems like a lot of stuff was offline this morning – try again?

---

### Post #4 — **dzheng1887** | 2022-11-06 01:46 UTC

sounds like that is stressful ![:sweat:](http://forum.numer.ai/images/emoji/twitter/sweat.png?v=12)
