---
title: "【中文】应对超大数据的一种方案——虚拟内存"
category: Other Languages
url: https://forum.numer.ai/t/topic/4395
created_at: 2021-10-25T03:46:13.535000+00:00
last_posted_at: 2021-10-26T16:16:10.761000+00:00
posts_count: 3
views: 842
tags: []
---

# 【中文】应对超大数据的一种方案——虚拟内存

---

### Post #1 — **sunkay** | 2021-10-25 03:46 UTC

Numerai的数据集越来越大了，最近Announcements里面是这样说的

Numerai Data V32 is coming December 25, 2021; prepare yourselves and your computers.

「真系好串啊。。」

你们的内存条够用吗？反正我是不可能光靠内存条的了。

于是我就想到了用硬盘设置虚拟内存来应对，实践起来觉得还不错。

对硬盘来说，主要有两个要求：  
1.读写速度要快  
2.需要耐读写

我的方案是将自己原有的两个镁光5100 MAX的SSD硬盘组成RAID0阵列，这样就可以将读写速度提高到单个盘的两倍。

另外这款SSD用的是MLC颗粒，因此有很高的擦写寿命，当内存来用的话，不会像一般的SSD那么容易用废。

我在这个分区上创建了512GB的分页文件作为虚拟内存，这样就基本不用担心算法运行到一半爆内存了。

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/904d1a251ad9e9f65f92f7884854247648a745df.jpeg)image400×400 71 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/904d1a251ad9e9f65f92f7884854247648a745df.jpeg> "image")

这两个硬盘是我以前买的，所以对我来说，这样的方案是物尽其用，我并不需要另外掏钱买。

供大家参考哈

* * *

我用内存很猛的，买内存条要达到我目前512G内存的配置，太贵了

所以个人还是倾向于用耐擦写的MLC颗粒SSD

---

### Post #2 — **autratec** | 2021-10-25 06:13 UTC

Chinese Content: 我的方案是希望那些云环境能继续支持, 如 COLAB 或者KAGGLE NOTEBOOK.

---

### Post #3 — **xiafanaina** | 2021-10-26 16:16 UTC

我直接买了点内存条，也没多少钱实际上

虚拟内存对硬盘损伤也是有的。
