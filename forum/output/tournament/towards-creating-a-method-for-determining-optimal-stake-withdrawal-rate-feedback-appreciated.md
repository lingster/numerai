---
title: "Towards creating a method for determining optimal stake withdrawal rate (feedback appreciated)"
category: Tournament
url: https://forum.numer.ai/t/towards-creating-a-method-for-determining-optimal-stake-withdrawal-rate-feedback-appreciated/2751
created_at: 2021-04-08T22:35:28.535000+00:00
last_posted_at: 2021-05-08T23:16:34.980000+00:00
posts_count: 13
views: 1397
tags: []
---

# Towards creating a method for determining optimal stake withdrawal rate (feedback appreciated)

---

### Post #1 — **no_formal_agreement** | 2021-04-08 22:35 UTC

With the staking cap close to being reached I believe that a lot of people will probably want to convert from a constantly compounding stake to a income generating stake (ie withdrawing a certain percentage each period of time). The goal here would be to come up with a optimal percentage to unstake every week such that you maximize the time-discounted net present value of the expected geometric mean of all future nmr payed out by unstaking it. Geometric mean is being used instead of the regular mean since rewards are multiplicative rather than additive and also since it is the metric used for Kelley Criterion. Hopefully coming up with a good strategy for this type of stake will prevent people from just going all in or all out on there stake based on the payout reduction. I anticipate that as the payout reduction increases, the optimal withdrawal rate will increase, which will create an equilibrium that prevents the total amount staked from getting too high while also keeping participants with a satisfactory payout. To that end I am going to be showing my progress on this publicly to get feedback from everyone.

Here is my current plan for developing the optimal stake withdrawal strategy:

1 Create method for simulating expected future returns  
2 Create dataset of 1000s of simulated returns timeseries over course of several years using method from 1  
3 Test different withdrawal rates on the timeseries dataset thereby creating a timeseries of ‘payments’  
4 Calculate time discounted net present value of the payment timeseries  
5 Determine optimal withdrawal rate by seeing which rate has the highest geometric mean net present value

For step one I want to figure out what type of probability distribution to sample from to simulated expected future returns. I can pull several participant scores from the API, mix them together and compare them to different types of probability distributions. Here is my current testing regarding what type of distribution to use:
    
    
    import numerapi
    import pandas as pd
    import numpy as np
    from scipy import stats
    
    
    #returns_distribution_test
    
    
    api = numerapi.NumerAPI()
    models = ['integration_test_7','no_formal_training','sorios','themicon','arbitrage','uuazed','niam','cryptoquant','no_formal_agreement','leverage','uuazed2','bookofillusions','era__mix__2000']
    
    
    user_df = pd.DataFrame(api.daily_submissions_performances("themicon")).groupby("roundNumber").last()
    
    
    all_corrs = []
    for i in range(len(models)):
        user_df = pd.DataFrame(api.daily_submissions_performances(models[i])).groupby("roundNumber").last()
        user_corrs = user_df.loc[:,"correlation"]
        user_corrs = user_corrs.dropna()
        user_corrs = user_corrs.values
        all_corrs = np.concatenate([all_corrs,user_corrs])
    
    mean = np.mean(all_corrs)
    
    std = np.std(all_corrs)
    
    random_gauss = np.random.normal(mean,std,len(all_corrs))
    random_lognorm = np.random.lognormal(np.log((mean**2)/(np.sqrt(mean**2+std**2))),np.sqrt(np.log(1+(std**2)/(mean**2))),len(all_corrs))
    random_laplace = np.random.laplace(mean,2**-0.5*std,len(all_corrs))
    
    print('Gaussian distribution similarity scores')
    print(stats.ks_2samp(all_corrs, random_gauss))
    
    print('log-normal distribution similarity scores')
    print(stats.ks_2samp(all_corrs, random_lognorm))
    

Here I use the ks statistic to compare how similar the returns from several models are to different distributions that all have the same mean and standard deviation. The output from this code is:
    
    
    Gaussian distribution similarity scores
    Ks_2sampResult(statistic=0.03429602888086647, pvalue=0.5255367523651229)
    log-normal distribution similarity scores
    Ks_2sampResult(statistic=0.2635379061371841, pvalue=3.355471473673669e-34)
    laplacian distribution similarity scores
    Ks_2sampResult(statistic=0.07490974729241878, pvalue=0.0037335231882827612)
    

The output shows that the gaussian distribution is by far the most similar to distribution of the payouts from participants. This is a little surprising as I would expect the ‘heavy-tailed’ laplacian distribution to be closer. Before I continue I would appreciate some feedback, both on my strategy and on my current testing.

