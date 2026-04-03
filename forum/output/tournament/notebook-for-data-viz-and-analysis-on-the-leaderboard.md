---
title: "Notebook for Data Viz and Analysis on the Leaderboard"
category: Tournament
url: https://forum.numer.ai/t/notebook-for-data-viz-and-analysis-on-the-leaderboard/2245
created_at: 2021-03-08T19:54:56.584000+00:00
last_posted_at: 2021-03-12T19:25:35.081000+00:00
posts_count: 5
views: 833
tags: []
---

# Notebook for Data Viz and Analysis on the Leaderboard

---

### Post #1 — **mrquantsalot** | 2021-03-08 19:54 UTC

Hi everybody,

I wrote a notebook to query the leaderboard and do a bunch of analysis on it. I wanted to figure out what successful users were doing and what % of users were successful.

Check out the notebook here:[Notebook on Leaderboard Analysis and Viz.](<https://drive.google.com/file/d/19Jm5YZu0rywDGgZx0aLPzBBCkrh1lXib/view?usp=sharing>)

Here are some of my results:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c00ba870760f0bbf880e2c7696e5c4b47694de9c.png)image556×494 21.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c00ba870760f0bbf880e2c7696e5c4b47694de9c.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/07ba03ca7633d5132c83410d41d0415a96ee4746_2_514x500.png)image519×504 20.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/07ba03ca7633d5132c83410d41d0415a96ee4746.png> "image")

You can copy the notebook and customize it to see other relationships in real time.

---

### Post #2 — **datacryptoanalytics** | 2021-03-12 00:21 UTC

Hi friend, great job, I added some improvements to the graph and add

> `import pandas.util.testing as tm`

[![download](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ac4638960cb3b1d7e1ce68f9886d1eca3b81e04c.png)download835×441 17 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ac4638960cb3b1d7e1ce68f9886d1eca3b81e04c.png> "download")

saved changes to this [repository](<https://github.com/felipsoarez/numerai-colab/blob/main/C%C3%B3pia_de_Numerai_Leaderboard_Viz_and_Analysis.ipynb>) on github

---

### Post #3 — **factorsparsity** | 2021-03-12 18:52 UTC

Just wondering - I see four colours in the graph but only three in the legend.

---

### Post #4 — **mrquantsalot** | 2021-03-12 19:03 UTC _(reply to #3)_

The alpha =.5 in the create_histogram() method is the opacity of each of the colors in the legend. The dark purple at the bottom is the where all of the colors overlap. There is probably a cleaner way to visualize this but I am not sure what it is.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bfff020b5b0c16c0ba18200c0281523ecdc17691.png)image988×163 12.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bfff020b5b0c16c0ba18200c0281523ecdc17691.png> "image")

---

### Post #5 — **factorsparsity** | 2021-03-12 19:25 UTC

Ah, cool. That’s why. Thanks.
