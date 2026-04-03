---
title: "Help us improve Numerai Compute!"
category: Feedback
url: https://forum.numer.ai/t/help-us-improve-numerai-compute/5480
created_at: 2022-06-08T02:26:05.259000+00:00
last_posted_at: 2022-12-02T02:32:09.546000+00:00
posts_count: 49
views: 3722
tags: []
---

# Help us improve Numerai Compute!

---

### Post #1 — **chanes** | 2022-06-08 02:26 UTC

Hi all,

Research has shown that trading earlier (at market open instead of market close) and more often (daily instead of weekly) can lead to better execution and better performance for the Numerai Hedge Fund.

To support this future, we are exploring the idea of daily rounds with much shorter submission windows. This change will effectively make model automation mandatory.

Currently, only 4.4% of staked submission models are automated using the Numerai Compute system. Our goal is to bring this number up to 100% by making the developer experience of model automation as smooth and pain free as possible.

Some questions for you:

  * Are your submissions automated now?
  * Do you submit from a home machine, compute/cloud or website?
  * Do you want to train your model locally or in the cloud?
  * How often do you retrain your models?
  * What cloud platform are you most comfortable with?
  * Do you use version control for your model code?
  * What are the biggest pain points with the current Compute setup?
  * How do you typically deploy a model to production?