Thanks in advance.

**edit fixed formatting

---

### Post #2 — **aanastasov** | 2021-04-08 22:50 UTC

Are you assuming that the return for each round is independent of the return of previous rounds? This ignores the autocorrelation of returns across time, which will bias your results.

You could also put some very bad returns in a number of consecutive eras for shock testing and see how that affects results. To be on the safe side, you should study scenarios that are not very likely but are still possible.

---

### Post #3 — **no_formal_agreement** | 2021-04-08 23:06 UTC _(reply to #2)_

Regarding autocorrelation, the issue with adding basic autocorrelation to the returns is that it will ‘smooth’ them out significantly, whereas in the actual returns we see significant swings occurring occasionally. The best solution I can think of right now to keep some autocorrelation while still allowing for large swings is to apply each randomly generated return multiple times. So for example, the randomly returns [+0.04, +0.06, -0.03, +0.01] would become [+0.04, +0.04, +0.04, +0.06,+0.06,+0.06,-0.03,-0.03,-0.03,+0.01,+0.01,+0.01]. This would keep the effects of autocorrelation without preventing the large swings from earn to burn that we have observed before.

---

### Post #4 — **no_formal_agreement** | 2021-04-16 05:15 UTC

Alright here is the results from my current investigations. TL;DR my original hypothesis was correct, as the payout factor becomes lower the optimal strategy for a completely rational and selfish net present value maximizing tournament participant is to withdraw a greater proportion of their stake each week, therefore creating a dynamic equilibrium that prevents infinitely increasing stake size and perpetually falling payouts.

So here is the code for running my simulations:
    
    
    import pandas as pd
    import numpy as np
    from scipy import stats
    #net_present_value_test
    
    #Create several time series that correspond to 4 weeks over scores each period
    #Default values are the average score distributions for several participants
    def generate_scores_monte_carlo(mean = 0.02334,std = 0.0357,years = 10, num_iterations = 10000):    
        return np.random.normal(mean,std,(num_iterations,int(years*13)))
    
    #Convert score time series to payouts timeseries with final value being remaining stake value
    def calculate_payouts_monte_carlo(scores, withdrawal_rate=0.04, payout_reduction=1, include_end_stake = True):
        payouts = np.zeros((len(scores),len(scores.T)+1))
        for i in range(len(scores)):
            stake_value = 1
            for j in range(len(scores.T)):
                stake_value = stake_value + stake_value*scores[i,j]*4*payout_reduction  #scores compounded over 4 weeks  with payout reduction
                payouts[i,j] = stake_value*withdrawal_rate # withdraw part of stake
                stake_value = stake_value - stake_value*withdrawal_rate
                
            payouts[i,len(scores.T)] = (stake_value)*include_end_stake #withdraw remaining stake after end of period
        
        return payouts
    
    
    #Convert numerous payout series to net present values
    #default time discount is equal to average 4 week return of s and p 500 not adjusted for inflation
    def get_net_present_values(payouts, time_discounting = 0.01047):
        npv = np.zeros((len(payouts)))
        discounts = (time_discounting + np.ones((len(payouts.T)))) ** np.array(range(len(payouts.T))) # there is probably a cleaner way to do this but I don't know it
        
        for i in range(len(payouts)):
            npv[i] = np.sum(((payouts[i,:])/discounts))
        
        
        return npv
    
    
    
    
    
    if __name__ == '__main__':
        
        scores = generate_scores_monte_carlo(mean = 0.02334,std = 0.0357,years = 10, num_iterations = 10000)
        npv_s= np.zeros((50))
        
        for i in range(50):
            payouts = calculate_payouts_monte_carlo(scores, withdrawal_rate=i*0.005, payout_reduction=0.95)
            
        
            npv_s[i] = stats.mstats.gmean(get_net_present_values(payouts, time_discounting = 8*0.01047))
            print(i)
        
        print("The net present value maximizing withdrawal rate is: ")    
        print(np.argmax(npv_s)*0.005)
    

This is one example where used scores distributions for a typical user and I set the payout factor to 0.95 and the time discounting to 8x the average s and p 500 returns. (As people in rocketchat have stated that they would stop staking long before we hit those levels of returns). Here the net present value maximizing withdrawal rate was 0.035 or 3.5% (although keep in mind the resolution is 0.5% points).

