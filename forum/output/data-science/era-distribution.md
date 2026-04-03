---
title: "Era distribution"
category: Data Science
url: https://forum.numer.ai/t/era-distribution/3875
created_at: 2021-07-29T15:38:07.398000+00:00
last_posted_at: 2021-07-30T10:22:26.077000+00:00
posts_count: 2
views: 855
tags: []
---

# Era distribution

---

### Post #1 — **marianotir** | 2021-07-29 15:38 UTC

Interesting era distribution. Am I missing something? I was expecting to have continous era. Or maybe the numbers does not matter? I expected a longer train era.

> import pandas as pd  
>  import numpy as np  
>  import plotly.express as px  
>  import plotly.graph_objects as go  
>  import [plotly.io](<http://plotly.io>) as pio  
>  from plotly.subplots import make_subplots  
>  pio.renderers.default = “browser”  
>  training_data = pd.read_csv(“numerai_training_data.csv”)  
>  tournament_data = pd.read_csv(“numerai_tournament_data.csv”)

> df = pd.concat([training_data, tournament_data],ignore_index=True)

> df[‘era_value’] = df[‘era’].str[3:]  
>  df.loc[df[‘era’] == ‘eraX’, ‘era’] = ‘era0’  
>  df[‘era_value’] = df[‘era’].str[3:].astype(int)  
>  max_era = df[‘era_value’].max()  
>  print(max_era)  
>  df.loc[df[‘era_value’] == 0, ‘era_value’] = max_era + 1

> fig = px.scatter(df, x=“era_value”, y=“data_type”, color=“data_type”,  
>  title=“Interesting era distribution”)  
>  fig.show()

[![newplot](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/11a22c19fc9c35315311f5390a4582dbb7d4f8f8_2_690x345.png)newplot2117×1060 79.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/11a22c19fc9c35315311f5390a4582dbb7d4f8f8.png> "newplot")

---

### Post #2 — **andy_shaps** | 2021-07-30 10:22 UTC

Not all eras are in months. the live, test and val2 eras are done in weeks. this results in more eras in them than would be expected. below is how the data is currently formatted. In the latest fireside chat they have said this will change soon though. They are planning to give us the target values for all train, val and test eras in a weekly format (if i understood correctly). hope this helps

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/da34bc8250b52db5f4f6adff4a569f4fba2887a3.png)image624×445 14.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/da34bc8250b52db5f4f6adff4a569f4fba2887a3.png> "image")

edit: ignore the current/proposed titles. this post was from a long time ago so only the “proposed” image is relevant today (but as i said, will probably change soon)
