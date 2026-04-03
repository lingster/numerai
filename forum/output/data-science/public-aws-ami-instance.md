---
title: "Public AWS AMI instance?"
category: Data Science
url: https://forum.numer.ai/t/public-aws-ami-instance/1481
created_at: 2021-01-17T01:00:02.165000+00:00
last_posted_at: 2021-12-13T19:22:22.595000+00:00
posts_count: 6
views: 1561
tags: []
---

# Public AWS AMI instance?

---

### Post #1 — **pumplerod** | 2021-01-17 01:00 UTC

I’ve reached the limits of what my poor laptop is able to crunch, so I’ve begun to explore some other cloud compute options.

Colab: Seemed like it might be promising, however even with their GPU instance it looked like I was going to exceed their time limit, and I found the system to be a little flaky at times. I had a Google drive mounted which stored an enormous amount of data I had written out for feature extraction that became corrupted and will now have to regenerate all that training/validation extracted feature data.

At the moment I’m exploring the use of EC2 and S3 with amazon and the Saturn service for Jupyter notebooks. If anyone has horror stories about this I would appreciate hearing them before I get in too deep.

I’m also wondering, and the main reason for this post, if anyone has already assembled or come across a pre-configured AMI that might be more specific to Numerai. Such as having already installed proper versions of python, tensorflow, etc… as well as the numerai module for down/uploading data and predictions. Ideally something with GPU support (I’m not sure if AWS offers TPU devices).

I’d appreciate any advice from folks that have already traveled this path.

---

### Post #2 — **domanton** | 2021-01-19 16:24 UTC

AWS and google are two known options - you can contact their support team and ask them about it and may be they can help you.

Contacting them is your best option otherwise maybe there is other option which provide exactly what you need - but you need to find that out. Your best option is twitter or facebook group.

tag like minded people their and they might be able to help you.

* * *

[Sharp & Fellows, Inc.](<https://www.sharpandfellows.com/>)

---

### Post #3 — **jackkidman123** | 2021-12-11 13:33 UTC

At the moment I’m exploring the use of EC2 and S3 with amazon and the Saturn service for Jupyter notebooks.

If anyone has horror stories about this I would appreciate hearing them before I get in too deep.

I’m also wondering, and the main reason for this post, if anyone has already assembled or come across a pre-configured AMI that might be more specific to Numerai.

Such as having already installed proper versions of python, tensorflow, as well as the numerai module for down/uploading data and predictions.

Ideally something with GPU support.

[Hidden Trails, Ltd.](<http://www.hiddentrails.com/>)

---

### Post #4 — **pumplerod** | 2021-12-11 16:53 UTC _(reply to #3)_

I would only caution you to take note of where and what AWS services and policies Saturn is creating on your account. Personally, I find AWS can become very confusing very quickly. Saturn wound up setting up services on my AWS which got buried on a different Amazon location than I usually use ( it put them on Ohio-east, if I remember correctly). Then, somehow, it left instances running after I was done testing. I became distracted with life and before I knew it months had gone by without me realizing that there were charges to AWS. Then it took a lot of digging to figure out where the mystery charges were coming from.

---

### Post #5 — **johnnywhippet** | 2021-12-13 15:41 UTC

I’m experimenting with [Paperspace.com](<https://www.paperspace.com/>)

So far… not bad, not but not excellent though does what I need it to in the timeframe I need. free* gpus are adequate for what I need. CPUs aren’t brill but I get plenty of ram (30Gb) for what I need, that being the big big dataset, and 15GB of storage, not a massive amount, All for $8 a month, roughly £6 .

---

### Post #6 — **objectscience** | 2021-12-13 19:22 UTC

[@pumplerod](</u/pumplerod>) I don’t know if this would help in the short term or not. We did a [Boruta](<https://github.com/johnputmanii/numerai_xgb_eb/tree/main/borutashap>) run not long ago and [@aventurine](</u/aventurine>) added a nice search function to it.

If that doesn’t work, I’m not beyond donating some local computer cycles to help you recreate what you lost.
