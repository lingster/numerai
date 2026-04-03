---
title: "Signals Neutralization?"
category: Signals
url: https://forum.numer.ai/t/signals-neutralization/3569
created_at: 2021-06-09T15:57:35.862000+00:00
last_posted_at: 2021-06-10T11:31:03.270000+00:00
posts_count: 2
views: 1353
tags: []
---

# Signals Neutralization?

---

### Post #1 — **gammarat** | 2021-06-09 15:57 UTC

I’m uncertain about the Signals Neutralization process, which is described [in the documents here](<https://docs.numer.ai/numerai-signals/signals-overview#neutralization>).  
particularly this bit:

> Every signal uploaded to Numerai Signals is neutralized **before** being scored.  
>  [bold mine]

That neutralization is apparently the removal of the orthogonal projection of Numerai’s prediction from the user’s prediction. (This is something that confused me earlier, until I clued into the fact Numerai is not really working with _signals_ , but with _predictions_ based on signals. A slightly different kettle of fish).

Anyway, I wanted to see what the effect of this was, so I created a really simple model. In this model there’s four components: a “true” set of stock returns, a “user” predicted set of returns, a “Numerai” set of predicted returns, and a “neutralized” set of returns, neutralized according to what I think they are doing according to the documents. **I would be very happy to have this understanding corrected if it is wrong**

The setup is deliberately cooked so that the user model starts off better than the Numerai model in the sense that while both give perfect scores on Spearman correlation (they are both monotonically increasing with the true data), the actual predictions for the user set are closer to the true set by a factor of about three.

Below is a plot of what I am talking about, which might be helpful:  


[![Neutralize](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4b09f191289d72027cabd699845aabf792cd2422.jpeg)Neutralize560×420 21.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4b09f191289d72027cabd699845aabf792cd2422.jpeg> "Neutralize")

~~(**note** \- this is a corrected version of the plot shown earlier)~~  
(the original was better, so I put it back in.)

Note that the neutralized model is no longer monotonic with respect to the true model, which destroys the Spearman correlation. As mentioned above, the Spearman correlations for the user model and the Numerai model were both 1; after neutralization the user model now has a Spearman correlation to about **-0.5**

Now I do hope I’m wrong in this, so if someone can correct my understanding, please do! If I’m not, then perhaps Numerai might want to look into doing something different, like doing the neutralization after, rather than before, the correlation. Though I haven’t worked through that yet. Perhaps something along the lines of the MMC in the Tournament would work.

NB. I hate arithmetic. But the issue still stands, neutralization prior to correlation can propagate error from the Numerai model into the the user model at the user’s expense.

---

### Post #2 — **chaotician** | 2021-06-10 11:31 UTC

You might want to check out the discussions here: [Feature Request – Publish Metamodel Feature Exposures - #8 by chaotician](<http://forum.numer.ai/t/feature-request-publish-metamodel-feature-exposures/3523/8>)
