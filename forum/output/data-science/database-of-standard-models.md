---
title: "Database of Standard Models"
category: Data Science
url: https://forum.numer.ai/t/database-of-standard-models/1290
created_at: 2020-12-10T03:08:33.179000+00:00
last_posted_at: 2020-12-15T02:40:53.834000+00:00
posts_count: 6
views: 1460
tags: []
---

# Database of Standard Models

---

### Post #1 — **hb_scout** | 2020-12-10 03:08 UTC

I’ve created a Google Sheet to compile all the standard models that are maintained by the Numerai team or the community that regularly submit various known models. Most users know about integration_test that submits the example predictions, but there are others that are currently not captured anywhere. This should help people find good benchmarks to compare their live performance.

Please feel free to add any users that submit standard models or any of your own models as well if you’d like to share the information. If you don’t plan on submitting the same model going forward, just put the rounds you submitted it in the past and indicate that you will not be actively maintaining it.

[docs.google.com](<https://docs.google.com/spreadsheets/d/1xaWY26aBN-kX77xskDA9zsmAIBV12cbV6666QGvmlTs/edit#gid=0>) [](<https://docs.google.com/spreadsheets/d/1xaWY26aBN-kX77xskDA9zsmAIBV12cbV6666QGvmlTs/edit#gid=0>)

### [Numerai Standard Models Database](<https://docs.google.com/spreadsheets/d/1xaWY26aBN-kX77xskDA9zsmAIBV12cbV6666QGvmlTs/edit#gid=0>)

Sheet1 Model Name,Model Link,Github Link,Submitted Rounds,Algorithm,Feature Neutralization,Era Boosting,Included Features,Included Eras,Point of Contact,Actively Maintained integration_test,<a...

---

### Post #2 — **perfect_fit** | 2020-12-14 19:43 UTC

This is awesome! Thank you!

What about all the COVID bots from the Numerai team? Anyone an idea what those models are about?

Example:  
<https://numer.ai/covid19>

---

### Post #3 — **hb_scout** | 2020-12-14 23:07 UTC

Those models seem like a user’s models, not necessarily “standard” models with the approach discussed publicly or, ideally, with published code. If any users want to add their personal models to this spreadsheet and share them, they certainly can, but I don’t have any info about the internals of those and I don’t think any of the Numerai team knows either.

---

### Post #4 — **wigglemuse** | 2020-12-14 23:13 UTC _(reply to #3)_

covid19 & covid20 are michael oliver models (that pre-date his joining the team)

---

### Post #5 — **hb_scout** | 2020-12-14 23:23 UTC _(reply to #4)_

Oh nice, yeah I didn’t see that they had the Numerai-team symbol next to them because I looked quickly on my phone.

It would be great if Michael Oliver and Mike P could add the models that Numerai plans to maintain internally to the list. If they made those covid models before joining and aren’t maintaining them in their numerai roles, they can share them if they want to also!

The other ones I’m interested in cataloging are any of the models that monitor specific subsets of features. I know that Uki discussed some of those in his blog post and if anyone has the details, please add them as well.

---

### Post #6 — **lackofintelligence** | 2020-12-15 02:40 UTC _(reply to #5)_

Maybe part of this effort could include nailing down the differences between the official integration_test model and the apparent one since people see discrepancies between the model as trained locally and the example predictions? The example predictions usually seem to perform better than locally trained models.
