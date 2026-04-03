---
title: "Meta-analysis: clustering model performances"
category: Data Science
url: https://forum.numer.ai/t/meta-analysis-clustering-model-performances/1653
created_at: 2021-02-09T17:45:28.541000+00:00
last_posted_at: 2021-03-01T20:07:23.755000+00:00
posts_count: 4
views: 1857
tags: []
---

# Meta-analysis: clustering model performances

---

### Post #1 — **sirmobius** | 2021-02-09 17:45 UTC

I’ve been doing some analysis of live models I thought I would share. It could be used to help you understand how diversified your models are relative to other competitors. It’s a work in progress, so please feel free to share ideas to how this can be improved.

## Overview of analysis

I embed live models into a 2D space using the UMAP algorithm. The end-of-round correlations for a set of resolved rounds are the variables used for the embedding. The 2D space can, therefore, be considered an abstract, long-term correlation space between models. In this space, models closer in proximity share more similar end-of-round correlations (note, this does not necessarily mean their predictions are similar, just that the overall correlation by round is similar).

I did the analysis twice for rounds 215-237 and rounds 221-245. There is temporal overlap but this provides some insight into how model performances are evolving with time. In future this could be (easily) calculated as a rolling-average per round which can give you an idea of temporal changes in this space.

**Some key caveats:**

  * Currently, I only take models which submit every round. UMAP can’t deal with NaNs, so this avoids imputation. For models missing one round it seems reasonable that mean imputation will not have a signifcant impact on structure.
  * Exact structure of the embeddings should be taken with a pinch of salt, depends heavily on hyperparameter selection. But these can be fixed to analyse temporal changes.
  * I believe UMAP does a ‘better’ job at preserving global structure than t-SNE, but this needs to be investigated.



## Model embeddings

The following figures are the UMAP embeddings in the 2D space. Left panels are coloured by mean end-of-round CORR and the right panels mean end-of-round MMC.

[![embedding_round_215_237](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/993f291f962bf577211c9597a7fcc727edb3262a_2_690x313.png)embedding_round_215_2372810×1276 516 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/993f291f962bf577211c9597a7fcc727edb3262a.png> "embedding_round_215_237")

* * *

[![embedding_round_221_245](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/73ee3fdbe3d4092e008701dca17e7e01c9c8765c_2_690x261.png)embedding_round_221_2452870×1086 478 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/73ee3fdbe3d4092e008701dca17e7e01c9c8765c.png> "embedding_round_221_245")

* * *

### Global structure

So far I have high level information on the following models:

model_name | Type | Feature neutralization  
---|---|---  
krat | NN | ?  
trivial | NN | ?  
floury_kerril_moodle | LinearRegression | No  
integration_test_7 | GBT | No  
budbot_7 | GBT | Yes  
  
I’ve labelled (where possible) where these models fall in the embeddings. Noting the differences between these models can help you understand the structure of the embedded space.

For example, I don’t think it is coincidence that budbot_7 (100 % feature neutralised model) is diametrically opposed to the linear model (floury_kerril_moodle) in the round 215–>237 figure. Additionally, it seems likely that models near integration_test are gradient boosted models without substantial feature neutralisation.

I’ve found a group of models (robprofit, wwmodel2, wwmodel3, wwmodel4, wwmodel5,..) who are somewhat anomalous - they are doing well MMC and CORR but with round correlation’s relatively dissimilar to other models.

### Temporal changes

There are several changes between the two figures (round 215–>237 and 221–>245):

  * Note how the mean correlation is much higher in later rounds (left panel of 221–>245 is consistently a darker shade of blue)
  * In the earlier rounds (215–>237) MMC tended to be localized in fewer models (particularily in Feature neutralized models around budbot_7). In later rounds (221–>245), MMC tends to be more ‘spread out’ (light shades of blue).
  * I assume there is a greater number of feature neutralized GBTs being used now (blob around budbot_7 is bigger in 221–>245 compared to 215–>237).
  * Models similar to integration_test_7 have a low MMC contribution - but there are some exceptions.



### What can this be used for?

Ideally, this is a visualisation which needs to be interactive so it can be explored (previously discussed in chat). I’m keen to work on this if there is sufficient merit in the visualisation. Such a visualisation can help perform meta-analysis of the competition, get an understanding of the diversity of your models relative to other competitors, and interestingly it is plausible that you can use this to predict what type of model a competitor is using by projecting it into this space. More data is required but this could get quite involved. For example, I wouldn’t be surprised if a certain dimension corresponds to the degree of feature neutralisation or linearity of the model to the features.

---

### Post #2 — **bor1** | 2021-02-15 08:37 UTC

Have you thought about splitting up models that clearly changed during the time interval you looked at? I’m not sure we have a simple way of doing that, other than the rather crude “correlation with metamodel”.

