---
title: "[Proposal] Numerai Community Compute"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-numerai-community-compute/5594
created_at: 2022-07-23T21:00:33.611000+00:00
last_posted_at: 2022-08-02T15:32:39.476000+00:00
posts_count: 6
views: 987
tags: []
---

# [Proposal] Numerai Community Compute

---

### Post #1 — **qeintelligence** | 2022-07-23 21:00 UTC

I hereby propose the development of a community-based compute solution which should be intended to be used by users which for whatever reason (technical / cloud-dependencies / … ) can’t make use of the (newly developed) Numerai Compute solution which will be AWS-based.

Keep in mind at the moment of writing the new Numerai Compute from the team is still being beta-tested and since the proposal has some possible dependencies on their solution things can change in the next weeks. I do want to put this proposal out in the open to get a feel whether or not people are actually interested in this, in which case I will follow through. I wanted to put this proposal already out during the London CoE meetup unfortunately I got sick and couldn’t join there ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12) I did gave the slides to [@ia_ai](</u/ia_ai>) and he put them online, thanks for that.

**1.Proposal**  
I’d like to build an open-source community compute solution for Numerai model predictions.

**Ideation** : There has already been lots of talk lately about moving towards a daily compute solution by the team, and currently they are busy with beta-testing this and from what I heard from 2chan this looks to be a clean simple solution (as in one-line commands). They did state though that initially it will still be a AWS-only solution which for a part of the tournament users will still be an issue for various reasons. I was already playing around for quite some time with different local and cloud compute solutions, hunting for the most simple/reliable and cost-effective solution and it seems now more than ever to get a general solution in place which takes away the difficulties of managing infrastructure whether on-premise of cloud-based.

**Problem statement** :  
Like a lot of tournament participants, I want to be able to easily create and manage my compute solutions used for daily or weekly predictions. I want to be able to quickly set it up and also be able to quickly make changes, scale up or down if needed and also get notified upon any problems. It should be a one-line command based solution (e.g. python) which should be in line with or an extension at the Numerai Compute solution.

**Solution** : An open-source software solution that will perform the mentioned compute, with the option to run it on various cloud providers (azure/oracle/cloud) or as a local compute (windows with wsl2, vm/docker, dedicated hardware) based on Ubuntu. Initially it would support python-based prediction pipelines.The basis functionalities should be the following:

**\- Easy setup of Compute Engine** : It should be possible to provision/deploy a compute solution based on user input (cloud or local, scaling, location, …)  
**\- Managing of Compute Engine** : It should be possible to manage the compute engine remotely, that is updating pipelines / changing starting times / changing notifications / …  
**\- Monitoring and Logging** : The solution should provide the user with notifications upon events, e.g. when an error occurred.  
**\- IP** : The solution should run on the users own local compute or cloud, that is they have full control of their compute and no other user can access it (or the data).

**2.Timeline**  
If approved, the earliest start date would be end of August, beginning of September. Initially we should start with an MVP, for example Oracle compute based on Ubuntu and then extend the solution from there.

**3.Best case outcome**  
A working solution which works seamlessly with the Numerai Compute solution, and is used by a large part of the community. The open-source solution is easily managed by other developers and can be extended with other functionalities, e.g. automatic uploading to Numerbay. The Numerai team sees the added-value of the solution and will work together with the community developers in maintaining the solution.

**4\. Worst case outcome**  
The solution has not been adopted by the community, at which case all efforts would have been in vain.

**5.Success criteria**  
This should be defined together with the CoE and community of what the success criteria should be, TBD.

**6.Funding required, if any.**  
I did do voluntary work before, I also created some examples on how to do compute for Azure and Oracle however they are still meant to be used by experienced users. In order to create a solution which can be used by a large part of the community it will take more effort in terms of software development, testing and documentation. Initially I cannot put an exact number on it but when it comes to delivering an MVP this should be possible in several weeks (ballparking it). When the idea at least is approved I will make a detailed planning including expected work hours. At least this is too much work do to this on voluntary basis again like before lol.

