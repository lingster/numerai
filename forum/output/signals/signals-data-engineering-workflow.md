---
title: "Signals Data Engineering Workflow"
category: Signals
url: https://forum.numer.ai/t/signals-data-engineering-workflow/2159
created_at: 2021-03-05T03:04:33.195000+00:00
last_posted_at: 2021-03-06T04:21:32.606000+00:00
posts_count: 2
views: 885
tags: []
---

# Signals Data Engineering Workflow

---

### Post #1 — **stacktrace** | 2021-03-05 03:04 UTC

I was wondering if anyone would be kind enough to share how they have setup their data engineering and automation for submitting to Signals.

I am already struggling with the most basic first step, i.e,:

  * **pricing data ETL** : on a weekly scheduled basis grab pricing for Signals universe from some provider endpoint from, say, t-10 years to t and push to some storage bucket



I **do not** want to manage any VMs so am trying to do this in a serverless way. I have tried **GCP Cloud Functions** which is _almost_ perfect, except the runtime is limited to 9 minutes and it takes about 40 minutes to grab pricing for the full universe. I have another data job which takes 4hrs.

How is everyone doing this? This is a common data engineering step that we all need to do.

---

### Post #2 — **whaleblotter** | 2021-03-06 04:21 UTC

One possibility is to download daily in daily or weekly chunks, and record progress to a file or Firestore document. Alternatively, if you must download all at once, create a function to trigger an AI Training Platform job.

There was a medium article about how AI Training Platform was poorly named. It can actually be used to for any long running job. I think the smallest machine size is n1-standard-4, though. So, it’s not the cheapest.
