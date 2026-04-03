---
title: "[Community Release] Oracle Compute for Numerai predictions"
category: Tournament
url: https://forum.numer.ai/t/community-release-oracle-compute-for-numerai-predictions/5592
created_at: 2022-07-23T18:20:15.420000+00:00
last_posted_at: 2022-11-30T02:48:37.103000+00:00
posts_count: 3
views: 891
tags: []
---

# [Community Release] Oracle Compute for Numerai predictions

---

### Post #1 — **qeintelligence** | 2022-07-23 18:20 UTC

Hi all, this is a follow-up on the Azure Compute I posted some time ago:

[[[Community Release] Azure Compute for Numerai predictions](<http://forum.numer.ai/t/community-release-azure-compute-for-numerai-predictions/4699>)](https://[Community Release] Azure Compute)

I was already working with Oracle cloud for some time now besides Azure, and I like the fact that the free tier gives you the option to configure 2 AMD compute engines and 1 Ampere compute engine for free 24x7! . At the moment I am now running my pipelines fully automated on an ubuntu install, I made some basic instructions on how to set everything up in the following repo including sample code:

![](https://github.githubassets.com/favicons/favicon.svg) [github.com](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

### [numerai_compute/oracle at main · jos1977/numerai_compute](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

[main/oracle](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

Numerai Compute. Contribute to jos1977/numerai_compute development by creating an account on GitHub.

This install still requires basic knowledge about ubuntu, ssh, tooling, cronjob etc and after listening to the fireside chat it is clear that short-term the team will only support AWS (but they do want other cloud providers). They are working on a simple solution for (daily/weekly) compute that they will release on a later time and should make AWS compute accessible for everyone, also if you dont have any infra knowledge. I will intend later this weekend to make a CoE proposal to do the same but then for non-AWS compute solutions and hopefully be able to build upon what the team is delivering together with my current solutions.

Anyway for now, hope you guys can use this and have some fun with it!

---

### Post #2 — **qeintelligence** | 2022-10-30 08:33 UTC

hi all, I am pushing this one up a bit again. Unfortunately the proposal at CoE for an ‘official’ compute which works for non-AWS cloud providers or local compute didn’t take off but I verified this weekend that the Oracle Compute as documented in the github link above still works and also for daily compute. Since there are no cost involved, you can easily get started with this one (provided that you have some experience in admin and programming ofcourse). Have fun!

![](https://github.githubassets.com/favicons/favicon.svg) [github.com](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

### [numerai_compute/oracle at main · jos1977/numerai_compute](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

[main/oracle](<https://github.com/jos1977/numerai_compute/tree/main/oracle>)

Numerai Compute. Contribute to jos1977/numerai_compute development by creating an account on GitHub.

---

### Post #3 — **degerhan** | 2022-11-30 02:48 UTC

I’ll second the Oracle Cloud idea. Thank you [@qeintelligence](</u/qeintelligence>) for alerting me to this service.

I’ve been running numerai fully automated for the past two years on a hosted-dedicated x64 box (which I pay for various other reasons). With those reasons soon coming to an end, I looked into both hosting and cloud providers for my numerai workload. I find it easier to build pipelines for an always-on single-computer than the multiple ephemeral containers approach of numerai-compute.

The always-free Oracle offering with 4 physical arm cores and 24 GB RAM is hard to beat. I did some spot tests this weekend: the same conda environment (exact python and library versions) generate the same results on the ARM machine from existing pickled models and python code. VSCode remote-ssh development works with the extensions I need. The python libraries I use are all available. I setup a 100 GB swap disk (also within the free storage quota), so the vm can now work with 124 GB of in-memory data (yes, slowly, but without blowing up).

If your numerai platform is linux and you are looking to have a reliable always on environment for automation, I suggest you take a look. My initial concern about moving to aarch64 from x64 seems to be a much smaller issue than I anticipated.