I also ran simulations on multiple payout reductions and time discount rates and in general what I saw was that the optimal strategy is to either withdraw your entire stake, or none of it. However in general there is a smooth transition when the payout factor gets worse. So as payouts decrease from too much staked we should see people withdraw a greater portion of their stake every 4 weeks.

Here is one instance of that at 8x S&P 500 discount rate (axis is stake proportion to withdrawal and y axis is net present value):

At payout = 1 (optimal withdrawal rate was 1.5%):  


[![npvs_1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3ae2b54e2287dc1251e74dd041ef80764101a649.png)npvs_1382×252 7.46 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3ae2b54e2287dc1251e74dd041ef80764101a649.png> "npvs_1")

At payout = 0.95 (optimal withdrawal rate was 3.5%):  


[![npvs_2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ee768003dc5b2f5d64bf2a83e1f0610e7d40d2ae.png)npvs_2375×252 5.48 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ee768003dc5b2f5d64bf2a83e1f0610e7d40d2ae.png> "npvs_2")

At payout = 0.90 (optimal withdrawal rate was the max of 22.5%):  


[![npvs_3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a4ab375cfdf16960170d7f85db1cd8f45d2c8b46.png)npvs_3375×253 6.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a4ab375cfdf16960170d7f85db1cd8f45d2c8b46.png> "npvs_3")

So this confirms my initial suspicions. Assuming people are rational, we shouldn’t see the payout factor drop super far though 8x the s&p 500 for time discounting is probably much higher than what most people intend so it will probably not be as early as 0.90 that people start withdrawing.

I’ll be investigating more in the future but I wanted to give some rough preliminary results based on what I have done so far and give others a chance to play with the code a bit if they want.

---

### Post #5 — **lucky_chicken** | 2021-04-17 23:58 UTC _(reply to #4)_

I’m not sure I understand. It seems to me that the fluctuations of the NMR/USD Exchange rate has a much larger than the payout factor. That randomness makes it really hard for me to make ‘optimal’ decisions.

---

### Post #6 — **no_formal_agreement** | 2021-04-18 00:58 UTC _(reply to #5)_

The net present value calculations here are denoted purely in NMR terms. So NMR/USD has no effect. No matter the change in exchange rate, having more NMR is better than having less NMR.

---

### Post #7 — **lackofintelligence** | 2021-04-19 23:07 UTC

This is interesting. Can you modify the MC to take into account the actual dynamic payout proration? Since all users have the same effective proration applied you could assume that the starting stake_value is 300K NMR. How can you estimate the optimal dynamic withdrawal rate given that the proration changes during the simulation?

---

### Post #8 — **lingzhou125** | 2021-04-19 23:53 UTC

I think quite the opposite will happen. Ppl will see the glorious gains which are easily double any other asset class over the past year leading to increases in stake rather than decreases. The value of nmr will keep going up as ppl try to increase their stakes to make up for the decreasing payout factor. Fomo is stronger than rationality even amongst data scientists.

---

### Post #9 — **wigglemuse** | 2021-04-20 00:56 UTC

Until there is a big burn, and then stakes will get lower just from burning, which makes the payout factor go back up, which means the burn the following rounds will be even worse. We think it is symmetrical, but over several rounds of auto-correlated burns the payout factor will magnify those burns, while the opposite happens when you have several good rounds in a row making the payout go down. So overall the floating payout factor is a danger, at least until we get some stake management to control our risk properly.

---

### Post #10 — **no_formal_agreement** | 2021-04-20 07:34 UTC _(reply to #8)_

Well using my own discounting rates and anticipated model means/standard deviations to calculate my own personal optimal withdrawal rate has me at 0% until the payout factor hits around ~0.43. We might not see any major withdrawals for a while, but ultimately people not withdrawing when my this model says they should are going to be hurting their own bottom line more than others especially given that sequential burns accelerate while sequential gains decelerate. At a certain point the risk outweighs the reward and my model gives a strong theoretical estimate as to where the tipping point will be (assuming you are accurate in anticipating the distribution of your models’ live performance).

Overall I’m satisfied with it for now, I think the next steps will be coming up with an estimator so I can very quickly calculate a ‘close’ to optimal result. The current method just takes too long for doing any other kind of analysis (like finding a dynamic equilibrium for large numbers of tournament participants with different discount rates and performances etc.)

---

### Post #11 — **wigglemuse** | 2021-04-20 14:27 UTC

