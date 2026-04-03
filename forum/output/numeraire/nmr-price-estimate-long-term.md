---
title: "NMR price estimate (long term)"
category: Numeraire
url: https://forum.numer.ai/t/nmr-price-estimate-long-term/5800
created_at: 2022-10-28T08:10:19.744000+00:00
last_posted_at: 2022-11-06T16:39:16.907000+00:00
posts_count: 16
views: 2026
tags: []
---

# NMR price estimate (long term)

---

### Post #1 — **nyuton** | 2022-10-28 08:10 UTC

Hi,

I’ve been thinking about staking more on my models, but I wanted do some math to see in what range I should expect NMR in the coming years.

I go with some simple assumptions:

  * NMR can’t go to 0. If NMR is 0 (or too low) then data scientists leave and the metamodel degrades to the sample script ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) Numerai wouldn’t allow that as long as they generate profit from the fund.
  * NMR can’t go to a million either. On the long run Numerai will have to purchase NMR from the market. That means they cannot pay more for the NMR than what they earn with the fund. Best case scenario is, when they spend all their profit on NMR purchases every year and distribute it back to the participating data scientists. So the fund earnings set a cup in spending.



Of course the NMR price can widely fluctuate near term, but the calculations below give it some limits on the long run.

I share the table here.  
Obviously it contains some assumptions. Feel free the copy and modify the green fields as you see fit. The red ones are calculated fields.

Any opinion on this?

[docs.google.com](<https://docs.google.com/spreadsheets/d/1WMnT1Njmmxuxcd3NGFddp9G13c0WfYY-Zv3Jl3wrPMg/edit?usp=sharing>) [](<https://docs.google.com/spreadsheets/d/1WMnT1Njmmxuxcd3NGFddp9G13c0WfYY-Zv3Jl3wrPMg/edit?usp=sharing>)

### [NMR price estimate](<https://docs.google.com/spreadsheets/d/1WMnT1Njmmxuxcd3NGFddp9G13c0WfYY-Zv3Jl3wrPMg/edit?usp=sharing>)

This Sheet is private

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3dcb4d17ddb7dce420ba0bca2f779140fc5625b4.png)image1155×702 30.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3dcb4d17ddb7dce420ba0bca2f779140fc5625b4.png> "image")

---

### Post #2 — **dzheng1887** | 2022-10-28 17:12 UTC

Regarding the assumption on the first bullet, I don’t think it is 0% or 100% probability the hedge fund generates profits. It would depend on their market excess risk adjusted return which affects AUM and subsequent profit like you have in the sheet. So just something to be careful of.

In the Excel sheet, it may be helpful to have a parameter to vary the % amount the hedge fund would contribute to buying back NMR rather than assuming that the hedge fund and its owners will take no profits. But something interesting here that I just realized from this sheet is that there is a risk that the price of NMR increases to a point where the hedge fund cannot buy back the coins at a reasonable price. They actually would have incentive to keep the price somewhat depressed. I wonder if an equilibrium can be found here.

You can also probably make more of a range with very conservative and very optimistic parameters and have them side by side. The given sheet seems pretty optimistic.

  * $3B AUM - optimistic and assumes this strategy and operations with current AUM of about $100M (I am not sure?) will still work at $3B AUM
  * 12% annual return - seems reasonable in the case where the hedge fund succeeds. After taking fees, it’s about 8% annual return which is about what the market is for break even in the long run
  * 1% management fee - I think this is conservative and can probably increase this. For different funds, just take some fund weighted average for this if doing it roughly all in
  * 25% performance fee - maybe optimistic given the high-water mark. It’s unclear to me how it will all workout if the performance is ever down and there will be periods of much less reduced income, but perhaps reasonable enough in the long run. For each chunk of AUM, with the given performance, 25% comes from a constant 1% management fee and 75% from the performance fee
  * Cost of running the fund - currently approximately 1.5x cost increase for 30x AUM increase. I don’t know if that’s reasonable, but you can probably log scale it somehow to AUM
  * NMR distributed per year - this actually looks reasonable to project future NMR distributions based on today due to the effect of the payout factor assuming no change in modeling CORR/TC and payout multiples
  * backing out total staked NMR from the NMR distribution and expected return seems creative



