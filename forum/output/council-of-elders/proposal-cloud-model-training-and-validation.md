---
title: "[Proposal] Cloud model training and validation"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-cloud-model-training-and-validation/4741
created_at: 2022-01-07T13:41:49.880000+00:00
last_posted_at: 2022-01-09T23:22:02.482000+00:00
posts_count: 5
views: 739
tags: []
---

# [Proposal] Cloud model training and validation

---

### Post #1 — **forstmeier** | 2022-01-07 13:41 UTC

**Proposal** :

I’m in the process of building a service that will allow contributors to offload model computation to the cloud.

The MVP feature set is going to be very basic, consisting of an API to upload the model Python code to and an email response containing presigned URLs to the generated artifacts. These would likely be the tournament and validation prediction output CSVs.

Future features could include directly invoking the Numerai validation API, in-line code editing, improve cost performance, and payments based on model performance.

**Timeline** :

I’m participating in the [#BuildSell30 challenge on Twitter](<https://twitter.com/forstmeier/status/1477323181979484164>) so the goal is to have the MVP done by the end of the month.

Currently, most of the backend is complete and I’ll be tweaking and fixing infrastructure through the weekend. After that’s done, I’ll pivot over and build a small wrapper UI or CLI and invite beta users - if you’re interested, sign up for email updates [here](<https://www.producthunt.com/upcoming/numermatic>).

**Best Case Outcome** :

Pretty straightforward in that a decent number (I don’t have a specific number) users would be using the platform and that we see an increase in submitted models as a result.

**Worst Case Outcome** :

Low user engagement in which case I might open source the code and take down any running instances in my own account.

**Success Criteria** :

This would be hitting the MVP of exposing a functional API and likely wrapping it with a UI or CLI depending on what the community is looking for.

**Funding Required** :

I don’t really need payment but I’ll track the hours regardless. It’s an evenings and weekends project so probably something like ~10hr / weekday evenings and ~10hr / weekend.

* * *

Let me know what you all think regarding feasibiltiy, features, and gathering more feedback from the community at large. I’m definitely interested in understanding what features and interface the community would prefer for something like this. If you’re interested in collaborating (project stack is Python and AWS serverless offerings) DM me!

Thanks!

P.S. Thanks to [@aventurine](</u/aventurine>) for bringing me in and recommending that I submit a proposal!

---

### Post #2 — **aventurine** | 2022-01-07 18:54 UTC

Thanks for the proposal! We will wait a little bit to see if there is some community discussion about this. I will ping the rocket chat channel with this so we can get some people in here chatting. Were you able to link up with Rick at all about working together?

---

### Post #3 — **forstmeier** | 2022-01-07 19:26 UTC _(reply to #2)_

Yes [@aventurine](</u/aventurine>), we’re still chatting about it. We haven’t established what overlap we might have yet but I figured getting the proposal out there for community feedback would be beneficial.

---

### Post #4 — **sneaky** | 2022-01-09 20:11 UTC

I think that numerai should support cloud computing for its users; However, the cloud should be decentralized, because models are the hearth of the hedge fund. For example Golem, iExec, NuNet, and many other projects are trying to solve this issue.

---

### Post #5 — **forstmeier** | 2022-01-09 23:22 UTC _(reply to #4)_

Yeah, [@sneaky](</u/sneaky>), I was thinking about that as well given distributed philosophy of Numerai. Thoughts on a centralized MVP (which I _should_ be able to wrap up in a couple weeks) to gauge user interest and suss out desired features and then exploring a decentralized option?