…and with current (lack of) stake management, we can’t really control withdrawal rate very well at all (you can’t make or adjust a withdrawal every week from a single model). You can sort of do it if you never actually want the NMR to go to wallet through stake reductions/cancellations/adjusted-stake-reductions – that way you can control the stake better, but you can never actually get the NMR if you want to sell it. In order to get anything to your wallet, you have to initiate a withdrawal, and then do no stake adjustments whatsoever for 5 weeks until it resolves (at least for a single model slot).

---

### Post #12 — **no_formal_agreement** | 2021-04-26 08:32 UTC

Just giving an update here with easier to use code for your own models:
    
    
    import numpy as np
    from scipy import stats
    
    #net_present_value_test
    
    #Create several time series that correspond to 4 weeks over scores each period
    #Default values are the average score distributions for several participants
    def generate_scores_monte_carlo(mean = 0.02334,std = 0.0357,years = 10, num_iterations = 10000):    
        return np.random.normal(mean,std,(num_iterations,int(years*13)))
    
    #Convert score time series to payouts timeseries with final value being remaining stake value
    def calculate_payouts_monte_carlo(scores, withdrawal_rate=0.04, payout_reduction=1, include_end_stake = True):
        payouts = np.zeros((len(scores),len(scores.T)+1))
        for i in range(len(scores)):
            stake_value = 1
            for j in range(len(scores.T)):
                stake_value = stake_value + stake_value*scores[i,j]*4*payout_reduction  #scores compounded over 4 weeks  with payout reduction
                payouts[i,j] = stake_value*withdrawal_rate # withdraw part of stake
                stake_value = stake_value - stake_value*withdrawal_rate
                
            payouts[i,len(scores.T)] = (stake_value)*include_end_stake #withdraw remaining stake after end of period
        
        return payouts
    
    
    #Convert numerous payout series to net present values
    #default time discount is equal to average 4 week return of s and p 500 not adjusted for inflation
    def get_net_present_values(payouts, time_discounting = 0.01047):
        npv = np.zeros((len(payouts)))
        discounts = (time_discounting + np.ones((len(payouts.T)))) ** np.array(range(len(payouts.T))) # there is probably a cleaner way to do this but I don't know it
        
        for i in range(len(payouts)):
            npv[i] = np.sum(((payouts[i,:])/discounts))
        
        
        return npv
    
    #Get the payout factor where you would begin withdrawing more than zero percent of the stake every 4 weeks
    def get_begining_payout_factor(scores, discount = 2):
        time_discounting = 0.01047*discount
        pf_begin_withdrawal = 1
        while True:
            payouts1 = calculate_payouts_monte_carlo(scores, withdrawal_rate=0, payout_reduction=pf_begin_withdrawal)
            payouts2 = calculate_payouts_monte_carlo(scores, withdrawal_rate=0.01, payout_reduction=pf_begin_withdrawal)
            npv1 = stats.mstats.gmean(get_net_present_values(payouts1, time_discounting = time_discounting))
            npv2 = stats.mstats.gmean(get_net_present_values(payouts2, time_discounting = time_discounting))
            #print(pf_begin_withdrawal)
            if npv2 > npv1:
                break
            else:
                pf_begin_withdrawal = round(pf_begin_withdrawal-0.01,2)
            
        
        return pf_begin_withdrawal
    
    #Get the payout factor where you would withdraw the entirety of the stake
    def get_ending_payout_factor(scores, discount = 2):
        time_discounting = 0.01047*discount
        pf_end_withdrawal = 0
        while True:
            payouts1 = calculate_payouts_monte_carlo(scores, withdrawal_rate=1, payout_reduction=pf_end_withdrawal)
            payouts2 = calculate_payouts_monte_carlo(scores, withdrawal_rate=0.99, payout_reduction=pf_end_withdrawal)
            npv1 = stats.mstats.gmean(get_net_present_values(payouts1, time_discounting = time_discounting))
            npv2 = stats.mstats.gmean(get_net_present_values(payouts2, time_discounting = time_discounting))
            #print(pf_end_withdrawal)
            if npv2 > npv1:
                break
            else:
                pf_end_withdrawal = round(pf_end_withdrawal+0.01,2)
            
        
        return pf_end_withdrawal
    
    #Evaluate a model with the given mean, standard deviation, and discount factor (as multiple of S&P 500 returns)
    def model_evaluation(mean = 0.02334,std = 0.0357,years = 10, num_iterations = 10000, discount = 2):
        scores = generate_scores_monte_carlo(mean = mean,std = std,years = years, num_iterations = num_iterations)
        output_dict = {}
        pf_begin_withdrawal = get_begining_payout_factor(scores, discount = discount)
        pf_end_withdrawal = get_ending_payout_factor(scores, discount = discount)
        output_dict['Mean'] = mean
        output_dict['Standard deviation'] = std
        output_dict['Discount factor'] = discount
        output_dict['Begin withdrawal'] = pf_begin_withdrawal
        output_dict['End withdrawal'] = pf_end_withdrawal
        return output_dict
    
    
    
    if __name__ == '__main__':
        print(model_evaluation(mean = 0.02334,std = 0.0357,years = 10, num_iterations = 10000, discount = 4))
    

