---
title: "Still understanding scores: CORR of the MM"
category: Tournament
url: https://forum.numer.ai/t/still-understanding-scores-corr-of-the-mm/7120
created_at: 2024-03-15T10:47:14.894000+00:00
last_posted_at: 2024-03-18T10:29:04.710000+00:00
posts_count: 6
views: 557
tags: []
---

# Still understanding scores: CORR of the MM

---

### Post #1 — **rpica** | 2024-03-15 10:47 UTC

Hello,

I’m checking the example model’s diagnostics with numerai-tools, and if I’m applying correctly to the provided MM (Meta Model) predictions, I get that the MM has worse CORR to the targets than the example model.

To compare apples to apples in the middle plot (MM correlation) I put the mean and std corr of the same-eras for MM data and my model validation outputs, to have a fair comparison.

If it is right, the MM has worse mean and std. Also worse diagnostics.

Is this true or (quite likely) I must have done something wrong on the way?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6baebf2dd4eedd2f83da7cfd868abde5c69c3862.png)image773×695 35.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6baebf2dd4eedd2f83da7cfd868abde5c69c3862.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e4d18b80ecacaee258bcc47c6c044bad115e8d74.png)image537×140 13.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e4d18b80ecacaee258bcc47c6c044bad115e8d74.png> "image")

EDIT: If this is right, the range of eras provided from the MM corresponds to a pretty bad one, doesn’t it? Could the MM predictions be provided for a longer period? Even if the way to get is changed I guess it could be calculated retrospectively for validation and MMC calculation.

Also, is it given somewhere how the MM is obtained? A weighted average of models’ predictions?

---

### Post #2 — **jefferythewind** | 2024-03-15 14:52 UTC

Looks about right to me. The MM is only available over the time the tournament was running, which is just the more recent few years. It also turns out that most models provide lower corr over this period compared to previous periods. There could be many explanations for why this happens. It’s good that your model can out-perform the meta model over this time period but it is the future that is at stake. I can probably find a model that outperforms over this time period as well, but could I have found that model 2 years ago, before we know what we know now?

---

### Post #3 — **rpica** | 2024-03-16 06:27 UTC _(reply to #2)_

Thanks [@jefferythewind](</u/jefferythewind>) ! My hesitation was about being the MM worse performing than the example model provided by numerai (my comparison is to that one).

I was expecting (naively?) that the MM would be somewhat … better (either in mean or in std). Specially compared to the model provided as a starting point. I was bought in the idea that an ensemble will normally be better than any of its component models individually ![:sweat_smile:](http://forum.numer.ai/images/emoji/twitter/sweat_smile.png?v=12)

Obviously, I have a lot to learn ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) and this reinforces that chasing CORR might be less important, given a minimum obviously, than trying to be more “different”.

---

### Post #4 — **jefferythewind** | 2024-03-16 13:16 UTC

Yes it is an interesting phenomenon that you bring up. For a while the tournament was run with corr and MMC (pre 2022) and I think at that time the MM was better than benchmarks, then after 2022 the payouts were switched to TC predominantly until the recent switch back to a new version of MMC. I think during the TC phase people were less concerned with getting good corr and wanted to chase TC. Maybe it was during this more recent couple year period where you see the MM corr w/ target decline? You could plot the diff between MM and Benchmark, might be easier to see. I’m pretty sure in 2024 the MM will outperform benchmark models by a decent margin in corr.

Also which benchmark model is this? I’m fairly certain this “benchmark” didn’t exist at the beginning of the meta model period. If the benchmark was trained and evaluated on Cyrus, Cyrus didn’t even exist until about 1 year ago, if I remember correctly. Previous versions of the tournament had less features and more primitive targets. So this isn’t really a fair comparison anyways, is informative though.

I would say you still gotta chase corr, but corr Sharpe in particular. Negative corr is bad. But also check the drawdown.

---

### Post #5 — **shatteredx** | 2024-03-16 20:17 UTC

If this is the v4.3 example model you’re looking at, then yeah, pretty sure it’s because it’s using much more data and the new target that the metamodel did not have access to at the time. They “backfill” the example model predictions with each new data release. That’s why it’s probably better to validate using BMC instead of MMC.

---

### Post #6 — **rpica** | 2024-03-18 10:29 UTC _(reply to #4)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jefferythewind/48/3270_2.png) jefferythewind:

> Also which benchmark model is this?

It’s not a benchmark model, at least directly, it’s the model I got following the hello_numerai notebook, the example one provided.
