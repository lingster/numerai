---
title: "AutoEncoder and multitask MLP on new dataset (from Kaggle Jane Street)"
category: Data Science
url: https://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338
created_at: 2021-10-15T14:54:43.640000+00:00
last_posted_at: 2022-03-07T23:31:10.711000+00:00
posts_count: 31
views: 9996
tags: []
---

# AutoEncoder and multitask MLP on new dataset (from Kaggle Jane Street)

---

### Post #1 — **jrai** | 2021-10-15 14:54 UTC

The top submission to the Kaggle Jane Street competition winner posted their [models](<https://www.kaggle.com/gogo827jz/jane-street-supervised-autoencoder-mlp>) and some [discussion](<https://www.kaggle.com/c/jane-street-market-prediction/discussion/224348>). Numerai and that Kaggle competition are fairly similar using low signal market data and you can also use multiple targets to predict just one target on which you’re ultimately scored. The initial idea for this model architecture came from this [notebook](<https://www.kaggle.com/aimind/bottleneck-encoder-mlp-keras-tuner-8601c5>) and this [paper](<https://www.semanticscholar.org/paper/Deep-Bottleneck-Classifiers-in-Supervised-Dimension-Parviainen/fb86483f7573f6430fe4597432b0cd3e34b16e43>) (Deep Bottleneck Classifiers in Supervised Dimension Reduction).

The author of the initial code explains “The idea of using an encoder is to denoise the data.” The competition winner, [Yirun Zhang](<https://www.kaggle.com/gogo827jz>) explains the model really well (I’ve made a few edits so it’s more applicable to the Numerai dataset):

> **"Deep Learning Model:**
> 
>   * Use autoencoder to create new features, concatenating with the original features as the input to the downstream MLP model
>   * Train autoencoder and MLP together
>   * Add target information to autoencoder (supervised learning) to force it to generate more relevant features, and to create a shortcut for backpropagation of gradient
>   * Add Gaussian noise layer before encoder for data augmentation and to prevent overfitting
>   * Use swish activation function instead of ReLU to prevent ‘dead neuron’ and smooth the gradient
>   * Batch Normalisation and Dropout are used for MLP
>   * Only monitor the MSE loss of MLP instead of the overall loss for early stopping"
> 


Here is Yirun’s diagram:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7b930b5d5df7195e64d7ecc325293790af8b62c2.png)image732×546 8.84 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7b930b5d5df7195e64d7ecc325293790af8b62c2.png> "image")

The Numerai architecture is the same, but we can just use regression loss functions instead of classification loss functions (i.e. MSE instead of BCE). Also, we can use a different number of targets. For example, you can have the model predict all of the 20 day targets at once and then the final prediction would be the mean of all of those predictions. My artistic interpretation of how it would look for Numerai:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/43895a446aecfbaf5aaa6c8e3b13e6710a664c03_2_545x500.jpeg)image882×808 152 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/43895a446aecfbaf5aaa6c8e3b13e6710a664c03.jpeg> "image")

The model outputs 3 different vectors: 1) it tries to recreate the feature vector after passing through an autoencoder to compress the feature space into a latent space. 2) it uses the decoder from the autoencoder to try to predict the targets (so it can generate more relevant features in the latent space) and 3) it uses a normal MLP to try to predict the multiple targets at once which can be averaged or ensembled for a final prediction.

With some hyperparameter searches, slightly different from the ones in the code below, initial results on validation (with zero feature neutralization) look quite good and fairly different from the new data’s example predictions:

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f87e7c357b0fad2c7774f88e6f1b2eebf5cf65d3.png)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d84fc60a89f5b661829e6a927311b6c78749ad88_2_616x500.png)image705×572 65.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d84fc60a89f5b661829e6a927311b6c78749ad88.png> "image")

Next steps and other thoughts:

  * Tune hyperparameters with Optuna
  * Ensemble CV folds and multiple models
  * Try different combinations of loss functions and targets
  * Train each era as a batch (use tf.keras.utils.Sequence)
  * Try different combinations of ensembling the target outputs



