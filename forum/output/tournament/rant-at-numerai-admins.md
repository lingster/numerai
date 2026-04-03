---
title: "Rant at numerai admins"
category: Tournament
url: https://forum.numer.ai/t/rant-at-numerai-admins/8261
created_at: 2026-03-15T12:57:24.221000+00:00
last_posted_at: 2026-03-17T15:54:24.455000+00:00
posts_count: 6
views: 160
tags: []
---

# Rant at numerai admins

---

### Post #1 — **slashv** | 2026-03-15 12:57 UTC

OK, so I was very busy the past 3 months and missed the 5.2 update. Result: lost one and half years of gains in two months. Why oh why do you not create a new submission endpoint for a new dataset??? It really would be zero trouble. It’s the umptieth time of showing you really don’t give a sh*t about participants.

---

### Post #2 — **ark** | 2026-03-16 18:07 UTC

Hi, I can understand how difficult it is to keep up with Numerai news, that’s why we make a significant effort to ensure we communicate on both discord and email. We release monthly posts and typically give everyone a 1-month notice period before major changes to give you time to retrain your models and/or simply unstake in case you’re busy and can’t retrain your models:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e8eaae55c41b60506ee3c662619c7a2873b5b6cd.png) [Numerai – 2 Dec 25](<https://blog.numer.ai/numerai-december-2025-update/> "04:17PM - 02 December 2025")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/55470ac6560349df33425f8fbe78712383bfd47c_2_690x388.png)

### [Numerai December 2025 Update](<https://blog.numer.ai/numerai-december-2025-update/>)

Numerai Monthly: $30m Series C, New Data & Target, Signals Payout Clip Increase Numerai raised $30 million at a $500 million valuation Numerai has closed a $30 million Series C fundraising round led by top university endowments. Other...

If there are additional communication channels / methods that you feel could have reached you even when life gets busy, we are more than willing to incorporate these methods to ensure every one of our users are notified about important changes like this.

On the topic of changing the submission endpoint:

There’s no easy way for us to know whether your models would perform well on a new target in a new round, so we specifically strive to maintain backward compatibility and try not to break old models. Obviously, if we have to perform a major version change on our datasets, this will come with breaking changes that we also try hard to communicate well in advance.

Keeping most minor dataset version changes backward compatible allows users to seamlessly transition to new datasets and targets with little-to-no code changes. Ideally, users simply retrain their models when there is a new dataset or target, and their existing pipelines continue to operate normally, just with a new model. We have to leave it up to you to decide how you want to handle new datasets and targets. It’s common for users to simply unstake when life gets busy and return to the tournaments when they’re ready.

---

### Post #3 — **slashv** | 2026-03-16 21:26 UTC _(reply to #2)_

[@ark](</u/ark>) as I found out, one would definitely not want to submit results of a model that predicts for a different target than the one being scored on, so your response makes no sense to me.

Also one has to change code anyway when predicting for a new target. Changing the endpoint along with that would be close to zero extra effort. So really not a valid argument imo.

”We told you in time” is just a really unhelpful response. As a software dev I try my very best to help my users not make costly mistakes and so should you. Saying ” it says not to do that in the manual” will not get me of the hook if I could have just easily prevented the mistake in the software.

I’ll build the required checks in my submission code now, but should not have been necessary.

---

### Post #4 — **ark** | 2026-03-16 22:07 UTC _(reply to #3)_

> one would definitely not want to submit results of a model that predicts for a different target than the one being scored on

It depends on the model. For example, here’s an uploaded v5 model that still performed decently over the same period: [Numerai](<https://numer.ai/koerrie5111>)

> Changing the endpoint along with that would be close to zero extra effort.

Maybe I don’t understand what you mean by “Changing the endpoint”. What do you imagine is the behavior of this endpoint? What is the outcome of submitting to one version of the endpoint versus another?

---

### Post #5 — **slashv** | 2026-03-16 23:45 UTC _(reply to #4)_

[@ark](</u/ark>) My models (several different) that were predicting for cyrus using v5 drew down 25% in three months. Max draw down in more than 2 years before that was less than 10%. That’s not a coincidence. I can’t tell for which target your example was predicting so it doesn’t mean much to me.

By different end-point I mean a different submission URL or query. I haven’t looked at how this works under the hood, but essentially add `dataset` and `target`parameters to `Api.upload_predictions`. I suppose this would also be valuable data for numerai to receive. And I would strongly suggest to just raise an error when the `target` parameter doesn’t match the scoring target and output a warning when the dataset is out of date.

---

### Post #6 — **wigglemuse** | 2026-03-17 15:54 UTC

If there is a change of target (or other wholesale change that really affects everything, which might include major scoring changes), it does make sense that old models shouldn’t be used. (Rather than just new features for same target and scoring.) So if the endpoint just changed and the old one stopped working (or a parameter was included as suggested that would fail if wasn’t set to current thing). It isn’t the worst idea in the world for safety…protects users and keeps bad models (that might only be “suddenly” bad because of target change) from being continually staked on. Then if you do “set it and forget it” the worst that will happen after a big change is it just stands idle. (We can imagine scenarios where this can be caused by things other than user neglect like “user gets hit by bus” and is just not able to attend to things.)
