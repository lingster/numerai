---
title: "Mapping of feature names from legacy to new"
category: Tournament
url: https://forum.numer.ai/t/mapping-of-feature-names-from-legacy-to-new/4661
created_at: 2021-12-22T02:17:31.518000+00:00
last_posted_at: 2022-04-11T03:12:48.073000+00:00
posts_count: 5
views: 1318
tags: []
---

# Mapping of feature names from legacy to new

---

### Post #1 — **mic** | 2021-12-22 02:17 UTC

Here is an unofficial mapping:

[github.com](<https://github.com/mizimno/numerai/blob/main/feature_mapping.csv>)

#### [mizimno/numerai/blob/main/feature_mapping.csv](<https://github.com/mizimno/numerai/blob/main/feature_mapping.csv>)
    
    
    legacy_feature,new_feature
    feature_charisma1,feature_revitalizing_dashing_photomultiplier
    feature_charisma2,feature_unco_terefah_thirster
    feature_charisma3,feature_vestmental_hoofed_transpose
    feature_charisma4,feature_unsparred_scarabaeid_anthologist
    feature_charisma5,feature_intended_involute_highbinder
    feature_charisma6,feature_recidivism_petitory_methyltestosterone
    feature_charisma7,feature_acerb_venusian_piety
    feature_charisma8,feature_terrific_epigamic_affectivity
    feature_charisma9,feature_headhunting_unsatisfied_phenomena
    feature_charisma10,feature_jiggish_tritheist_probity
    feature_charisma11,feature_whitened_remanent_blast
    feature_charisma12,feature_glyptic_unrubbed_holloway
    feature_charisma13,
    feature_charisma14,feature_descendent_decanal_hon
    feature_charisma15,feature_synoptic_botryose_earthwork
    feature_charisma16,feature_desiderative_commiserative_epizoa
    feature_charisma17,feature_nucleophilic_uremic_endogen
    feature_charisma18,feature_questionable_diplex_caesarist
    feature_charisma19,feature_sudsy_polymeric_posteriority
    

This file has been truncated. [show original](<https://github.com/mizimno/numerai/blob/main/feature_mapping.csv>)

Numerai said that the new features aren’t exactly the same as the old features, so these are the closest matches. Features that don’t exist in the new data set are left blank.

The mapping is reverse engineered from the datasets themselves. I have no knowledge of the feature engineering Numerai did to create the features.

---

### Post #2 — **ml_is_lyf** | 2021-12-22 19:05 UTC

This is great, thanks! How did you determine this?

---

### Post #3 — **mic** | 2021-12-23 06:51 UTC _(reply to #2)_

The pairs were selected as those with maximum average correlation (averaged across eras) and a tie break if a feature was selected in multiple pairs. From memory, I think only one tie break was needed, for `charisma72`, that resulted in `feature_acerb_venusian_piety` being paired with its second choice of `charisma7` instead, which had nearly the same correlation on both fronts.

For validation I sampled a few to check it looked right, but you might want to check a pair or two yourself before you go to town with it.

---

### Post #4 — **mic** | 2022-04-11 01:47 UTC

Updated with mapping for v3 to v4.

[github.com](<https://github.com/miciasto/numerai>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0d71a9fe9dd60b21aec496f98e2df34fb3fb677d_2_690x344.png)

### [GitHub - miciasto/numerai](<https://github.com/miciasto/numerai>)

Contribute to miciasto/numerai development by creating an account on GitHub.

---

### Post #5 — **mic** | 2022-04-11 03:12 UTC _(reply to #4)_

sorry, just corrected some duplicated mappings, please re-download if using
