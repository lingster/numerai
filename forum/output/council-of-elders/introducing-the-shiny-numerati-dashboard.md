---
title: "Introducing the Shiny Numerati Dashboard"
category: Council of Elders
url: https://forum.numer.ai/t/introducing-the-shiny-numerati-dashboard/6826
created_at: 2023-11-28T09:42:30.824000+00:00
last_posted_at: 2024-07-05T20:52:47.668000+00:00
posts_count: 7
views: 1416
tags: []
---

# Introducing the Shiny Numerati Dashboard

---

### Post #1 — **ia_ai** | 2023-11-28 09:42 UTC

Hey fam, as promised, I am writing this post about **Shiny Numerati**. It is a community dashboard for the main Numerai tournament. You can use it to track your model performance and payouts.

The main objectives of this forum post:

  1. Onboarding new users with a simple quick-start guide
  2. Collecting feedback from the community (bugs and feature requests)
  3. Providing a roadmap (and polls to upvote feature requests from time to time)
  4. Providing updates on new features



OK, let’s get started!

# 1\. Links to App:

  * App with HF nav bar: [Shiny Numerati - a Hugging Face Space by jofaichow](<https://huggingface.co/spaces/jofaichow/shiny-numerati>)
  * App without HF nav bar: <https://jofaichow-shiny-numerati.hf.space/>
  * Source code (HF): [jofaichow/shiny-numerati at main](<https://huggingface.co/spaces/jofaichow/shiny-numerati/tree/main>)
  * Source code (GitHub): [GitHub - woobe/shiny-numerati](<https://github.com/woobe/shiny-numerati>)



# 2\. Quick-start Guide

### Step 1: “Start Here” → Use the picker input widget to select your model(s) → Step 2: Download data from Numerai

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e06634327ac61cb625e1a201133d8cf344258aa7_2_627x500.png)image2159×1719 223 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e06634327ac61cb625e1a201133d8cf344258aa7.png> "image")

### Step 3: “Performance Summary” → Step 4: Adjust the Era/Round Filter → Step 5: Generate

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/922a55bec6ada10f02667c2c0a85d44a073fbbbd_2_400x499.png)image2159×2697 476 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/922a55bec6ada10f02667c2c0a85d44a073fbbbd.png> "image")

### Explore Other Performance Summary Tabs

#### KPI Analysis (CORRv2 vs. TC)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b11ef3fdf78ac800abf5706ba116c6cb016fe538_2_400x499.png)image2159×2697 404 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b11ef3fdf78ac800abf5706ba116c6cb016fe538.png> "image")

#### Payout Summary (Overview)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cd89c51e2e655b51a23bc8677b5fd869c0da96af_2_466x500.png)image2159×2316 334 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cd89c51e2e655b51a23bc8677b5fd869c0da96af.png> "image")

#### Payout Summary Chart (Individual Models)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/24544c51ac5d1340e986cf4b7749acd273f03e67_2_466x500.png)image2159×2316 312 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/24544c51ac5d1340e986cf4b7749acd273f03e67.png> "image")

#### Download Raw Data

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4d8d225e708233fbfc9165e1f7643f3983b823ba_2_690x305.png)image2159×956 121 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4d8d225e708233fbfc9165e1f7643f3983b823ba.png> "image")

#### Materials from CoE Sponsored Events

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3cf826d75aa7ed1c1ebf738a60f7e1f0d6227a50_2_419x500.jpeg)image1920×2286 330 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3cf826d75aa7ed1c1ebf738a60f7e1f0d6227a50.jpeg> "image")

# 3\. Roadmap

I will continue to update this section after collecting some user feedback.

Some feature requests that I remember from various discussions on Discord:

  * Around the world with Numeratis Survey results ![:white_check_mark:](https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15)
  * Flexible model name inputs (e.g. text, account level, json)
  * More KPI charts (with options to pick different KPIs for x and y-axis)
  * Shiny Numerati for Signals
  * Artificial stakes for payout simulation
  * Numerai’s benchmark models (a button to download and show data from benchmark models)



(Polls will come soon after I have collected more feedback)

# 4\. Feedback

Please comment below and let me know what you want ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=15)

---

### Post #2 — **ia_ai** | 2023-11-28 18:56 UTC

# 2023-11-28 - Version 0.2.5

Added a new **Score Multipliers: 0.5 x CORRv2 + 2.0 x MMCv2**

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/418ccc64b8ec09a7e3de863a251451b1e8d323ee_2_400x499.png)image2159×2697 454 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/418ccc64b8ec09a7e3de863a251451b1e8d323ee.png> "image")

---

### Post #3 — **ia_ai** | 2023-11-29 12:16 UTC

## 2023-11-29 - Version 0.2.6

Added [**Survey Results**](<http://forum.numer.ai/t/around-the-world-with-numeratis-survey-for-upcoming-events/>) to **Community Events** tab

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e50baf32dfbed708ccb8c997b24b82ff913c07e1_2_481x500.png)image2159×2243 292 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e50baf32dfbed708ccb8c997b24b82ff913c07e1.png> "image")

---

### Post #4 — **animalfarm** | 2023-12-13 10:29 UTC _(reply to #3)_

Hi, your dashboards are very useful, how often you check for new models, I uploaded some last week, but no first results yet.

---

### Post #5 — **ia_ai** | 2023-12-13 13:02 UTC _(reply to #4)_

Hey [@animalfarm](</u/animalfarm>) thanks for your kind words. I usually update my dashboard when new scores become available. I am relying on the `get_leaderboard` API function to get the list of all models which have at least one resolved round. If your models are “too new” (i.e. no resolved round yet), you will have to wait until they have their first resolved round.

Having said that, there is a quick hack if you don’t want to wait. You can fork my app on HF and then edit [this line](<https://huggingface.co/spaces/jofaichow/shiny-numerati/blob/1fefb3a9c52d3510d3dab3880595798f35f7243d/app/app.R#L243>). Replace `choices = ls_username,` with `choices = c("model_name_1", "model_name_2")`. Then you can run the app with specific model names.

---

### Post #6 — **animalfarm** | 2023-12-13 13:54 UTC _(reply to #5)_

[@ia_ai](</u/ia_ai>) I really appreciate your answer and will definitely check it out.

---

### Post #7 — **ia_ai** | 2024-07-05 20:52 UTC

## 2024-07-05 - Version 0.2.9

Added `KPI (C&M)` tab for `CorrV2` and `MMC` performance analysis.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/66a5100d4c416593cc95f5cdcd5244f96f93421a_2_380x500.png)image2159×2834 399 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/66a5100d4c416593cc95f5cdcd5244f96f93421a.png> "image")
