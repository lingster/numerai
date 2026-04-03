---
title: "Signals Diagnostics Update"
category: Tournament
url: https://forum.numer.ai/t/signals-diagnostics-update/6130
created_at: 2023-02-13T20:55:19.412000+00:00
last_posted_at: 2023-02-13T23:01:10.358000+00:00
posts_count: 3
views: 627
tags: []
---

# Signals Diagnostics Update

---

### Post #1 — **slyfox** | 2023-02-13 20:55 UTC

**FNCv4 bug fix**  
We have identified a subtle bug in FNCv4 scores in the Signals Diagnostics tool.

The [FNCv4 calculation](<http://forum.numer.ai/t/new-signals-targets/5853>) is supposed to pre-neutralize your predictions against “all of the factors and features that the target_20d_factor_feat_neutral target is neutral to” before calculating correlation with the target. Specifically, it is supposed to pre-neutralize against all of the V4 features (which is a superset of V2 features, minus the dangerous features). The previous implementation of FNCv4 incorrectly pre-neutralized against V2 features minus the dangerous features only but not the full set of V4 features. The fix that we just rolled out on 2023-02-09 now correctly pre-neutralizes against the full set of V4 features.

To be clear, this bug only applied to Signals Diagnostics and not live scoring. Live scoring of FNCv4 has always been correct.

We have not and will not backfill this fix to previous diagnostic results. Instead, we recommend that you re-run any diagnostics before 2023-02-09.

We apologize for any inconvenience caused. Please contact [@chanes](</u/chanes>) if you have any questions.

**Unification of live and diagnostics scoring**  
The root cause of the FNCv4 bug above is that diagnostics and live scoring did not share the same code, so it was possible for them to diverge.

To fix this issue permanently, we have unified the code used for live scoring and diagnostics. So we don’t expect this type of bug to appear ever again.

**Misc upgrades to the diagnostics backend**  
As part of the bug fix above, we have also thoroughly audited and rebuilt parts of the Signals Diagnostics backend data pipelines. Many small improvements and clean up in this area have been made, including better ticker mappings.

---

### Post #2 — **richai** | 2023-02-13 21:58 UTC

what? isn’t FNCv4 neutral to v4 features only as the name would suggest? why would we neutralize by v2 as well? this seems wrong.

---

### Post #3 — **slyfox** | 2023-02-13 23:01 UTC _(reply to #2)_

Apologies for the confusion, I have edited the original post to be more clear. The key thing to clarify here is that V4 features is a superset of V2 features.

Previously, diagnostics incorrectly only pre-neutralized to V2 features. After the fix, diagnostics now correctly pre-neutralizes to the full set of V4 features (which includes V2 features).