Its somewhat of a shame that the diagnostics stats are not publically available. They would help enormously in teasing apart when models changed. [@richardcraib](</u/richardcraib>), maybe the diagnostics could be open?

---

### Post #3 — **sirmobius** | 2021-02-15 09:44 UTC

I was concerned about this but decided the only mitigations I could do for now was to use as ‘short’ a time window as possible and hope competitors didn’t change their model.

I’ve ran these with a round-by-round rolling window and you could identify models which are changed by looking at big changes throughout the space with time. This needs some thought though as the rotational invariance of UMAP is causing me problems, I have some potential solutions for this but not had a chance to implement them.

Will share some code snippets to reproduce these soon.

---

### Post #4 — **sirmobius** | 2021-03-01 20:07 UTC

If of interest here is a code snippet for reproducing one of the plots. Originally I used Numerai’s api to download the data, but someone kindly pointed out [Jo-fai (Joe) Chow’s website](<https://www.jofaichow.co.uk/numerati/>) and I make use of that here.
    
    
    import os
    import requests
    import csv
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import umap # pip install umap-learn
    
    # You can change what rounds to look at here
    LAST_ROUND = 245 # Last round to include in creating embedded space
    FIRST_ROUND = 221
    
    # coords are position to plot text relative to model position
    KNOWN_MODELS = {'budbot_7':(-2,-2),
                    'integration_test_7':(2,0.5),
                    'krat':(-0.25,-2.5),
                    'trivial':(-2,-2)
                   }
    
    get_data() # this is defined below
    
    df = pd.read_csv('round_data.csv')
    pivoted_df = pd.pivot(df, 
                          index='model', 
                          columns='round', 
                          values=['corr','mmc'])
    
    round_corrs = pivoted_df['corr'] # model per row, round per column
    round_mmcs = pivoted_df['mmc']
    
    # calculate the embedding in end-of-round correlation space
    X = round_corrs.loc[:,FIRST_ROUND:LAST_ROUND]
    
    # UMAP doen't like NaNs, either impute or remove rows models with NaN
    nan_mask = X.isna().sum(axis=1)==0
    X = X[nan_mask]
    
    embedder = umap.UMAP(random_state=42, n_neighbors=30)
    X_emb = embedder.fit_transform(X.to_numpy())
    mean_corr_by_model = np.mean(X.to_numpy(), axis=1)
    
    fig, ax = plt.subplots()
    cax = ax.scatter(X_emb[:,0], 
                     X_emb[:,1], 
                     c=mean_corr_by_model,
                     cmap='RdBu',
                     s=18,
                     vmin=-0.03,
                     vmax=0.03)
    cb = fig.colorbar(cax, 
                      ax=ax, 
                      label='Mean end-of-round correlation',
                      fraction=0.03)
    cb.ax.tick_params(labelsize=8)
    
    # Add annotation of known model names
    for key, value in KNOWN_MODELS.items():
            try:
                annotate_model(ax, X, X_emb, key, value)
            except:
                pass
            
    ax.axis('off')
    
    def annotate_model(ax, X, X_emb, model_name, xytext=(-2,-2)):
        """
        Adds model name annotation to ax.
    
        Parameters:
        -----------
            ax : matplotlib.Axes, 
            Axes to plot to.
        
        X : pd.DataFrame,
            The round correlations, with model names as index.
        
        X_emb: np.array, 
            The 2D embedding.
            
        model_name : str, 
            Name of the model to annotate
            
        xytext : tuple, 
            Coords relative to point to plot.
        """
        mask = X.index==model_name
        coords = X_emb[mask][0]
        
        ax.annotate(model_name,
                    xy=coords, 
                    xycoords='data',
                    xytext=(coords[0]+xytext[0], coords[1]+xytext[1]),
                    textcoords='data',
                    size=9,
                    va="center",
                    ha="center",
                    arrowprops=dict(arrowstyle="simple",
                                    connectionstyle="arc3,rad=0.2",
                                    color='k'))
        
    def get_data(data_url=None):
        """
        Checks if round_data is available and if not loads the data from 
        "ia_ai_Joe's" webpage (https://www.jofaichow.co.uk/numerati/).
        
        Parameters:
        -----------
        data_url : str (default=None),
            URL where the round data is held. If None default is used.
        """
        if data_url is None:
            data_url = 'https://raw.githubusercontent.com/woobe/numerati/master/data.csv'
            
        if not os.path.isfile('round_data.csv'):
            # get data from ia_ai_Joe's webpage
            resp = requests.get(data_url)
            with open('round_data.csv', 'w') as f:
                writer = csv.writer(f)
                for line in resp.iter_lines():
                    writer.writerow(line.decode('utf-8').split(','))
        else: 
            print('Data already downloaded.')
