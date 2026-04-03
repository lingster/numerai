---
title: "Possible collaboration"
category: Data Science
url: https://forum.numer.ai/t/possible-collaboration/7558
created_at: 2024-07-07T21:19:18.590000+00:00
last_posted_at: 2024-07-09T15:25:03.354000+00:00
posts_count: 5
views: 507
tags: []
---

# Possible collaboration

---

### Post #1 — **thornam** | 2024-07-07 21:19 UTC

Hi everyone,

I’m about to start building a new model and am looking for one or multiple people to collaborate with. I have previously collaborated with people from this community, sharing ideas, interesting articles, and code with success.

I’m always interested in hearing other ideas or perspectives on problems, and I believe there is a lot to gain from it.

For this specific project, I’m building a new model from scratch, but because of limited time, it could be nice to have a partner. Optimally, it would be someone with experience in writing efficient code and possibly in a low-level language, as the model needs to handle matrices that are too large to have in memory. The model itself is not complicated but the setup around it will be because of the size. But this we will talk about

If this sounds interesting and you would like to hear more, or if you just want to connect, then reach out to me here or on [LinkedIn](<https://www.linkedin.com/in/jacob-eriksen/>), and we will talk.

Just some short things about me. Professionally, I’m working as a quant (not in the equity space). I’ve partitioned in Numerai for a bit less than a year with a focus on Signals and have been lucky to have some success lately with my models, where I’m in the top 10 in the open seasonal rank. To get an idea of what I have worked with previously, you can look at this forum post ([Master Thesis subject](<http://forum.numer.ai/t/master-thesis-subject/6482>))

Hope to hear from you

---

### Post #2 — **wigglemuse** | 2024-07-07 23:26 UTC

How big are the matrices that they won’t fit in memory? (i.e. how much memory would you need to fit them in memory?)

---

### Post #3 — **thornam** | 2024-07-08 14:44 UTC _(reply to #2)_

I have done some initial testing, where it required 75 GiB of ram for a subset of 10.000 rows (around 1.5 years) of the Signals dataset. And the model complexity increases by the number of rows, with a magnitude of 10. So model complexity is approximately 10*T, where T is number of rows given to the model.

---

### Post #4 — **thornam** | 2024-07-08 21:21 UTC _(reply to #3)_

Sorry, I mean the size of the matrices will increase by (10*T)^2

---

### Post #5 — **sergedavid** | 2024-07-09 15:25 UTC

Hi Thornam, software engineer here (David Tello). I added you on LinkedIn to share ideas about the implementation. I don’t know if I will have enough time to work on it, but I can probably provide solutions for the implementation and infraestructure.