The output for these parameters is: “{‘Mean’: 0.02334, ‘Standard deviation’: 0.0357, ‘Discount factor’: 4, ‘Begin withdrawal’: 0.49, ‘End withdrawal’: 0.45}”

So a person with a typical model and a discount factor 4x the returns of the S&P 500 would begin withdrawing part of their stake if the payout factor reached 0.49 and withdraw the entire stake if the payout factor got as low as 0.45

To use this code for your own model simply input the anticipated mean and standard deviation of your model’s scores as well as your subjective discount factor (as multiple of S&P 500 returns).

---

### Post #13 — **no_formal_agreement** | 2021-05-08 23:16 UTC

Below is about 32 starting and ending withdrawal rates for several different mean, std, and discount rate values:

Mean | Standard deviation | Discount factor | Begin withdrawal | End withdrawal  
---|---|---|---|---  
0.02334 | 0.0357 | 4 | 0.49 | 0.45  
0.02334 | 0.0357 | 5 | 0.62 | 0.57  
0.02334 | 0.0357 | 6 | 0.77 | 0.67  
0.02334 | 0.0357 | 7 | 0.92 | 0.78  
0.02334 | 0.04 | 7 | 0.97 | 0.78  
0.02334 | 0.04 | 6 | 0.8 | 0.7  
0.02334 | 0.04 | 5 | 0.64 | 0.56  
0.02334 | 0.04 | 4 | 0.5 | 0.47  
0.02334 | 0.04 | 3 | 0.36 | 0.34  
0.02 | 0.04 | 3 | 0.44 | 0.42  
0.02 | 0.04 | 4 | 0.61 | 0.53  
0.02 | 0.04 | 5 | 0.8 | 0.66  
0.02 | 0.04 | 6 | 1 | 0.8  
0.03 | 0.04 | 6 | 0.57 | 0.53  
0.03 | 0.04 | 5 | 0.47 | 0.44  
0.03 | 0.04 | 4 | 0.37 | 0.36  
0.03 | 0.04 | 3 | 0.27 | 0.26  
0.03 | 0.03 | 3 | 0.27 | 0.27  
0.03 | 0.03 | 4 | 0.37 | 0.36  
0.03 | 0.03 | 5 | 0.45 | 0.44  
0.03 | 0.03 | 6 | 0.55 | 0.53  
0.02 | 0.03 | 6 | 0.89 | 0.78  
0.02 | 0.03 | 5 | 0.72 | 0.65  
0.02 | 0.03 | 4 | 0.57 | 0.52  
0.02 | 0.03 | 3 | 0.41 | 0.41  
0.02 | 0.02 | 3 | 0.4 | 0.39  
0.02 | 0.02 | 4 | 0.54 | 0.53  
0.02 | 0.02 | 5 | 0.68 | 0.65  
0.02 | 0.02 | 6 | 0.83 | 0.78  
0.02 | 0.02 | 7 | 0.98 | 0.93  
0.02 | 0.03 | 7 | 0.98 | 0.93  
0.03 | 0.03 | 7 | 0.65 | 0.62  
  
One of the interesting things I’ve noticed with these values is that a lot of the time there is very little space between the ‘begin withdrawing’ phase and the ‘withdraw absolutely everything’ phase which indicates that overwhelmingly often the optimal strategy is going to be to either not withdraw at all, or withdraw the entirety of the stake. This wasn’t my hypothesis going in and I’m still kind of have a hard time accepting it, but if we aren’t going to update are conceptions based on testing then what is even the point of testing.

On a related note, I am curious how people are deciding to manage when to withdraw their stake based on payout. So here’s a poll:

How do you decide when/how much NMR to withdraw from your stake

  * I follow the methods described in this thread
  * I have my own personally developed unshared programmatic method
  * I just go with whatever I intuitively feel is right at the time
  * I am still waiting for ‘stake management’ features to be built in to the tournament before I put any effort into deciding how/when to begin withdrawing stake
  * I have not put any thought into when I want to start withdrawing stake yet



0 voters
