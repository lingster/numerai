---
title: "Incorporate era similarity in ranking models"
category: Data Science
url: https://forum.numer.ai/t/incorporate-era-similarity-in-ranking-models/5379
created_at: 2022-05-10T10:01:11.463000+00:00
last_posted_at: 2022-05-20T12:25:31.550000+00:00
posts_count: 10
views: 2007
tags: []
---

# Incorporate era similarity in ranking models

---

### Post #1 — **kayeffnumeraitor** | 2022-05-10 10:01 UTC

Hello together,

recently I played around with the new v4 dataset and tried to create a new ranking model.

During experimentation, I noticed that ranking the rows within an era is relatively “easy”: If the model is trained on lets say half of the data from eraXYZ and then tested on the other half of the same era, which it has not seen during training, it is possible to get (obviously?) really high ranking correlations, sometimes more than 0.3.

I also noticed that said model which was trained on a specific era performs also really well on some other eras, while on some eras, it performs even worse than guessing, as if the sorting mechanics were completely reversed. This is not a really surprising result, but I tried to get a better feel for that, so I made a correlation matrix of the era dependencies to see what is going on.

What you can see here is something like: When the model has positive correlation on eraX, then it has the color coded correlation on eraY, where blue are correlations > 0 and red correlations < 0:  


[![corrm](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ef294ab6df42d514deffffeae61676fc33f81e73.png)corrm583×578 75.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ef294ab6df42d514deffffeae61676fc33f81e73.png> "corrm")

Things are more interesting if the columns are sorted against a specific era, like here, where I sorted it on the 99th used era:  


[![sorted_corrm_era_index_99](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/56652b2b56dfd0f0ffb1759751c30064eacb9e3d.png)sorted_corrm_era_index_99583×578 75.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/56652b2b56dfd0f0ffb1759751c30064eacb9e3d.png> "sorted_corrm_era_index_99")

  
If you look closely, apart from the row that is perfectly sorted, there are a few other rows that show clear “ranking mechanic similarity”, while others seem to be completely reversed.

What I did next was sorting the rows by the strength of this correlation dependency, (correlation of correlation), to see how many other eras are sorted in the same way, as these eras seem to be closely related. This is the one with the most similar eras:  


[![lowest_uniqueness](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35a891e8339d84f934bbf2c55d1ad7cb17f95ab1.png)lowest_uniqueness583×578 75 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35a891e8339d84f934bbf2c55d1ad7cb17f95ab1.png> "lowest_uniqueness")

As another example, here is another one sorted against the era with the least similarity to others:  


[![highest_uniqueness](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f452a4c7dfd4df74a520e6397dea2f8dab211dad.png)highest_uniqueness583×578 75.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f452a4c7dfd4df74a520e6397dea2f8dab211dad.png> "highest_uniqueness")

You can think of the latter era as being more “unique” than the first one.

I tried to feed the output of a convolutional neural net that convolutes the entire data set of one era into the ranker model to somehow “identify”, which sorting scheme to use. But in the end, my model really struggles to learn the appropriate sorting scheme.

It somehow also fits the observation that a lot of models keep performing really well for a certain period of time only to sink down in the tournament to be never seen again, so my guess is that most models are more or less “lucky” to perform well on those eras in the training set that are similar to the actual live data era.

What do you think about it? Do you have suggestions about how to incorporate the era similarity into an actual model?

---

### Post #2 — **sneaky** | 2022-05-10 21:45 UTC

