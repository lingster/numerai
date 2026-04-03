---
title: "Removing Dangerous Features"
category: Data Science
url: https://forum.numer.ai/t/removing-dangerous-features/5627
created_at: 2022-08-03T20:43:59.499000+00:00
last_posted_at: 2022-08-30T17:50:35.664000+00:00
posts_count: 24
views: 4835
tags: []
---

# Removing Dangerous Features

---

### Post #1 — **master_key** | 2022-08-03 20:43 UTC

You may be familiar with the idea of “removing risky features” from around cell 102 in the [analysis_and_tips notebook](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>) or from the [example_script](<https://github.com/numerai/example-scripts/blob/master/example_model.py#L69>).

These analyses aim to find features which behave very differently from one era to the next, or which are behaving in recent times very differently from how they behaved in the past.

The risk with features like these is that your model might learn to really like a feature and become reliant on it, but then in live, the feature is behaving completely differently and so your model flounders.

There are 5 features which are particularly bad offenders:
    
    
    ['feature_unsustaining_chewier_adnoun',
     'feature_coastal_edible_whang',
     'feature_trisomic_hagiographic_fragrance',
     'feature_censorial_leachier_rickshaw',
     'feature_steric_coxcombic_relinquishment']
    

If you look at these features’ correlations with the target over time, you will see that they are very consistently negatively correlated for most of the data, but in more recent times have almost 0 correlation with the target.

Here is a cumulative sum of these features correlation with the target, to make the shift easy to see.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c0a7e94d1d10d6babff7336c3be33925fadef43b_2_598x500.jpeg)image1436×1200 101 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c0a7e94d1d10d6babff7336c3be33925fadef43b.jpeg> "image")

Typically, we try to stick to a philosophy of giving the users all of the features, even if we don’t think it’s necessarily good to use them, with the hope that the users will be better at deciding which features to use, and how to use them, than we are.

However in this case, we find that the features’ behavior differences are so problematic to the point that no model should be using these features in any way.

In one simple test, we find that removing these features entirely can boost performance from a correlation of about 0.023 up to 0.025 over the validation eras, and a similar level of performance boost will continue into the future.

These 5 are the worst offenders, but we also suggest removing 5 more features as well due to a similar reason. Below are the complete lists of features to remove from your models in the v4 and v3 datasets.

v4:
    
    
    ['feature_palpebral_univalve_pennoncel',
     'feature_unsustaining_chewier_adnoun',
     'feature_brainish_nonabsorbent_assurance',
     'feature_coastal_edible_whang',
     'feature_disprovable_topmost_burrower',
     'feature_trisomic_hagiographic_fragrance',
     'feature_queenliest_childing_ritual',
     'feature_censorial_leachier_rickshaw',
     'feature_daylong_ecumenic_lucina',
     'feature_steric_coxcombic_relinquishment']
    

v3:
    
    
    ['feature_base_ingrain_calligrapher',
     'feature_unvaried_social_bangkok',
     'feature_deliberative_connatural_kinetoscope',
     'feature_haziest_lifelike_horseback',
     'feature_accusatory_disinfectant_deportment',
     'feature_exorbitant_myeloid_crinkle',
     'feature_jerkwater_eustatic_electrocardiograph',
     'feature_undivorced_unsatisfying_praetorium',
     'feature_direst_interrupted_paloma',
     'feature_lofty_acceptable_challenge']
    

These features are not present in v2 data.

We will not be changing the construction of the v3 and v4 datasets, because we are very sensitive to disrupting user pipelines.

Future data releases will not include any of these features of course.

---

### Post #2 — **wigglemuse** | 2022-08-03 21:19 UTC

