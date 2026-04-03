---
title: "Staking and numerapi issues/questions"
category: Feedback
url: https://forum.numer.ai/t/staking-and-numerapi-issues-questions/1757
created_at: 2021-02-12T23:27:27.374000+00:00
last_posted_at: 2021-02-14T09:05:18.107000+00:00
posts_count: 4
views: 1188
tags: []
---

# Staking and numerapi issues/questions

---

### Post #1 — **profricecake** | 2021-02-12 23:27 UTC

Hi there.

I’m trying to do some stake-related calculations using numerapi inside python and I’m running into a few issues.

First, there seems to be a bug with `get_stakes()` in that it doesn’t operate as advertised (indeed, it crashes). I already [posted an issue on github](<https://github.com/uuazed/numerapi/issues/38>) about that one.

I found two other (functioning) API calls that seem to report stake information. The first is `stake_get()` and it runs like this:
    
    
    napi.stake_get("chunkyricecake")
    '51.190740969723066000'
    

The second is `public_user_profile()` which runs like this:
    
    
    napi.public_user_profile("chunkyricecake")["totalStake"]
    '50.014825201822514796'
    

Note the different values. Which is correct?  
The latter number is what’s reported by the numerai UI:  


[![Screen Shot 2021-02-12 at 3.20.14 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3058b8eb68982680a69d4346ea56f425f15dc78a.png)Screen Shot 2021-02-12 at 3.20.14 PM301×119 5.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3058b8eb68982680a69d4346ea56f425f15dc78a.png> "Screen Shot 2021-02-12 at 3.20.14 PM")

And it’s also what appears as the stake for the current round (250):  


[![Screen Shot 2021-02-12 at 3.20.28 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7ab454f11f82430b9b24dfa8b17a9e79b86b1dcf.png)Screen Shot 2021-02-12 at 3.20.28 PM301×190 7.25 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7ab454f11f82430b9b24dfa8b17a9e79b86b1dcf.png> "Screen Shot 2021-02-12 at 3.20.28 PM")

Questions:

  1. What does the output of `stake_get()` mean?
  2. Why do the numbers from `stake_get()` and `public_user_profile()` differ?
  3. Why do neither of these stake measures (nor the value displayed under “NMR Staked” in the UI) reflect the total stake across all the four current rounds?
  4. Once `get_stakes()` is fixed, should there really be three ways of getting stake information and if so shouldn’t they all return consistent results?



I realize my post touches on API questions and also on the whole complex business of staking. I’m eager for input from anyone who can help me understand either better!

Thanks so much in advance.

PRC

---

### Post #2 — **uuazed** | 2021-02-13 19:59 UTC

In general, numerapi is developed by the community (mainly me) and it’s meant to simplify the interaction with numerai’s API for Python users. The numerai guys are taking care of the data, what is available etc. Numerapi interacts with the graphql backend and provides all relevant information via a python interface. In case you are curious, you can browse their API on <https://api-tournament.numer.ai/>

Regarding your questions

  1. earnings are currently automatically added to your stake. `stake_get` includes your earnings from not fully resolved rounds. So this value is changing with every daily score.
  2. in contrast, the stake value in public_user_profile does not contain those future earnings. Thus, this is the NMR you’ve staked
  3. Summing up those stakes doesn’t make sense. It’s the same NMR that is staked. For example you staked around 50NMR, not 200 (4 x 50)
  4. get_stakes was a left-over, which I removed in the latest numerapi release. Thanks for reporting! (In the past, users needed to stake every round - meaning stakes did not roll-over to the next round. That get_stakes function allowed to get your stakes per round. This is no longer relevant and numerai is no longer providing that information)



I hope that helps you at least a bit.

---

### Post #3 — **profricecake** | 2021-02-14 08:47 UTC _(reply to #2)_

This was very helpful - thank you. I learned a lot about the graphql approach by digging into the numerapi code and those docs.

Still, I predict that the choice to include expected earnings in one stake value and not in the other will be just as confusing to future users as it is (or, was) to me. Might it make more sense to offer an optional keyword param like `include_future_earnings` to any and all stake calls, and/or always include the future estimated earnings as a second returned value? In other words, anytime you ask for stakes you get back two values instead of one, perhaps `committed_stakes` and `estimated_earnings` or something similar?

Curious for your thoughts, [@uuazed](</u/uuazed>) !

PRC

---

### Post #4 — **uuazed** | 2021-02-14 09:05 UTC _(reply to #3)_

The keyword approach won’t work in that case, because I don’t control what the numerai graphql backend returns. So returning two values for stakes would be a task for the numerai guys to implement. Once the information is there, we could adjust numerapi accordingly.  
However, I’ll update the documentation to make it more obvious what is going on.
