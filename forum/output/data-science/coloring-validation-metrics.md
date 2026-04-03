---
title: "Coloring validation metrics"
category: Data Science
url: https://forum.numer.ai/t/coloring-validation-metrics/1269
created_at: 2020-12-06T13:38:44.572000+00:00
last_posted_at: 2021-05-11T15:35:23.366000+00:00
posts_count: 5
views: 1270
tags: []
---

# Coloring validation metrics

---

### Post #1 — **jrb** | 2020-12-06 13:38 UTC

I’ve been computing the validation metrics locally and keeping my local validation code in sync with all the recent changes (per-era feature-neutral mean and feature exposure, for instance). One thing that I haven’t been able to do until last week was color the metrics the way they’re displayed on the website. I asked [@master_key](</u/master_key>) (MikeP on Rocket Chat) for the intervals and percentiles they use for coloring the metrics on the website, and he shared the numbers with me.

Here’s some quick and dirty Python code that I wrote based on the numbers that [@master_key](</u/master_key>) shared with me. I suspect there are many others who compute validation metrics locally, who might benefit from this. BTW, if you aren’t already compute validation metrics locally, I’d recommend doing it.All the code needed to compute the validation metrics can be found in the [example model](<https://github.com/numerai/example-scripts/blob/master/example_model.py>).
    
    
    import numpy as np
    from scipy import stats
    
    from colorama import Fore, Style
    
    VALIDATION_METRIC_INTERVALS = {
        "mean": (0.013, 0.028),
        "sharpe": (0.53, 1.24),
        "std": (0.0303, 0.0168),
        "max_feature_exposure": (0.4, 0.0661),
        "mmc_mean": (-0.008, 0.008),
        "corr_plus_mmc_sharpe": (0.41, 1.34),
        "max_drawdown": (-0.115, -0.025),
        "feature_neutral_mean": (0.006, 0.022)
    }
    
    
    def color_metric(metric_value, metric_name):
        low, high = VALIDATION_METRIC_INTERVALS[metric_name]
        pct = stats.percentileofscore(np.linspace(low, high, 100),
                                      metric_value)
        if high <= low:
            pct = 100 - pct
        if pct > 95:  # Excellent
            return f"{Style.BRIGHT}{Fore.GREEN}{metric_value:.4f}" \
                   f"{Fore.BLACK}{Style.RESET_ALL}"
        elif pct > 75:  # Good
            return f"{Fore.GREEN}{metric_value:.4f}{Fore.BLACK}"
        elif pct > 35:  # Fair
            return f"{metric_value:.4f}"
        else:  # Bad
            return f"{Fore.RED}{metric_value:.4f}{Fore.BLACK}"
    

I use the [colorama](<https://pypi.org/project/colorama/>) module for coloring text (and it works with Jupyter notebooks, as well as the terminal). It’s quite straightforward to use something else in its place, if needed.

---

### Post #2 — **mindyoself** | 2021-05-10 17:07 UTC

Hello [@jrb](</u/jrb>),  
Thanks for that, that’s awesome, I was searching for this. Quick question though. These intervals surely change though don’t they or are they the Gold standard for now?

---

### Post #3 — **jrb** | 2021-05-11 10:55 UTC _(reply to #2)_

I believe they’re still the same. I compare the colouring between what’s shown on the website and what gets rendered locally, every once in a while. And I haven’t noticed a difference, yet. Also, you’re right. They’ll almost certainly change in the future. Perhaps when the target changes or when we have more features.

---

### Post #4 — **themicon** | 2021-05-11 12:01 UTC

Just a quick addition: If you use a terminal with a strange colour scheme, you might need to change this “Fore.BLACK” to something else. I needed to check my terminal colour value for text and update the script accordingly.

Awesome script BTW [@jrb](</u/jrb>) \- Really useful

---

### Post #5 — **mindyoself** | 2021-05-11 15:35 UTC _(reply to #3)_

Now numerai may want to withold these threshold values or are we allowed to have them? Because I can see you have to hard code the means and their upper and lower limit of all the metric intervals everytime right in the dictionary up there. Ideally it would be better if those values were locked in a validation meteric class or separate functions and easily callable that way we don’t have to keep hard coding it everytime. Is that feasible?
