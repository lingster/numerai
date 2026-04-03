---
title: "What is good models for numerai signals?"
category: Signals
url: https://forum.numer.ai/t/what-is-good-models-for-numerai-signals/5508
created_at: 2022-06-16T10:47:34.102000+00:00
last_posted_at: 2022-10-05T21:47:04.808000+00:00
posts_count: 16
views: 3458
tags: []
---

# What is good models for numerai signals?

---

### Post #1 — **habakan** | 2022-06-16 10:47 UTC

Hi, Numerai Community!  
I share my model approach and its insight, because of changing phases of signals.  
My best performance model is [habakan_x](<https://signals.numer.ai/habakan_x>), and achieved LB top of 1year return([habakan](<https://signals.numer.ai/habakan>), top of 1year return model has almost submitted prediction of habakan_x).  
But monitoring mmc and IC, I don’t think this model is good for TC.  
So I think sharing is no-problem for me and good for the community.  
This content was prepared after a discussion with katsu-san. (Thanks [@katsu1110](</u/katsu1110>) for your advice and discussion!)

**Summary**

  * habakan_x add only the following pipelines to [kaggle starter notebook](<https://www.kaggle.com/code/code1110/numeraisignals-starter-for-beginners/notebook>) by katsu(model is katsu1110_edelgard) 
    * statisticaly denoising of data
    * binning
  * comparing live performance between habakan_x and katsu1110_edelgard 
    * Both of IC was correlated, but Corr is lower 
      * Neutralization is influenced by denoising and binning
    * Analysis of Corr and IC for each model 
      * habakan_x is a lower correlation between Corr and IC than katsu1110_edelgard
    * habakan_x is pretty low TC, and katsu1110_edelgard is high



**About My model: habakan_x**  
It’s jnot need to explan detail about my model. Because my model(habakan_x) is based of signals starter notebook published by katsu(model is [katu1110_edelgard](<https://signals.numer.ai/katsu1110_edelgard>)).  
And habakan_x is added only pipeline to katu1110_edelgard.

  * Denoising data using basic statistical outlier detection
  * binning (num of bin is 9: no particular reason)



This approach is not bad for signals task handling noisy data.  
As a result, this model is good performance than my model added unique feature.  
I want to comparing katsu1110_edelgard, so feature, classifier and hyperparmeter is same.

**Comparing habakan_x and katsu1110_edelgard**  
Analysis of comparing both models (same feature and classifier) are interesting insights.  
Data for analysis can collect by live perfomane of models.

The following is each metrics of statistics.

| Corr Mean | Corr Sharpe | MMC Mean | IC Mean  
---|---|---|---|---  
habakan_x | 0.0247 | 1.1160 | 0.0177 | -0.0090  
katsu1110_edelgard | 0.0152 | 0.5704 | 0.0105 | -0.0178  
  
This metrics can conclude that corr of habakan_x is better than katsu1110_edelgard, but it is more interesting to focus IC.

**Analysis of IC**  
The figure1 is both of IC transition.(Round 289 ~ 307)  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a1c4f16761750926d097dccc607b128299fd5573.png)730×195 5.88 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a1c4f16761750926d097dccc607b128299fd5573.png>)

  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1ced2c7eabaef9213a43395cadba9bc8ba1f5b0f.png)730×195 5.88 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1ced2c7eabaef9213a43395cadba9bc8ba1f5b0f.png>)

  
Figure1: IC transition habakan_x (top) katsu1110_edelgard (bottom)

In terms of qualitative, transition of IC is very similar.  
Also, figure2 is mapping both of metrics(IC, Corr) and correlation analysis.  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e30931b5a3ebe58bb26c72295b1d87ed062c5ee6_2_690x207.png)2132×642 132 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e30931b5a3ebe58bb26c72295b1d87ed062c5ee6.png>)

  
Figure2: habakan_x and katsu1110_edelgard metrics Mapping Corr（Left）, IC（Right）

R2 of IC is over 0.89, but R2 of Corr is 0.69.  
IC result is make sense because mean correlation both of validation prediction is 0.89.  
Considering the result, neutralization of signals may be influenced by even denoising or binning proccessing.

