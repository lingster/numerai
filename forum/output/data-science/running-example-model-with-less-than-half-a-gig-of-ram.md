---
title: "Running example model with less than half a gig of RAM"
category: Data Science
url: https://forum.numer.ai/t/running-example-model-with-less-than-half-a-gig-of-ram/786
created_at: 2020-08-17T18:00:11.851000+00:00
last_posted_at: 2021-04-19T11:45:00.113000+00:00
posts_count: 2
views: 2527
tags: []
---

# Running example model with less than half a gig of RAM

---

### Post #1 — **jrb** | 2020-08-17 18:00 UTC

Recently, I was travelling for a couple of weeks with only an iPad and my phone for compute. The plan was to VPN home and ssh into my desktop to run the docker container that submits my predictions, every weekend.

The plan worked flawlessly for the first week. But from the 2nd week onwards, a dead IoT switch (Belkin Wemo) that I was using to turn my desktop on and off remotely, foiled the plan. Fortunately for me, my spouse was carrying her travel laptop, a 2017 Retina MacBook with a measly 8GB of RAM. I use git to version all my code and [git lfs](<https://git-lfs.github.com/>) for versioning the model weights, so getting them on the laptop wasn’t a problem. But running my inference container with only ~5GB of usable memory was. My first thought was to spin up a big EC2 instance and run everything off of it. But then I thought it might be worth trying to run small batch inference on the tiny laptop. And it worked quite well. I managed to submit predictions for 2 weeks with it.

Now that I’m back home, I’ve clean up the code a bit and adapted it to run the example model. The code iterates over the tournament data one row at a time in a background thread and emits a `DataFrame` every time it crosses an era boundary. The output file is also appended to on an incremental basis. Also, I profiled the code to measure its peak memory usage. I compared naively running inference on the whole tournament dataset with era-wise batched inference. Peak memory usage goes down from `11662.2 MiB` to `463.7 MiB` (96% decrease). Although the inference time goes up from `3:13.16` minutes to `10:46.79` minutes (234% increase). The inference time could perhaps be slightly improved by not counting the number of eras in the tournament dataset. Counting eras is necessary for displaying the [tqdm](<https://pypi.org/project/tqdm/>) progress bar, but it comes at the cost of having to read the compressed dataset once more.

I thought people people running compute might find it useful, which is why I’m posting it here.
    
    
    import csv
    import lzma
    import pathlib
    import queue
    import re
    import threading
    
    import numpy as np
    import pandas as pd
    import tqdm
    import xgboost as xgb
    
    from typing import Any, Callable, IO, List, Set
    
    TOURNAMENT_NAME = "kazutsugi"
    PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"
    SUBMISSION_FILENAME = f"{TOURNAMENT_NAME}_submission.csv"
    
    ERA_RE = re.compile(r"(era(?:X|\d+))")
    
    
    def open_file(file_path: pathlib.Path, mode: str = "rt") -> IO:
        if file_path.suffix == '.xz':
            return lzma.open(file_path, mode)
        else:
            return open(file_path, mode)
    
    
    def maybe_float16(x: str) -> np.float16:
        return np.float16(x if x else np.nan)
    
    
    def build_conversions(column_names: List[str]) \
            -> List[Callable[[str], Any]]:
        conversions = []
        for name in column_names:
            if name.startswith('feature_'):
                conversions.append(np.float16)
            elif name.startswith('target_'):
                conversions.append(maybe_float16)
            else:
                conversions.append(str)
        return conversions
    
    
    def distinct_eras(file_path: pathlib.Path) -> Set[str]:
        eras = set()
        chunk_size = (1024 * 10) ** 2  # Read in chunks of 10 MiB
        with open_file(file_path) as f:
            while True:
                s = f.read(chunk_size)
                if not s:
                    break
                matches = ERA_RE.findall(s)
                eras.update(matches)
                if 'eraX' in eras:
                    break
        return eras
    
    
    def iter_csv(file_path: pathlib.Path):
        with open_file(file_path) as f:
            reader = csv.reader(f)
            column_names = None
            era_col_idx = None
            conversions = None
            current_era = None
            df_dict = {}
            for row in reader:
                if column_names is None:
                    era_col_idx = row.index('era')
                    conversions = build_conversions(row)
                    column_names = row[1:]
                    continue
                row_ = [conversions[idx](x) for idx, x in enumerate(row)]
                row_era = row_[era_col_idx]
                if current_era is None:
                    current_era = row_era
                elif current_era != row_era:
                    current_era = row_era
                    df = pd.DataFrame.from_dict(df_dict, orient='index',
                                                columns=column_names)
                    df_dict = {}
                    yield df
                df_dict[row_[0]] = row[1:]
            if df_dict:
                df = pd.DataFrame.from_dict(df_dict, orient='index',
                                            columns=column_names)
                yield df
    
    
    class Prefetcher(threading.Thread):
        SENTINEL = ()
    
        def __init__(self, iterator, queue_length=2):
            super().__init__()
            self.iterator = iterator
            self.queue = queue.Queue(queue_length)
    
        def run(self):
            for data in self.iterator:
                self.queue.put(data)
            self.queue.put(self.SENTINEL)
    
        def __iter__(self):
            return self
    
        def __next__(self):
            data = self.queue.get()
            if data is self.SENTINEL:
                raise StopIteration
            return data
    
    
    def main():
        # The numerai example model
        # https://github.com/numerai/example-scripts/blob/master/example_model.py
        model = xgb.XGBRegressor()
        model.load_model("example_model.xgb")
        # Downloaded from:
        # https://numerai-public-datasets.s3-us-west-2.amazonaws.com/
        p = pathlib.Path("latest_numerai_tournament_data.csv.xz")
        eras = distinct_eras(p)
        pf = Prefetcher(iter_csv(p))
        pf.start()
        feature_cols = None
        for idx, df in tqdm.tqdm(enumerate(pf), total=len(eras), disable=None):
            if feature_cols is None:
                feature_cols = [x for x in df.columns if x.startswith('feature_')]
            pred = model.predict(df[feature_cols].values)
            p = pd.Series(pred, index=df.index).to_frame(PREDICTION_NAME)
            if idx == 0:
                p.to_csv(SUBMISSION_FILENAME, index_label="id")
            else:
                p.to_csv(SUBMISSION_FILENAME, mode='a', header=False)
    
    
    if __name__ == '__main__':
        main()

---

### Post #2 — **rw227** | 2021-04-19 11:45 UTC

Hi, code was great, however, my memory issues persist as it is in “Training” that memory has issues, never gets to create that .xgb. Some pointers how to adapt the above would be great … or sites where some answers may lay. R
