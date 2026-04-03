---
title: "Error of running example_model.py in Kaggle"
category: Tournament
url: https://forum.numer.ai/t/error-of-running-example-model-py-in-kaggle/4354
created_at: 2021-10-18T07:28:10.924000+00:00
last_posted_at: 2021-10-18T23:01:00.595000+00:00
posts_count: 5
views: 755
tags: []
---

# Error of running example_model.py in Kaggle

---

### Post #1 — **autratec** | 2021-10-18 07:28 UTC

Hi all, i want to run latest example_model.py, collected from: <https://github.com/numerai/example-scripts/blob/master/example_model.py>, under kaggle notebook and encounter some basic error related to utlis

i have installed utils: !pip install utils  
but still encountered error to following instruction:

from utils import save_model, load_model, neutralize, get_biggest_change_features, validation_metrics, download_data

error: ImportError: cannot import name ‘save_model’ from ‘utils’ (/opt/conda/lib/python3.7/site-packages/utils/**init**.py)

Any suggestion here to fix it ? thanks.

---

### Post #2 — **kenfus** | 2021-10-18 10:39 UTC

utils is a py-script, not a package

---

### Post #3 — **autratec** | 2021-10-18 11:16 UTC _(reply to #2)_

What does it mean ? And how I can fix it under kaggle environment ?

---

### Post #4 — **suud** | 2021-10-18 16:27 UTC _(reply to #3)_

The functions you are trying to import can be found in [this module](<https://github.com/numerai/example-scripts/blob/master/utils.py>)

---

### Post #5 — **autratec** | 2021-10-18 23:01 UTC _(reply to #4)_

Thanks for that advice. Problem solved.