As long as they are “real” features that potentially have some relevance (and aren’t arbitrarily changing in their composition over time), I’d prefer you leave them in the future. Maybe add another json list of “risky features” to identify them. Non-correlation (or changing correlation) with the target isn’t necessarily a huge red flag just by itself is it? (I would find that rather expected.) I assume the true value of many features is only uncovered via its (possibly non-linear) relationships to other features that you won’t see in isolated correlation analysis of single features vs the target (such simple linear relationships we aren’t supposed to be relying on anyway). Don’t try to child-proof the data, just put a warning on it if you’re worried about it. (And maybe expand the “train” labeled eras out to era 800 or so to encourage training of more recent eras.) After all, with TC we aren’t even primarily being judged on correlation with the target anymore, and there are a whole bunch of targets!

---

### Post #3 — **master_key** | 2022-08-03 21:32 UTC _(reply to #2)_

Totally agree with you.

This is a special case though where the construction of these features have actually changed irreparably and we can’t keep the same definition going forward.

They are beyond “risky features” and would be more accurately described as “invalid features” now.

No child-proofing, promise!

---

### Post #4 — **wigglemuse** | 2022-08-03 21:38 UTC

Okey-dokey, fair enough. (And you probably should put that list in the json file for v3/v4.)

My existing models would be too costly to retrain, but I could just fill-in those features with a constant middle-value for every row and see if that helps or at least doesn’t hurt.

---

### Post #5 — **restrading** | 2022-08-04 02:09 UTC

[@master_key](</u/master_key>) are all of these features listed in the post “invalid features” or just some of them?

---

### Post #6 — **wigglemuse** | 2022-08-04 03:00 UTC

Looks like it is fundamentally just two features (each repeated in slightly different version 5x and v3 & v4 same features under different names).

---

### Post #7 — **master_key** | 2022-08-04 03:12 UTC _(reply to #5)_

They are all invalid

---

### Post #8 — **jackerparker** | 2022-08-04 07:10 UTC

Are there any extra features which you do not consider as “risky” but the construction of which have been changed?

---

### Post #9 — **benben11** | 2022-08-04 12:29 UTC

Another way to communicate with to the other might be to give us a json file containing all the very stable features, i.e. things that are not going to change? That would be very helpful.

---

### Post #11 — **kenfus** | 2022-08-05 12:40 UTC

Why are you looking at Corr when deciding if the features are good or not? Should you not look at TC?

---

### Post #12 — **wigglemuse** | 2022-08-05 13:03 UTC

You guys are all echoing my concern, but it kinda sounds (from his follow-up post) that these features are essentially just not available anymore, and any predictive value you were getting out of them is gone as well so that’s that. I imagine for most existing models if retraining is infeasible, then setting up your pipeline to use dummy values for those features (e.g. a constant 0.5) is probably the way to go. But if Numerai did that for you, it might break some pipelines – if there was a constant value it might cause a model that z-scored the variables to crash (for instance) because deviation would be zero which would usually never happen with the normal binned values. (Maybe they’d want to do that anyway, but not before giving you a chance to make your own workaround which in a case like that you’d fill-in zeros after scaling.)

No matter what they were before, I guess it is unclear WHAT are those variables _now_? Are they essentially random, or are they something that is still a feature but it is just a different feature?

---

### Post #13 — **yxbot** | 2022-08-05 14:09 UTC

[@master_key](</u/master_key>) would you please give a timeline on when/how you would treat these features in the upcoming data release? so that we can act accordingly

---

### Post #14 — **master_key** | 2022-08-05 19:46 UTC _(reply to #8)_

No! These are the only ones for sure.

---

### Post #15 — **master_key** | 2022-08-05 19:50 UTC _(reply to #13)_

Nothing is going to change in the data file construction, no pipelines will be affected.

So there is no urgent action to take, other than retraining your models to ignore these features, which will likely lead to a performance boost.

We considered making these columns nan, or filling them all with 0.5, but decided this was too risky since we don’t know how everyone’s pipelines or models would handle this sort of change.

When I say they will be removed from a future data release, I just mean that when an eventual “v5” dataset is released sometime in the future, these won’t be included.

---

### Post #16 — **qeintelligence** | 2022-08-06 07:42 UTC

hi [@master_key](</u/master_key>) , are these features part of the small or medium feature sets? Probably a lot of the newer users this year started with one of those.

---