**Points for discussion** :

  1. Minimum Features that should be in the MVP
  2. Long-term / Short-term goal
  3. Expected deliverables
  4. Anything else



Well lets first see what people think of it before I add more stuff to this already long story ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #2 — **qeintelligence** | 2022-07-23 21:09 UTC

What do you think about this proposal?

  * This sounds great!
  * Not too sure about this…
  * But what about …? [Please leave your comments below]
  * Man, this really sucks! No way!



0 voters

---

### Post #3 — **bor1** | 2022-07-24 17:20 UTC _(reply to #2)_

This is not wearing my Council of Elders hat (or cape), but as a brew-your own compute user - previously using google cloud ([Automated submission with google cloud](<http://forum.numer.ai/t/automated-submission-with-google-cloud/3888>)), and now just using my home machine.

Here is one whatabout :-).

_“local compute (windows with wsl2, vm/docker, dedicated hardware) based on Ubuntu”_

In my current windows compute I have a task scheduled that calls the below batch file once a week. Running wsl2 on windows to have some docker vm run my models in ubuntu seems like several layers of engineering overkill to me, or am I wrong there?

> cd C:\Users\bor\projects\valkyrie3  
>  powershell -command clj -X valkyrie.fetch/fetch-live  
>  powershell -command clj -M:predict  
>  powershell -command clj -X valkyrie.submit/submit

I know I am using clojure, but someone could make the same using python and numerapi and a batch file, and that would cover windows and linux home machines.

---

### Post #4 — **qeintelligence** | 2022-07-24 20:03 UTC _(reply to #3)_

Thats a good one [@bor1](</u/bor1>), I need to clear this one up for you. The local compute I mentioned there were just examples, like:

  * A windows PC with WSL2 (ubuntu) or just a PC with a clean install of ubuntu
  * A (hypervisor) PC running VM’s
  * A PC with Docker Desktop installed running Docker Containers
  * A Jetson Nano dedicated hardware with ubuntu



It doesn’t mean though we would be running WSL which would run docker or VM’s ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) I also like the idea of having a clean simple installation with as little overhead as possible. My current setup for example is just ubuntu running in Oracle with python scripts triggered by cronjob, and this is actually how I would want to start with this Numerai Compute.

The actual idea of this proposal is to make a python library from where you can easily deploy your compute to a cloud environment or a local environment. Deploy would mean: provision the compute including os, deploy your prediction pipelines (that is your python scripts, virtual environments) and then some configuration (memory, cronjob configurations, etc). And all that through simple one-line commands to hide the complexity of a cloud environment or local setup and also to make it possible to setup everything up within minutes. This is also I think what the numerai team is going to deliver with their AWS solution. Anyway ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) as an answer to your last question, yes thats actually what this proposal is also about.

---

### Post #5 — **bor1** | 2022-08-02 07:30 UTC _(reply to #4)_

Polled the other CoE’s, and the consensus is something along the lines of “let’s wait and see if there is a sizable fraction of people that need something else than the new compute that is coming”.

For home use, just running a cron job or a scheduled task that runs a bash/batch script seems always the simpler application, but maybe there is a fraction of people whose models don’t fit on AWS lambda, or have some other reason that they cannot use AWS[1]

[1] I would hope that the single digit dollar costs of AWS isn’t a limitation for anyone - else buying into NMR for staking is going to be a big hurdle also. But maybe the problem is having a credit card or something like that.

---

### Post #6 — **qeintelligence** | 2022-08-02 15:32 UTC _(reply to #5)_

Fair enough, lets put this one on a hold until the (beta) version of the numerai compute arrives or until daily predictions is announced with a date. Other reasons for not using the aws could be because some people have a better price deal with another public or private cloud provider and has a need for more cpu/gpu compute.

I am curious though how much people are actually spending on their compute with predictions, did anyone do a poll on that? Local compute would be the electricity bill and maybe hardware investments.
