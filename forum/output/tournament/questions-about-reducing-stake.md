---
title: "Questions about reducing stake"
category: Tournament
url: https://forum.numer.ai/t/questions-about-reducing-stake/2973
created_at: 2021-04-20T06:36:21.097000+00:00
last_posted_at: 2021-04-20T16:11:54.732000+00:00
posts_count: 4
views: 840
tags: []
---

# Questions about reducing stake

---

### Post #1 — **profricecake** | 2021-04-20 06:36 UTC

Hi all. I could use a little help understanding stake decreases.

For the purpose of easy discussion, let’s say I have 15 NMR staked on a model and I wanted to get 10 of that NMR back into my wallet so I can stake it on another model.

So I scheduled a -10 NMR stake reduction last week.

It went through. Now for round 259 the stake on the model in question has clearly been lowered by 10 NMR. Hurrah.

Of course some earnings rolled over from 255, so now the model’s stake for 259 is 6 NMR.

I understand that multiple rounds need to clear in order for that 10 NMR to get back into my wallet. The question is: what should I do for the next 3 weeks so that the 10 NMR actually gets there?

There remains a pending -10 NMR stake change set on this model. To my naive eyes, reducing a 6 NMR stake by 10 NMR would bring it to ZERO and that’s not what I’m intending to do. So I’m inclined to cancel the stake change. I’m guessing that Numerai’s default behavior for staked changes is to “let them ride” and in this case I’m looking for just a one-time 10 NMR reduction.

However, what will happen when round 256 resolves on Wednesday? That round still has a stake of approximately 15 NMR. If I understand correctly, any payouts from 256 will roll into 260, but not the stake itself. Is that correct? In which case I should for sure cancel the change.

But if the stake value from 256 is rolled over into 260 along with the payout, then I absolutely need to leave that -10 NMR change in place for another 3 weeks. I don’t think this is right, but it’s not immediately clear from the docs.

The algorithm to compute the stake in round Y seems to be this:
    
    
    stake(Y) = payout(Y-4) + total_stake(Y-1) + pending_stake_change
    

If that’s correct, then my 10 NMR reduction in round 259 means that round 260 should be the newly-lowered stake plus whatever payouts come from 256.

Is that right, and therefore I should cancel this week’s stake change so that I don’t pull out all the stake from this model?

I tried looking to stake increases thinking they might help me understand this decrease question. But to no avail. With stake increases, you schedule an increase of some NMR, that NMR leaves your wallet and suddenly appears on the model for the next scheduled round. It’s very clear. And the NMR is never in limbo.

In the case of a decrease, however, that 10 NMR I pulled out (or am trying to pull out) does not immediately go into my wallet. I get that it takes some time to get out of the tourney, but there’s no obvious indicator (like in my wallet) which says “on this day, your wallet is scheduled to gain this much NMR assuming you don’t burn it all first”. I’d like to log that as a feature request because the only indication that I have any NMR slated to exit the tourney and enter my wallet is the negative delta in stake for this model between rounds 258 and 259. And I think it should be made much more clear.

Thanks in advance to anyone who can help clarify this for me.

prc

---

### Post #2 — **wigglemuse** | 2021-04-20 14:18 UTC

Don’t do anything, and you’ll get your 10 NMR in your wallet eventually (unless it burns first). (And it actually should tell you the date on the stake change dialog if you bring it up – BUT DON’T CHANGE ANYTHING IF YOU DO.)

This is why having no stake management is so maddening. Let’s say you want to increase your withdrawal, or have one every week – can’t do it without cancelling and starting over. Even if you only have one model, it makes sense to stake it with multiple times over several slots just so you can do increases/decreases with shorter time-frames than 5 weeks. (i.e. you can withdraw on one slot a week, or change your mind on that one without ruining some other withdrawal 3 weeks in, etc.)

---

### Post #3 — **profricecake** | 2021-04-20 16:05 UTC _(reply to #2)_

Thank you [@wigglemuse](</u/wigglemuse>). This is starting to get a little clearer.

You’re right - in the “manage stake” popup window, I can see an “effective from” date (when the reduction first applied) and a “releasing on” date. And there are exactly 4 weeks between those two dates. Should I assume then that once my “releasing on” date is hit, the NMR will hit my wallet and there will be no further stake change on that account (assuming I don’t change it)?

Out of curiosity, what happens if I do cancel the change? Will the stake bounce back up for the next round to the level it was at prior? And there will just be this little blip for one tourney round where the stake was 10 NMR lower?

Also: what happens if I cancel my change but then set a new stake reduction of, say, 5 NMR instead of 10? Will that take a full 4 weeks to go through or will it realize that I’ve already pulled 10 NMR for one week and that it should therefore only take 3 weeks?

Let’s assume you want to pull 10 NMR from the tourney weekly. If I understand correctly what you’re saying here, would that require having 4 models, each with a stake reduction of 10 NMR but each staggered 1 week after the other? Do I have that right?

Thanks again.

---

### Post #4 — **wigglemuse** | 2021-04-20 16:11 UTC

Yeah, as soon as you cancel it is like you never did it (going forward). So if you cancel and that’s it, your stake will go up 10 NMR for the next round. There is no “changing” your stake adjustment – you cancel and start over – takes another 4 weeks. I think it even takes 4 weeks if you haven’t been submitting for the last month, which makes no sense since there are no rounds to resolve for you. Basically current state of stake management is absurdly primitive and we are way past due just to get to the acceptable minimum functionality…
