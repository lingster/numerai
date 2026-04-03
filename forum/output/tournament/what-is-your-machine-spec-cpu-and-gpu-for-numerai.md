---
title: "What is your machine spec(CPU and GPU) for NUMERAI?"
category: Tournament
url: https://forum.numer.ai/t/what-is-your-machine-spec-cpu-and-gpu-for-numerai/5737
created_at: 2022-10-01T06:17:10.794000+00:00
last_posted_at: 2022-10-28T00:06:09.519000+00:00
posts_count: 29
views: 2181
tags: []
---

# What is your machine spec(CPU and GPU) for NUMERAI?

---

### Post #1 — **ryo_matsuzaka** | 2022-10-01 06:17 UTC

I am just curious about it.

---

### Post #2 — **jacob_stahl** | 2022-10-01 20:38 UTC

GPU : gtx 1080  
CPU : Ryzen 3700 8 core  
RAM : 128gb

I’m probably going to get an rtx 4090 when those come out

---

### Post #3 — **ryo_matsuzaka** | 2022-10-02 02:13 UTC

Thank you very much.  
Similar spec as mine(5900HX, RTX2080, 64GBRAM).  
I am also considering to upgrade it.

---

### Post #4 — **gammarat** | 2022-10-02 03:11 UTC

11th Generation Intel Core i9-11900K @3.50GHz, 16 Logical processors  
64 GB memory  
NVidia GeForce RTX 3070

I don’t use the RTX 3070 processor much for Numerai, as most of my processing is non-linear.

---

### Post #5 — **ryo_matsuzaka** | 2022-10-02 03:33 UTC

Thank you very much.  
Also I mainly use CPU now.

---

### Post #6 — **by256** | 2022-10-02 19:10 UTC

CPU: Intel i7-9800X, 3.80GHz 16 cores  
GPU: RTX 3090  
RAM: 128 GB

---

### Post #7 — **david_plutus** | 2022-10-02 19:12 UTC

CPU: Intel i9-7900X (10 core, @3.3 GHz)  
GPU: NVIDIA Geforce RTX 3090  
RAM: 64 GB  
built in early 2020; GPU upgrade in 2022; RAM upgrade in 2021 (32->64).

training and predicting neural networks on the GPU, xgboost training on GPU but prediction on CPU (due to too high memory usage even for the 3090).  
Was first hesitant with the 3090 because of price, now I’m very happy with it, mainly due to the fast iteration on modeling ideas. Came from a GTX 1060 6 GB.

Besides Numerai I use the workstation for trying out other heavy compute things like simulations, or deep learning generated images like from Stable Diffusion model.

---

### Post #8 — **dzheng1887** | 2022-10-06 21:25 UTC

i7-6800k, gtx 1070, 128 GB of ram, recently upgraded from 64 earlier this year!

---

### Post #9 — **ryo_matsuzaka** | 2022-10-07 13:22 UTC _(reply to #8)_

Currently 64 GB is enough for me. The reason you increased the RAM is 64GB is not enough for you?

---

### Post #10 — **dzheng1887** | 2022-10-07 13:58 UTC _(reply to #9)_

Yeah I probably could’ve been smarter about some things but yeah I ran out of ram when I was modeling with XGBoost and I’m too lazy to get it working with less memory.

---

### Post #11 — **shatteredx** | 2022-10-07 16:06 UTC _(reply to #10)_

I currently use Google Colab Pro+ which has some sort of Intel Xeon, 50GB RAM, and an Nvidia Tesla V100. Occasionally I get lucky and score an A100 instance.

Yes, XGBoost is very greedy with memory, especially on Windows. It can easily run out of memory even with 64GB on the full v4 dataset.

For some reason, XGBoost behaves better under Linux with less “out of memory” scenarios. I am not sure why.

In my experience, LightGBM can handle twice as much data as XGBoost using the same amount of RAM.

EDIT: Google is now enforcing a credit system with Colab, can’t use their high end GPUs nonstop anymore ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12) Probably will shift model training to my desktop, which is Intel 8700k, 64 GB RAM, Nvidia 3090.

---

### Post #12 — **dzheng1887** | 2022-10-07 16:19 UTC _(reply to #11)_

