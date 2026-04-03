---
title: "Numerai NPV investment analysis"
category: Tournament
url: https://forum.numer.ai/t/numerai-npv-investment-analysis/5543
created_at: 2022-06-30T17:15:00.901000+00:00
last_posted_at: 2022-07-01T14:55:04.746000+00:00
posts_count: 5
views: 797
tags: []
---

# Numerai NPV investment analysis

---

### Post #1 — **dzheng1887** | 2022-06-30 17:15 UTC

Hey so nice coin price jump today, but that’s not the point of this post.

I found something very interesting. And perhaps this is how I should initially be thinking of this. In the recent downturn last month, I considered if I should be selling and to get out of this (got in over my head), but I cannot do so after this analysis even with the coin price at $7. I was wondering if anyone else has insights in this.

But essentially, if we think of the numerai as a dividend, where we sell our earnings each week, the net present value of that stream of payments (assuming 2% return per week, 20% discount rate, and stable coin price) is 4.5x your initial investment. So putting in $1000 today is like converting it to $4500 in NPV terms if you are willing and able to hold for the rest of your life. So even when the NMR coin was $7, it’s still worth 4.5x times as much for me to keep doing this for the hedge fund.

I did some sensitivity analysis (randomly mess with parameters) and found that if you apply a 40% discount rate and the coin price halves, when you need to sell each week, then it about breaks even. That seems to be on the extreme side, but of course you have some liquidity issues too by having this stream of payments rather than the initial cash investment up front.

In light of this, why are people not investing more into this? Perhaps there is some concern if the hedge fund/coin will be viable in the future (huge discount rate?), maybe the payout factor makes any more investments less attractive (reduced weekly return?). There is concern your model will not do well (reduced weekly return?). Those are definitely some additional factors to consider.

I am curious if others have went through this NPV cash flow scenario and what general parameters and processing they are modeling for this activity in the future.

---

### Post #2 — **yxbot** | 2022-06-30 18:49 UTC

nice analysis - I didn’t do such an analysis but had kind of this projection in my head, only that I am not quite buying into “the divident for life” scenario, yet ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

As to why are people not investing more into this, I have come across the following:

  * not aware of Numerai
  * not confident about the ML aspect of this
  * people get into this while NMR was 30+ USD, and find it demotivating after 75%+ drawdown
  * quite a lot of poeple into altcoin are not in it for the long run - i.e. mainly for short term trading and speculation
  * Crypto/Defi or just numerai itself sounds to risky even for good ML people - I find at least in my network large of portion of DS/ML people are risk averse, like why do I risk it given I am already with a well-paid job?
  * alternative games for probability based profit, such as stock/fx trading or sport betting



IMO, price at below $10 would be great entry point into this - but I think most people don’t want to “catch a falling knive”?

---

### Post #3 — **dzheng1887** | 2022-06-30 20:32 UTC _(reply to #2)_

Thank you for your thoughts. I agree with the “dividend for life” scenario. A lot still needs to happen for that to occur which I am not even sure about, which is also another reason a 40% discount rate doesn’t seem _too unreasonable_ to me. Like trying to price in bankruptcy for levered companies. Regarding the other bullets, yes, I also agree there is likely a bunch of behavioral aspects (we not really the perfectly rational agent traditional finance/economic academics like to promote) that cause some reluctance to participate more fully.

I would still like to hear, however, if anyone else has “rational” reasons to not engage in this competition in terms of NPV cash flow. For example, I am sure someone will throw in some idea of marginal decreasing utility and consumption which is also not really in my purview for my own reasons. Just curious if others, for example, are using a significantly different discount rate, expect another level of returns, or are just pricing in some NMR value deterioration in the coming years.

Like I was trying very hard to convince myself to stop doing this tournament a few weeks ago, and I just can’t. I even had to stop myself from participating more when the NMR coin dropped to $7.

---

### Post #4 — **lothlorien** | 2022-07-01 08:46 UTC

Like [@yxbot](</u/yxbot>), I had this NPV roughly in my mind - good job making it explicit and finding some break-even parameter settings!

For me, the volatility of the payouts is not so much an issue any more (I can quantify it quite well), but the volatility of the NMR price is a problem because I find there is much less basis for saying anything about the future price levels and changes therein. [@dzheng1887](</u/dzheng1887>) you describe a further halving of the coin price as “on the extreme side”, but it did halve in recent history, and then halve again, and then again! I also vaguely remember a time when NMR was 2 bucks, so in my mind, the future price could be all over the place.

Even with the price uncertainty, this Numerai thing has been my main investment (and source of income), and the only reason I’m not investing more is that I now have a different investment avenue with even higher expected returns and lower volatility.

---

### Post #5 — **dzheng1887** | 2022-07-01 14:55 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/l/71e660/48.png) lothlorien:

> ncertainty, this Numerai thing has been my main investment (and source of income), and the only reason I’m not investing more is that I now have a different investment avenue with even higher expected returns and low

Congratulations on your investment avenues! Could you link the model you are using for your Numerai? I am curious to see what you find sufficient to rely on for income.

I agree the price is very volatile and it can half multiple times. But only halfling is an extreme, but possible, down side case in my mind. For example, if the coin price persisted at $2 for multiple years. At that point, I also imagined the hedge fund would start considering DS attrition.

For sure, this is not really possible to predict with certainty any fundamental shift in NMR pricing, but just to illustrate that there could be upsides as well. Like the (random?) increase in NMR price was a pleasant surprise this week too. If I had to guess (based on 0 analysis on my part and my nonexistent TA knowledge), maybe these crypto charts are following some sort of TA processed by machines because I am also not sure what else you can do with these except for price movements.
