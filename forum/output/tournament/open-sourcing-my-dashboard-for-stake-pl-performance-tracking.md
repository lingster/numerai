---
title: "Open sourcing my dashboard for Stake PL & Performance Tracking"
category: Tournament
url: https://forum.numer.ai/t/open-sourcing-my-dashboard-for-stake-pl-performance-tracking/5334
created_at: 2022-04-29T08:39:51.267000+00:00
last_posted_at: 2022-04-29T08:39:51.516000+00:00
posts_count: 1
views: 843
tags: []
---

# Open sourcing my dashboard for Stake PL & Performance Tracking

---

### Post #1 — **yxbot** | 2022-04-29 08:39 UTC

Dear fam:

I would like to share and completely open source the numerai dashboard I have built over the last 10 months for my personal usage.

**Streamlit Cloud link** : <https://share.streamlit.io/yifanxie/numerdash/main/numerdash_app.py>  
**Source code:** [GitHub - yifanxie/numerdash: yet another numerai dashboard](<https://github.com/yifanxie/numerdash>)

**Overview**  
This provides the following

  * Portfolio (i.e. bundles of models) based Stake P/L overview

  * Performance, metrics(TC/Corr/FNCV3), trend tracking and comparison.




It is developed using Streamlit + NumerAPI, and hosted on Streamlit Cloud

Here are some screenshot examples:

_Stake Overview_  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b6aa4676d02360c3c7fc0c96ae938ed984940dc4_2_690x404.jpeg)image1102×646 141 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b6aa4676d02360c3c7fc0c96ae938ed984940dc4.jpeg> "image")

_Performance Tracking_  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a24c6427735fe880bbae16612e46568b21c8198c_2_690x364.jpeg)image1264×668 160 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a24c6427735fe880bbae16612e46568b21c8198c.jpeg> "image")

**Usage Instruction**  
Should be easy enough to operate, but here is a simple [usage instruction](<https://docs.google.com/presentation/d/1MoHCltsKLu1FjPXxxIMMqYUrijnBYoK-xqno3d6EBvA/edit?usp=sharing>)

**Known issues and some remedies**

  * some typos here and there
  * Live rounds P/L could display old values if the browser session was left open overnight - just open a new browser session
  * In the “Stake_type” in live rounds P/L doesn’t have TC yet.
  * Streamlit Cloud reloading every 15 minutes also, sometime cause error - just need refreshing



Feel free to enjoy using it, or even better build on it ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

**Acknowledgement**  
First of all, I want to thank Joe ([@ia_ai](</u/ia_ai>)) for 1) getting me back to the tournament, and 2) bouncing ideas and feedback with me for all these time

  * All the dashboard builders especially [@ceunen](</u/ceunen>) and [@ia_ai](</u/ia_ai>) for your existing implementations, got lots of inspiration from it.
  * [@uuazed](</u/uuazed>) and the Numerai team for Numerapi, without it this wouldn’t be possible



Best Regards  
Yifan
