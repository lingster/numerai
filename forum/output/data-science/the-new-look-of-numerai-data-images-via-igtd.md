---
title: "The New Look of Numerai Data, Images via IGTD"
category: Data Science
url: https://forum.numer.ai/t/the-new-look-of-numerai-data-images-via-igtd/5997
created_at: 2023-01-01T22:19:42.211000+00:00
last_posted_at: 2023-01-03T15:06:14.807000+00:00
posts_count: 3
views: 1387
tags: []
---

# The New Look of Numerai Data, Images via IGTD

---

### Post #1 — **jefferythewind** | 2023-01-01 22:19 UTC

Greetings Fam. I had started work on this topic about 7 months ago and had to put it aside for a while, while life moved on. So I have some time over holidays here and wanted to finally post something (with code) to let people ponder, try, and hopefully unlock some fresh TC.

The basic motivation here is that much of the recent progress in AI has been in the realm of image recognition and vision systems, however financial (Numerai) data is inherently tabular, so it seems we aren’t able to really catch the wave of progress in the field of vision. Or can we? This is the question I chose to explore.

To my delight there has already been substantial progress in this arena. In this post we will delve into a cool algorithm called IGTD (Image Generator for Tabular Data), which is described in a paper by Zhu et. al.: [_Converting tabular data into images for deep learning with convolutional neural networks_](<https://www.nature.com/articles/s41598-021-90923-y>).

I won’t re-write the paper here, please read through. This algorithm is designed to do exactly what we want: convert our tabular data into coherent images. Converting the data to images is nothing more than re-arranging the feature positions from the 1-dimensional tabular format to a 2-dimensional image format. The question is: how to do this in a coherent way, where space in the images actually means something? The IGTD algo does this by considering 2 sets of distance measures: one between features and one between pixels. Similar features should be located near each other in the image. An error function is developed which calculates the error between feature distance compared to the pixel distance, and an iterative algorithm is developed which aims to minimize this error function, resulting in an optimal map from tabular feature position to image pixel position. Nearby pixels represent features which are close in distance. The idea of distances here are general so, different distance metrics can be substituted.

The effect is interesting. Here was compare the optimized image embeddings against the naive (no re-arrangement) embeddings, and we see that in the optimized embeddings, we have larger patches of similar values next to each other, which suggests the algo is working. Features with similar values will be placed next to each other.

Naive Embedding  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5369f83e91cebdfce6615dd99b2fb51a52e43dc9.png)image491×418 13.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5369f83e91cebdfce6615dd99b2fb51a52e43dc9.png> "image")

Optimized Embedding  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9f6fc187f7b4febb5629773c5abe4be127d0eb12.png)image491×418 12.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9f6fc187f7b4febb5629773c5abe4be127d0eb12.png> "image")

One thing that pops out that is kinda of cool is that features with N/A values (which we now have a lot of in training data) get grouped toward the outside of the image. The feature distance metric used here in Pearson correlation, after a min-max scaling, so anything with N/A values will become N/A. Revealing that in this scheme, the optimal shape of such an embedding is a circle and a not a square. However, we lose a lot of information, so i will go back and fill the N/A values with 0.5 to get a better comparison with the baseline.

Optimized Image with Filled N/A Values  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6719183de3625aace445f287a7e6e959fe2d3770.png)image491×418 12.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6719183de3625aace445f287a7e6e959fe2d3770.png> "image")

But why are we doing this? What do we hope to gain from this? My answer is that we believe that there are some interactive effects between features, similar to way there are interacting effects between the pixels of an image, which give rise to identification of more global structure. This is what we’re hoping to achieve here.

My initial attempt was to take a [ResNet](<https://arxiv.org/abs/1512.03385>) off the shelf and train it on these images, et voila. Reality wasn’t that simple, and what I found is that over-fitting happened almost immediately, and nothing was generalizable. This was a cool idea, which implemented the [Coral Ordinal](<https://arxiv.org/abs/1901.07884>) loss function for ordered classes. I will make a follow-up post about this.

Instead here I proposed to experiment with 1 convolutional filter, since this really captures the essence of what we are trying to achieve. A convolutional filter is a small (eg. 3x3) matrix, which is multiplied by each applicable (3x3) region of the image, and each multiplication results is one number. The result is an image of smaller size, often called a feature map. Here we have an example of a 3x3 uniform filter (all values are the same). For fun I visualize the effect of applying the filter once and then twice to the image. We can see this filter create a blurring effect, which makes sense. Each pixel in the feature map is a sum (or average) of the surrounding 9 pixels. This acts like a moving average over time.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7e944f47fa278ec74de94b082276dd6c3703ee10_2_690x194.jpeg)image850×239 48.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7e944f47fa278ec74de94b082276dd6c3703ee10.jpeg> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aa8c1641f3650c96576ae0a3e6cb8c34c5e9737b.png)image416×414 4.21 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aa8c1641f3650c96576ae0a3e6cb8c34c5e9737b.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ed691bf8bd58cde358a38445b824d6746a8c7774.png)image416×413 5.31 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ed691bf8bd58cde358a38445b824d6746a8c7774.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd22f29af8e5678f16aeb53c557e6ac5f10b073b.png)image416×413 10.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd22f29af8e5678f16aeb53c557e6ac5f10b073b.png> "image")

