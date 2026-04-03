---
title: "Question: Public AWS AMI instance"
category: Data Science
url: https://forum.numer.ai/t/question-public-aws-ami-instance/3657
created_at: 2021-06-24T19:06:36.901000+00:00
last_posted_at: 2021-06-25T09:59:16.882000+00:00
posts_count: 3
views: 621
tags: []
---

# Question: Public AWS AMI instance

---

### Post #1 — **mikeklien** | 2021-06-24 19:06 UTC

I’ve reached the limits of what my poor laptop is able to crunch, so I’ve begun to explore some other cloud compute options.

Colab: Seemed like it might be promising, however even with their GPU instance it looked like I was going to exceed their time limit, and I found the system to be a little flaky at times.

I had a Google drive mounted which stored an enormous amount of data I had written out for feature extraction that became corrupted and will now have to regenerate all that training/validation extracted feature data.

At the moment I’m exploring the use of EC2 and S3 with amazon and the Saturn service for Jupyter notebooks. If anyone has horror stories about this I would appreciate hearing them before I get in too deep.

I’m also wondering, and the main reason for this post, if anyone has already assembled or come across a pre-configured AMI that might be more specific to Numerai. Such as having already installed proper versions of python, tensorflow, etc… as well as the numerai module for down/uploading data and predictions. Ideally something with GPU support (I’m not sure if AWS offers TPU devices).

I’d appreciate any advice from folks that have already traveled this path.

* * *

[SeatsAndChairs.com Inc](<https://seatsandchairs.com/>)

---

### Post #2 — **minou** | 2021-06-25 08:52 UTC

Yes, they have deep learning amis. [Amazon Deep Learning AMIs](<https://aws.amazon.com/machine-learning/amis/>)  
I’ve used the one with the most recent ubuntu. The motd has instructions and a choice of scripts for setting up the environment after login with a single command, e.g. for tensorflow2 with python 3. numerai isn’t installed but any extra packages you might need can be easily installed with pip. Using spot instances works out the most cost effective, and by bidding up to 150% of the current spot price I had no terminations over runs of several hours at a time. I used single and 4 CPU instances p2.2xlarge and g4dn.12xlarge but found multigpu had slow startup due to tensorflow limitations, so leant towards single gpu. Note that some instances have directly connected ephemeral storage which isn’t formatted and mounted by default so you’d need to do that. I created a few scripts to handle rsyncing code and setup scripts to quickly bootstrap a new instance, format and mount the ephemeral drive as /mnt/data if the instance has one or else just create a directory there, upload data from local or download it to the instance etc. Didn’t use notebooks or anything like that.

---

### Post #3 — **autratec** | 2021-06-25 09:59 UTC

Why not using azure ml studio ? It is free .
