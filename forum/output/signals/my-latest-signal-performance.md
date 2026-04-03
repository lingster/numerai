---
title: "My latest signal performance"
category: Signals
url: https://forum.numer.ai/t/my-latest-signal-performance/4290
created_at: 2021-10-07T23:30:54.336000+00:00
last_posted_at: 2021-10-08T15:27:56.054000+00:00
posts_count: 2
views: 823
tags: []
---

# My latest signal performance

---

### Post #1 — **autratec** | 2021-10-07 23:30 UTC

This is the second week received my signal performance, after numerai changed the duration rule from 1week to 4 weeks. Be honest, my return was dramatically reduced, even I have adjusted my prediction period in my model. I assume my old model only suitable for short term prediction rather than middle term.

I need to redesign my model, picking new indicators to start from scratch again.

Do you have similar experience ? Pls share your comments and suggestions.

---

### Post #2 — **jeremy_berros** | 2021-10-08 15:27 UTC

Yep same for me on one of my models which is a variation of Value Strategy that used to perform well on Corr4. That’s why I asked Liam to get the info on Corr4 after the change to Corr20.

If you are interested here is the query to compare Corr4 and Corr20:
    
    
    query {
      signalsUserProfile(username:"YOUR_MODEL_NAME") {
        latestRoundPerformances {
          correlation
          corr20d
          date
          day
          roundNumber
        }
      }
    }
    

You can use the GraphQL interface here <https://api-tournament.numer.ai/> or directly through the numerapi.

Hope that helps.