For the sake of simplicity, in this example, I then flatten the result of this feature map and feed it into a LightGBM Regressor, and compare the results of the baseline tabular data. The idea is to have a kind of apples-to-apples comparison of the new feature map to the original data. The general trend here is that correlation performance deteriorates, however as-does the correlation of the new predictions with the baseline predictions, which is something we are looking for. Finally we take a look at the correlation Sharpe to see if there is any added performance there.

Training is done on data before round 850, and test set is all eras afterward. Baseline uses the first 1521 features, and the IGTD uses the same features re-arranged into the image, then passed through the convolutional filter and flattened again.

**Results**

Correlation drops considerably from 0.033 to 0.025, however corr Sharpe stays strong going from 0.88 to 0.87, and the IGTD predictions are only 0.75 correlated with the baseline.

I have posted the entire working code in [my forked Github project here](<https://github.com/jefferythewind/IGTD>). Check for the [Jupyter notebook in the Scripts folder](<https://github.com/jefferythewind/IGTD/blob/jtw_lite/Scripts/IGTD%20with%20ConvNet%20-%20Forum%20Post.ipynb>).

**Update**

I just added [the default CNN implementation from the IGTD paper](<https://github.com/jefferythewind/IGTD/blob/jtw_lite/Scripts/Default%20CNN%20on%20Numerai%20IGTD%20Data.ipynb>) to my repo, you can find it here. The architecture is fairly basic as far as CNNs go, but interestingly it shows pretty decent performance out-of-the-box, especially compared to the ResNet that I had tried before. It’s very fitting since this is also a regression task.

With the default short training time, we’re able to attain 0.022 corr with Nomi target, compared to 0.033 baseline with LightGBM, while only having about 50% correlation with the baseline. This is very promising, and additional adjustments to the CNN architecture should yield some better results. Can we beat LGBM?!

**Discussion**

My intention with this post is to inspire some more creative research in this area. Indeed this is a topic that many Numerai modelers have found interesting, yet tough to tackle. Perhaps someone has some ideas about how to better apply more sophisticated ConvNet models to this idea, with some good reasons for that? I mentioned this line of research to a top vision neuropsychologist at the Université de Montréal. While interesting, he though the idea of applying a ResNet to this data was somewhat arbitrary, and rightly so. These aren’t human-readable images, so we shouldn’t expect human-inspired architectures to be able to decipher them. What kind of patterns would we hope to extract from these images and what would these tell us? Does translation/rotation invariance (one of the hallmarks of modern deep convnets) matter? Can we perhaps improve the IGTD to better fit our needs? Perhaps in order to make progress in this are we have to start thinking like a new kind of financial AI robot?

An interesting this to note here is that [a custom CNN framework](<https://www.nature.com/articles/s41598-021-90923-y/figures/3>) was developed in the original IGTD paper which was found to out-perform LightGBM in R2 score on the regression task of drug screening that was performed in the paper. It seems fitting to apply the proposed architecture as a next step in this research. However, there wasn’t a lot of explanation into why this particular architecture was chosen.

Per the update, we now have some decent performance coming from a CNN with this images. What I have in the back of my mind is that we could possible start experimenting with the [over-parametrized interpolating regime that has been the topic of considerable research](<https://arxiv.org/pdf/2201.02177.pdf>). It isn’t so straight-forward how this would work with LightGBM, but in the world of NNs and CNNs, it becomes a possiblity.

Happy modeling!

---

### Post #2 — **kenfus** | 2023-01-03 12:55 UTC

Very cool, fascinating and fun! But just to understand: The IGTP algo is “trained” on the whole set and the image is created per row? That is super interesting actually and I might give it a try.

---

### Post #3 — **jefferythewind** | 2023-01-03 15:06 UTC _(reply to #2)_

[@kenfus](</u/kenfus>) yes the IGTD* could be considered a pre-processing step, where we just use the input data. The result of the process is simply an index map file which tells you which feature should go into which which pixel location is the resulting image. The motivation is that similar features should be close together and non-similar features should be far apart in the resulting images. The notion of “similarity” is general, and in this case we use the Pearson correlation to judge how similar features are, and Euclidean distance to determine how close the pixels are.

It’s kinda tough to rationalize, since we know that correlations between features can change over time. It would be cool to make an improvement to the algo specifically for non-stationary financial data like we have.
