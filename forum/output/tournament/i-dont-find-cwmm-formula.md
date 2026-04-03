---
title: "I don't find CWMM formula"
category: Tournament
url: https://forum.numer.ai/t/i-dont-find-cwmm-formula/7090
created_at: 2024-03-09T00:00:28.605000+00:00
last_posted_at: 2024-03-09T00:00:28.684000+00:00
posts_count: 1
views: 364
tags: []
---

# I don't find CWMM formula

---

### Post #1 — **eleven_sigma** | 2024-03-09 00:00 UTC

In CWMM are predictions and meta model ranked and gaussianized?  
Both use pot = 1.5 too or only preds or none?  
I don’t find the code for CWMM in

[github.com/numerai/numerai-tools](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py>)

#### [numerai_tools/scoring.py](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py>)

[`master`](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py>)
    
    
    from typing import List, Tuple, Union, Optional
    
    import numpy as np
    import pandas as pd  # type: ignore
    from scipy import stats  # type: ignore
    from sklearn.preprocessing import OneHotEncoder  # type: ignore
    
    
    # sometimes when we match up the target/prediction indices,
    # changes in stock universe causes some stocks to enter / leave,
    # this ensures we don't filter too much
    DEFAULT_MAX_FILTERED_INDEX_RATIO = 0.2
    
    
    def filter_sort_index(
        s1: Union[pd.DataFrame, pd.Series],
        s2: Union[pd.DataFrame, pd.Series],
        max_filtered_ratio: float = DEFAULT_MAX_FILTERED_INDEX_RATIO,
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Filters the indices of the given series to match each other,
    

This file has been truncated. [show original](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py>)

EDIT:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/90e8adeb4f6f03ac5b052087372c6555fb93d298_2_500x500.png) [docs.numer.ai](<https://docs.numer.ai/numerai-tournament/scoring/correlation-corr>)

### [Correlation (CORR) | Numerai Docs](<https://docs.numer.ai/numerai-tournament/scoring/correlation-corr>)

Where is CWMM? is numerai_corr function used between mm and preds?