Some proposals we have:

  * Automated command-line tool to deploy Sagemaker Studio notebooks and webhook. The CLI tool would deploy: a training notebook, a submission notebook, and a webhook that Numerai calls. This setup would remove the need for Docker and Terraform and would hopefully give users a more familiar UX by running things in a notebook.
  * Using Linode Stackscript to deploy a cloud computing machine with all the dependencies installed. It’s much easier to get up and running in Linode vs. AWS, so this path would be helpful to users who aren’t comfortable working with AWS.
  * Automated command-line tool to deploy a scheduled Google Colab notebook (h/t to bor for his Google cloud post [here](<http://forum.numer.ai/t/automated-submission-with-google-cloud/3888>))



Which of these is most appealing to you? What changes would you make?

---

### Post #2 — **wigglemuse** | 2022-06-08 03:07 UTC

Daily submissions give us how long a submission window? 24 hours? And I know you want to talk about automation, but none of it is appealing to me without knowing the context of how staking and rounds would work. (My computing needs are onerous.) Same target horizon of 20 days? Would a round be ending every day or folded together into some kind of weekly average? (If the former how would that overlap work? You’d have to cap daily payouts at 1/20th). etc etc i.e. is there additional (or fasted paced) reward for the additional burden? (Even if automated I don’t care what anybody says, it will still be a much bigger burden and possibly with a significant actual dollar cost.) And you know…what if I just don’t wanna do it and will only submit once or twice a week? I would imagine you’ll get a lot of such gaps (even if automated pipelines break and there won’t be much time to recover) so the daily metamodel may become quite “choppy” with models dropping in and out all the time.

As far as automation, my models take hours to run a set of predictions on live (on a very well-provisioned local machine). I’m capable of automated the pipeline locally (or remotely) without any help from Numerai, but if local that’s hours of development time lost every day while the computer is spitting out new predictions (I typically have it churning away on some new experiment practically 24/7), and if I want to avoid that and use the cloud that would cost me $3-$8 daily probably (rough estimate) because I’d have to have a lot of cores to run it in reasonable time. (For the cloud, I’d probably get a Linode or similar with 32-56 cores and would need to run it for 1-3 hours/day maybe at roughly $1-$3/hr depending on the setup – would have to experiment with different levels and see how fast they really are. I could also cost much more – just guessing at the moment based on the rates I’m browsing.)

---

### Post #3 — **restrading** | 2022-06-08 04:02 UTC

Please have account-level staking out before moving to mandatory automation, model slot switching would be hard with automation. Account level staking and instant stake adjustment can eliminate the need for slot switching.

---

### Post #4 — **gammarat** | 2022-06-08 05:08 UTC

* _Are your submissions automated now?_  
No.

  * _Do you submit from a home machine, compute/cloud or website?_  
Home machine.

  * _Do you want to train your model locally or in the cloud?_  
Locally

  * _How often do you retrain your models?_  
Very rarely, I hope. I just started my new architecture around round 308, and it’s been unchanged since round 311.

  * _What cloud platform are you most comfortable with?_  
I’ve never used one. I’m such a neanderthal.

  * _Do you use version control for your model code?_  
No, but I could. It’s not a big deal.

  * _What are the biggest pain points with the current Compute setup?_  
I am Python, Compute, and internet programming illiterate. And I currently work in MatLab. ![:older_man:](http://forum.numer.ai/images/emoji/twitter/older_man.png?v=10) My bad. On the plus side, in the past I usually estimate 3 weeks to be functional in a new language, 6 weeks to moderately fluent (I’ve worked in lots).

  * _How do you typically deploy a model to production?_  
I just code it up, spend some time debugging it, and then let it run. I am so bad at doing this properly ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=10) I used to be much more formal in my approach (working for years in defense research makes one that way), but I’ve happily put that behind me.




As for actually working on the problem as stated, I think I could adapt. The actual production of the 50 submissions takes just a minute or two; the whole process (download the live data, process it, upload the submissions) takes about 20 minutes. So I could probably still do it all by hand…

Despite my whining, if you feel this move is of benefit to Numerai, then go for it. Just give us a few weeks notice before switching over, and maybe some links to practice on.

As for the proposals, they’re all Greek to me, I’m not familiar with any of it. ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=10) OTOH, if you simply do what you do for the Tournament, but on a daily basis ~~with a twelve or twenty four hour window, that would work for me well.~~ a window of just a few hours is fine. Especially if you don’t mind some entries being skipped (we’re heading into beach weather).

Before I forget, I’m currently downloading Tournament results periodically to build up statistical estimates for my models’ performance. I need those to estimate the best way of distributing my NMR before staking any significant amounts. If payouts are to be made on a daily model submission, then I’ll need those on a daily basis, though delayed a few days is fine.

---

### Post #5 — **jay1100** | 2022-06-08 11:42 UTC

I use the current compute pipeline (docker+terraform) and I find it really easy to use because of the nice scripts that numerai provided. (for other projects I tried to setup servers using terraform on my own and that was a lot more pain). I like the setup. I do not really understand why only so few people are using it.

---

### Post #6 — **wigglemuse** | 2022-06-08 13:08 UTC _(reply to #3)_

Great point. This is probably one of the big reasons for lack of automation (it is for me as well as just the computing needs) – we have to switch out models/slots all the time to control our staking.

---

### Post #7 — **uuazed** | 2022-06-08 13:56 UTC

* Are your submissions automated now?  
yes, fully automated. most of them using compute, some others also dockerized and scheduled with prefect
  * Do you submit from a home machine, compute/cloud or website?  
home machine for the non-compute ones. mainly because I retrain those models each week (or because I was too lazy to port to compute)
  * Do you want to train your model locally or in the cloud?  
locally for now. However, my machine is quite dated and I am looking into cloud training
  * How often do you retrain your models?  
Most of my models are not retrained. some need weekly training, which is fully automated
  * What cloud platform are you most comfortable with?  
GCP
  * Do you use version control for your model code?  
of course
  * What are the biggest pain points with the current Compute setup?  
I really enjoy the setup. Uploading the docker images is slow, which is a bit annoying. And I’d enjoy some better monitoring (trigger failures per model, response time per model, etc)
  * How do you typically deploy a model to production?  
compute or prefect

---

### Post #8 — **bor1** | 2022-06-08 17:31 UTC

* Are your submissions automated now?



Yes, local task scheduler on windows that runs a batch file.

  * Do you submit from a home machine, compute/cloud or website?



home machine.

  * Do you want to train your model locally or in the cloud?



locally

  * How often do you retrain your models?



once every 6 months

  * What cloud platform are you most comfortable with?



Google, but willing to use anything that can do a few hours of compute and has local storage.

  * Do you use version control for your model code?



yes

  * What are the biggest pain points with the current Compute setup?



all I want from the compute solution from numer.ai is something that triggers the running of some batch file / startup script. I can do the downloading / prediction / submission myself.

  * How do you typically deploy a model to production?



Duplicate the previous production directory, add a fresh git archive to the directory, exclude the files that hold the model api keys from github. update a few files within it based on how my model has evolved in the last 6 months, and add the batch files that does the downloading/computing/submission to the task scheduler.

A notebook kind of template that has a webhook in it sounds interesting, not sure if it runs clojure (there seems to be a clojure/jupyter bridge, so maybe that works). Otherwise - I would like something that is most similar to having a home machine in the cloud that responds to a trigger from numer.ai by running a prespecified script would be great.

---

### Post #9 — **qeintelligence** | 2022-06-08 18:11 UTC

Some questions for you:

_> * Are your submissions automated now?_  
_> \- semi-automated (that is i press the button to start the pipeline, but it could be automated if i want to)_  
_> * Do you submit from a home machine, compute/cloud or website?_  
_> \- home machine and gcp cloud_  
_> * Do you want to train your model locally or in the cloud?_  
_> \- local and cloud_  
_> * How often do you retrain your models?_  
_> \- maybe 1 model per 2/3 weeks_  
_> * What cloud platform are you most comfortable with?_  
_> \- azure or gcp_  
_> * Do you use version control for your model code?_  
_> \- lol sort of, github_  
_> * What are the biggest pain points with the current Compute setup?_  
_> \- with terraform its meant to be platform-agnostic, however looking at the current code it still seems like a lot of work to get that compute ready for gcp/azure/oracle/…_  
*> *  
_> * How do you typically deploy a model to production?_  
_> \- either overwrite python files directly (conda env) or use docker_

I am sure that besides the current compute there are a lot of users in the community who could provide high-quality howto’s on how to setup an automated pipeline in the cloud based on python and a compute engine, maybe some bonus on those tutorials could also help with getting more people using a compute solution?

As for other questions you could ask are the following:

  * How many models do you have and how long does it take for your current setup to actually predict and submit?
  * How much cost do you have on a weekly/monthly basis with your current prediction setup?

---

### Post #10 — **permistiro** | 2022-06-08 18:37 UTC

* Are your submissions automated now?



Yes, all of them, but they are called from a single webhook (so your 4.4% number probably isn’t correct).

  * Do you submit from a home machine, compute/cloud or website?



Cloud, a mix of AWS and Google Colab.

  * Do you want to train your model locally or in the cloud?



Cloud.

  * How often do you retrain your models?



Some of my models are retrained every week due to a custom dimensionality reduction step. Some of these take many hours to retrain (5h or more). And from time to time they fail due to cloud shenanigans. So I’m not happy about reducing the submission time.

  * What cloud platform are you most comfortable with?



AWS.

  * Do you use version control for your model code?



Yes.

  * What are the biggest pain points with the current Compute setup?



Certainly the overly complex setup required by AWS. And the fact that ECS doesn’t support machines with GPUs.

  * How do you typically deploy a model to production?



I develop a notebook on Google Colab, and have a Puppeteer script run it from a ECS job.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/chanes/48/2562_2.png) chanes:

> Automated command-line tool to deploy Sagemaker Studio notebooks and webhook. The CLI tool would deploy: a training notebook, a submission notebook, and a webhook that Numerai calls. This setup would remove the need for Docker and Terraform and would hopefully give users a more familiar UX by running things in a notebook.

If you go the Sagemaker way, please let us use “spot” instances. An alternative is AWS Batch, which deals with failures/retries. I’d love to have an easy, programmable, version-controlled setup for it.

---

### Post #11 — **mundan** | 2022-06-08 19:06 UTC

TL,DR; do not make things overly complex, maximum information and flexibility is not always the best for participants, as they will feel suboptimal when not being able to work as much as they think they should.

In general, numerai tournament developement is quite fast-paced to me. For many of us it’s a side hobbie which has flexibility (you can stop running exp or do nothing for a month) and some returns (well, losses, given the current crypto market and my first stake time).  
This is good, but it’s less so with the frequent changes.

Luckily the community is active and data version changes are backward compatible. But it is easy for the development team to evaluate incremental complexity increases relative to the current setup and not in absolute terms that really refer to entry barriers. As an illustration, one could imagine (roughly and not accurately) some experience levels:

  * manually download a `.csv` , look at it, create one manually and upload it via GUI
  * manually download a `.csv` and analyze it locally helped by whatever tool you use (excel, matlab, python, R…), manually generate a new csv and upload it
  * do the same with a `.parquet` file
  * understand and use an API to download data and upload predictions
  * automate the analysis and prediction generation in a programming language
  * update the data to a new version, be rich and buy plenty of ram (or code in C++, or run small-batched models or be really smart)
  * automate the training and execution of prediction-generating models
  * move the execution of models to the cloud
  * move the training of models to the cloud
  * deploy an NLP bot to answer this blogpost ![:exploding_head:](http://forum.numer.ai/images/emoji/twitter/exploding_head.png?v=10)



The development of the tournament is making participants escalate this “sophistication” ladder, and this makes barriers of entry tougher. **The psychology of the participant is to be taken into account** : For instance, if in the new setup evaluation is done per-week, no penalization occurs if missing a day prediction, and no intermediate information is provided, then the upgrade is simply automating a model and making it run every day. This is relatively easy given enough guidance. Else, the participant will worry a lot about making the _best_ possible thing which involves 1) daily adjusting the stake, 2) making the automation overly robust, and 3) retraining every day. This is the spirit of [@wigglemuse](</u/wigglemuse>) which I subscribe to: we don’t want to feel suboptimal and this might make being optimal harder.

Now the questions

  * Are your submissions automated now?  
_No, but I connect to the server once a week to run`commands.sh` which does everything I want_
  * Do you submit from a home machine, compute/cloud or website?  
_university server, oups_
  * Do you want to train your model locally or in the cloud?  
_I train it on the clusters of my institution, which is presumably more powerful and cheaper than what the cloud will provide_
  * How often do you retrain your models?  
_I’m just deploying v4, and I plan to finetune every week (of course, just because validation data is being updated)_
  * What cloud platform are you most comfortable with?  
_I have never used one, only remote servers via ssh_
  * Do you use version control for your model code?  
_Yes_
  * What are the biggest pain points with the current Compute setup?  
_I have to read how to use it_
  * How do you typically deploy a model to production?  
_For numerai, I have my predict scripts (frozen models), I run them, generate the csvs, and upload the csvs. Otherwise I have used cron_



**The biggest pain points are**

  * I use python, C, and ssh in linux. Apparently have to learn cloud and code in notebooks? This would be terrible! Colab has not enough RAM to work comfortably. People that do data analysis don’t need to know how to code and people that know how to code don’t need to know how to cloud-deploy.
  * if cloud is not free, then trying a model (without staking) will cost money, which is a huge barrier of entry because it takes starting in numerai from zero-cost and zero-risk to costly and risky. I can’t feel like staking in a model without evaluating live performance, and if I can’t evaluate live performance for free (as I do now) then I would not do numerai.
  * I think there should be an example project for numerai research and deployment of models, the example scripts is not that good nor simple for building upon / deploying



best

---

### Post #12 — **rigrog** | 2022-06-08 19:31 UTC

Each week’s submission requires several un-automated hours to prepare.

Most of the time (about 2/3) is spent incorporating the newest ‘live’ rows, into the web of connections between all the rows. Some call this ‘unsupervised learning’, but in fact I supervise it rather closely! The remaining time is spent using that web, to interpolate target numbers into those live rows. Also un-automated.

If you require five or seven submissions a week, I’ll just have to give up. Please keep weekly submission, at least as an option.

But if you do go daily: why not hourly, or minutely, or… ? HFT has been a thing, for some while now.

---

### Post #13 — **bor1** | 2022-06-08 20:20 UTC _(reply to #11)_

>   * I use python, C, and ssh in linux. Apparently have to learn cloud and code in notebooks? This would be terrible! Colab has not enough RAM to work comfortably. People that do data analysis don’t need to know how to code and people that know how to code don’t need to know how to cloud-deploy.
> 


>   * if cloud is not free, then trying a model (without staking) will cost money, which is a huge barrier of entry because it takes starting in numerai from zero-cost and zero-risk to costly and risky. I can’t feel like staking in a model without evaluating live performance, and if I can’t evaluate live performance for free (as I do now) then I would not do numerai.
> 


It seems to me that the two options numer.ai should offer is

  1. two notebooks - one that trains the example predictions model, and one that comes with a webhook that can submit live predictions every time, using the trained example predictions model. This is your low-entry free barrier. People can tweak the example predictions, store the models they like, and set up copies of the submitter notebook that each use a trained model.

  2. some kind of solution that can wake up a box and trigger a script to run on some cloud server or trigger a script on some always-on box

