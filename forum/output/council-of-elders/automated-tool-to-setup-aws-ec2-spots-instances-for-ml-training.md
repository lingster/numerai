---
title: "Automated tool to setup aws ec2 spots instances for ml training"
category: Council of Elders
url: https://forum.numer.ai/t/automated-tool-to-setup-aws-ec2-spots-instances-for-ml-training/4723
created_at: 2022-01-04T11:16:20.655000+00:00
last_posted_at: 2022-01-07T00:06:18.607000+00:00
posts_count: 8
views: 1143
tags: []
---

# Automated tool to setup aws ec2 spots instances for ml training

---

### Post #1 — **malembetirick** | 2022-01-04 11:16 UTC

Hi all,  
First of all I wish you all the best and happiness for this new year.  
I plan to launch very soon a platform of automated management of aws ec2 spots instances which would allow the community to :

  * save up to 90% of the costs
  * develop, test and iterate quickly in a secure way, new algorithms of artificial intelligence  
I would be delighted if you could take 2 minutes to answer my survey if interested  
[https://docs.google.com/forms/d/e/1FAIpQLSfKUlg00-4FTYEjViN-7Jzwi3iBlTXb9DDq9EOgfZOov1QQfw/viewform?usp=pp_url&entry.1591633300=<+10h&entry.806387985=utc+1&entry.326955045=50-100$&entry.1696159737=20:00](<https://docs.google.com/forms/d/e/1FAIpQLSfKUlg00-4FTYEjViN-7Jzwi3iBlTXb9DDq9EOgfZOov1QQfw/viewform?usp=pp_url&entry.1591633300=%3C+10h&entry.806387985=utc%2B1&entry.326955045=50-100$&entry.1696159737=20:00>) .



> [![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4b70780826074f958715861c19f3229a0f71a1f7.png)](<https://docs.google.com/forms/d/e/1FAIpQLSfKUlg00-4FTYEjViN-7Jzwi3iBlTXb9DDq9EOgfZOov1QQfw/viewform?usp=pp_url&entry.1591633300=%3C+10h&entry.806387985=utc%2B1&entry.326955045=50-100>)
> 
> [docs.google.com](<http://docs.google.com>)
> 
> [**Quick survey**](<https://docs.google.com/forms/d/e/1FAIpQLSfKUlg00-4FTYEjViN-7Jzwi3iBlTXb9DDq9EOgfZOov1QQfw/viewform?usp=pp_url&entry.1591633300=%3C+10h&entry.806387985=utc%2B1&entry.326955045=50-100>)
> 
> First of all I wish you all the best and happiness for this new year. I plan to launch very soon a platform of automated management of aws ec2 spots instances which would allow you to : - save up to 90% of the costs - develop, test and iterate quickly in a secure way, new algorithms of artificial intelligence I would be delighted if you could take 2 minutes to answer my survey.

---

### Post #2 — **uuazed** | 2022-01-05 09:18 UTC

Have you heard about `nimbo` ([GitHub - nimbo-sh/nimbo: Run compute jobs on AWS as if you were running them locally.](<https://github.com/nimbo-sh/nimbo>))? Sounds similar to what you are trying to do.

---

### Post #3 — **malembetirick** | 2022-01-05 20:34 UTC _(reply to #2)_

Hi [@uuazed](</u/uuazed>), i check your link. Nimbo is an interesting tool but it doesn’t totally cover my need, which is to set up an automated intelligent cloud solution managing aws spot instances (#cloudhack) by auto-scaling. It will help the community setup and run ec2 instances while saving up to 90%.  
Thanks for the suggestion

---

### Post #4 — **uuazed** | 2022-01-05 21:03 UTC _(reply to #3)_

Nimbo works with spot instances, just saying. I guess, what I am missing in the proposal is the numerai specific part.

Anyway, I am curious to hear what the community things about your proposal and the outcome of your survey.

---

### Post #5 — **malembetirick** | 2022-01-05 23:39 UTC _(reply to #4)_

How does Nimbo handle aws spot instance interruptions ?  
Is there an automatic instance allocation function after an interrupt ?, or do I need to allocate manually by re-executing shell command ?

---

### Post #6 — **malembetirick** | 2022-01-05 23:47 UTC _(reply to #5)_

Is the price of aws spot instances refreshed every time you execute the command ?  
Can we configure a scheduler to refresh the prices of spot instances dynamically with Nimbo ?  
How long have you been using Nimbo, I just want to know if the tool is suitable for what I want to do.

---

### Post #7 — **uuazed** | 2022-01-06 07:28 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/8c91f0/48.png) malembetirick:

> How does Nimbo handle aws spot instance interruptions ?

I don’t know. Probably no automatic re-allocation. Results / files are stored in an s3 bucket, so retrieving some previous state might be possible

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/8c91f0/48.png) malembetirick:

> Is the price of aws spot instances refreshed every time you execute the command ?  
>  Can we configure a scheduler to refresh the prices of spot instances dynamically with Nimbo ?

I assume the prices are refreshed with each call. There is probably no build in scheduler, as this is just a command line tool.

---

### Post #8 — **malembetirick** | 2022-01-07 00:06 UTC _(reply to #7)_

Thank you for your help. It’s appreciable. I am still investigating the different possibilities. Nimbo seems like something simple and easy to set up. I’ll let you know what happens next.
