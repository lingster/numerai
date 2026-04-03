---
title: "Any Julia lang developers?"
category: Data Science
url: https://forum.numer.ai/t/any-julia-lang-developers/2814
created_at: 2021-04-11T19:33:58.614000+00:00
last_posted_at: 2021-07-29T20:10:41.446000+00:00
posts_count: 13
views: 2421
tags: []
---

# Any Julia lang developers?

---

### Post #1 — **pacio** | 2021-04-11 19:33 UTC

I’m looking for anyone who’s been using Julia for Numerai. To support my fellow Julia developers, I created a version of [uuazed/numerapi](<https://github.com/uuazed/numerapi>) in Julia:

[NumerAPI.jl (https://github.com/richardskim111/NumerAPI)](<https://github.com/richardskim111/NumerAPI>)

I managed to copy nearly all of the Python uuazed/numerapi for both the Tournament and Signals, but it still needs a lot of work including documentation. I’m looking for collaborators to finish the library. I also have not published a registered Julia package before so I humbly ask for help from someone who’s done it before.

Hopefully, I am not the only Julia user here, and if so, that would be unfortunate.

I’ve been using Julia since 2016 for graduate school. It has highly readable syntax like Python and Matlab but has the added benefit of having the speed of many low-level languages like C and Fortran. Like most people here, I started Numerai with Python, but I switched to Julia right away, which allowed me to iterate through different models much quicker.

I’m also planning to write a tutorial to introduce Numerai to the broader community of Julia developers. Any suggestion on what I should include in that tutorial would be appreciated.

---

### Post #2 — **pellej** | 2021-04-13 07:53 UTC

Hi,

Great work! I use Julia for Numerai and will definitely look into your package and try to contribute in the future.

Regarding publishing “official” Julia packages, I unfortunately don’t have any experience.

---

### Post #3 — **pacio** | 2021-04-13 12:32 UTC _(reply to #2)_

That’s great! Please raise issues if you run into bugs. That alone helps me a lot.

---

### Post #4 — **ulzee** | 2021-04-27 20:29 UTC

Really nice! We have a small community on Discord and just recently started an investment game with a Discord.jl bot.

[github.com/Humans-of-Julia/HoJBot.jl](<https://github.com/Humans-of-Julia/HoJBot.jl/pull/53>)

####  [Investment game 💵 📈 🎉](<https://github.com/Humans-of-Julia/HoJBot.jl/pull/53>)

`main` ← `tk/investment-game`

opened 10:18PM - 25 Apr 21 UTC

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a78ff69b920925eebab7e4ecb2dd397b4431c42b.jpeg) tk3369 ](<https://github.com/tk3369>)

[ +1655 -14 ](<https://github.com/Humans-of-Julia/HoJBot.jl/pull/53/files>)

Some screenshots: ![image](https://user-images.githubusercontent.com/1159782/[…](<https://github.com/Humans-of-Julia/HoJBot.jl/pull/53>)116011289-155f8580-a5d9-11eb-8895-7cbcb7a9a503.png) ![image](https://user-images.githubusercontent.com/1159782/116011332-4c359b80-a5d9-11eb-9540-c382082c50b8.png) ![image](https://user-images.githubusercontent.com/1159782/116011326-3fb14300-a5d9-11eb-8532-eea1388bfacd.png) ![image](https://user-images.githubusercontent.com/1159782/116011344-5c4d7b00-a5d9-11eb-9e24-efd163eeaddb.png)

It’s very simple yet, but we may find ways to combine it.

Certainly we can help you with registering the package, and maybe you want to place it into our org if you like.

Feel free to join and introduce yourself, I’m a mod there and my name is Mark.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3f62cd33e67fecf7d516d173af443f163f90650a.png) [Discord](<https://discord.com/invite/C5h9D4j>)

### [Join the Humans of Julia Discord Server!](<https://discord.com/invite/C5h9D4j>)

Humans of Julia is an official community of Julia users on Discord | 3465 members

Check the #trading channel!

Best regards

---

### Post #5 — **pacio** | 2021-04-30 12:51 UTC _(reply to #4)_

Hi Mark, Thanks for inviting me to the Discord community. I just joined.

As a mathematician, my software engineering skills is still rough around the edges. I am happy to place it under HoJ org, if the community would like that. Let me know.

---

### Post #6 — **ulzee** | 2021-05-01 06:38 UTC

Yep, I’m sure we can help, check out the #trading channel for introduction.

I have a trading strategy, but it is more for scalping and I do not know much machine learning. Wondering if I can put it into a model somehow.

---

### Post #7 — **schnetzlerjoe** | 2021-05-17 21:39 UTC

I am a Julia developer. Will check this out. Great work!

---

### Post #8 — **brickfrog** | 2021-07-10 14:49 UTC

Have you ended up making a tutorial yet? I was working on doing a conversion of the Python tips and tricks Jupyter notebook (mostly as an exercise to flex my Julia muscles in an attempt to mirror the outputs (near-ish) exactly)

---

### Post #9 — **johnnywhippet** | 2021-07-10 14:53 UTC

Purely python at  
The mo but my project requires two languages so I’m going to be shifting to Julia sometime soon. If that doesn’t work out, Scala is next on the list…

---

### Post #10 — **dmoore** | 2021-07-25 01:35 UTC

Brand new to Numerai but I’ve been using Julia for about a year and half at work as structural engineer whenever I can. Thanks for developing this package to make it easier to get in on the action!

---

### Post #11 — **rigrog** | 2021-07-25 17:49 UTC

I find Python a little easier to read and write, but the prospect of C-ish performance in Julia tempts me.

Does Julia offer an “on ramp”, that would make it as easy as Anaconda/Spyder makes Python? I.e., no git commands needed.

---

### Post #12 — **david_plutus** | 2021-07-29 18:47 UTC _(reply to #11)_

[@rigrog](</u/rigrog>), the Julia REPL (a bit like ipython console) and VSCode with the official Julia extension would work great.  
I don’t know what you mean with git commands. Usually Julia packages are installed from the REPL with the Package Manager, this is quite easy and the documentation around that is very good.

---

### Post #13 — **rigrog** | 2021-07-29 20:10 UTC _(reply to #12)_

Thanks, I’ll try VSCode.

I whine about git, because I don’t want to learn that whole language of commands. I liked being able to just download stuff I wanted from sourceforge.
