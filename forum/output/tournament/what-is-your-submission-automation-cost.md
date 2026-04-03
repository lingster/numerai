---
title: "What is your submission automation cost?"
category: Tournament
url: https://forum.numer.ai/t/what-is-your-submission-automation-cost/5755
created_at: 2022-10-18T00:26:40.662000+00:00
last_posted_at: 2023-03-27T08:15:52.838000+00:00
posts_count: 24
views: 2782
tags: []
---

# What is your submission automation cost?

---

### Post #1 — **ryo_matsuzaka** | 2022-10-18 00:26 UTC

I am thnking about submission automation in cloud.

---

### Post #2 — **jacob_stahl** | 2022-10-18 00:59 UTC

I’m considering moving my submission code to Azure Functions [Azure Functions Overview | Microsoft Learn](<https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview>). The cost is basically $0, I just haven’t gotten around to it yet.

---

### Post #3 — **ryo_matsuzaka** | 2022-10-18 03:31 UTC _(reply to #2)_

Does it have enough computational resources?  
Similar service like GCP cloud functions has limatation for memory which is not suitable for training, I think.

---

### Post #4 — **jacob_stahl** | 2022-10-18 23:18 UTC _(reply to #3)_

Not for training, like not even close. Azure functions are limited too ~1.5GB of memory, which should be enough for most models to predict a single era. I think Google Cloud and AWS offer equivalent, but I don’t know what their limitations are.

---

### Post #5 — **ryo_matsuzaka** | 2022-10-19 03:59 UTC _(reply to #4)_

Don’t you update trained model with updated dataset?

---

### Post #6 — **jacob_stahl** | 2022-10-20 01:26 UTC _(reply to #5)_

I have a lot of older models that I’m afraid to retrain.

---

### Post #7 — **papaemman** | 2022-11-30 00:21 UTC

[@jacob_stahl](</u/jacob_stahl>) [@ryo_matsuzaka](</u/ryo_matsuzaka>)

I have published an article describing “How I automated my Numerai weekly submission pipeline for free, using Azure functions and python”.

I think you will find it useful!

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0f95de5840ff0771b84ea77cfa42a1e98b4f1614.png) [Medium – 23 May 22](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c> "09:56AM - 23 May 2022")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b14fe246a06308eb911c06967bef537823c16135_2_690x171.png)

### [How I automated my Numerai weekly submissions pipeline for free, using Azure...](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c>)

This guide describes how I set up my own weekly submission pipeline from scratch, using Microsoft Azure and python for free. 🚀