Yeah, but you can’t say XGBoooOOOOOOSTTT with LightGBM ![:confused:](http://forum.numer.ai/images/emoji/twitter/confused.png?v=12)

---

### Post #13 — **jacob_stahl** | 2022-10-08 01:06 UTC _(reply to #9)_

The dataset will probably get bigger in the future and even 128 GB won’t be enough. Hopefully the price of NMR 10x before that so i can buy a machine with even more memory.

---

### Post #14 — **ryo_matsuzaka** | 2022-10-08 02:12 UTC

[@dzheng1887](</u/dzheng1887>)  
By the way, why do you use XGBoost? You do not use LightGBM?

---

### Post #15 — **joakim** | 2022-10-08 03:15 UTC

CPU: AMD TR 1920x  
GPU: RTX 3090 x2  
RAM: 128GB

---

### Post #16 — **svendaj** | 2022-10-08 11:14 UTC

I am running my models for free ![:crazy_face:](http://forum.numer.ai/images/emoji/twitter/crazy_face.png?v=12) in [Kaggle notebooks CPU runtime](<https://www.kaggle.com/docs/notebooks#technical-specifications>) mostly XGBoost or LGBM without GPU or TPU.  
But [@nyuton](</u/nyuton>) here explains how you can train your model on full V4 dataset with only 8GB RAM:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) [How to train on the full V4 dataset with 8GB RAM](<http://forum.numer.ai/t/how-to-train-on-the-full-v4-dataset-with-8gb-ram/5734>) [Data Science](</c/data-science/5>)

> Hi, I guess I’m not the only one here, who doesn’t have 128GB RAM at hand. So it might be helpful to share, how it is possible to use the full dataset with <8GB RAM. The basic idea is to split the full dataset into chunks (split by era). Save these chunks as separate parquet files and then load them on the fly in parallel threads. The result is not a significant compromise on speed. It requires very little RAM and needs only 5 threads to continously read the data from disk. The number of thre…

---

### Post #17 — **bor1** | 2022-10-08 14:35 UTC

3060ti (8GB) + intel i9-10980XE + 64GB ram. Heavily leaning on Intel MKL for a lot of the calculations, and only sending the NN training off to the GPU. A future GPU with a larger memory might allow me to stay more on the GPU, but I wasn’t going to pay more than what they asked for a 3060ti back when I bought one :-).

---

### Post #18 — **dzheng1887** | 2022-10-08 16:26 UTC _(reply to #14)_

No reason in particular, it wins a lot of kaggle competitions and it’s sort of a running gag for me now to act silly and push data through XGBoost to solve all my problems

That said, I learned recently that you can generally think of boosting algorithms as a non parametric approach to estimation, so good reason why it does well generally. Combining a non-parametric approach with true structural assumptions in how the data behaves is always more optimal though, but it requires more work and thinking about the actual underlying process than just getting predictions out of xgboost

---

### Post #19 — **jrb** | 2022-10-09 16:42 UTC

Primary machine:  
CPU: 12 core Intel i9 10920X @ 3.5Ghz  
RAM: 256GB  
GPU: 2x 3090 with 24GB of GPU memory on each card

Older secondary machine:  
CPU: Quad core Intel i7-7700k @ 4.2Ghz  
RAM: 64GB  
GPU: 2x 2080TI with 11GB of GPU memory on each card

Both machines are headless.

---

### Post #20 — **joakim** | 2022-10-10 01:08 UTC _(reply to #19)_

Hi JRB,

I have 2x 3090 as well, blower style 2-slot so room for 2 more if my PSU can handle it (at least 1 would require a riser cable).

Would linking them with an NVLINK help at all on the Numerai data you reckon? Or not really? I’m mostly looking for an easy way to pool the ram together for a total of 48GB.

---

### Post #21 — **ryo_matsuzaka** | 2022-10-10 03:41 UTC

I thought someone use threadripper. No one uses it?

---

### Post #22 — **nyuton** | 2022-10-10 06:37 UTC _(reply to #21)_

With pytorch and cuml you can push all your ML load to GPUs. They are faster and cheaper then a threadripper.

---

### Post #23 — **ryo_matsuzaka** | 2022-10-10 07:13 UTC _(reply to #22)_

Thank you very much. I misunderstood that for GBDT many core CPU is faster than GPU. I will tri it.

---

### Post #24 — **jrb** | 2022-10-10 08:46 UTC _(reply to #20)_

I have NVLINK on both my machines. I haven’t used it for Numerai data, although I have for used it for some large computer vision models in the past. I don’t know of any automatic way to use multiple GPUs as one, for this use-case (model parallelism). When people say multi-GPU training, they usually mean training large batches on multiple GPUs (data parallelism), which is the easy case and trivially automated by all frameworks.

It’s fairly straightforward to place some layers (i.e weights for those layers) on different GPUs. I’ve done this with tensorflow and JAX. Still a bit slower than using a single GPU, but noticeably faster than when doing the same without NVLINK, because device to device copies are much faster with it.

---

### Post #25 — **joakim** | 2022-10-10 09:40 UTC _(reply to #21)_

My CPU is a first Gen threadripper. 12 cores 24 threads, and fairly slow compared to latest Gen CPUs (I’ve overlooked it though so all cores are running at 4ghz all the time.). I use it mostly for pre and post processing. Been contemplating if I should upgrade to a 2990wx second Gen (32 cores 64 threads), which is the biggest one the motherboard supports. I don’t really need it though.

---

### Post #26 — **joakim** | 2022-10-10 09:49 UTC _(reply to #24)_

Thanks for a very thorough answer!

---

### Post #27 — **objectscience** | 2022-10-17 16:00 UTC _(reply to #15)_

3090 x 2… Do the house lights dim just a little when you fire that up? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) Nice setup!

---

### Post #28 — **jxtrbtk** | 2022-10-27 12:46 UTC

An Asus Eee PC 901, shipped with an Intel N270 Atom CPU clocked at 1.6GHz and 1GB of RAM.  
It runs on Debian 9 and I use it for inference only !!!  
I have models using XGBoost and that’s fine. I had to struggle a bit more with my PyTorch models as it is 32bit device and not PyTorch is not working on 32bit systems. So I have broken my models down to play them with the simple linear algebra using numpy.

Of course for training I have other devices : a MSI laptop (i7, 16GB, GTX 1060) and a retired open air mining rig (AMD CPU, 12GB, GTX 1080) but no data science war machine.

---

### Post #29 — **autratec** | 2022-10-28 00:06 UTC

All models are running on cloud. Start fromAzure ML studio. Moved to Colab and Python as others suggested. Moved to Kaggle notebook later and now using Deepnote to conduct daily submission.