Here is the modified code for Numerai predictions from Yirun’s notebook to get you started, but you may need a few dependencies and other variable definitions. There may be errors or things that can be done better, appreciate any input:
    
    
    def create_architecture(num_columns, num_labels, hidden_units, dropout_rates, lr=1e-3):
        tf.keras.backend.clear_session()
    
        inp = tf.keras.layers.Input(shape=(num_columns,))
        x0 = tf.keras.layers.BatchNormalization()(inp)
    
        encoder = tf.keras.layers.GaussianNoise(dropout_rates[0])(x0)
        encoder = tf.keras.layers.Dense(hidden_units[0])(encoder)
        encoder = tf.keras.layers.BatchNormalization()(encoder)
        encoder = tf.keras.layers.Activation("swish")(encoder)
    
        decoder = tf.keras.layers.Dropout(dropout_rates[1])(encoder)
        decoder = tf.keras.layers.Dense(num_columns, name="decoder")(decoder)
    
        x_ae = tf.keras.layers.Dense(hidden_units[1])(decoder)
        x_ae = tf.keras.layers.BatchNormalization()(x_ae)
        x_ae = tf.keras.layers.Activation("swish")(x_ae)
        x_ae = tf.keras.layers.Dropout(dropout_rates[2])(x_ae)
    
        out_ae = tf.keras.layers.Dense(num_labels, activation="sigmoid", name="ae_targets")(
            x_ae
        )
    
        x = tf.keras.layers.Concatenate()([x0, encoder])
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(dropout_rates[3])(x)
    
        for i in range(2, len(hidden_units)):
            x = tf.keras.layers.Dense(hidden_units[i])(x)
            x = tf.keras.layers.BatchNormalization()(x)
            x = tf.keras.layers.Activation("swish")(x)
            x = tf.keras.layers.Dropout(dropout_rates[i + 2])(x)
    
        out = tf.keras.layers.Dense(num_labels, activation="sigmoid", name="targets")(x)
    
        model = tf.keras.models.Model(inputs=inp, outputs=[decoder, out_ae, out])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
            loss={
                "decoder": tf.keras.losses.MeanSquaredError(),  # how does the decoder do on translating back to features
                "ae_targets": tf.keras.losses.MeanSquaredError(),  # how does the decoder do with predicting targets
                "targets": tf.keras.losses.MeanSquaredError(),
            },
        )
    
        return model
    
    targets = [
        "target_nomi_20",
        "target_jerome_20",
        "target_janet_20",
        "target_ben_20",
        "target_alan_20",
        "target_paul_20"
    ]
    
    model_name = f"keras_{datetime.now().strftime('%s')}"
    
    params = {
        "num_columns": len(feature_names),
        "num_labels": len(targets),
        "hidden_units": [96, 96, 896, 448, 448, 256],
        "dropout_rates": [
            0.035,
            0.035,
            0.4,
            0.1,
            0.4,
            0.3,
            0.25,
            0.4,
        ],
        "lr": 1e-4,
    }
    
    model = create_architecture(**params)
    
    history = model.fit(
        X =  train_data[feature_names].values
        y = [train_data[feature_names].values,
            train_data[targets].values,
            train_data[targets].values]
        epochs=1,
    )

---

### Post #2 — **yxbot** | 2021-10-15 15:51 UTC

I have been using DAE on the legacy dataset, but haven’t got around to tailor it for the new dataset, for what it is worth, here is the python class that I have been using in Pytorch:
    
    
    class Denoise_Autoencoder(nn.Module):
    def __init__(self, in_dimension, embedding_dimension=10):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Dropout(p=0.1),
            nn.Linear(in_dimension, 256),
            nn.BatchNorm1d(256),
            nn.Hardswish(),
            nn.Dropout(p=0.1),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.Hardswish(),
            nn.Dropout(p=0.1),
            nn.Linear(128, embedding_dimension),)
        self.decoder = nn.Sequential(
            nn.BatchNorm1d(embedding_dimension),
            nn.Hardswish(),
            nn.Dropout(p=0.1),
            nn.Linear(embedding_dimension, 128),
            nn.BatchNorm1d(128),
            nn.Hardswish(),
            nn.Dropout(p=0.1),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.Hardswish(),
            nn.Dropout(p=0.1),
            nn.Linear(256, in_dimension),)
    def forward(self, x):
        embedding = self.encoder(x)
        decode = self.decoder(embedding)
        return embedding, decode
    