Hi, I did the exactly same thing and shared it here: [Clustering Eras - #7 by sneaky](<http://forum.numer.ai/t/clustering-eras/4863/7>). Currently I’m working with 5 strong clusters of eras. I tried several methods to predict which era fits in which cluster, but IMO it is not possible with tournament data.

I tracked the performance of each cluster by learning a model on each and uploading the models predictions. When I compared the performances with real data like S&P500, VIX, … I found some patterns. But, I doubt we have enough eras to train it.

I did a lot of experiments on this, but never had time to format it and share it in a clear form.

This picture shows the 5 (4) clusters that I found. Each dot represents similarity between two eras. Y and X axis are sorted by clusters.  


[![usefullness_of_eras2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f09436174ff51299fec0f27db2d68d8479dc9ade.png)usefullness_of_eras2480×480 160 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f09436174ff51299fec0f27db2d68d8479dc9ade.png> "usefullness_of_eras2")

  * Cluster 0, which is the first square of eras in the interval from 0 to +/-120 is cluster of unique eras, that do not fit to any other cluster.
  * Cluster 1, the second square, is the cluster of eras where the market acts predictably, also it is the cluster of eras that are easy to predict and most of the models have high correlations when they occur.
  * Cluster 2 and 4, the third square, originally there were only 4 clusters, but I extended them to 5 and this image is from before.
  * Cluster 3, the last square, this cluster is special, because it is negatively correlated to cluster 1, 2, and 4. The eras within the cluster are the eras that the majority of the tournament models have struggle with.



So I trained a model on each cluster separately and these are their results:  


[![Screenshot from 2022-05-11 00-51-36](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/186cbc06460ad697612c99134e27c227b1c85881_2_690x99.png)Screenshot from 2022-05-11 00-51-361319×190 32.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/186cbc06460ad697612c99134e27c227b1c85881.png> "Screenshot from 2022-05-11 00-51-36")

It was evaluated on eras from validation data (V3 version)

It is clear that cluster 2 strongly correlates with cluster 4 (expected), and every model that wasn’t trained on the cluster 3 has negative correlation with eras from the cluster 3.  
This trend I found in other models I trained. Whenever I have model that is significantly better at predicting eras from cluster 3, the correlation of eras from the other clusters goes down.

---

### Post #3 — **sneaky** | 2022-05-11 12:28 UTC _(reply to #2)_

I thing it could help if the numerai team would provide obfuscated dataset of higher level features. I tried to create some aggregation functions to create those features from the instances, but without any success. I think it is due to the regularization and normalization of every era.

---

### Post #4 — **jacob_stahl** | 2022-05-12 06:58 UTC

I’ve done something similar to this and got (somewhat) decent results. One way you can measure era similarity is to compute a correlation matrix of all features for each era.  


[![output_1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b040d848a3e407f9b855fe0bcfc36965b6b5cdb0_2_485x500.jpeg)output_11072×1105 564 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b040d848a3e407f9b855fe0bcfc36965b6b5cdb0.jpeg> "output_1")

  
This captures how features interact with each other in a given era. We would expect similar eras to have similar correlation matrices. We can measure era similarity by computing cosine similarity between 2 era matrices.  


[![era_similarity](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e3963b649f8e7a81120552bf10e61d1199d2fac0_2_690x345.jpeg)era_similarity1920×961 84.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e3963b649f8e7a81120552bf10e61d1199d2fac0.jpeg> "era_similarity")

  
You can incorperate this into a model by turning some of the elements in each correlation matrix into new “era wise” features.Think of it as telling your model what “kind” of era it is making predictions in by giving it some context.

---

### Post #5 — **kayeffnumeraitor** | 2022-05-12 07:44 UTC _(reply to #4)_

Wow, this are really nice diagrams, should have thought of it the same way. I will try to incorporate it into my model and give an update

---

### Post #6 — **kayeffnumeraitor** | 2022-05-12 14:19 UTC _(reply to #4)_

So I tried to use cosine similarity, however this was too computationally intensive for me. Also I don’t really like the idea of having to manually craft features where I dont really know if they make sense in latent space. So instead I compute the correlation matrix during inference, and let the network itself “learn” about eras.  
Here is a quick plot of what the network “thinks” about eras (This is after one epoch, as I was curious and couldnt wait):  


[![era_latent_space](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8cea636e43644f542ca66abadec0b2faa6779a28.png)era_latent_space331×848 37.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8cea636e43644f542ca66abadec0b2faa6779a28.png> "era_latent_space")

from top to bottom are the eras, and from left to right are the latent space vectors. The eras span from the first era in the official training set to the last validation era containing targets, but only every 4th with some eras taken out.  
The eras seem to be mostly similar with some periods where eras are probably behaving differently, notably around row 60 and 170.

Ill let the model continue training and hope the ranking stability is improved.

---

### Post #7 — **climber_1** | 2022-05-13 03:47 UTC

Yeah market style and market paradigm change. I remember reading some papers in the continuous learning field, where they train multiple models for different environments and have a way to detect environments.

---

### Post #8 — **sneaky** | 2022-05-18 11:39 UTC

IMO, there is a potential in time series. I plotted the cluster models’ correlations between their predictions and the target (models that were trained on different clusters of eras).  
The plot shows that the dominance (highest corr) of a model often persists for several eras.

[![Screenshot from 2022-05-18 13-35-01](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f7dde27dabfa1fada78d7749eb907c32afdbea69_2_379x500.png)Screenshot from 2022-05-18 13-35-01779×1027 185 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f7dde27dabfa1fada78d7749eb907c32afdbea69.png> "Screenshot from 2022-05-18 13-35-01")

  * X axis = eras
  * Y axis = correlation
  * Color of a data point represents the dominant model of the era
  * The plotted eras are from the v3 validation dataset and the models didn’t train on them nor validated on them.

---

### Post #9 — **kayeffnumeraitor** | 2022-05-20 08:55 UTC _(reply to #8)_

Nice plot, this fits my observations as well. It almost seems as if each ‘vanilla’ model has a random chance of performing well in a given era. I think the key takeaway is that the numerai task is not so much about accurately ranking the rows, but rather to predict HOW to rank in a given era.

Right now there are 960 overlapping eras or 240 independent(non-overlapping) eras spanning 20 years of data, which essentially means 960 datapoints for predicting the ranking mechanics, which is not much, but by grouping the eras into just a few era groups, it might be possible to extract the information.

---

### Post #10 — **sneaky** | 2022-05-20 12:25 UTC

I matched the eras with the real dates and plot the basic indexes, atleast I hope so. I assume that every era ends one week before the next era ends, and that there are no gaps. It seems that, as I suspected, the model 3 profits when there is high fear in the market.

[![Screenshot from 2022-05-20 14-18-33](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0eaa28400637cb60e45c58839dd0015a532e2b34_2_235x499.jpeg)Screenshot from 2022-05-20 14-18-33784×1666 284 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0eaa28400637cb60e45c58839dd0015a532e2b34.jpeg> "Screenshot from 2022-05-20 14-18-33")

  


[![Screenshot from 2022-05-20 14-38-05](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/de5c2f5e482c9d4dd811dc284f72eba17a94131d_2_234x499.jpeg)Screenshot from 2022-05-20 14-38-05782×1666 224 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de5c2f5e482c9d4dd811dc284f72eba17a94131d.jpeg> "Screenshot from 2022-05-20 14-38-05")
