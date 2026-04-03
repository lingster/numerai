---
title: "Lagacy Predictions"
category: Tournament
url: https://forum.numer.ai/t/lagacy-predictions/5155
created_at: 2022-03-28T02:14:25.824000+00:00
last_posted_at: 2022-03-28T18:14:22.587000+00:00
posts_count: 9
views: 828
tags: []
---

# Lagacy Predictions

---

### Post #1 — **ihab** | 2022-03-28 02:14 UTC

Hello,

I tried today to upload my legacy predictions but the upload link is not there any more. Have it been removed or that was just an error?

Any one, please? Thank you.

---

### Post #2 — **richai** | 2022-03-28 02:37 UTC

We removed it but you can still upload legacy predictions just use the main upload button (works for new and legacy now).

---

### Post #3 — **ihab** | 2022-03-28 02:50 UTC _(reply to #2)_

Thank you for your response, Richard.

I tried but and got the following error:  
“Invalid submission headers. Headers must be id and prediction.”

Have the expected format changed?

And I also, tried the suggested header: "id, “prediction,” then I got another error saying:  
“You must provide predictions for ALL live IDs. Make sure you are using the latest live data.”

I had to upload my new model on the new data for now, but it is still experimental, and I would like to be able to upload my legacy prediction until I am comfortable with the new model.

Any suggestion, please? Once again, thank you Richard.

---

### Post #4 — **ark** | 2022-03-28 03:47 UTC _(reply to #3)_

Hey, ihab, legacy predictions are still accepted; I am able to upload the old example predictions and an old legacy model is still successfully submitting. Although the recent switch stopped accepting some of the very old column names, the live IDs its checking haven’t changed between dataset versions. Are you sure that your legacy model is predicting on live IDs? I recommend double checking the live tournament data file and the example predictions files.

---

### Post #5 — **ihab** | 2022-03-28 04:03 UTC

Hello [@ark](</u/ark>)  
Thank you for your reply.

I have been submitting predictions from my same models for many months now and have not changed anything at all.

All the sudden they stopped validating this week, coincidentally with the change on Numer.ai.

---

### Post #6 — **rdr91h** | 2022-03-28 11:25 UTC _(reply to #5)_

I had the same problem, the name of the columns of the submitting predictions has to be ‘id’, ‘prediction’

---

### Post #7 — **ark** | 2022-03-28 17:23 UTC

Apologies for this issue. Moving forward I’ll be adding more tests to our system to prevent accidental depreciation of prediction headers in the future. [@ihab](</u/ihab>) I’m going to DM you about the Live ID issue. The Live IDs haven’t changed so I’d like to get more information on this.

---

### Post #8 — **ihab** | 2022-03-28 17:56 UTC _(reply to #7)_

Thank you [@ark](</u/ark>)

I will respond to your DM now.

---

### Post #9 — **ihab** | 2022-03-28 18:14 UTC _(reply to #7)_

Hey [@ark](</u/ark>),  
I responded to your DM but it bounced back undeliverable.

here is what I tried to email you:  
I download the data every week as I always have, through the numerai api and not manually.  
Also,I have not touched my models for quite some time.  
My workflow for getting the data and generating my predictions have not changed for months. Thank you.
