---
title: "[Community Release] Azure Compute for Numerai predictions"
category: Tournament
url: https://forum.numer.ai/t/community-release-azure-compute-for-numerai-predictions/4699
created_at: 2021-12-29T18:36:26.034000+00:00
last_posted_at: 2022-05-23T12:52:26.028000+00:00
posts_count: 12
views: 1294
tags: []
---

# [Community Release] Azure Compute for Numerai predictions

---

### Post #1 — **qeintelligence** | 2021-12-29 18:36 UTC

Hi all, I mentioned it before in the chat that I also was busy with getting an Azure environment up and running with the example model that makes use of the webhook functionality provided by numerai. Guess what, version 1 is available for you!

The github repo with everything needed to get it up and running is:

<https://github.com/jos1977/numerai_compute/>

There is already some documentation available but I intend to improve that more after my holiday (which starts tomorrow). The highlights of Azure Compute are:

  * Docker containers: it makes use of Docker Hub for storing the docker private container that contains the inference code. Example python code (that is based on the example model from the team) and powershell code are in the repo
  * Azure Container Instance + Logic App: it makes use of these 2 resources to have the webhook functionality working, every week the container will be started, and after uploading the predictions it will terminate to save cost. For the example model (38 features minimal set) it is enough to have 2.5 Gb ram reseverd in Azure Container Instance, which means <<1 dollar per month. Ofcourse, depending on what you want to do more Ram may need to be reserved (or GPU instead of CPU but for inference I think most of us dont need that power).
  * Fully automated powershell scripts in the repo to provision the Azure resources, you only need to fill in required information like subscription, credentials, etc…



And since it uses docker containers it is also quite easy to first run it locally for testing, or later switch to another cloud provider for example. I intend to get the Oracle version also working after the holidays, to see if the example models can also run on their free tier (24Gb ram, 4 Ampere cores 24x7x31days, 10Gb storage for free).

Ofcourse I am open to any improvements and such, and ofcourse you can tweak all the code to include stuff like GPU, multiple models, etc. First I am off for a couple of days and relax a bit ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10) Have a nice new year!

---

### Post #2 — **aventurine** | 2021-12-31 03:37 UTC

Wow I just have to say, thanks for all this extra side work you do to make Numerai awesome!

---

### Post #3 — **qeintelligence** | 2022-01-07 11:49 UTC

I did some testing again, this time trained the example model from the team based on ‘medium’ features (400) and then used that model with Azure Container Instances. If you use 16Gb Ram for the container it will succeed, without any memory optimizations (like only train on live for example instead of the whole tournament data).

---

### Post #4 — **jacob_stahl** | 2022-01-08 04:00 UTC _(reply to #3)_

I looked at Azure ACI for automating my predictions but they have a maximum of 16 gb of memory. That’s a tight fit if you use very feature. Is there a similar way to do this if I need more memory?

---

### Post #5 — **qeintelligence** | 2022-01-08 08:44 UTC _(reply to #4)_

yeah you are absolutely right about that one, its unfortunately a hard limit when using ACI (you can use GPU though). Besides memory-optimizing your code when using Azure I can only see using Kubernetes or a VM (with optionally docker) as an alternative, both will have also storage/infra costs besides the compute costs. Yesterday I got the Oracle cloud vm with docker working though, which gives you 24Gb ram on the always free tier, also it looks like 4xampere cpu is working nicely. When I am ready I will also put a tutorial for that one on github.

---

### Post #6 — **monticola** | 2022-01-09 10:04 UTC _(reply to #4)_

Using Azure functions, I have managed to automate the upload of my predictions with only 1GB of memory. Processing the round data in batches did the trick. I was unable to load the parquet file in batches though, so I had to fall back to using the CSV. The results are not 100% the same, but my understanding is that differences are negligible. I would be cool if Numerai produced parquets that can be load in batches, if possible.

One of the disadvantages of Azure Functions is that the resources that the function use are allocated all the time, even when the function is only triggered by a timer event on sundays. The price for 8 or 16 GB was absurd for something that runs 4 times a month. Does the same thing happen with ACI?

---

### Post #7 — **jacob_stahl** | 2022-01-09 17:42 UTC _(reply to #6)_

