---
title: "Signals diagnostic script"
category: Signals
url: https://forum.numer.ai/t/signals-diagnostic-script/3461
created_at: 2021-05-28T07:46:00.426000+00:00
last_posted_at: 2021-05-28T09:31:49.225000+00:00
posts_count: 2
views: 659
tags: []
---

# Signals diagnostic script

---

### Post #1 — **nyuton** | 2021-05-28 07:46 UTC

Does anyone know, how to calculate diagnostics properly for Signals?  
I modified my scripts from the main tournament, but they give different results then what I get on the website.  
What am I doing wrong? I can’t find the official scrips.  
Here is mine:
    
    
    def correlation(predictions, targets):
        ranked_preds = predictions.rank(pct=True, method="first")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    
    def score(df):
        return correlation(df['signal'], df['target'])    
    
    def evaluation(df, plot=True):
    
        scores = df.groupby(df.index).apply(score)
        
        mean = scores.mean()
        std = scores.std(ddof=0)
        sharpe = mean / std
    
        sortino = 0
        if np.sum(np.minimum(0, scores))!=0:
            sortino = scores.mean() / (np.sum(np.minimum(0, scores)**2)/(len(scores)))**.5
    
        rolling_max = (scores + 1).cumprod().rolling(window=100, min_periods=1).max()
        daily_value = (scores + 1).cumprod()
        max_drawdown = -((rolling_max - daily_value) / rolling_max).max()
    
        if plot==True:
            cumsum = scores.cumsum()
            plt.xticks(rotation='vertical')
            plt.plot(val.index.unique(), cumsum)    
    
        print(f'Weeks: {len(scores)}')
        print(f"Correlation sharpe: {sharpe:.4f}")
        print(f'Mean Correlation: {mean:.4f}')
        print(f'Correlation SD: {std:.4f}')
        print(f'Profitability: {(np.power(mean+1, 52)-1)*100:.2f}%')
        print(f'Drawdown: {max_drawdown:.4f}')    
    
        return mean, std, sharpe, sortino, max_drawdown

---

### Post #2 — **restrading** | 2021-05-28 09:31 UTC

The Signals validation metrics given on the website are calculated after your predictions are neutralized to their features. It is not possible to replicate locally.
