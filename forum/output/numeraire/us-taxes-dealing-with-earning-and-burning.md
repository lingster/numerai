---
title: "US Taxes dealing with Earning and Burning"
category: Numeraire
url: https://forum.numer.ai/t/us-taxes-dealing-with-earning-and-burning/6075
created_at: 2023-01-27T18:59:29.007000+00:00
last_posted_at: 2024-05-21T20:56:52.732000+00:00
posts_count: 5
views: 1079
tags: []
---

# US Taxes dealing with Earning and Burning

---

### Post #1 — **red_leader** | 2023-01-27 18:59 UTC

Curious how other people treat their earns/burns for tax reporting purposes. Do you take the net earns and burns (calculated using USD since each week its a different price) as earned income? Do you account them differently somehow and take it as earned income?

Do you treat it as a capital gain on the original token?

Something different?

For purposes of this question assume no buying or selling occurs I’m only interested in the tax effect of earning and burning.

---

### Post #2 — **dzheng1887** | 2023-01-28 18:42 UTC

I have done no research into this, but my best guess is that you can treat NMR coin appreciation like capital gains and earning and burning like dividends (regular income) when it occurs at the USD value of that time. I am thinking like in this scenario

$100 @ $10/NMR given 10 tokens staked 1/1/22  
earn 4 NMR tokens at $11/NMR on 1/8/22  
earn 6 NMR tokens at $10/NMR on 1/15/22  
burn 8 NMR tokens at $8/NMR on 1/22/22

As of 1/22/22, If you did no buying or selling, you would essentially have this much in earned income: 4x11 + 6x10 - 8x8 = $40

For the capital side,  
10 tokens depreciated from $10 to $8  
4 tokens depreciated from $11 to $8  
6 tokens depreciated from $10 to $8

You had to “sell” 8 tokens when it burns at $8. I think you can “identify” which coins you are trying to sell like stocks like when you sell a covered call that is exercised? Otherwise probably FIFO? So to max losses, you sell the 4 tokens bought at $11 and 4 tokens (lot of 6) bought at $10 for a loss of $12+$8 = $20. Otherwise, FIFO results in selling the 8 of the initial 10 tokens at $8 for a loss of $16.

In balance

10 tokens capital loss from $100 to $80 = $20  
4 token dividend (+$44) with capital loss from $44 to $32 = $12  
6 token dividend (+$60) with capital loss from $60 to $48 = $12  
8 token burn (-$64). Depending on which tokens you “choose” to sell, you realize the above capital loss.

Start: $100  
Income: +$40  
Capital Loss Realized: $12 + $8 = $20 (sell the lot of 4 and 4/6 lot)  
Capital Loss Unrealized: $24  
End: $96

Report the income of $40 and short term capital loss of $20. My best guess ![:confused:](http://forum.numer.ai/images/emoji/twitter/confused.png?v=12) I will also have to do this for my tax returns so I’d appreciate any further good advice for correct accounting or to minimize tax bill ![:pray:](http://forum.numer.ai/images/emoji/twitter/pray.png?v=12)

---

### Post #3 — **psyrex** | 2024-05-20 21:33 UTC _(reply to #2)_

[@dzheng1887](</u/dzheng1887>) \- did you manage to sort it out? curious what steps you took I am also trying to wrap my head around how to handle the earns and burns from staking

---

### Post #4 — **dzheng1887** | 2024-05-21 19:52 UTC

If you earned/burned, count it as other income by the approximate price on that day. If you want to be fancy, you can probably call it business income. There’s a box you should check “yes” too. Keep these amounts and dates as you’ll need it when you sell.

If you didn’t sell last year, then that’s all you have to do. If you did, you need to treat it as the usual capital gain or loss based on the value you sold the coin and the approximate value when you got the coins. I sold everything, so I am not sure what to do with partial sells. I asked the Oracle and it replied with this

> When reporting capital gains or losses for tax purposes to the IRS, you need to use a method that is allowed by the IRS and stick with it consistently for your records. Here are the options and some guidance on choosing the right one:
> 
> ### Methods Allowed by the IRS:
> 
>   1. **FIFO (First In, First Out)** : This is a common method where you sell the oldest coins first. It is straightforward and widely accepted.
>   2. **Specific Identification** : This allows you to specify which particular coins you are selling. You need to keep detailed records of each coin’s acquisition date and cost.
>   3. **LIFO (Last In, First Out)** : This is less commonly used for personal investments, and you should check with a tax professional or the IRS if this method is permissible for your specific situation.
> 


I used to do things by hand, but I use this software now. <https://www.freetaxusa.com/> It’s pretty handy. You have to pay for state returns. I’d still check some items against the actual IRS form documents though and see how it flows through the generated forms. They had this FAQ <https://www.irs.gov/pub/irs-drop/n-14-21.pdf>

---

### Post #5 — **psyrex** | 2024-05-21 20:56 UTC _(reply to #4)_

Thanks a lot! This is helpful!!