I tried to put something together with these thoughts, but couldn’t really make much more progress. This seems very interesting though and promising.

At the current NMR price of $15, this framework will need $350M AUM and $7M costs and 100% profit for buyback for the price. Or about $500M AUM and $7M costs with 50% of profits for NMR buyback.

---

### Post #4 — **nyuton** | 2022-10-28 18:36 UTC _(reply to #2)_

Hi,

Thanks for giving it a thought. Any idea for improvement is welcome. I’m trying to make a case for further investment…

  * Management and Performance fees are given. See numerai.fund
  * AUM is 120M now, but it was ~0 a year ago. In 3-5 years 3B could be realistic, if the fund keeps up with the good performance. There are many worse funds with higher AUM.
  * Yeah, cost of running the fund is tricky. To be frank, I have no idea here, so I just picked a number. Your guess is at least as good as mine.
  * Certainly not all profits will be paid out for data scientist. 100% redistribution is kind of an upper limit.



What caught me in this calculation is the total stake amount given the expected return. 3.1M NMR is not much. There is 11M available. So it’s a reasonable question to ask, what happens with the rest and how it affects the price.

---

### Post #5 — **baare** | 2022-10-28 18:50 UTC

Hi,

There is another assumption you are making, namely that they have to buy NMR to pay out the rewards. I just took a quick look at CMC and there is only 54% of all NMR in public circulation. If they hold the other 46% - and that would be logical - they would not have to worry about this for a long time.

Does anyone have any detailed information on this?

---

### Post #6 — **dzheng1887** | 2022-10-28 18:51 UTC _(reply to #4)_

Yes, that 3.1M is a very interesting figure and it seems completely reasonable. Perhaps it’s just leeway that allows the hedge fund to adjust their multipliers to lever certain incentives.

I am not sure who would be willing to hold the 8.1M coins if the price has reached some long run equilibrium. Maybe just the hedge fund will store it and float out 500k onto the market?

For the cost of running a fund, I tried to see if we could find income statements for asset managers. I found a few, but not enough to fit some line between their total revenue or AUM and their operating expenses (and cogs?). Also, I doubt traditional funds will be close enough to numerai to be comparable so I gave up, but I feel it should be able to inform to within a factor of 10, like maybe numerai would be 1/2 the expense of another typical fund with $3B AUM. Just a very rough nearest neighbors approach with some benefits for being technologically efficieint.

---

### Post #7 — **dzheng1887** | 2022-10-28 18:59 UTC _(reply to #5)_

I wonder if the hedge fund doesn’t even hold any NMR they don’t buy themselves? Maybe all the payouts are based on the blockchain operations?

Maybe this will inform? <https://numer.ai/whitepaper.pdf> Sorry, haven’t done the work myself to help

---

### Post #8 — **nyuton** | 2022-10-28 19:08 UTC _(reply to #5)_

Sure, they are not buying any NMR now. But at some point in time they will have to, in order to keep the fund running.

---

### Post #9 — **greyone** | 2022-10-28 19:51 UTC

