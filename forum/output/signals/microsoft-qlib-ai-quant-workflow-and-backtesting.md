---
title: "Microsoft Qlib: AI Quant workflow and backtesting"
category: Signals
url: https://forum.numer.ai/t/microsoft-qlib-ai-quant-workflow-and-backtesting/1315
created_at: 2020-12-15T18:01:56.269000+00:00
last_posted_at: 2021-02-08T22:07:14.830000+00:00
posts_count: 6
views: 3259
tags: []
---

# Microsoft Qlib: AI Quant workflow and backtesting

---

### Post #1 — **objectscience** | 2020-12-15 18:01 UTC

Richard pinged us earlier with Microsoft Qlib and has asked “The Mikes” to investigate. I suspect we’ll see code and Numerairish examples follow. Thought it might be a good idea to also start a user thread where we can centralize questions, answers and insights. For those of us without full-blown HF pipelines can this can check a lot of boxes.

[github.com](<https://github.com/microsoft/qlib>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4fb4890ae4d77bdcdd77ed2b040f22a7b66abef3_2_690x344.png)

### [GitHub - microsoft/qlib: Qlib is an AI-oriented quantitative investment...](<https://github.com/microsoft/qlib>)

Qlib is an AI-oriented quantitative investment platform that aims to realize the potential, empower research, and create value using AI technologies in quantitative investment, from exploring ideas to implementing productions. Qlib supports diverse machine learning modeling paradigms. including supervised learning, market dynamics modeling, and RL.

> Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies.

Qlib documentation:  
<https://qlib.readthedocs.io/_/downloads/en/latest/pdf/>  
or,

[qlib.readthedocs.io](<https://qlib.readthedocs.io/en/latest/>)

### [Qlib Documentation — QLib 0.9.6.99 documentation](<https://qlib.readthedocs.io/en/latest/>)

Qlib : An AI-oriented Quantitative Investment Platform (thanks Jrdi):  
<https://arxiv.org/pdf/2009.11189.pdf>

---

### Post #2 — **objectscience** | 2020-12-15 18:53 UTC

Note to Windows users. You’ll need C++ 14.0 or higher*, else you fail on the “cvxpy==1.0.21”, requirement. Outside of that Install is ezpz and the example workbook on the git page works as expected.

  * <https://visualstudio.microsoft.com/visual-cpp-build-tools/>

---

### Post #3 — **surajp** | 2020-12-17 05:07 UTC _(reply to #2)_

I am trying to do this in colab and the default notebook [workflow_by_code.ipynb](<https://github.com/microsoft/qlib/blob/main/examples/workflow_by_code.ipynb>) seems to be working well. Models and training loop are highly customizable

We just need to somehow get our signals data into this.

---

### Post #4 — **restrading** | 2020-12-23 06:57 UTC

Am I the only one who’s curious about why Microsoft is getting into quant investment? ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=9)

---

### Post #5 — **dk5zm** | 2021-02-08 19:04 UTC

[@objectscience](</u/objectscience>) have you been using Qlib since? Any reliability issues so far? I’m always hesitant to adopt larger open source projects with small user-base/community in fear of uncovering bugs. But it does seem like development and maintenance is there based on their commit history!

---

### Post #6 — **objectscience** | 2021-02-08 22:07 UTC _(reply to #5)_

I got started and then got sidetracked. Haven’t gone back to it.