**Relashionship of IC and Corr for each models**  
Above experiment was analysis of relashionships of models.  
Next experiment is analysis Corr and IC (same model).  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7dadf436a544f330f98cf4acbd1361c12ae37e08_2_690x213.png)2142×662 106 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7dadf436a544f330f98cf4acbd1361c12ae37e08.png>)

  
Figure3: Corr and IC Mapping habakan_x（Left）, katsu1110_edelgard（Right）

R2 of IC and Corr in katsu1110_edelgard is 0.323, in habakan_x is 0.065.  
It is difficult to conclude using only this result, because these R2 are depended on latent variables those are inclusion rate of alpha and neutralization factor.  
But, it is very strange that there is a difference by only denoising or binning.

**Analysis of TC**  
Monitoring TC, there is a difference rank TC.  
habakan_x: 2713  
katsu_edelgard: 234  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5d06583c3e9497bc535c08ceb2ab205d7d798104_2_690x151.png)1820×400 38.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5d06583c3e9497bc535c08ceb2ab205d7d798104.png>)

  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1e60070c7997827686fd6a7e3f0cc2fdb8225e59_2_690x151.png)1820×400 33 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1e60070c7997827686fd6a7e3f0cc2fdb8225e59.png>)

  
Figure4: TC transition habakan_x (top) katsu1110_edelgard (bottom)

Cumulative of TC seems to be reverse trend.  
I have not analysis deeply, TC is also change by denoising or binning.  
Honestly, I’m not very serious this result, because I thought this model is “not uniqueness but good perfomance”.  
I felt good for valid information result rather than😂

I think It is good that TC is based on Numerai performance.  
But, It is also important to feedback the result of signals modeling.  
Is above of analysis and result make sense to Numerai Competitor and supporter?  
I hope this thread is a chance to share ideas of signals for communiy.  
Thank you!

---

### Post #2 — **annon** | 2022-06-17 06:51 UTC

Hello habakan san,

Awesome analysis as usual.

If the data removed by denoising (or binning) was actually important data for TC improvement,  
I think that is something success of pick-up-TC-essence.

And IC seems to be mainly contained in un-denoised (majority) data.

To improve TC, Is there any possibility to give weight or  
focus on the data that is to be denoised when perform learning?

Sorry if my comment is out of line. Since I am terrible ossan novice,  
I don’t know about denoising at all.

(If you give me some reference or example of denoising (Japanese OK), That would be great.)

---

### Post #3 — **habakan** | 2022-06-17 13:13 UTC _(reply to #2)_

Thanks, comments!! And, your insights on twitter are always helpful for me!

Unfortunately, my model(habakan_x) has lower TC performance(rank is 2713) than katsu1110_edelgard(rank is 234).  
So, denoising or binning approaches may be bad for TC.

My denoising approach is extracting data using quantile 1% ~ 99% in each feature.  
This is sample script.
    
    
    upper_thresh = 0.99
    lower_thresh = 0.01
    
    feature_df = df.copy()
    for feature in features:
        upper_q = df[feature].quantile(upper_thresh)
        lower_q = df[feature].quantile(lower_thresh)    
        feature_df = feature_df.query('@lower_q < ' + feature + ' < @upper_q')
    

If you want to use more techniques about denoising, it may be good to survey anomaly detection or outlier detection.  
This approach is very simple, but based on “Mahalanobis distance” and Hotelling’s T^2.