### Post #17 — **jrb** | 2022-08-06 17:35 UTC

Like I said in yesterday’s [CoE twitter space](<https://twitter.com/NumeraiCoE/status/1555607434416328704>), I add an extra category to my embeddings for handling missing values. GBDT models ([XGBoost](<https://xgboost.readthedocs.io/en/stable/faq.html#how-to-deal-with-missing-values>), [LightGBM](<https://lightgbm.readthedocs.io/en/latest/Advanced-Topics.html#missing-value-handle>), [CatBoost](<https://catboost.ai/en/docs/concepts/algorithm-missing-values-processing>), etc) also support handling missing values during inference. The missing features just need to be set to `NaN`.

Here’s a [Python function](<https://gist.github.com/jeethu/763a6866ee945ac8a04660d3c15934f0>) to replace the dangerous features in a pandas DataFrame with `NaN` or anything else. It works with both v3 and v4 data. Tree bros who don’t have the time to retrain their models, might find it useful.

---

### Post #18 — **joakim** | 2022-08-09 01:07 UTC

[@master_key](</u/master_key>) how about v3.1 and v4.1 datasets without these invalid features, with a deprecation warning message via the API when accessing v3 or v4? Perhaps also update the example scripts to not use these features? Not everyone will see this forum post, especially not new(er) users.

---

### Post #19 — **gammarat** | 2022-08-09 17:19 UTC

Thanks for the heads up re. those questionable features.

If I could make a suggestion: if the construction of those features is going to remain stable going forward, could you just leave them in as is, and put a indication (say in the JSON data) that they were changes, and when? That way in the future people could use them or not as they choose.

The change, after all, seems to have occurred for data around 7 years ago (i.e. around era 650); the cumulative sum for correlation for that going forward looks ok.

---

### Post #20 — **rigrog** | 2022-08-09 17:52 UTC

I prefer to call the 5*210 + 149 = 1199 v4 features 0, 1, … , 1198. Instead of feature_meaningless_preposterous_verbosity, and so forth.

Is there any chance I could get that list of dangerous features, by integer index? Less of my thinning hair would get pulled out that way.

Thanks!

---

### Post #21 — **wigglemuse** | 2022-08-09 18:18 UTC _(reply to #20)_

These are the raw column indexes: 196 211 406 421 616 631 826 841 1036 1051  
(features start at column 3, index3 = feature1)

These are actual the feature indexes: 194 209 404 419 614 629 824 839 1034 1049  
(i.e. -2 of the column indexes with index1 = feature1)

But if you’re in a 0-indexed environment like python, gotta subtract 1 from all of these I guess. It seems like such a simple question…

---

### Post #22 — **rigrog** | 2022-08-09 18:47 UTC _(reply to #21)_

Big thanks, wigglemuse!

We’ve discussed before, the tight correlation between features x, x+210, … , x + 840; we can see that in play here:

194, 194+210 = 404, 194 + 420 = 614, 194 + 630 = 824, 194 + 840 = 1034;  
209, 209 + 210 = 419, 209 + 420 = 629, 209 + 630 = 839, 209 + 840 = 1049.

So actually just two out 210 features, if one “unredundifies” v3. And there were no “dangerous” features features, from the 149 added in v4?

---

### Post #23 — **wigglemuse** | 2022-08-09 20:13 UTC _(reply to #22)_

Yeah, the first 1050 features in v4 are more-or-less the same 1050 features in v3 in the same order but with different names. (MikeP tells us some of them are slightly different, but essentially they are the same set.)

---

### Post #24 — **qeintelligence** | 2022-08-21 17:46 UTC

Got home last week from holiday and had a chance to check whether or not those features are also in the small and medium feature-set. The answer is a yes. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) And also 6 features in the small feature-set, so I guess maybe not a good choice to try that one for now…

---

### Post #25 — **bor1** | 2022-08-30 17:50 UTC

I am just really curious what those features can be…

Car-brand driven by the CEO? Average response time at the helpdesk? Something in the data provider pipeline borked?
