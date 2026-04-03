---
title: "Daily Tournament - Update #1"
category: Tournament
url: https://forum.numer.ai/t/daily-tournament-update-1/5817
created_at: 2022-11-03T21:56:56.973000+00:00
last_posted_at: 2023-02-10T15:55:38.886000+00:00
posts_count: 30
views: 3554
tags: []
---

# Daily Tournament - Update #1

---

### Post #1 — **slyfox** | 2022-11-03 21:56 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fad111be2ae66b1fa374fbd740b59dcb92a7469f_2_690x365.png)image1380×730 109 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fad111be2ae66b1fa374fbd740b59dcb92a7469f.png> "image")

**Daily tournament adoption**  
It has only been a week since the [launch](<http://forum.numer.ai/t/daily-tournaments/5766>) of the first daily round and we have already seen some great adoption.

In terms of staked models, 34% of Numerai Tournament and 20% of Numerai Signals are now submitting daily. In terms of total NMR staked, 44% for Numerai Tournament and 32% for Numerai Signals.

To everyone who has started submitting daily - great job and thank you! To everyone else - please let us know if there is anything we can do to assist you.

**Priorities - Stabilization then Payouts**  
Our top priority now is to stabilize the daily tournament system. Many you have experienced issues with our data and submission APIs over the past week. Thank you for your bug reports and patience with us as we get these issues resolved.

Once the system has stabilized, we will look to roll out payouts for the new daily rounds. We have gotten both the supportive and critical feedback on the proposed payout system and we are working to release an updated rollout plan with details soon.

**Weekend round scheduling changes on Nov 12**  
Starting on Nov 12, Saturday rounds will open 5 hours earlier on Saturday 13:00 UTC instead of 18:00 UTC, and the deadline will shift 30 minutes earlier on Monday 14:00 UTC instead of 14:30 UTC. For those of you on Compute, your models will be triggered as soon as the data is ready at this earlier open time.

And as a reminder, the open and close times of rounds are subject to delays based on our data vendors and may also change over time as we improve the speed of our own pipelines. The best way to make sure your model pipelines handle these changes is to integrate with Compute and just rely on our systems to inform you of when the data is ready.

---

### Post #2 — **gbrecht** | 2022-11-04 07:38 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/da6949/48.png) slyfox:

> To everyone else - please let us know if there is anything we can do to assist you.

my blocker to switch all my models (and staking any) to daily submission is int8 data support for compute-light.

---

### Post #3 — **kreator** | 2022-11-04 17:05 UTC

In order to join the daily format quickly, I would need a submission window of 90-120 min …

---

### Post #4 — **taori** | 2022-11-08 10:52 UTC

The main reason I do not submit daily rounds is disappointment. Instead of making daily tournaments appealing due to a higher potential earning, Numerai decided to take the other direction and make the weekly tournament less remunerative (70% of the current payout) so that users must do more to get almost the same. I do not like this approach at all.

---

### Post #5 — **wigglemuse** | 2022-11-08 12:50 UTC _(reply to #2)_

What’s the problem with int8? Can’t you download any dataset you want from compute?

---

### Post #6 — **psyrex** | 2022-11-08 14:55 UTC

Any update on accepting delayed submissions automatically for D+1? I have a few models which take way longer and I think this would really help/motivate me to participate in daily rounds.

---

### Post #7 — **mrotsdma** | 2022-11-09 14:28 UTC

I am seeing an error for my daily submissions on numerapi 2.9.4

> 2022-11-09 13:38:07,147 ERROR numerapi.base_api: You must provide predictions for the current live IDs. Make sure you are using the latest live data.

Even though i am downloading round 351 tournament data.

> Downloading numerai_tournament_data_351.parquet ⠙

Is anyone facing this issue as well?

---

### Post #8 — **shatteredx** | 2022-11-09 14:44 UTC _(reply to #7)_

You need to download numerai_live_data.parquet instead. numerai_tournament_data only gets updated weekly.

---

### Post #9 — **autratec** | 2022-11-11 01:44 UTC

i am pretty confused with all impacts after daily tournament started: no more daily/monthly/annual gain. weekly submission result was disconnected. no daily submission return estimation, etc. not sure how soon every will be back to normal.

---

### Post #10 — **objectscience** | 2022-11-11 03:13 UTC _(reply to #9)_

Pretty sure all the functionality will return, it’s just going to take a little bit. The jump to daily put a massive load on the data-base. I think once they get things optimized we’ll see that data reappear.

---

### Post #11 — **pschork** | 2022-11-12 07:00 UTC _(reply to #9)_

We turned off returns because we thought daily rounds might be polluting the numbers (they were not) and the current returns numbers are not easily verifiable from the outside. We are doing some more validation before re-enabling (soon).

The current Numerai and Signals returns calculations live in separate pipelines with their own bespoke implementations. The code is complex and hard to debug because it essentially boils the ocean from the beginning of time re-simulating every tournament scoring change, recalculating every payout, multiplier change, etc to derive returns.

Returns will return soon, and I will publish an accompanying worksheet explaining how users can audit/verify 1d, 3mo & 12mo returns using Excel themselves.

Thanks for your patience.

---

### Post #12 — **gbrecht** | 2022-11-23 17:09 UTC _(reply to #5)_

[@wigglemuse](</u/wigglemuse>) You can in compute-heavy. You cannot in compute-light. That is what I desire. I have been complaining about it in all the channels (RC, the Trello, now here) without any success so far.

---

### Post #13 — **wigglemuse** | 2022-11-23 17:37 UTC _(reply to #12)_

Hmmm…makes no sense to me, but I guess I don’t understand it. You’ve got an environment right, can’t it just do any arbitrary internet (and therefore api) call you want? If I can download int8 outside of compute why can’t you do it inside? What is actually stopping you?

---

### Post #14 — **gbrecht** | 2022-11-24 12:49 UTC _(reply to #13)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/2708_2.png) wigglemuse:

> You’ve got an environment right 

no, in compute-light you do not have an evironmanet, but you deploy a pickled model file, the version of data (v2,3,4) and the list of features the model expects to the numerai endpoint. The rest is handled by numerai.

The models predict method is called during live with a pd.DataFrame of the data. That’s it.  
That being said, I could of course start my predict method by ignoring the passed data, creating an API link and downloading the data. Apart from technical issues (can the script write to where it is running??) that completely defeats the compute-light goal of maximum integration so what I am asking for is to have another deployment parameter for int8 or float data.

---

### Post #15 — **wigglemuse** | 2022-11-24 15:10 UTC _(reply to #14)_

Yeah, ok, pretty limited. I’m not saying they shouldn’t have int8 (and I’d need a whole lot more than that to make compute workable), but seems like you could get around it in the meantime as well. Can you just multiply the data * 4 to convert to int or does that cause memory issues?

---

### Post #16 — **autratec** | 2022-11-25 05:38 UTC

any idea when the staking for daily tournament will be started ?

---

### Post #17 — **gbrecht** | 2022-11-25 10:11 UTC _(reply to #15)_

thank you for that tip. That is a reasonable workaround. I will try to do it that way!

---

### Post #18 — **develuse** | 2022-11-25 13:34 UTC

When does the Friday round opens? I am getting ‘ValueError: Current round not open for submissions’

---

### Post #19 — **develuse** | 2022-11-25 13:41 UTC _(reply to #18)_

see it just opened, must be more patient. missing indication in gui

---

### Post #20 — **jxtrbtk** | 2022-11-27 10:19 UTC _(reply to #16)_

up ! I think this would be good to give an end this in-between period…  
Please start daily payouts !

---

### Post #21 — **autratec** | 2022-12-01 01:13 UTC

Recognized that daily submission timeslot was changed. Like yesterday, the notification email was received at 1:43AM (GMT8), comparing with original schedule - 9PM (GMT8).

May i know this is temporary arrangement for test or there will be new fixed timeslot for data submission ?

---

### Post #22 — **liborty** | 2022-12-01 02:00 UTC

MAJOR BUG REPORT:

How come that `numerapi check-new-round --hours 1` returns 0 , except at the critical times after 13:00 UTC, when we need it to test for 1 to know when to start processing? But, then it just generates a whole stack of errors, making it useless and the daily tournaments opening times undetectable. It has been like this for the last two tournaments. Combined with the fact that you keep changing the opening times, it makes the daily tournaments totally impractical to participate in.

If you want us to be detecting the opening times, you must provide a functioning CLI test, not something buggy like this. If you are doing this to force us into using ‘compute’, then I am out of here. I am not willing to struggle with the complexities of AWS and pay for the ‘privilege’ when I have a perfectly functioning automation of my own. Or at least I had one …

---

### Post #23 — **kayeffnumeraitor** | 2022-12-01 08:15 UTC _(reply to #22)_

Yesterday the data vendor was late, afterwards Numerai encountered an issue, delaying the opening time significantly. However, this scenario was already foreseen which is a major reason why Numerai pushes for “predictions on demand” rather than scheduled submissions.

What you can do is having an email listener on a low power computer waiting for a round open mail and starting your main computer via wake on LAN and running your submission script. For the past month, this has been my setup and worked perfectly. If there is interest I can clean up the code and put it on github.

---

### Post #24 — **liborty** | 2022-12-01 13:38 UTC _(reply to #23)_

See the latest version of my Bash script which I believe solves this problem:  
[http://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806/2?u=liborator](<http://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806/2>)

---

### Post #26 — **autratec** | 2022-12-08 04:58 UTC _(reply to #25)_

here is the telegram channel created to publish daily submission notification:

![](https://telegram.org/img/website_icon.svg?4) [Telegram](<https://t.me/numeraidaily>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f1be713231a12acdfae4d71909ac80c166f67896.jpeg)

### [Numerai Daily](<https://t.me/numeraidaily>)

Provide open notification of NUMERAI daily prediction submission window.

---

### Post #27 — **quantized** | 2023-01-07 12:11 UTC

Any updates on payout factor for daily rounds? It’s been several months now.

---

### Post #28 — **jxtrbtk** | 2023-01-27 09:44 UTC _(reply to #27)_

up! I’d like also to know when the daily payout will start. Even a raw estimate. Could we have an update ? Is there one somewhere ?

---

### Post #29 — **taori** | 2023-01-27 14:43 UTC

I hope they deliver the account level staking feature before they start with the daily payout.

---

### Post #30 — **kayeffnumeraitor** | 2023-02-10 11:41 UTC

So it has been 3 months now since daily rounds are active and almost the same timespan since this update, what is the status now? I turned my daily pipeline off for now to save some power costs, as there is still no payout whatsoever.

Are there still stability issues? Have priorities shifted? Are the preliminary results from daily MM predictions worse than expected?

It would be great to have a second update post like this one, even if it is just saying “We are still working on ABC but have troubles with XYZ”.

---

### Post #31 — **wigglemuse** | 2023-02-10 15:55 UTC _(reply to #30)_

Daily staking presents some enormous complications. I suspect we’ll get some updates at the fireside next week.
