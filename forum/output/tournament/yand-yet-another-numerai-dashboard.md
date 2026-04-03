---
title: "YAND: Yet Another Numerai Dashboard"
category: Tournament
url: https://forum.numer.ai/t/yand-yet-another-numerai-dashboard/6792
created_at: 2023-11-12T21:17:23.306000+00:00
last_posted_at: 2026-01-22T22:30:54.279000+00:00
posts_count: 16
views: 2827
tags: []
---

# YAND: Yet Another Numerai Dashboard

---

### Post #1 — **numerologist** | 2023-11-12 21:17 UTC

Ever wondered how you perform versus your fellow Numerati?  
Benchmark models are too easy / not enough of embarrassment?  
I present to you: yet another Numerai dashboard! Yep, that’s the name.

[![Screenshot 2023-11-12 at 12.23.18 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6b0dc0fe055fd8b42b560be8e68f8c45add61dab_2_690x389.png)Screenshot 2023-11-12 at 12.23.18 AM2874×1624 358 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6b0dc0fe055fd8b42b560be8e68f8c45add61dab.png> "Screenshot 2023-11-12 at 12.23.18 AM")

[YAND: Yet Another Numerai Dashboard](<https://yand.pythonanywhere.com/>)

Main features:

  * First of its kind, apple-to-apple comparison of Numerai users with date range selection
  * TC and CORRv2 summary table with filtering and multi-column sorting
  * Simplicity: get all the info you need with no extra clicks or we’ll give you your money back



Credits and acknowledgments:

  * [@pschork](</u/pschork>) for the favicon I stole from Discord memes
  * Everyone who upvoted [my discord post](<https://discord.com/channels/894652647515226152/1147604839619112980/1147604839619112980>) for the support
  * [@ia_ai](</u/ia_ai>) and [@jrai](</u/jrai>) with their dashboards for inspiration
  * [@uuazed](</u/uuazed>) for numerapi, Numerai team for the API, plotly for plotly



Roadmap:

  * Add a models page?
  * Feedback and suggestions are welcome!

---

### Post #2 — **wigglemuse** | 2023-11-12 22:09 UTC

So this is based on account-level data and not model-level data. So how is that aggregated/weighted?

---

### Post #3 — **danzell** | 2023-11-12 22:52 UTC

Any idea on how account titles like grand master, master, etc. are created? Is this part of the api or did you do some sort of mapping?

---

### Post #4 — **numerologist** | 2023-11-13 02:49 UTC

> how is that aggregated/weighted?

Just an average of whatever you see in the charts. And the charts, in turn, come from user profiles, so it’s the average over cumulative stake-weighted-average CORRv2/TC of all models.

> how account titles like grand master, master, etc. are created? Is this part of the API?

Yes. I think it’s part of the not-yet-released grandmasters proposal: [Grandmaster Proposals - Google Docs](<https://docs.google.com/document/d/1IkpbpnO_ynZ76Ah4eCnha_sgM8rOwHpQ2T3Ua3nErEU/edit>)  
No real purpose here, just think of it as an easter egg, expert danzell ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=12)

---

### Post #5 — **numerologist** | 2023-11-16 20:12 UTC

A small update. I managed to get Numerai endpoints added to [Allowlisted sites for free users: PythonAnywhere](<https://www.pythonanywhere.com/whitelist/>), so now community projects on pythonanywhere should be much easier to make. Heck, you can even try to do submissions from there ![:grin:](http://forum.numer.ai/images/emoji/twitter/grin.png?v=12)

---

### Post #6 — **numerologist** | 2023-11-28 19:56 UTC

Account-level MMC charts are now live on the dashboard.  
Also, benchmark models now appear by default.

---

### Post #7 — **numerologist** | 2024-02-02 03:36 UTC

The dashboard has been updated to reflect the current leaderboard sorting.

It’s interesting to see that some of the top participants are highly correlated… like, _almost 100%_ correlated. ![:stuck_out_tongue:](http://forum.numer.ai/images/emoji/twitter/stuck_out_tongue.png?v=12)

[YAND.](<https://yand.pythonanywhere.com/>)

---

### Post #8 — **numerologist** | 2024-03-11 19:23 UTC

**YAND 2.0 is out!**

What’s new:

  * Added a Models page
  * Replaced TC chart with Payout metric (0.5xCORR 2xMMC)



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/49493908983f1f336ce2a0e4fff618df67e577d8_2_690x463.png)image2083×1398 181 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/49493908983f1f336ce2a0e4fff618df67e577d8.png> "image")

Also, it looks like we’re pushing the limits of free hosting, so please be gentle ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=13)

---

### Post #9 — **numerologist** | 2024-03-13 21:06 UTC

A minor update: pushed some optimizations and caching, the website should be a little more robust now.

---

### Post #10 — **eleven_sigma** | 2024-03-15 08:11 UTC _(reply to #9)_

Really great! Thank you a lot!  
For YAND 3.0 this is my ‘wish list’ ![:heart_eyes:](http://forum.numer.ai/images/emoji/twitter/heart_eyes.png?v=12)  
Save groups of models and assign a label, like ‘top performers MMC’, ‘top stackers’, ‘My lgb models’,…  
and then be able to select a group to watch, instead of one by one.

---

### Post #11 — **numerologist** | 2024-11-12 23:44 UTC

**YAND gained some new features!** ![:partying_face:](https://emoji.discourse-cdn.com/twitter/partying_face.png?v=13)

[YAND](<https://yand.pythonanywhere.com/>) supports both user and model comparison for all 3 tournaments now: Main, Signals, and Crypto. This includes displaying the corresponding payout metrics for each of the tournaments. Check it out:  
Signals:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/499fae03afa6c2c409f1c044c1609650811d7efe_2_690x384.png)image1905×1061 142 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/499fae03afa6c2c409f1c044c1609650811d7efe.png> "image")

  
Crypto:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f7c4fd8fa2f03fc87428c35226edcce088962557_2_690x384.png)image1905×1061 143 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f7c4fd8fa2f03fc87428c35226edcce088962557.png> "image")

  
[YAND.](<https://yand.pythonanywhere.com/>)

---

### Post #12 — **numerologist** | 2024-12-17 02:07 UTC

I haven’t had much time for this project recently, so no UI changes, but for those who need it, I just pushed an updated version of YAND with the feature to support sets of models and users for all 3 tournaments.

To use it, simply add `?set=...` in the URL, where `...` is a comma-separated list of models/users for the appropriate dashboard.  
For example,

  * <https://yand.pythonanywhere.com/main/?set=numerologist,svendaj,benchmark_models> shows performance for the Main tournament for the specified 3 users only;
  * <https://yand.pythonanywhere.com/main/models?set=nmrology,super_model,numerai_swmm> shows performance for the Main tournament for the specified 3 models only;
  * <https://yand.pythonanywhere.com/signals/models?set=shallow_alpha,simple_lgbm_ffn> \- for Signals models;
  * <https://yand.pythonanywhere.com/crypto/models?set=joe_the_degen_01,joe_the_degen_02,joe_the_degen_03,joe_the_degen_04> \- for Crypto models etc.



Note: the URL param overrules whatever is set in the dropdown, so the dropdown will be ignored if the `set` param is present. You can still freely adjust the time range.

Using your browser bookmarks, you can achieve the groups [@eleven_sigma](</u/eleven_sigma>) requested, just with your browser instead of fancy UI. ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=12)

---

### Post #13 — **numerologist** | 2025-05-16 01:50 UTC

![:dizzy:](https://emoji.discourse-cdn.com/twitter/dizzy.png?v=14) **May 2025 Updates:**

  * Removed the dropdown limitation if you use URL params.
  * Unresolved rounds are now highlighted on the Models page.
  * Added Churn charts (currently, data available for Signals only).
  * More params: `start_date` and `end_date`. Try it out: [/main/models/?set=numerai_swmm&start_date=2025-01-01&end_date=2025-05-01](<https://yand.pythonanywhere.com/main/models/?set=numerai_swmm&start_date=2025-01-01&end_date=2025-05-01>)

---

### Post #14 — **numerologist** | 2025-08-03 19:00 UTC

Alpha & MPC scores have been added for Signals users and models pages.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/370358a460616abc9b7ec4ab1acc32e1022199c7_2_690x296.png)image1898×815 83.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/370358a460616abc9b7ec4ab1acc32e1022199c7.png> "image")

---

### Post #15 — **numerologist** | 2025-10-23 22:34 UTC

![:dizzy:](https://emoji.discourse-cdn.com/twitter/dizzy.png?v=15) **October 2025 Update:**

  * Updated charts for Signals and Crypto; account for unresolved 90d rounds in Signals
  * New URL param for the `Models` page: `mode=bar`. Example: [YAND: mode=bar&set=jos_xb_lazy,jos_all_lazy](<https://yand.pythonanywhere.com/main/models?mode=bar&set=jos_xb_lazy,jos_all_lazy>)



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ebae3da16ea839a62b935e1d241b764358930eb6_2_650x500.png)image1903×1463 140 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ebae3da16ea839a62b935e1d241b764358930eb6.png> "image")

---

### Post #16 — **fish_n_chips** | 2026-01-22 22:30 UTC

Hi,

May I share my NMR - Numerai Model Reviewer tool, with a modern retro 80s theme!

Available at numerdiff [dot] imperialai [dot] ai

And opensourced on github lingster/numerai-model-reviewer

Crypto (and mayb\e signals versions in the pipeline)

Enjoy!

(for some reason I can’t image images or links, maybe as I’m still new here)
