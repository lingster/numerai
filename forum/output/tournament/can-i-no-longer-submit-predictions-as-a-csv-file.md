---
title: "Can I no longer submit predictions as a CSV file?"
category: Tournament
url: https://forum.numer.ai/t/can-i-no-longer-submit-predictions-as-a-csv-file/7730
created_at: 2024-09-15T00:32:25.352000+00:00
last_posted_at: 2024-10-03T17:12:20.663000+00:00
posts_count: 8
views: 577
tags: []
---

# Can I no longer submit predictions as a CSV file?

---

### Post #1 — **rigrog** | 2024-09-15 00:32 UTC

Back in July, I tried to submit my usual CSV file prediction, but it was not accepted as usual.

It seems that a PKL (pickled Python program?) is now required.

Is there no longer a way to run my own models on my own machine, and submit the results in CSV format?

---

### Post #2 — **wigglemuse** | 2024-09-15 01:39 UTC

Hi, nice to see you back. You can still do it – problem must be something else. Are you getting a particular error or…?

---

### Post #3 — **rigrog** | 2024-09-15 02:31 UTC _(reply to #2)_

Hi Wigglemuse! I was guessing it’d be you, who’d extend the helping hand.

One Saturday in July, after making my CSV file, I attempted to submit it the same way I did the previous Saturday – but Numerai wasn’t having it! It was demanding PKL.

The way I had been submitting: click a link on the “Submissions” page, which opens a dialog box, for selecting the file to submit. One Saturday it accepted CSV, the next Saturday it wouldn’t.

Perhaps to submit CSV, I’ll have to submit via Numerapi?

---

### Post #4 — **wigglemuse** | 2024-09-15 02:49 UTC _(reply to #3)_

Sounds like you are just hitting the wrong button. The one on the left with the cloud is the pkl button – it is the third button from the right (plain up arrow) that you want for a csv file.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1b97d393cf8d7f484abb106f10924c04c1399058.png)image197×118 593 Bytes](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1b97d393cf8d7f484abb106f10924c04c1399058.png> "image")

---

### Post #5 — **rigrog** | 2024-09-15 14:15 UTC _(reply to #4)_

Thanks, wig! [need 20 chars…]

---

### Post #6 — **hatcat** | 2024-10-01 13:36 UTC

Do you have a working example of automated csv (predictions) submission via api ? Because nothing of this works // import numerapi  
api = numerapi.NumerAPI(public_id=publicId, secret_key=secretKey)  
model_id = api.get_models()[“model_name”] # neither with directly uuid model id  
api.upload_predictions(predName, model_id=model_id)

Thanks for any help!

---

### Post #7 — **shatteredx** | 2024-10-01 22:37 UTC _(reply to #6)_

Your code looks fine.

What error are you getting?

Could be bad API key or invalid predictions.

---

### Post #8 — **hatcat** | 2024-10-03 17:12 UTC

Thanks, imports were not correct // Here is an auto uploads script that actually works, check out numerai-crypto-helper on github