from a crude first look, seems the only significant difference from Yirun’s approach is their use of Gaussian noise, which I shall try in due time.

Another departure of my own approach is that I extracted the features, concat them with original feature - it was ok with the old dataset, not sure about the new one - and run it via lightgbm on different tree models

---

### Post #3 — **jrai** | 2021-10-15 16:35 UTC _(reply to #2)_

The autoencoders look very similar. Are you training on an era by era basis?

There is a lot you can do with the latent space (using it as features for other models, concatenating it to a subset of features, etc.). The multitask training and combination with autoencoder being trained at the same time just seemed particularly elegant in this case.

---

### Post #4 — **yxbot** | 2021-10-15 16:41 UTC _(reply to #3)_

I kind of used a “stupid and dumb” approach, so feature generation with DAE is a completely separate step from training pipeline. I just extracted the middle layer - the last layer of the encoder - but for this, it became unsupervised learning and I do it on train+val+test- all in one go. I then use the DAE model to generate features for each live round.

On the actually model training under supervised learning context, i.e. with target, basically repeated CV on separated eras - I didn’t even do timesplit for any of my legacy models - they still do quite ok.

For the new dataset, yes I completely agree there are tones of things to try alongside this direction ![:slight_smile:](//forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #5 — **jrai** | 2021-10-15 16:45 UTC _(reply to #4)_

That is a good idea. For this model, the autoencoder could still be pre-trained or fine-tuned on train+val+test as well to leverage the full unsupervised data. Although it would add leakage in validation stats.

---

### Post #6 — **yxbot** | 2021-10-15 16:48 UTC _(reply to #5)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> Although it would add leakage in validation stats.

I doubt - this is Qinong’s abysmal diagnostics ![:joy:](https://emoji.discourse-cdn.com/twitter/joy.png?v=14)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/24a1718dd08c94f1f0d015fd8baaa50d77a5aca7.png)image291×510 17.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/24a1718dd08c94f1f0d015fd8baaa50d77a5aca7.png> "image")

---

### Post #7 — **hedgingcat** | 2021-10-16 18:50 UTC

Glad to see my solution being discussed here. The unsupervised autoencoder without label information can be trained on train+valid+test, however, the supervised version in my solution should take extra care due to label leakage. So, I trained it in every fold to prevent leakage.

BTW, the highlight in my winning solution is the sample weight training which gives a boost to both public and private scores. But I am not sure if it can be useful in Numerai.

---

### Post #8 — **sunkay** | 2021-10-19 08:14 UTC

The feature vector compressed by the encode is just another version of the original features, I don’t understand why it could makes the model better.

---

### Post #9 — **perfect_fit** | 2021-10-28 11:26 UTC

Nice! Was pretty blown away when I saw the 1st place solution for Jane Street. Last time I saw someone win a tabular Kaggle competition with pure NNs was [Porto Seguro 4 years ago, which also used denoising autoencoders](<https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629#250927>).

Very cool to see that you implemented this for Numerai [@jrai](</u/jrai>) ! [@hedgingcat](</u/hedgingcat>), nice to see that you are also part of the Numerai community! ![:wink:](//forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #10 — **luee** | 2021-10-28 15:13 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/hedgingcat/48/984_2.png) hedgingcat:

> BTW, the highlight in my winning solution is the sample weight training which gives a boost to both public and private scores. But I am not sure if it can be useful in Numerai.

Depending on your cross-val scheme I would be wary of adding the valid + test data in the autoencoder loop, you don’t want to test a model on data in 2018 that uses 2020 data for dimensionality reduction.

---

### Post #11 — **danzell** | 2021-11-08 08:25 UTC _(reply to #9)_

Here is some further autoencoder stuff. I used a DAE in TPS Jan 21 & Feb 21 Competitions @kaggle.  
Write up Jan:  
[link to write up](<https://www.kaggle.com/springmanndaniel/1st-place-turn-your-data-into-daeta>)

Write up Feb:  
[link to write up](<https://www.kaggle.com/c/tabular-playground-series-mar-2021/discussion/229868#1259091>)

---

### Post #12 — **stoicism** | 2021-12-23 12:17 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> Use autoencoder to create new features, concatenating with the original features as the input to the downstream MLP model

Can anyone explain this? Autoencoder is a lower dimensional representation of the original features, how concatenating those contribute to improved performance by the MLP?

---

### Post #13 — **jrai** | 2021-12-23 14:43 UTC _(reply to #12)_

The autoencoder is trying to do dimensionality reduction (compression), and in that goal it may be doing noise reduction. The jargon to describe this autoencoder is a bottleneck denoising autoencoder. There’s a bunch of prior literature on why it might be beneficial to create a latent space for training a downstream model and to “learn” feature engineering. You may not even have to concatenate the latent space to the original features, you can also experiment with just using the latent space as features (at which point you should also still learn it end to end).

Here are a couple of articles and quotes from them:

“With this approach, our model isn’t able to simply develop a mapping which memorizes the training data because our input and target output are no longer the same. Rather, the model learns a vector field for mapping the input data towards a lower-dimensional manifold (recall from my earlier graphic that a manifold describes the high density region where the input data concentrates); if this manifold accurately describes the natural data, we’ve effectively “canceled out” the added noise.”

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/54a203077095d5037c45efc09b56f148760c207c.png) [Jeremy Jordan – 19 Mar 18](<https://www.jeremyjordan.me/autoencoders/> "04:25AM - 19 March 2018")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/54225e848add73ef21870edb85a011c27b407df9_2_690x251.jpeg)

### [Introduction to autoencoders.](<https://www.jeremyjordan.me/autoencoders/>)

Autoencoders are an unsupervised learning technique in which we leverage neural networks for the task of representation learning. Specifically, we'll design a neural network architecture such that we impose a bottleneck in the network which forces a...

“**Autoencoders are used for Noise Removal:** If we can pass the noisy data as input and clean data as output and train an autoencoder on such given data pairs, trained Autoencoders can be highly useful for noise removal. This is because noise points usually do not have any correlations. Now, as the autoencoders need to represent the data in the lowest dimensions, the encodings usually have only the important relations there exists, rejecting the random ones. So, the decoded data coming out as output of an autoencoder is free of all the extra relations and hence the noise.”  
<https://towardsdatascience.com/introduction-to-autoencoders-7a47cf4ef14b>

---

### Post #14 — **stoicism** | 2021-12-23 20:06 UTC _(reply to #13)_

Thanks for the references, much appreciated. I am familiar with Autoencoders and their noise reduction capability. I was just wondering how appending the encoded features with the original one provides performance boost. What if we don’t append at all and only use the encoded and denoised features only? I have seen several examples where the features were reduced based on correlation matrix. I also have seen examples where PCA was used to claimed to not have performed well, probably since PCA only accounts for linear relationships where autoencoders are much more general.

---

### Post #15 — **gbrecht** | 2021-12-25 10:40 UTC _(reply to #14)_

I fed my DAE features to the example model and the results were very bad. Maybe my DAE was bad, but it made me ditch the idea of training on reduced features only

---

### Post #16 — **olivepossum** | 2022-01-01 09:14 UTC

Thanks for sharing [@jrai](</u/jrai>), super interesting!  
I’ve tried to port to PyTorch the architecture mentioned in the post (not much success in terms of performance but nothing tuned yet). The code is quite verbose but should behave very similar than the the Keras one.  
Not a PyTorch expert (as you’ll notice looking at the code) so any feedback, suggestion, correction or bug spotted is very appreciated.

The architecture looks like this:
    
    
    targets = ["target_nomi_20", "target_jerome_20", "target_janet_20", "target_ben_20", "target_alan_20", "target_paul_20"]
    inp = len(feature_names) 
    targets_len = len(targets)
    
    hidden_units = [96, 96, 896, 448, 448, 256]
    dropout_rates = [0.035, 0.035, 0.4, 0.1, 0.4, 0.3, 0.25, 0.4]
    lr = 0.0001
    
    concatenated_input = inp + hidden_units[0]
    
    class AEMLP(nn.Module):
      def __init__(self):
          super(AEMLP, self).__init__()
    
          #encoder
          self.gaussian_noise = GaussianNoise(dropout_rates[0])
          self.batchnorm1_encoder = nn.BatchNorm1d(inp)
          self.linear_encoder = nn.Linear(inp, hidden_units[0], bias=True)
          self.batchnorm2_encoder = nn.BatchNorm1d(hidden_units[0])
          self.hardswish = nn.Hardswish()
    
          #decoder
          self.dropout_decoder = nn.Dropout(dropout_rates[1])
          self.linear_decoder = nn.Linear(hidden_units[0], inp, bias=True)
    
          #x_ae - decoder predicting targets
          self.linear_x_ae = nn.Linear(inp, hidden_units[1], bias=True)
          self.batchnorm_x_ae = nn.BatchNorm1d(hidden_units[1])
          self.dropout_x_ae = nn.Dropout(dropout_rates[2])
          self.linear_out_ae = nn.Linear(hidden_units[1], targets_len, bias=True)
          self.sigmoid_x_ae = nn.Sigmoid()
    
          #x - mlp predictions
          self.batchnorm1_x = nn.BatchNorm1d(concatenated_input)
          self.dropout_x1 = nn.Dropout(dropout_rates[3])
    
          self.layers = nn.ModuleList()
          prev_dim = concatenated_input
          for i in range(2, len(hidden_units)):
              self.layers.append(nn.Linear(prev_dim, hidden_units[i], bias=True))
              self.layers.append(nn.BatchNorm1d(hidden_units[i]))
              self.layers.append(nn.Hardswish())
              self.layers.append(nn.Dropout(dropout_rates[i + 2]))
              prev_dim = hidden_units[i]
    
          self.linear_x_out = nn.Linear(prev_dim, targets_len, bias=True)
          self.sigmoid_x = nn.Sigmoid()
    
          #init linear layers
          torch.nn.init.xavier_uniform_(self.linear_encoder.weight)
          torch.nn.init.xavier_uniform_(self.linear_decoder.weight)
          torch.nn.init.xavier_uniform_(self.linear_x_ae.weight)
          torch.nn.init.xavier_uniform_(self.linear_out_ae.weight)
          torch.nn.init.xavier_uniform_(self.linear_x_out.weight)
          for layer in self.layers:
            if isinstance(layer, nn.Linear):
                torch.nn.init.xavier_uniform_(layer.weight.data)
                if layer.bias is not None:
                    torch.nn.init.zeros_(layer.bias)
    
      def forward(self, inpu): 
          #encoder 
          x0 = self.batchnorm1_encoder(inpu)
    
          encoder = self.gaussian_noise(x0)
          encoder = self.linear_encoder(encoder)
          encoder = self.batchnorm2_encoder(encoder)
          encoder = self.hardswish(encoder)
    
          #decoder 
          decoder = self.dropout_decoder(encoder)
          out_decoder = self.linear_decoder(decoder)
    
          #x_ae 
          x_ae = self.linear_x_ae(out_decoder)
          x_ae = self.batchnorm_x_ae(x_ae)
          x_ae = self.hardswish(x_ae)
          x_ae = self.dropout_x_ae(x_ae)
          x_ae = self.linear_out_ae(x_ae)
          out_ae = self.sigmoid_x_ae(x_ae)
    
          #mlp predictions 
          x = torch.cat((x0, encoder), 1)
          x = self.batchnorm1_x(x)
          x = self.dropout_x1(x)
    
          for layer in self.layers:
            x = layer(x)      
          x = self.linear_x_out(x)
          out = self.sigmoid_x(x)
    
          return out_decoder, out_ae, out
    

Then we need three loss functions:
    
    
    func_loss_out_decoder = nn.MSELoss().cuda()
    func_loss_out_ae = nn.MSELoss().cuda()
    func_loss_out = nn.MSELoss().cuda()
    

Iterations over epochs and batches calculating the global loss would look like this (just included the relevant part of the loop code):
    
    
    for epoch in epochs:
          for era in eras:  
                batch_count += 1
                x, y = get_data(era)
                out_decoder, out_ae, out = aemlp(x)
                loss_out_decoder = func_loss_out_decoder(out_decoder, x)
                loss_out_ae = func_loss_out_ae(out_ae, y)
                loss_out = func_loss_out(out, y)
                loss = (loss_out_decoder + loss_out_ae + loss_out)/3
                loss.backward()
                optimizer.step() 
          acc_loss_train += loss
    loss_train = acc_loss_train / batch_count
    check_early_stopping(validation_data)
    

In early stopping, just use func_loss_out to calculate the loss.

Finally, a class to generate Gaussian Noise:
    
    
    class GaussianNoise(nn.Module):
        def __init__(self, sigma=0.1, is_relative_detach=True):
            super().__init__()
            self.sigma = sigma
            self.is_relative_detach = is_relative_detach
            self.register_buffer('noise', torch.tensor(0))
    
        def forward(self, x):
            if self.training and self.sigma != 0:
                scale = self.sigma * x.detach() if self.is_relative_detach else self.sigma * x
                sampled_noise = self.noise.expand(*x.size()).float().normal_() * scale
                x = x + sampled_noise
            return x

---

### Post #17 — **gbrecht** | 2022-01-01 20:52 UTC

I hope it is okay to ask a few questions.

  1. Do I understand correctly that your encoder does Normalization => Noise => Linear ==> Normalization ==> Activation ? If so, why two times activation? Do you think one layer is enough?
  2. Is there a special reason your decoder is not a mirror of your encoder?
  3. Why no normalization on the decoder?



I am sure I have more once I understand more, thx

---

### Post #18 — **maxchu** | 2022-01-01 23:15 UTC _(reply to #16)_

Can you reproduce the same validation result as [@jrai](</u/jrai>) ?

---

### Post #19 — **olivepossum** | 2022-01-01 23:58 UTC _(reply to #18)_

At the moment, not at all. There might be something wrong in my code

---

### Post #20 — **jrai** | 2022-01-02 16:12 UTC _(reply to #17)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gbrecht/48/3456_2.png) gbrecht:

>   1. Do I understand correctly that your encoder does Normalization => Noise => Linear ==> Normalization ==> Activation ? If so, why two times activation? Do you think one layer is enough?
>   2. Is there a special reason your decoder is not a mirror of your encoder?
>   3. Why no normalization on the decoder?
> 


These architecture questions are probably better for [@hedgingcat](</u/hedgingcat>) and I’d also be curious to hear thoughts from [@jrb](</u/jrb>) or [@mdo](</u/mdo>)

![](https://avatars.discourse-cdn.com/v4/letter/m/dec6dc/48.png) maxchu:

> Can you reproduce the same validation result as [@jrai](</u/jrai>) ?

The validation results I posted are after a fair amount of hp tuning, playing with different loss functions, number of layers, etc (so it’s also possible the validation results are just wildly overfit). I think the code provided is a very good starting point though.

---

### Post #21 — **maxchu** | 2022-01-02 22:22 UTC _(reply to #20)_

[@olivepossum](</u/olivepossum>) correct me if I am wrong, the additive Gaussian noise seems not the same as the TensorFlow one. The sigma should be absolute rather than relative?

[@jrai](</u/jrai>) thanks for the comments. I thought you just do CV on the hp in “params”. I have also tried DenseNet and “autofeature” (similar to autoencoder but uses subnetwork to predict masked features), i need to use differential spearman corr to get reasonable results. Using MSE is not very good in my previous network. I have also added a bunch of different losses like maximizing MMC for example prediction, minimizing feature exposure.

---

### Post #22 — **gbrecht** | 2022-01-03 19:39 UTC

How many epochs do you train before you see the loss going down? On my potato PC I trained for 10 epochs and the loss of the provided code is just stationary

---

### Post #23 — **jrai** | 2022-01-04 00:23 UTC _(reply to #22)_

the loss should go down right away if everything is flowing correctly

---

### Post #24 — **olivepossum** | 2022-02-27 08:56 UTC _(reply to #23)_

[@jrai](</u/jrai>) did you manage to get good live results with this architecture? With my ‘port’ to pytorch I managed to get good val but I guess I have used way too much that data.

---

### Post #25 — **jrai** | 2022-02-27 15:13 UTC _(reply to #24)_

No unfortunately not yet. Here’s one account with this MLP + AE architecture plus feature neutralization: [Numerai](<https://numer.ai/crowdcent_cu2xa8>). It started off looking promising. It’s definitely easy to overfit and that’s likely what I did, but I also like the model’s metamodel correlation. It may still have some good performance in different regimes. Also just rolling out some other models to test this architecture with other parameters.

---

### Post #26 — **jefferythewind** | 2022-03-07 14:34 UTC

Hi [@olivepossum](</u/olivepossum>) I just noticed your pytorch implementation, that’s great. I am going to try the code, but I did notice something in your training loop. At the beginning of each iteration, you need to call `optimizer.zero_grad()` at the top. Pytorch by default accumulates gradients, so what you’re doing here is adding the gradients to the previous values at each step and back propagating, which isn’t usually what we want. For most vanilla MLP style optimization, we need to call `zero_grad` at the top to set all the gradients back to zero before computing the loss.

---

### Post #27 — **jefferythewind** | 2022-03-07 14:52 UTC

Just in general of considering and comparing alternate models, we should always look at cross validation scores. This way we compare out-of-sample performance on as much data as possible. After a long journey I’m fairly convinced that this is really the only way to do it. For neural nets I find it always adds a layer of complexity to the algo, since you need to automate things like how long you train for or early stopping. The training time should even be optimized for. I think this is the only way to objectively do it. If we’re tuning the model by just looking at validation performance after fitting to training data, we can’t tell if the improved performance works on other folds of the data or just validation.

---

### Post #28 — **olivepossum** | 2022-03-07 15:02 UTC _(reply to #26)_

You mean it should look like this right?
    
    
    for epoch in epochs:
          for era in eras:  
                batch_count += 1
                x, y = get_data(era)
                out_decoder, out_ae, out = aemlp(x)
                loss_out_decoder = func_loss_out_decoder(out_decoder, x)
                loss_out_ae = func_loss_out_ae(out_ae, y)
                loss_out = func_loss_out(out, y)
                loss = (loss_out_decoder + loss_out_ae + loss_out)/3
                optimizer.zero_grad()
                loss.backward()
                optimizer.step() 
          acc_loss_train += loss
    loss_train = acc_loss_train / batch_count
    check_early_stopping(validation_data)

---

### Post #29 — **jefferythewind** | 2022-03-07 15:14 UTC _(reply to #28)_

yes exactly. I might just put it all the way at the top for good measure but I think that yes that should work.

---

### Post #30 — **jefferythewind** | 2022-03-07 19:17 UTC

So what is the target `y` supposed to be? A vector with all the targets?

**EDIT** More importantly what shape data should I feed to `aemlp`? I have it instantiated here but when I try to feed it one era of data, I throughs errors about the shape of the data, and I can’t reshape it to work at the moment.

---

### Post #31 — **maxchu** | 2022-03-07 23:31 UTC _(reply to #30)_

In PyTorch, the first dimension needs to be the same, so I will suggest you use the number of eras as batch size (1st dimension), then the second dimension is the number of stock and the last dimension as feature dimension.