It would be nice if eras were in separate files, and you could query them one at a time from the API. From what I can tell, you can start and stop Container Instances on a schedule. You only get a bill for the time you use * the resources + storage costs. I don’t know for sure because I haven’t set it up yet ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10)

---

### Post #8 — **qeintelligence** | 2022-01-09 19:18 UTC

[@jacob_stahl](</u/jacob_stahl>) : Yes, if would definitely be nice if you could choose what to download (e.g. only live eras), but the team is working on that one. As for the ACI, you only have compute costs until your container reaches status ‘terminated’ , i.e. when runtime is ended. As for the storage costs, you dont have that for ACI. You would have costs if you would be using Azure Container Registry, however my example uses Docker Hub which gives you 1 private and multiple public container storage for free.

As for the schedule, you can use logic apps with a webhook just like in my example. The numerai server will trigger that one for you when the round is open.

---

### Post #9 — **qeintelligence** | 2022-01-09 19:26 UTC

[@monticola](</u/monticola>) : I am not sure what you used for Azure Functions, if you would be using an App Service Plan then yes costs would be for the whole month. If you would choose to run Azure Function consumption-based then you would only pay for actual compute runtime and storage. ACI only has compute costs which you can minimize by terminating the container at the end of your run.

I also thought about using Azure Functions however the downside is it meant to be used for short periods of compute time (<10 mins), there are ways around that with durable functions but I think there are better solutions like ACI or VM+docker containers.

An interesting alternative would be to use App Service Plan + Linux App Service and downscale/upscale the service plan at the right times using rest api. You would still be paying for some storage costs but your compute costs would be minimized and you can upscale to >64Gb Ram for example. I didn’t test this myself but it could work i guess. At the moment my focus is on Oracle cloud ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #10 — **monticola** | 2022-01-09 20:00 UTC _(reply to #9)_

I chose a consumption based plan. I really can’t remember what my mind understood after going through the documentation for the different plans. I think I recall thinking that consumption plans where ok but only allowed for 1 or 1.5 GB of memory. Thats why I had to tweak my code to fit there ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10) .

And yes, probably Azure Functions are not the best solution. It just works, but it is not very elegant. For instance, that 10 min limit you mention. I set up my function so I runs every 20 mins on Sundays. It downloads data just once, and skips the models that have been already submitted. So as long as downloading the data or predicting one of the models does not take more than ten minutes, I’m good :D.

I will definitely check your git repo when I have some spare time to see how to improve my current submission solution. App Service Plan + Linux App Service to upscale/downscale…Sounds like it would take my some time to wrap my head around that :D.

---

### Post #11 — **qeintelligence** | 2022-01-09 20:11 UTC _(reply to #10)_

![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=13)

[learn.microsoft.com](<https://learn.microsoft.com/en-us/rest/api/appservice/app-service-plans/create-or-update>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d8015098442cb37d276b03eb02b492be40db363c_2_690x362.png)

### [App Service Plans - Create Or Update - REST API (Azure App Service)](<https://learn.microsoft.com/en-us/rest/api/appservice/app-service-plans/create-or-update>)

Learn more about App Service service - Description for Creates or updates an App Service Plan.

Yeah I can image if it is the first time, I was thinking about using the above rest api, and change the sku to the free tier when done with compute and change it to ‘something that costs money’ when you start the compute on sundays.

---

### Post #12 — **papaemman** | 2022-05-23 12:52 UTC _(reply to #11)_

Hello guys,

I just published a Medium article describing “How I automated my Numerai weekly submission pipeline for free, using Azure functions and python”.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0f95de5840ff0771b84ea77cfa42a1e98b4f1614.png) [Medium – 23 May 22](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c> "09:56AM - 23 May 2022")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/ba31d9578ab6005b70e2d7ddf765e32ce38463de_2_690x171.png)

### [How I automated my Numerai weekly submissions pipeline for free, using Azure...](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c>)

This guide describes how I set up my own weekly submission pipeline from scratch, using Microsoft Azure and python for free. 🚀

Reading time: 8 min read

Here is the source code: [GitHub - papaemman/azure-functions-with-python: A complete guide on developing and deploying Azure functions with Python, using VSCode and Azure extension.](<https://github.com/papaemman/azure-functions-with-python>)

I hope it helps. Thanks!