[NMRCirculatingValue - Google Sheets](<https://docs.google.com/spreadsheets/d/1JmhlXkOZNQCu0cNzFiTlgSSzaofIKg1LZtcXlnWemRA/edit#gid=0>) Adjusted model to ask what level of AUM would be needed to justify an NMR price where it would make sense for modelers to own 100% of NMR’s current circulating supply. Assumes 50% of profits would be distributed to NMR current supply and uses 15% capitalization rate.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a96054672580f8681f78108b86c40b9a8d71cbc1_2_690x360.png)image1213×634 67.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a96054672580f8681f78108b86c40b9a8d71cbc1.png> "image")

Assumes that instead of NMR payouts, all payouts would be in cash from Numerai’s HF profit stream.

---

### Post #10 — **nyuton** | 2022-10-28 20:33 UTC _(reply to #9)_

Interesting! Good approach!  
Wouldn’t it make sense to take the total staked amount instead of the circulating supply?  
They would distribute to the stakers only.  
The current staked amount is 1305991. It should increase in the future tough.

---

### Post #11 — **greyone** | 2022-10-28 21:28 UTC _(reply to #10)_

I can see that logic. But how about a modeler who, in that past, has been very successful and has earned a lot of NMR and he is now still holding but not staking anymore. Might not be fair for him.

---

### Post #12 — **joakim** | 2022-10-29 00:07 UTC _(reply to #8)_

Not necessarily. Once Numerai is profitable, and there’s some performance returns to speak of, they could gradually move away from compensating with NMR (so their treasury never runs out), and instead gradually distribute profits in USD (or ETH, etc) to models that contributed the most to returns? Why? They may not be allowed (by current regulation) to purchase their own token (I’m speculating)? We can though, and if profits are distributed based on how much NMR was staked on a model (times cumulative TC the past year perhaps), then demand (from the best data scientists; supply from speculators, hodlers, and bad modellers) to purchase NMR from the market will determine the price of NMR? Just thinking out-loud here a little bit.

Regarding cost of running the fund, hopefully the management fee can pay for most of it, eventually anyway.

---

### Post #13 — **dzheng1887** | 2022-10-29 02:49 UTC _(reply to #12)_

I think someone mentioned to me that one of the reasons the hedge funds needs to pay in NMR is due to regulations. Something like they can’t be responsible for our reasonable expectation of profit for our DS activities or we’ll be categorized as employees and need some certifications or something I dunno

---

### Post #14 — **nyuton** | 2022-10-29 09:41 UTC _(reply to #11)_

Why should Richard share the profit with anyone, who is not continously contributing to the fund? Past performances were paid for in the past…

---

### Post #15 — **dzheng1887** | 2022-10-29 15:17 UTC _(reply to #14)_

I think his argument for using all the NMR circulating for the DS staking is that perhaps that is the fundamental reason for anyone to even hold NMR. Somewhat trying to address your 3.1M to 11M shortfall in NMR stakes. In other words, the guy who won a lot of NMR would have not reason to keep holding on to it except for staking all of it.

But I’m all fuzzy about it, the discussion is not too clear to me why a result would be interesting and what conclusions we should be moving toward. But it does seem it should matter in some manner, just cannot pin it down, I guess maybe because I don’t even have a framework to comprehensively consider why people would hold nonperforming assets.

---

### Post #16 — **nyuton** | 2022-10-29 19:06 UTC _(reply to #15)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/f475e1/48.png) dzheng1887:

> just cannot pin it down, I guess maybe because I don’t even have a framework to comprehensively consider why people would hold nonperforming assets.

That’s funny, but true!  
Maybe ask all those bitcoin hodlers ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #17 — **dzheng1887** | 2022-11-06 16:39 UTC

I also had another random thought for AUM while I was chatting in rocketchat.

Perhaps one of the reasons they are developing numerai supreme is now the risk free rate is over 4%. Based on the market neutral monthly returns they posted, they have an annualized return of 8.4% and an annualized standard deviation of 6.7% which is an amazing sharpe when the risk free rate was more around 1-3% but less so with a 4% risk free rate. One can probably say the same about several other asset class too though.

I am not involved in the finance area at all, but I am curious if anyone else has any thoughts on how the current and projected fed funds rate will affect AUM and hedge funds in general? I would think it makes it a harder game. A simple idea is perhaps a large group of savers may just be okay piling their money into Treasuries and TIPs (I think there’s a limit on TIPs?) ? I would be curious how asset flows are looking. I think I remember seeing something on bloomberg showing flows out of mutual funds for some reason very vaguely blah blah I dunno
