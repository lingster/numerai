---
title: "[Proposal] Numerai.cloud - Open source cloud workspace for the community"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-numerai-cloud-open-source-cloud-workspace-for-the-community/5311
created_at: 2022-04-24T14:47:24.437000+00:00
last_posted_at: 2022-04-30T20:10:40.485000+00:00
posts_count: 16
views: 1369
tags: []
---

# [Proposal] Numerai.cloud - Open source cloud workspace for the community

---

### Post #1 — **malembetirick** | 2022-04-24 14:47 UTC

**Overview**  
After many months of research, I am pleased to propose numerai.cloud which will be an open source workspace in the cloud allowing the community to organize, track and version their ML projects by applying the best mlops guidelines.  
This space will also offer a tool to visualize and compare models based on custom metrics.  
I propose a frictionless tool that will boost our productivity with a git friendly approach.  
This platform will belong to the community.  
The computation costs will be shared equally by the community and a dao (NumeraiCloudDAO) will be set up to allow everyone to contribute and participate in decisions in a democratic way.  
Members can donate ETH/NMR and receive $NMRC in return which gives them voting rights.  
Community members will no longer have to deal with infrastructure issues and can focus on providing value by doing what they do best.  
I call on the community to help me make this proposal a reality by building the product together.

**Next steps**

  * Setup kubernetes cluster (fargate, arm ec2 instances and gpu spot instances) using pulumi + aws organization

  * Build a code editor (atom: [GitHub - atom/atom: The hackable text editor](<https://github.com/atom/atom>)) that integrates git and jupyter notebook

  * Build UI [Overview — Aim 3.8.1 documentation](<https://aimstack.readthedocs.io/en/latest/>) for tracking training models and make it accessible using lambda url function

  * [OPTIONAL] Setup a community gitlab server to manage repositories

  * Setup project examples using best software principles to train models just in one click using github actions

  * Setup a tool to version data <https://dvc.org/> and build ML pipelines

  * [OPTIONAL] Build sybil-resistant smart contracts with membership nfts and governance strategy to define with community (i.e quadratic voting/Multi-sig voting, …)

  * [OPTIONAL] Deploy smart contracts on testnet and generate fake tokens to allow community to test




**Timeline**  
It would takes me 2 months to deliver the mvp, on a 30h/week work rhythm → 240h for 2 months

**Best Case Outcome**

  * Optimal compute cost control

  * Better ML project structure that will increase community productivity

  * Good DAO treasury management

  * Allow community to increase ml experiments and build more efficient AI models

  * More models stacked

  * Easy onboarding for the new community member

  * NMR and NMRC to the moon

  * Low gas fees




**Worst Case Outcome**

  * Hacking issue with DAO

  * Uncontrol compute cost

  * App performance issues

  * Bugs

  * High gas fees




**Costs**

  * Buy domain name numerai.cloud (15,18$) → done (to renew each year)

  * Development cost (60$ * 240h) → 14400$

  * Hosting cost (50$*12) → 600$ (to renew each year)

  * [OPTIONAL] NFT hash pinned using pinata.cloud → 240$

  * [OPTIONAL] Deploy smart contracts to mainnet + security audit + hackaton to break smart contract + bugs → 50000 $ (to do after we validate smart contracts on testnet)




**Success Criteria**

  * MVP deployed with all important features on numerai.cloud

  * Community satisfaction

  * Stakeholder satisfaction

  * Respect of deadlines

  * well managed cost

---

### Post #2 — **hell_no** | 2022-04-25 11:10 UTC

A few quick questions and my personal sentiment towards this proposal:

  * What will be the benefit of this product? Why is a centralized kubernetes cluster helpful?
  * What are existing competitors?
  * What is the value proposition to use this cloud vs. Google Colab (hosted notebooks) vs. AWS EC2 (“self-managed server in the cloud”)?



My personal opinion and reluctance toward this proposal:

It seems like you want to centralize the work and knowledge of Numerai tournament participiants.  
I appreciate the current approach put forward by Numer.ai Compute: everyone uses their own setup in training and weekly inference. No one but me has access to my local machine or cloud setup. I don’t see myself trusting a system that seems like a perfect honeypot for bad actors to gain access and acquire code/models/knowledge from many participants.

My suggestion: condense this proposal to create a Docker image (or similar) to become the standard training image for Numerai particpants. This could include all common ML packages, plus Numerai specific tools like Numerapi, [Numerblox](<https://github.com/crowdcent/numerblox/>), advanced example scripts, wandb.ai, etc.

This would allow new and existing participants to iterate faster, make better contributions and create a common resource for the community. At the same time every participant would continue to be responsible for their own security.

I like the direction of the proposal, would love to support to create tools for the community and want to start a discussion on this. Hopefully my rambling above can help and be constructive, don’t want it to seem as only negative towards this, especially because of my username on the forum ![:sweat_smile:](http://forum.numer.ai/images/emoji/twitter/sweat_smile.png?v=10)![:grinning_face_with_smiling_eyes:](http://forum.numer.ai/images/emoji/twitter/grinning_face_with_smiling_eyes.png?v=10)![:partying_face:](http://forum.numer.ai/images/emoji/twitter/partying_face.png?v=10) we can also chat on RocketChat

---

### Post #3 — **malembetirick** | 2022-04-25 13:32 UTC _(reply to #2)_

Hi,  
To answer your questions:

  * This product that i want to build will belong to the community. This platform will allow everyone to quickly build their AI models without worrying about infrastructure issues or low computes machines since most of the members of this community are data scientists. So the first advantage is the time saving and therefore an increase in productivity. As a member of the community myself, I must admit that my first steps in the community were very complicated. I had no experience in cloud, no knowledge in finance and had a lot of difficulties to understand the problem and how to build a performing model and defining the best objective function. I would go faster if we had this product that I am proposing.

  * I wanted to simplify things as much as possible and allow the provision of a ready and scalable working environment whether we have 10 users or thousands. Each member of the community will have access to his own ephemeral working environment that will allow him to pull his code from git and do what he does best. I also chose kubernetes to give the community access to the best cloud instances. To easily adapt its infrastructure according to the needs of ressource (cpu, gpu or memory). I’m passionate about AI and I do a lot of monitoring to see the new AWS instances with an interesting cost/performance ratio.the training data evolves and grows. It is therefore important for us to define an infrastructure that evolves according to the new needs.

  * My proposal is to use pulumi which is built on top of terraform and allow us to build quickly a cloud agnostic platform. Maybe tomorrow we will need to optimize our compute cost and we can just choose Azure compute instances instead of AWS.

  * I will based my product on existing open source project that are well established. I want to be able to define a automated pipeline that will retrain my models based on data version and version models and data, so that i can compare easily my models based on metrics that i define. I want to be able to build a pipeline that will dynamically tell me what is my top models and adapt my staking strategy for example. Each week chose the best performers and reallocate nmr on them.

  * There are many existing competitors that you can google. But none will be built by the community and for the community.

  * My goal is to pool our resources to allow unlimited access to computing instances. People will no longer limited in terms of experiment new AI approaches or state of the art algorithms. I believe in the collaborative power.

  * It’s up to community to choose what is best for them.

  * This platform will allow all members to build a ML architecture using the best industry practices.

  * It will be open source and transparent to community.

  * I am not interested in stealing or copying the projects of others and for me this kind of behavior will be sanctioned by the DAO which will govern the rules of governance of the platform. Rules that will be voted by the community. if you are worried about your personal data, we could also integrate the AWS cloudtrail service that will log a history of activity for all aws account(audit events) [CloudTrail concepts - AWS CloudTrail](<https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html>).

---

### Post #4 — **hell_no** | 2022-04-26 18:35 UTC

> I wanted to simplify things as much as possible and allow the provision of a ready and scalable working environment whether we have 10 users or thousands. Each member of the community will have access to his own ephemeral working environment that will allow him to pull his code from git and do what he does best.

100% agree to this.

> pool our resources to allow unlimited access to computing instances

I don’t understand how this will work besides some external sponsorship or other means of funding. Why would I as a contributor donate computing power to others?

> This product that i want to build will belong to the community.

I understand that it will be open-source and rely on other open-source projects. My main concern is **where will computation and storage happen?**. As far as I understand you want to centralize this and run it in an AWS that belongs to the NumeraiCloudDAO. Just my opinion that even with the best security I wouldn’t hand over my models and code to anyones cloud setup.

---

### Post #5 — **malembetirick** | 2022-04-28 06:51 UTC _(reply to #4)_

Hi,  
The goal is not to pay for others and yes, i think it’s better to only pay for what you consume. That’s why it’s important to define an efficient management strategy for computing instances. Pooling our resources and making intensive use of cloud instances would allow us to negotiate better deals and therefore in the short and long term we can save money. AWS is innovating a lot and there are new compute instances available in preview that could benefit the community which are very efficient and economical. This is a lot of work for a data scientist, it’s a thankless task that I prefer to dedicate to numerai.cloud and focus on creating value. With the agreement of the community, I will initiate the project and then it will be up to the members of the DAO to vote for the administrator of the platform and the rules of operation. We are a community and we need to trust each other. Having this centralized cloud agnostic platform would also allow us to put cloud platforms in competition with each other so that the community only benefits from the best priced instances. So in the long run, we will save money. Having unlimited resources means having the freedom to experiment and make numerai more efficient on the markets.

I understand that you’re not thrilled with the idea of running your models on a cloud over which you have no direct control and maybe this solution is not for you but I would still like you to allow me to realize it so that you can test and confirm that it is indeed not suitable for your needs. I have planned in beta, free access to the computing instances for the first 100 users during 2 weeks. So, if my proposal is accepted, you will be able to train your models for free during 2 weeks, I will take care of the costs. I will also activate aws cloudtrail so that you can monitor all the actions on your environment and make sure that nobody stole your data and ensure that you are the only person to have access to your data. The administrator is just there to manage the infrastructure and fix bugs, it may happen that the administrator needs to access your account but it will always be with your consent.

---

### Post #6 — **malembetirick** | 2022-04-28 08:22 UTC _(reply to #5)_

Another thing, to connect to the platform, you will just need a metamask account, have nmr/eth and nfts numerai. This is our definition of your identity, we don’t want to link to your numerai account and know your identity and the performance of your model.

---

### Post #7 — **malembetirick** | 2022-04-28 08:51 UTC _(reply to #6)_

Maybe it’s better to ask community what is better between a fair sharing of the bill and each person paying for their usage ?

---

### Post #8 — **jacob_stahl** | 2022-04-28 20:44 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/hell_no/48/1458_2.png) hell_no:

> My suggestion: condense this proposal to create a Docker image (or similar) to become the standard training image for Numerai particpants. This could include all common ML packages, plus Numerai specific tools like Numerapi, [Numerblox](<https://github.com/crowdcent/numerblox/>), advanced example scripts, wandb.ai, etc.

I like this idea. A standardized container would make it easier for users to offload their compute to the cloud. It would make it easier to do weekly predictions, and use services like [vast.ai](<https://vast.ai>) for training.

---

### Post #9 — **aventurine** | 2022-04-28 21:20 UTC

We see this and usually allow for a couple weeks of discussion from the community before making decisions. If you would like to also come on our Council of Elders twitter space tomorrow or next Friday to talk a bit about this more and also maybe answer some community questions for those interested let us know.

---

### Post #10 — **uuazed** | 2022-04-29 07:29 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jacob_stahl/48/881_2.png) jacob_stahl:

> I like this idea. A standardized container would make it easier for users to offload their compute to the cloud. It would make it easier to do weekly predictions, and use services like [vast.ai](<https://vast.ai>) for training.

Hm, a Dockerfile with some packages installed isn’t that helpful I believe. For those of us that know how to run some docker container in the cloud, the standardized image won’t bring anything new. For those new to docker, they wouldn’t know what to do with it. Of course, if enough people find that useful, why not.

Regarding the original idea, I don’t see the added benefit over using existing cloud providers. They also provide tools to easily run ML pipelines (vertex ai on Google, Amazon’s sagemaker, google colab, etc). In contrast, centralizing everything (shared kubernetes cluster, self hosted version control, … ) creates too many security issues. Overall, I believe the proposal is a monster of a project, which would require tons of work, while mostly re-inventing the wheel. Making it governed by the community, or even giving out it’s own token, gives it a nice “crypto-spin”, but I am not convinced.

Sorry for sounding too pessimistic, I actually love the idea of building more community tools.

Things I would love to see developed:

  * A guide for hyperparameter tuning a numerai model in the cloud. Part of that tutorial could be some standardized docker container that works with different libraries. That could be with any cloud provider, ideally an affordable solution
  * A PR for numerai-cli that adds Google cloud or Azure support
  * in general, improvements to numerai-cli that makes it easier to use / more powerful
  * A tutorial that shows how to automatically schedule some Jupyter notebook for automated submission, either with numerai-cli or some other tool (colab, etc).
  * malenbetirick mentioned Aim for tracking model runs. I haven’t heard about that one, looks nice! Maybe build something on top of that, which allows having a “diagnostic tool” offline. E.g. show correlation per era plots, …
  * …

---

### Post #11 — **arbitrage** | 2022-04-29 15:32 UTC

This just seems too complex and I’m not keen on funding a governance token. I’d rather a project use NMR natively. I concur with @uuzed \- this is a monster project, and I don’t see the direct benefit beyond a small subset of users (a dozen or less).

---

### Post #12 — **wigglemuse** | 2022-04-29 16:25 UTC

If it could be shown that a user would somehow have access to computing power that wouldn’t have otherwise (for a much lower price) – which seems impossible – then I don’t really get it either. If want to use the cloud, I’ll use the cloud – why do we need a _Numerai_ cloud? It’s not like we need special hardware (like a particle accelerator or a radio telescope) to crunch our numbers – any cloud provider will do. And there are other cloud agnostic generalized services cropping up all the time to find the best resources, gpu rental marketplaces, etc to run any project. I think this would be obsoleted pretty quickly just by the overall marketplace for cloud services generally. It would have to offer some _unique_ major unbeatable (and continuous) benefit, i.e. more than somewhat faster ramp-up time or slightly numer-centric tools we already have. There are maybe parts of this or germs of ideas for things that would really be valuable (maybe a special tool for X would actually be nice – just make that and find out), but it does seem like a likely boondoggle in current form with all these parts and a DAO on top.

---

### Post #13 — **jacob_stahl** | 2022-04-29 22:04 UTC _(reply to #10)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/uuazed/48/3333_2.png) uuazed:

> A tutorial that shows how to automatically schedule some Jupyter notebook for automated submission, either with numerai-cli or some other tool (colab, etc).

I’ve been wanting to do exactly this for the past few weeks. The problem is, my notebooks take up too much memory to fit comfortably in an Azure ACI.

---

### Post #14 — **malembetirick** | 2022-04-30 15:26 UTC _(reply to #13)_

Numerai.cloud is not intended to reinvent the wheel but to simplify the organization of a ml project (integrating the best practices of software architecture to a ml project) and training in the cloud. When creating an aws account, we do not automatically have access to all ec2 instances, it is often necessary to make a request to have access to more powerful instances at lower costs. Sometimes the access to this kind of instances requires a significant spending history for the aws instances. The innovative character comes from the implementation of a DAO that will manage this platform. This would be the first step, for a larger vision where we could have each model created by a user represented as an nft that he will own and that he will be able to sell to several people based on the performance of this model. This is a feasible project, the most complex part is the dao part and the nft memberships, which can be realized later.

---

### Post #15 — **malembetirick** | 2022-04-30 17:57 UTC _(reply to #10)_

I understand that you are skeptical about the security aspect of the platform, we can also consider a decentralized approach and improve numerai-cli with visualization features, automatically train its model in the cloud from a command using ec2 spots and also do data analysis A docker friendly approach at the same time and provide aws ec2 instances recommendations

---

### Post #16 — **wigglemuse** | 2022-04-30 20:10 UTC

Still, a system needs users. Besides yourself, who is enthusiastic about this and feels this need? (Anybody who feels this really would fill a void and would be first in line to sign up please chime in.)
