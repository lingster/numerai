---
title: "Sharpe and Sortino ratios on live performance of your models"
category: Data Science
url: https://forum.numer.ai/t/sharpe-and-sortino-ratios-on-live-performance-of-your-models/1551
created_at: 2021-02-02T16:33:50.510000+00:00
last_posted_at: 2021-08-17T11:34:43.350000+00:00
posts_count: 3
views: 1770
tags: []
---

# Sharpe and Sortino ratios on live performance of your models

---

### Post #1 — **degerhan** | 2021-02-02 16:33 UTC

As numerai models only earn or burn when the round is resolved, you may be ignoring the information content of the 20 daily scores in between.

The daily gyrations of a model is similar to the daily account value of a buy-and-hold brokerage account. Yes, you don’t realize profit or loss until you sell, yet a slow and steady climb might be more deserving of your hard earned NMRs.

More critically, historical daily scores are a high resolution indicator of your model’s volatility under different staking regimes, and may influence your choice of stake type. For example, half-mmc would yield higher Sharpe and Sortino ratios for [@mdo](</u/mdo>) over the past six months compared to other staking methods.

Feed a list of accounts (yours and those you follow) to the [live-sharp-sortino](<https://gist.github.com/degerhan/172be51b80c3d9b218d3d46c5fad6a69>) notebook. It will read the daily scores from numerai and calculate sharpe and sortino ratios on their live daily-score performance.

So, put this in the notebook:
    
    
    # your models and others you want to bencmark
    account_list = [
        "degerhan",
        "era__mix__2000",
        "hiryuu",
        "integration_test",
        "mdo",
        "sorios",
        "themicon",
        "arbitrage",
    ]
    

and receive:

| annual_return_corr | annual_return_halfmmc | annual_return_1mmc | annual_return_2mmc | sharpe_corr | sharpe_halfmmc | sharpe_1mmc | sharpe_2mmc | sortino_corr | sortino_halfmmc | sortino_1mmc | sortino_2mmc | rows  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
themicon | 1.333991 | 1.710942 | 2.082832 | 2.811966 | 2.572024 | 2.838774 | 2.938870 | 2.965025 | 4.005048 | 4.448977 | 4.652587 | 4.872778 | 130.0  
degerhan | 1.780967 | 2.237819 | 2.679758 | 3.523582 | 2.564452 | 2.661918 | 2.703920 | 2.711582 | 4.292114 | 4.627113 | 4.731770 | 4.605466 | 37.0  
hiryuu | 1.164212 | 1.507592 | 1.850411 | 2.532070 | 1.987121 | 1.854426 | 1.766267 | 1.660042 | 3.529113 | 3.270079 | 3.053915 | 2.822324 | 130.0  
mdo | 0.958362 | 1.103332 | 1.243571 | 1.509940 | 1.844011 | 1.904945 | 1.873802 | 1.729242 | 3.301595 | 3.398901 | 3.190205 | 2.735015 | 130.0  
era__mix__2000 | 1.369557 | 1.743672 | 2.112315 | 2.833632 | 2.362132 | 2.362064 | 2.322188 | 2.242782 | 3.169988 | 3.030299 | 2.871511 | 2.664848 | 130.0  
sorios | 0.977431 | 1.110031 | 1.239880 | 1.491600 | 1.867191 | 1.791917 | 1.648394 | 1.399152 | 2.507887 | 2.460163 | 2.356310 | 2.064312 | 130.0  
arbitrage | 0.885076 | 0.941292 | 0.995323 | 1.096883 | 1.617012 | 1.522430 | 1.400110 | 1.169640 | 2.887307 | 2.723927 | 2.332565 | 1.768363 | 130.0  
integration_test | 1.041502 | 1.104208 | 1.165780 | 1.285710 | 1.492098 | 1.437492 | 1.373536 | 1.243987 | 2.374332 | 2.202366 | 2.008255 | 1.720881 | 130.0

---

### Post #2 — **nyuton** | 2021-05-21 13:17 UTC

Very interesting! Thank you for sharing!

---

### Post #3 — **mindyoself** | 2021-08-17 11:34 UTC

[@degerhan](</u/degerhan>) Thanks for sharing this.