---

### Post #14 — **jdclark** | 2022-06-08 22:08 UTC

To be completely honest, I’d love to continue doing everything locally through a scheduled R script that uses the rnumerai package. I’ve looked into using compute and as easy as it might be for some I simply do not have the time to learn to do it.

Although my best model ([Numerai](<https://numer.ai/teagueia_1>)) is fairly small and generates predictions quickly, many models I’ve experimented with take quite a bit of time and submitting all 50 models takes my machine about 6 hours I believe. I could limit experiments to smaller models, but of course that means reducing the diversity of my models. Alternately, if I do keep experimenting with larger models it means my computer is bogged down for six hours per day constantly. I suppose I could live with that as long as I have high-performing models to stake on, but it raises the “hassle factor” another notch closer to the point where I need to stop participating in the tournament entirely. I’d probably keep participating as long as I can keep doing things locally, but it would be a pain in the ass. My office is already hard to keep cool in the summer haha!

As for forced automation, it would raise the hassle factor substantially and I would probably stop participating entirely for the foreseeable future. I have too many other projects (and children) to put in the time needed to make the switch. I know some will say its only a few hours, but “a few hours” is essentially all of my free time as someone with 3 toddlers and an infant. I’m not doing that. At least, not until the little ones are not so little anymore.

In sum, my ability to keep participating is marginal at the moment and raising the hassle factor too far will tip me over. My guess is that at least some other participants are in the same boat. The question is whether the benefits of doing daily submissions with forced automation offset the downsides of losing marginal participants like myself.

(PS - Yes I stake quite a bit on the model I linked, so although I am “marginal” my influence on the meta-model is non-zero. The one I linked is just the one I used to test it initially)

---

### Post #15 — **mundan** | 2022-06-08 22:33 UTC _(reply to #13)_

Your ideas are good!

  * I would also add a python script option, notebooks are nice to interact with data, but it should work with a more fundamental script too.
  * the notebook/script should have a clear output (e.g. a csv file at some specified dir)

---

### Post #16 — **hiydavid** | 2022-06-09 03:22 UTC

**Are your submissions automated now?**  
No.

**Do you submit from a home machine, compute/cloud or website?**  
Home machine.

**Do you want to train your model locally or in the cloud?**  
Eventually want to train and submit models from the cloud.

**How often do you retrain your models?**  
Once a model is trained I won’t retrain unless there’s new training data. However, when I have an idea to tweak an existing model, I train them as separate models in order to track performance over time.

**What cloud platform are you most comfortable with?**  
GCP.

**Do you use version control for your model code?**  
Yes.

**What are the biggest pain points with the current Compute setup?**  
Haven’t tried but I saw that you have to have AWS in order to use it. Is that true?

**How do you typically deploy a model to production?**  
Would love to have something like DataBricks where you can just schedule-run a notebook.

---

### Post #17 — **taori** | 2022-06-09 06:03 UTC

* Are your submissions automated now?



Yes

  * Do you submit from a home machine, compute/cloud or website?



Home machine

  * Do you want to train your model locally or in the cloud?



Locally

  * How often do you retrain your models?



Every week

  * What cloud platform are you most comfortable with?



Indifferent

  * Do you use version control for your model code?



Yes

  * What are the biggest pain points with the current Compute setup?



It is an unnecessary additional step that I don’t need, which means it is a burden.  
The simplicity and flexibility of numerai was the main reason I started playing with it years ago and one of the reason numerai is so better than others finance tournament out there

  * How do you typically deploy a model to production?



Long period of development and testing. Then simply update the production code folder to the latest version of my code repository and that’s it. My cronjob will take care of running and submitting predictions every week

---

### Post #18 — **zoenolan** | 2022-06-09 17:56 UTC

* Are your submissions automated now?  
Yes

  * Do you submit from a home machine, compute/cloud or website?  
compute/cloud.

  * Do you want to train your model locally or in the cloud?  
Both but mostly locally currently.

  * How often do you retrain your models?  
Not very often

  * What cloud platform are you most comfortable with?  
AWS and GCP mostly

  * Do you use version control for your model code?  
Yes. I have a monorepo for all my models under git

  * What are the biggest pain points with the current Compute setup?  
AWS account memory limit was a hassle to get increased. Building docker images.

  * How do you typically deploy a model to production?  
Manually currently. I have the production model which is staked then a number of other testing various updates to the code. Once I’m happy with the new code. I update the production models code and rebuilt docker images and deploy.




I do have some GitHub actions to lint the code.

I’m happy enough with AWS. Now I have things running. It costs less than $1 a month to run, so must be costing AWS to process my payment.

---

### Post #19 — **quantverse** | 2022-06-10 21:53 UTC

> Are your submissions automated now?

Yes

> Do you submit from a home machine, compute/cloud or website?

cloud (AWS)

> Do you want to train your model locally or in the cloud?

Locally for now, probably will use vast.ai later…

> How often do you retrain your models?

Basically never.

> What cloud platform are you most comfortable with?

AWS, Vultr

> Do you use version control for your model code?

I use Git.

> What are the biggest pain points with the current Compute setup?

I want to have 100% control of the deployment process and of what is being done on background. Also, the idea that each model is triggered by a webhook is a non-sense. I am using docker + amazon ECS + amazon Fargate + scheduled tasks.

> How do you typically deploy a model to production?

`docker build` \+ `docker push`

---

### Post #20 — **monticola** | 2022-06-11 10:51 UTC

> Are your submissions automated now?

Yes

> Do you submit from a home machine, compute/cloud or website?

Cloud (Azure Container Instances)

> Do you want to train your model locally or in the cloud?

I don’t have a preference. If the model is to big and does not fit in my computer, Im ok using the cloud.

> How often do you retrain your models?

Never. I just recently started doing ML stuff, I am not in the point where I would consider retraining on any basis.

> What cloud platform are you most comfortable with?

Azure. Just because it is the one I have used the most.

> Do you use version control for your model code?

Yes, git(hub).

> What are the biggest pain points with the current Compute setup?

When I first arrived at numerai, it felt overwhelming. Probably beacuse everything was new to me: ml, python, numerai rounds, cryptos, staking, rounds, corr, mc… It was very hard for me to make heads or tails from it. I ended up doing my own thing on Azure because I have some free monthly quota there, I learnt along the way and I was uncertaing Compute was what I wanted/needed.

> How do you typically deploy a model to production?

Manually. It involves copying some files to a safe place on the Azure Cloud and modifying and pushing a docker image. I m ok with it since it is a straightforward procedure and it is something I only do from time to time.

---

### Post #21 — **qeintelligence** | 2022-06-11 19:15 UTC

I am working a little bit on automating it further and into the cloud, especially since holidays and other trips are coming up ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10) Anyway, using oracle free tier I managed to predict and upload 20 v3/v4 models based on the smaller feature-set within 10 mins on that free tier (with only 1gb memory) so that’s working nicely.

I also got it working with the medium feature-set (i forgot how many that was, somewhere between 300 and 500?), loading the training set for neutralization purposes ofcourse takes longer but I am guessing 20 models still would go within the hour, not bad for free compute which you can keep on 24/7.

I will write a forum post soon on how I did this with some example code/instructions, maybe others can benefit from it too.

---

### Post #22 — **mic** | 2022-06-13 02:41 UTC

Are your submissions automated now?
    

Semi automated (manually triggered)
    
    
    Do you submit from a home machine, compute/cloud or website?
    

Local machine
    
    
    Do you want to train your model locally or in the cloud?
    

Depending on resources needed. Prefer local.
    
    
    How often do you retrain your models?
    

Manually, no set schedule.
    
    
    What cloud platform are you most comfortable with?
    

AWS (but am open to options)
    
    
    What are the biggest pain points with the current Compute setup?
    

Lack of information. More explanation would be helpful, to see if it works for me or not, and whether the cost is worth it. Not even sure what the costs would be.
    
    
    Some proposals we have:  Which of these is most appealing to you? What changes would you make?
    

None of them look appealing as I’m not so interested in notebooks. Probably need to store an image of environment to run all models in single instance and run it on your trigger. Would only use a notebook service if it was secure and cheap.

---

### Post #23 — **restrading** | 2022-06-13 04:35 UTC

> Are your submissions automated now?

Partially, manually triggered each week

> Do you submit from a home machine, compute/cloud or website?

Home machine

> Do you want to train your model locally or in the cloud?

Locally because of extensive GPU usage and retrainings and model iterations

> How often do you retrain your models?

Each week for Signals, never for Classic

> What cloud platform are you most comfortable with?

Google Cloud

> Do you use version control for your model code?

Yes

> What are the biggest pain points with the current Compute setup?

I need to swap models each week to adjust stake weightings, that’s my main block for complete automation.

> How do you typically deploy a model to production?

Jupyter notebooks or model dump

---

### Post #24 — **kenfus** | 2022-06-15 08:06 UTC

* Are your submissions automated now?  
Yes
  * Do you submit from a home machine, compute/cloud or website?  
Google Cloud
  * Do you want to train your model locally or in the cloud?  
Locally
  * How often do you retrain your models?  
Tournament: Never, Signals: Weekly
  * What cloud platform are you most comfortable with?  
Google Cloud
  * Do you use version control for your model code?  
Yes, git + yaml-files.
  * What are the biggest pain points with the current Compute setup?  
Not enough Memory
  * How do you typically deploy a model to production?  
Usually dockerized but currently I have a bash-script deployed on a VM, which spins up weekly and runs that script via a startup-script. The bash script pulls from github, loads the model from google buckets and runs a script.

---

### Post #25 — **malembetirick** | 2022-06-21 20:43 UTC

* Are your submissions automated now? No
  * Do you submit from a home machine, compute/cloud or website? Google colab
  * Do you want to train your model locally or in the cloud? both
  * How often do you retrain your models? Everytime that i have new idea
  * What cloud platform are you most comfortable with? AWS
  * Do you use version control for your model code? Yes
  * What are the biggest pain points with the current Compute setup? Many configurations to do to deploy and just setup webhook
  * How do you typically deploy a model to production? I just import the model in my google colab notebook



My suggestions are :

  * Improvement of numerai-cli by replacing api-gateway with lambda function urls [Announcing AWS Lambda Function URLs: Built-in HTTPS Endpoints for Single-Function Microservices | AWS News Blog](<https://aws.amazon.com/fr/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices/>) (it’s less costly), add feature to visualize and track model performance <https://aimstack.io/> based on user custom metrics, add feature to train easily and at low cost our model in the cloud using spots instances <https://github.com/iterative/terraform-provider-iterative>

  * Embed numerai-cli and its dependencies (docker, terraform) to vagrant <https://www.vagrantup.com/> that will help build a common environment for all numeratis and help them focus on adding value to numerai meta-model

  * Build a docker image that will contain all common ML framework to build AI model (tensorflow, pytorch, lightgbm, xgboost, catboost) and vscode with notebook, git extension




The main objective is to have all environment setup in vagrant file that will be run in one click after installation of virtualbox, vmware,hyper-v with vagrant.  
If someone want to share its work, he could use vagrant share.

I will be happy to work on something like this if this idea interests community.

---

### Post #26 — **malembetirick** | 2022-06-21 20:50 UTC _(reply to #25)_

Other option will be <https://cml.dev/> which is a git friendly approach that use github actions to trigger cloud computing

---

### Post #27 — **factorsparsity** | 2022-06-28 19:04 UTC

* Are your submissions automated now?



Sort of. I need to start them manually but I could do that from a phone while travelling.

  * Do you submit from a home machine, compute/cloud or website?



Home machine, unless I’m travelling.

  * Do you want to train your model locally or in the cloud?



Locally.

  * How often do you retrain your models?



I don’t. However, I’m moving to v4 now and I really need to come to terms with TC.

  * What cloud platform are you most comfortable with?



Google Cloud.

  * Do you use version control for your model code?



Yes, just CVS.

  * What are the biggest pain points with the current Compute setup?



I don’t find the time to look at it. ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10)

  * How do you typically deploy a model to production?



Manually.

---

### Post #28 — **sneaky** | 2022-07-03 07:56 UTC

1. Are your submissions automated now?


  * Semi automated


  2. Do you submit from a home machine, compute/cloud or website?


  * Home machine, don’t wish to use anything else.


  3. Do you want to train your model locally or in the cloud?


  * Locally.


  4. How often do you retrain your models?


  * Once a month.


  5. What cloud platform are you most comfortable with?


  * None.


  6. Do you use version control for your model code?


  * Yes.


  7. What are the biggest pain points with the current Compute setup?


  * I would like to try it sometime, but I am finding myself too lazy to do that.


  8. How do you typically deploy a model to production?


  * By changing a model-to-id mapping.

---

### Post #29 — **qeintelligence** | 2022-07-03 08:30 UTC

Its quite interesting to see there are still a lot of people who don’t even consider cloud as an option (at least for weekly predictions). It makes me think that a general solution should be capable of supporting both cloud and local compute out-of-the-box.

---

### Post #30 — **shatteredx** | 2022-07-03 21:32 UTC

* Are your submissions automated now?  
**Semi-automated**
  * Do you submit from a home machine, compute/cloud or website?  
**Google Colab**
  * Do you want to train your model locally or in the cloud?  
**No preference.**
  * How often do you retrain your models?  
**Every week.**
  * What cloud platform are you most comfortable with?  
**No preference.**
  * Do you use version control for your model code?  
**No.**
  * What are the biggest pain points with the current Compute setup?  
**Haven’t tried Compute**
  * How do you typically deploy a model to production?  
**Manually.**



**Whatever can easily/cheaply store a model and trigger it is what I’m for. If Compute already does that, then cool.**

---

### Post #31 — **robo_boi** | 2022-07-05 09:06 UTC

* Are your submissions automated now?  
Yes

  * Do you submit from a home machine, compute/cloud or website?  
Cloud

  * Do you want to train your model locally or in the cloud?  
Cloud

  * How often do you retrain your models?  
Classic: Whenever new data is released for 99% of the models. Experimenting with weekly re-training  
Signals: Weekly for most, monthly or quarterly for some. Some are not models but just features and calculated weekly

  * What cloud platform are you most comfortable with?  
Google Cloud Platform

  * Do you use version control for your model code?  
Not really

  * What are the biggest pain points with the current Compute setup?  
Never tried it

  * How do you typically deploy a model to production?  
Test locally then upload it to google cloud storage. The most recent version will get downloaded each week and used




Similar to [@jrai](</u/jrai>), I use GCP and just run everything on a vm. The vm is on a cron job, downloads the latest python files from cloud storage, runs them, submits the predictions and then shuts down automatically. For batch predictions like we’re doing this works very well.

---

### Post #32 — **dev0n** | 2022-07-09 21:21 UTC

* Are your submissions automated now?  
Yes
  * Do you submit from a home machine, compute/cloud or website?  
Classic: numerai-compute on AWS. Signals: Dedicated server
  * Do you want to train your model locally or in the cloud?  
Classic: Cloud. Signals: Dedicated server
  * How often do you retrain your models?  
Classic: Never. Signals: Every submission
  * What cloud platform are you most comfortable with?  
GCP
  * Do you use version control for your model code?  
Yes
  * What are the biggest pain points with the current Compute setup?  
Signals: Terraform is too opaque for me to understand how to use it to kick off my complex Signals pipeline, so I just roll my own with [schedule](<https://schedule.readthedocs.io/en/stable/>). I’d be open to setting up a webhook you could call if timing is variable
  * How do you typically deploy a model to production?  
Signals: `Docker-compose up` on dedicated server



Bonus questions:

  * How long does your pipeline take?  
Classic: 2-5 min (inference only on legacy data). Signals: >24 hours (data collection of the past week + retraining + inference)
  * How easy would it be to move to daily submissions?  
Classic: Pretty easy. Signals: Pretty hard, would require significant rearchitecting of data pipeline

---

### Post #33 — **dg1** | 2022-07-09 22:02 UTC

* Are your submissions automated now?  
Yes

  * Do you submit from a home machine, compute/cloud or website?  
numerai-compute on AWS

  * Do you want to train your model locally or in the cloud?  
locally

  * How often do you retrain your models?  
Classic: ~5% of slots weekly, some trained years ago still running Signals: Every 3 - 6 months

  * What cloud platform are you most comfortable with?  
AWS

  * Do you use version control for your model code?  
Yes

  * What are the biggest pain points with the current Compute setup?  
Initial setup, diagnosing problems, shutting down/restart via AWS if needed  
Lack of AWS creds accessible from env like Numerai creds. (AWS Creds used for S3- bucket read/saves/archiving/ensembling etc.)

  * How do you typically deploy a model to production?  
Numerai node deploy




Bonus questions:

  * How long does your pipeline take?  
Classic: ~20 min (FE then inference only for 50 slots, single slot trigger). Signals: >1 hour (data retrieval + feature engineering + inference)
  * How easy would it be to move to daily submissions?  
Classic: Pretty easy. Signals: Dicey depending upon time allowed after trigger because of data pipeline

---

### Post #34 — **by256** | 2022-07-11 09:12 UTC

* Are your submissions automated now?
        




Kind of. I have a single script that submits all of my models that I run manually.

  * Do you submit from a home machine, compute/cloud or website?
        




Home.

  * Do you want to train your model locally or in the cloud?
        




Locally.

  * How often do you retrain your models?
        




Never.

  * What cloud platform are you most comfortable with?
        




AWS.

  * Do you use version control for your model code?
        




Yes.

  * What are the biggest pain points with the current Compute setup?
        




Not enough RAM; a pain to set up 20+ times for each model; don’t want to have to use Docker or other similar dependencies.

  * How do you typically deploy a model to production?
        




Create a predict.py script for each model and run these every weekend.

---

### Post #35 — **malembetirick** | 2022-07-15 21:53 UTC

Hello Numeratis,  
A few months ago, I made you a proposal to set up a dedicated cloud workspace [[Proposal] Numerai.cloud - Open source cloud workspace for the community](<http://forum.numer.ai/t/proposal-numerai-cloud-open-source-cloud-workspace-for-the-community/5311>). Despite some skeptics I decided to make this project a reality, so I set up a subscription page for those wishing to access the app in beta and support the project at this link <https://numerai-cloud.ghost.io/>.  
I am convinced that this would make life easier for all of us, reduce friction and allow us to quickly onboard new Numeratis and explore more ideas TC friendly.

---

### Post #36 — **taori** | 2022-09-01 21:32 UTC _(reply to #35)_

I had a look at the Compute Lite Beta Testing [Document](<https://docs.google.com/document/d/1RCKgL4SAqEJ2atnMsdaPHdlV-d7pxJl9dB__mSx11CM/edit?usp=sharing>).
    
    
    napi.deploy(model_id, model, napi.feature_sets('small'), 'requirements.txt')
    

What does this code do? What is happening behind the scene?

> ### Will this work with my model?
> 
> This works with any model or pipeline that matches the sklearn interface. As long as your model has a predict function it will work.

This is such a big limitation and assumption. Many user models will not work.

> ### What are the limitations of Compute Lite?
> 
> Compute Lite uses Lambda to run your deployed model, so there are run time and memory constraints. Lambda has a maximum run-time of 15 minutes and maximum memory allocation of 3GB. If your model inference exceeds these limits, it will not work until we add support for AWS Batch

Same as above

---

### Post #37 — **taori** | 2022-09-01 22:05 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> What does this code do? What is happening behind the scene?

That is actually well explained in the document

---

### Post #38 — **kayeffnumeraitor** | 2022-09-14 15:56 UTC

> Are your submissions automated now?

Yes I have a cronjob on a local raspberry waking up my main computer to run the scripts.

> Do you submit from a home machine, compute/cloud or website?

Home machine

> Do you want to train your model locally or in the cloud?

Locally

> How often do you retrain your models?

Depends on the model, those that I retrain once per month

> What cloud platform are you most comfortable with?

None of them

> Do you use version control for your model code?

Yes

> What are the biggest pain points with the current Compute setup?

Lack of control. I don’t like private code somewhere other than my local machines. I also don’t like the approach “Let me handle everything for you” and would rather have “Here is a ready to use solution, but you can also modify it or do everything on your own”. Also, some of my models require some compute power, and I already have a local machine capable of doing that. I don’t want to spend extra money for expensive cloud services. If a webhook trigger mechanism becomes mandatory, I would really like to be able to set custom webhook URLs in my Numerai account, and let me do my own thing.

> How do you typically deploy a model to production?

For most models I create a custom model file that can be added to a folder of deployed models after I have trained it.

> To support this future, we are exploring the idea of daily rounds with much shorter submission windows. This change will effectively make model automation mandatory.

Just define a daily time window where models are supposed to upload their predictions, i.e. every Mon-Fri from 6:00 UTC to 10:00 UTC. A simple cronjob will work just fine.

The key message I want to convey is that I am fine with everything unless it becomes impossible to upload predictions other than by using a Numerai Compute node running in a cloud service.

---

### Post #39 — **nyuton** | 2022-09-18 14:22 UTC

* Are your submissions automated now?



Semi automated. All models can be sumitted by manually triggering a single script.

  * Do you submit from a home machine, compute/cloud or website?



home machine

  * Do you want to train your model locally or in the cloud?



Locally

  * How often do you retrain your models?



Not too often. Mostly they are trained once and get included into the pipeline without retraining

  * What cloud platform are you most comfortable with?



AWS and GCP

  * Do you use version control for your model code?



No

  * What are the biggest pain points with the current Compute setup?



I often add new models and remove bad models. Change the script, what goes into the ensemble.

Model files are big. Building a container and uploading the whole packet into the cloud takes looong.

---

### Post #41 — **taori** | 2022-09-21 10:08 UTC

While I understand the need and advantage for many users, I am worried that the new Numerai Compute will take away the clean, straightforward and above all **flexible** approach of Numerai tournament (download data → do whatever you want → upload the predictions).

With Numerai Compute the user models are run on demand by Numerai. Numerai decides when to call what, which is a big shift from the current standard where is the user who decides to do what and when.

I can understand the Numerai’s need for this paradigm shift, but I do not accept the decrease in flexibility on how I can run my model or what I can do (which is a limit imposed by both the current form of Numerai Compute and the fact we have to use AWS).

if this paradigm shift will become mandatory, please, please, please add the possibility to skip Numerai Compute and allow users to register a Webhook on their account instead. The Webhook would work as a simple trigger that starts user models. That would give us back the flexibility to do anything our models need.

---

### Post #42 — **restrading** | 2022-09-21 14:15 UTC _(reply to #41)_

I second [@taori](</u/taori>) please keep the webhooks or at least a way to make external custom calls outside of aws.

---

### Post #43 — **chanes** | 2022-09-21 15:21 UTC _(reply to #42)_

Rest assured, we are keeping webhooks. The new Compute setup is not mandatory and never will be. Our goal with Compute Lite is to get as many people as possible automated and our initial offering relies on AWS. For users that are already automated, they can keep their existing setup whether it uses Compute or not.

---

### Post #44 — **taori** | 2022-09-22 09:13 UTC _(reply to #43)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/chanes/48/2562_2.png) chanes:

> The new Compute setup is not mandatory and never will be.[…] For users that are already automated, they can keep their existing setup whether it uses Compute or not.

Ah, I was worrying for no reason then. Thank you for clarifying this.

---

### Post #45 — **nyuton** | 2022-10-06 08:39 UTC

Compute should support the deployment and ensembling of multiple models!  
Also it would be beneficial, if it could support reading model data from S3.

Building and reuploading a docker container with several models is very slow even with a good internet connection.

---

### Post #46 — **stochastic_geometry_1** | 2022-10-26 08:50 UTC

* Are your submissions automated now?  
Yes
  * Do you submit from a home machine, compute/cloud or website?  
Cloud
  * Do you want to train your model locally or in the cloud?  
Cloud
  * How often do you retrain your models?  
About three times yearly.
  * What cloud platform are you most comfortable with?  
Saturn
  * Do you use version control for your model code?  
Yes.
  * What are the biggest pain points with the current Compute setup?  
I’m not very familiar with docker containers. It’s a steep learning curve.
  * How do you typically deploy a model to production?  
Straight from github.

---

### Post #47 — **liborty** | 2022-10-26 10:55 UTC

* Are your submissions automated now?  
Yes, I have just automated them on my home machine for the daily tournaments. Using cron, bash scripts and back end Rust. All I ask is some guaranteed deadline within the submission window, by which the data will be available for download.

  * Do you submit from a home machine, compute/cloud or website?  
Home machine

  * Do you want to train your model locally or in the cloud?  
Locally

  * How often do you retrain your models?  
Not often, just when I get some ideas for (hoped for) improvements.

  * What cloud platform are you most comfortable with?  
github actions

  * Do you use version control for your model code?  
Yes

  * What are the biggest pain points with the current Compute setup?  
Too pythonesque. I have put quite a lot of effort into setting everything up my own way, in Rust, so that it runs orders of magnitude faster. Any changes assuming all kinds of complications on your side induce pain.

  * How do you typically deploy a model to production?  
I get an idea, I change my rust source accordingly, train a new model and run some benchmarks. If the results appear to show promise, I put it into production. Sometimes I iterate this loop a few times.




None of your proposals are appealing, I know nothing about all that bull and don’t need any of it. Mandatory ‘Compute’ and the fees associated with it would make me pull out of numerai entirely. If you follow my suggestion and have a guaranteed UTC time for data being available, I can synchronise my cron to it and do everything locally in just a few short minutes, quicker than your ‘Compute’ can ever aspire to.

PS. I do not think it is at all reasonable to have a hard submission deadline for us but not to have a hard deadline for you to provide the data.

---

### Post #48 — **dordas** | 2022-11-05 10:24 UTC

* Are your submissions automated now?  
Yes!
  * Do you submit from a home machine, compute/cloud or website?  
Azure Cloud
  * Do you want to train your model locally or in the cloud?  
Cloud, because of memory requirements.
  * How often do you retrain your models?  
Never.
  * What cloud platform are you most comfortable with?  
Azure
  * Do you use version control for your model code?  
Yes, I have a private DevOps git.
  * What are the biggest pain points with the current Compute setup?  
I have some monthly free Azure credits, so I prefer Azure vs AWS.
  * How do you typically deploy a model to production?  
I use a container instance to submit all my models, so I must update a script to include the model, then rebuild and push the new docker image.



I need only one trigger to submit all my models, so I had to put a compute webhook in one of my models, what is a little bit odd. Seems like I have only 1 computed model.  
Maybe could be a place to define a webhook for all models.

---

### Post #49 — **unsentient** | 2022-11-30 20:31 UTC

If you want to improve Numerai Compute, you could update the docs and provide an updated tutorial. The docs page [Numerai CLI and Compute - Numerai Tournament](<https://docs.numer.ai/tournament/compute>) hasn’t been updated in 7 months.

---

### Post #50 — **smilence666** | 2022-12-02 02:32 UTC

* _Are your submissions automated now?_  
No.
  * _Do you submit from a home machine, compute/cloud or website?_  
Home machine.
  * _Do you want to train your model locally or in the cloud?_  
Locally
  * _How often do you retrain your models?_  
Very rarely
  * _What cloud platform are you most comfortable with?_  
I’ve never used one. I’m such a neanderthal.
  * _Do you use version control for your model code?_  
No
  * _What are the biggest pain points with the current Compute setup?_  
Cloud
  * _How do you typically deploy a model to production?_  
Run my script to generate prediction for all my models and then upload them one by one. deployment is just adding a trained model folder name to my pipe.