Reading time: 8 min read

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/papaemman/48/1453_2.png) [[Community Release] Automated Numerai Tournament weekly submission pipeline for free, using Azure functions and python](<http://forum.numer.ai/t/community-release-automated-numerai-tournament-weekly-submission-pipeline-for-free-using-azure-functions-and-python/5432>) [Tournament](</c/tournament/7>)

> Hello guys, I know that many people are struggling to set up the Numerai Compute either because they don’t have an AWS account or because numerai-cli seems strange. Anyway, I just published a Medium article describing “How I automated my Numerai weekly submission pipeline for free, using Azure functions and python”. Here is the source code: [GitHub - papaemman/azure-functions-with-python: A complete guide on developing and deploying Azure functions with Python, using VSCode and Azure extensio…](<https://github.com/papaemman/azure-functions-with-python>)

---

### Post #8 — **ryo_matsuzaka** | 2022-11-30 03:28 UTC _(reply to #7)_

Thank you very much for the information! I absolutely check it.

---

### Post #9 — **hiydavid** | 2022-11-30 17:17 UTC

I use Deepnote. I’m able to submit daily predictions using their notebook scheduler feature.

---

### Post #10 — **jacob_stahl** | 2022-12-02 01:09 UTC _(reply to #9)_

Thats a thing?  
![d63c1ef766f4d12f14127148d3c0e45a](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d5ae86a43a205cba51d4de50dcc0ed03d4c471af.gif)

---

### Post #11 — **autratec** | 2022-12-02 13:23 UTC _(reply to #9)_

But now the submission changed to email triggered, how the schedule will work ?

---

### Post #12 — **monticola** | 2022-12-02 18:33 UTC

My submission automation cost it around 0.6 €/Month on Azure. It runs on a container instance that loads the models from a cloud storage, predicts and stores the results on the same cloud storage until the next round. It runs very fast since it only predicts using live data, so no training is performed.It takes the container about 90 seconds to run my 12 models.  
My whole cloud infrastructure consist in the container instance, the cloud storage, one http trigger for the submissions, one http trigger for numerbay sales and two scheduled triggers, one for daily rounds and one for weekend rounds.  
The only small detail is that my container image is hosted on a free private repository outside Azure, so that cost it is not accounted for. Actually, that image repository would be the most expensive resource, costing about 4.2€ per month. Although I would not be surprised if there are less expensive alternatives out there.

Edit: I forgot to mention that this represents the cost of daily and weekly predictions. Since this thread is relatively old, maybe I should remark that. I am bad at predictions, but been smoothly predicting daily since day 1 of daily predictions ![:sunglasses:](https://emoji.discourse-cdn.com/twitter/sunglasses.png?v=13) ![:stuck_out_tongue_winking_eye:](https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_winking_eye.png?v=13)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/792fc5059bbdb42961090d8485588ae1a3747170_2_690x259.png)image707×266 17.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/792fc5059bbdb42961090d8485588ae1a3747170.png> "image")

---

### Post #13 — **nyuton** | 2022-12-06 08:42 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/806eb9dd806cb9d4989455d993fa3d054572d767_2_690x473.png)image769×528 34.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/806eb9dd806cb9d4989455d993fa3d054572d767.png> "image")

I have some non-Numerai data in S3 as well, so compute for one model is less than this.

---

### Post #14 — **svendaj** | 2022-12-08 16:42 UTC

I am using Kaggle for training and for submissions, because they provide for free notebooks with 4 CPU cores and 30GB RAM. Their notebook scheduling capability is not usable for numerai submissions, so I have created [workaround solution with (always ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)) free Oracle Cloud compute node, running Kaggle public API and `cron` trigerring my numerai notebooks at announced round openning times](<https://www.kaggle.com/discussions/product-feedback/371090>). Inside of my notebooks I [wait for actual round openning](<http://forum.numer.ai/t/server-errors-on-friday/5883/5>).  
To sum it up: I remain at big fat **zero** automation costs ![:nerd_face:](http://forum.numer.ai/images/emoji/twitter/nerd_face.png?v=12)

---

### Post #15 — **autratec** | 2022-12-09 01:54 UTC _(reply to #14)_

thanks for the sharing. any idea to go further, to get kaggle notebook be trigger by an external API call ? like web hooks, or something else ?

[@svendaj](</u/svendaj>) hi, i just had a thought to include your round readiness checking script in my notebook. and still leverage deepnote to run the notebook at every evening 9pm and check the round open status every 10mins. I think i will resolve the daily submission now. Again. thanks for the shasing.

---

### Post #16 — **autratec** | 2022-12-09 15:13 UTC

just tried script: napi.check_round_open() in deepnote.

And realize that deepnote gives following error: AttributeError: ‘NumerAPI’ object has no attribute ‘check_round_open’

Same code run in colab is working fine.

Any one encounter this issue before in deepnote ?

---

### Post #17 — **svendaj** | 2022-12-11 23:01 UTC _(reply to #15)_

Sorry for later reply, so far I was working on running my notebook swarm in Kaggle. Today I have published [Kaggle notebook which can create and control complex pipeline of other notebooks](<https://www.kaggle.com/code/svendaj/running-pipeline-of-notebooks-with-kaggle-api>).

This was needed for my Saturday night numerai fever, when I was manually running 18 notebooks. Starting with [weekly data update](<https://www.kaggle.com/code/svendaj/numerai-data>), immediately followed by 9 notebooks and 3 sub-pipelines with models to be retrained on weekly data. When this was ready (usually Sunday morning) I launched final stacking notebook.

Now I am able to put everything to one master notebook and launch it with `cron` from cloud automatically ![:sunglasses:](http://forum.numer.ai/images/emoji/twitter/sunglasses.png?v=12)

Webhooks will be my next step, but not sure when I will have some time to have a look at it.

---

### Post #18 — **autratec** | 2022-12-12 03:47 UTC _(reply to #17)_

thanks for the sharing - “one ring rule them all”

---

### Post #19 — **nosaai** | 2022-12-16 13:31 UTC _(reply to #9)_

Would you mind enlightening on how you got the notebook to make submissions on Deepnote? What I really mean is getting the auto-submission to work. Using the Numerai submission API gives really funny errors

---

### Post #20 — **nosaai** | 2022-12-16 13:48 UTC _(reply to #16)_

I have had exactly the same problem only this is in VSC on my computer. This must be something to do with the api. If you manage to solve the problem, please let me know.

---

### Post #21 — **shatteredx** | 2022-12-16 14:56 UTC _(reply to #20)_

update the numerapi package

---

### Post #22 — **svendaj** | 2023-03-25 20:03 UTC

I have finally completed [solution which will launch my Kaggle submission and training notebooks with Numerai compute webhooks](<https://www.kaggle.com/discussions/questions-and-answers/397468>). My previous solution with [`cron` scheduled execution of notebooks](<https://www.kaggle.com/discussions/product-feedback/371090>) and waiting loop for round opening was sufficient, but on Saturday when I am running also training tasks, I sometimes got beyond 12h run limit of Kaggle notebook (because of long waiting for round opening).

It is based on python Flask server - easy to implement in various environments. I am using free Oracle Cloud Ubuntu VM instance.

So now I am completely switching to “compute” style automation - triggered by webhook.

---

### Post #23 — **mic** | 2023-03-26 22:01 UTC _(reply to #22)_

Hi [@svendaj](</u/svendaj>) why do you use a kaggle notebook instead of putting it all into the oracle instance?

---

### Post #24 — **svendaj** | 2023-03-27 08:15 UTC _(reply to #23)_

I am a cheap guy ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12) so when something is for free, it’s the winner. I could not have 4 cores and 30GB RAM in always free tier of OCI. Plus, I have started in Kaggle about year ago and now I have 20 models in roughly the same number of notebooks, so it would not be trivial to run it elsewhere.