![](https://scikit-learn.org/stable/modules/outlier_detection.html/../_static/favicon.ico) [scikit-learn](<https://scikit-learn.org/stable/modules/outlier_detection.html>)

### [2.7. Novelty and Outlier Detection](<https://scikit-learn.org/stable/modules/outlier_detection.html>)

Many applications require being able to decide whether a new observation belongs to the same distribution as existing observations (it is an inlier), or should be considered as different (it is an ...

But, I think more influence to Corr, MMC, or TC is binning, because denoising approach is only change little data as above.  
And the point of TC is calculated using select signals from predction likely TB200, not using all signals of prediction.  
I think Getting low TC and high Corr means correlation of signals not using in TC is just good.  
So, Binning may be removing signals contributed by TC.

---

### Post #4 — **annon** | 2022-06-17 22:08 UTC _(reply to #3)_

Thank you very much for your response and example.  
Your through explanation is very logical and make sense even for osssan novice.

I could think of two items that are lost in the binning and denoising.

One is outlier, and the other is distribution (nonlinear component).

Both binning and denoise discard outliers in a sense.  
Also, if the type of binning is like qcut() and its labeling value are equally spaced,  
The distribution information of original data would be lost.

Regarding classic tournament, the data is binned and its distribution is Gaussian.  
It seems that some distribution remains, but some information might be discarded.

Perhaps such distribution information would be useful to complement something lost in the classic data.  
(though signals and classic targets are different and things are not so simple…)

To verify this issue, it might be good to compare different type of binning.(remains distribution or not)

---

### Post #5 — **habakan** | 2022-06-18 02:53 UTC _(reply to #4)_

Using binning, the data is changed distribution like your idea, and reduced cardinality.  
I tried to change num of binning, but 5 ~ 20 bins seems to be no change for TC.  
I have not tried more than above bins.

---

### Post #6 — **annon** | 2022-06-18 03:56 UTC _(reply to #5)_

I just noticed that my signals models are also doing 7 bins qcut and its distribution information was completely lost.

According to my program which was written by me before,  
I am not using katsu san’s starter, but using similar technical features.

And I also noticed that My model’s TC is poor, so I will make some models with different type of binning (keep some distribution) and see if TC improves.

I will inform you if I get any feedback in the future.

Thank you for your valuable insights!

---

### Post #7 — **arnokha** | 2022-07-05 16:54 UTC

Just anecdotal, but I have a similar example. Very similar on all metrics except TC:  
<https://signals.numer.ai/zenith_10>  
<https://signals.numer.ai/cognac>

The “shape” of the TC lines is similar, but the magnitude is different.

---

### Post #8 — **olivepossum** | 2022-08-02 08:30 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/habakan/48/2594_2.png) habakan:

> 
>     upper_thresh = 0.99
>     lower_thresh = 0.01
>     
>     feature_df = df.copy()
>     for feature in features:
>         upper_q = df[feature].quantile(upper_thresh)
>         lower_q = df[feature].quantile(lower_thresh)    
>         feature_df = feature_df.query('@lower_q < ' + feature + ' < @upper_q')
>     

Hi [@habakan](</u/habakan>), thanks for sharing, really interesting insights! Did you do this part of denoising data on a per ticker base for each feature or you remove the quantiles for each feature taking into account all the tickers at once?

Thanks.

---

### Post #9 — **habakan** | 2022-08-04 10:55 UTC _(reply to #8)_

[@olivepossum](</u/olivepossum>)  
Thanks, comments!  
My approach is denoising using all tickers.  
The purpose of the denoise is to remove records that included specific outlier by y-finance source.  
Also, denoise is processed before binning.

---

### Post #10 — **olivepossum** | 2022-08-04 12:07 UTC _(reply to #9)_

Thanks for the answer [@habakan](</u/habakan>). But then, if you do not do it on a per ticker basis but with all tickers at the same time… You could have false positives and false negatives due to having different currencies?  
I’m thinking if it could make sense this anomaly detection “grouping by” currency or any other field

---

### Post #11 — **habakan** | 2022-08-05 03:14 UTC _(reply to #10)_

Thank you, [@olivepossum](</u/olivepossum>).  
I think so too in the case that denoising for the price of ticker like close price.  
But this approach is the calculation for features.  
Features of the starter are technical indicators that are calculated time-series relatively, so I assumed those distributions are not quite different for each ticker.  
However as you think, I cannot say this approach doesn’t have false positives and negatives.

In the first place, it may be solved by detecting outliers using price data, but removing the price record we have to design how to interpolate.  
I judged it seems to be complex for me as a baseline model.

The following figures are visualizations of the histogram before/after denoising.

before denoising  


[![before_denoising](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/01aea19206044eb0debe5feac83017769412269f_2_500x500.png)before_denoising1432×1432 64.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/01aea19206044eb0debe5feac83017769412269f.png> "before_denoising")

after denoising  


[![after_denoising](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d64943f538a59b01391fe59b9d3d0d8494550f33_2_499x500.png)after_denoising1431×1432 77.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d64943f538a59b01391fe59b9d3d0d8494550f33.png> "after_denoising")

---

### Post #12 — **olivepossum** | 2022-08-05 07:26 UTC _(reply to #11)_

thanks [@habakan](</u/habakan>), now I got it! And thanks for the chart, is also self explanatory! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #13 — **mattiasl** | 2022-09-28 10:23 UTC

[@habakan](</u/habakan>) Thanks for sharing. Your post has made me think quite a bit.

One thing I don’t understand is why is denoising necessary for you if you are using binning afterwards? It looks like your denoising simply transforms a very unbalanced distribution into a somewhat “normal” bell curve distribution. You then use these bell curve distributions to populate your bins.

From my perspective, the main purpose of denoising should be outlier detection/rectification. With binning, if you have 9 bins, the outliers automatically get put in bin 1 or bin 9 - the bins on the edge. This happens whether you de-noise or not?

The bigger question for me in terms of outlier feature detection / rectification, does it make more sense to do what I described above, or does it make more sense to scrap completely that outlier value and create some kind of model to guesstimate what that value should be based on all the other feature values (a best estimate of some sort). Such a methodology would have the advantage of often bringing back an outlier feature value in the middle bins instead of being on the outer edges. This might have a stabilizing effect on both the training process and predictions.

---

### Post #14 — **habakan** | 2022-09-29 14:46 UTC _(reply to #13)_

[@mattiasl](</u/mattiasl>)  
Thanks for your comment!  
As a premise, this method is a purpose of only baseline.  
And, it is not probably the best way to improve performance.

> With binning, if you have 9 bins, the outliers automatically get put in bin 1 or bin 9 - the bins on the edge. This happens whether you de-noise or not?

What I mean by denoise is “detecting outliers among the features and deleting the records”.  
So, I don’t convert outlier value to proper value.  
I may not understand your questions completely, outlier value does not binning because of removing records including outliers.  
Since the binning process I used has a smaller sample ratio of 0, 1 compared to other bins, if outliers are converted to 0, 1 binning, the outlier records may have a significant impact on training, which I considered undesirable, so I deleted them instead of binning.  
But, I think outliers don’t have an strong impact on binning other data, same the calculation of median.

As you said, converting outliers to neutral(0.5) or interpolating using statistical methods may be the choice for improving performance.  
What I was thinking at the first time prediction of financial machine leraning task is almost noise(corr 0.03 at the best) comparing other machinlearning task, and y-finance is included some noise.  
So, I thought baseline is proper that training using completely observed data than interpolating in perspective p(X_missed | X_observed) or training all data without thinking.  
I’m very interested in how to interpolate.

---

### Post #15 — **mattiasl** | 2022-10-01 06:18 UTC _(reply to #14)_

Now I understand. You delete the whole row if it’s considered an outlier in the multidimensional space. You are not talking about outliers at a feature by feature level. I haven’t really thought about that but it somewhat makes sense to delete the entire row/record in these cases as it’s the entire occurrence that is an outlier. Though, I guess one has to be careful to set the threshold very low (1% or below) as in finance it’s often the outliers in the top/bottom 5% that determine your outperformance/underperformance in a large portfolio. If there’s a typical set-up for stocks that often outperform the pack by 5% or more, you don’t want your model to miss that! At least you probably want to remove the significant outliers in terms of features, and not of targets!

Yes, I believe interpolation techniques and de-noising can lead to significant model outperformance. I’m going to try to learn how to use auto-encoders to denoise features. The idea is to use neural network to essentially look at each feature and interpolate that feature based on all the other features. There’s a high probability that such de-noising can improve the training efficiency of our models.

Autoencoders in 2 minutes: [What is an Autoencoder? | Two Minute Papers #86 - YouTube](<https://youtu.be/Rdpbnd0pCiI>)

There was a winning solution on Kaggle’s Jane Street competition that used such an auto-encoder to denoise data.

Thanks for helping me think differently about this interesting problem!

---

### Post #16 — **olivepossum** | 2022-10-05 21:47 UTC _(reply to #15)_

[@mattiasl](</u/mattiasl>) you might be interested in this post [AutoEncoder and multitask MLP on new dataset (from Kaggle Jane Street)](<http://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338>)

Best,
