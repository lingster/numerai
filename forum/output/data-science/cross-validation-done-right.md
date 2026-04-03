---
title: "Cross-validation done right"
category: Data Science
url: https://forum.numer.ai/t/cross-validation-done-right/2979
created_at: 2021-04-20T13:28:52.058000+00:00
last_posted_at: 2021-05-02T08:56:42.124000+00:00
posts_count: 5
views: 2438
tags: []
---

# Cross-validation done right

---

### Post #1 — **nyuton** | 2021-04-20 13:28 UTC

Hi,

I’ve recently read Marcos Lopez de Prado’s great book on “Advances in Financial Machine Learning”.  
I’ve learnt quite a few things and I would like to share some improvements I made.

Doing cross-validation properly is something that greatly affected my model selection process and improved my confidence in my models.

He suggests making best use of the data we have and do cross-validation the following way:

  1. Split you dataset into N splits (6 in this example)
  2. Take all possible combinations of k splits as validation set (k=2 in this example)
  3. Use the rest of the data as training set.



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b8cdba389a04327a451458edb1820ae3bbf0cdbc_2_690x157.png)image962×219 13.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b8cdba389a04327a451458edb1820ae3bbf0cdbc.png> "image")

By splitting the data into N=6 splits and using and using k=2 splits as validation set, you end up with 15 valid combinations of train/validation sets.  
He argues, when data in the splits are independent and non-overlapping validation on data that preceeds training data is a valid process. In our case the eras in the numerai training data are non-overlapping.

You can download and tweak my code here:

[github.com](<https://github.com/nemethpeti/numerai>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d5cb66788d34511826e150c94dde50d21b01a0ae_2_690x344.png)

### [GitHub - nemethpeti/numerai](<https://github.com/nemethpeti/numerai>)

Contribute to nemethpeti/numerai development by creating an account on GitHub.

Yes, it takes a lot of time to train these models, but at least you can trust the results.  
Have fun!  
Feedback is welcome!

---

### Post #2 — **schot** | 2021-04-20 14:43 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> In our case the eras in the numerai training data are non-overlapping.

It’s a common practice for time series analysis to make sort of some lagged features like price of the security a month ago. I don’t know how long, but it’s safe to have some gap between training and validation set, I guess.

I don’t have any hard evidence that the dataset is overlapping in terms of eras though. It’s just my speculation.

---

### Post #3 — **nyuton** | 2021-04-20 15:38 UTC _(reply to #2)_

The code I shared has the parameter “embargo”. That’s the minimum gap between train and validation.  
I’ve tried a couple of values, but it doesn’t have any significant effect. Seems like the eras are not overlapping.

---

### Post #4 — **jackerparker** | 2021-04-21 08:04 UTC

Hi nyuton,

Your groups (G) are divided using next eras: 1-30 (G1), 31-60, 61-90, 91-120, 121-132 and 197-212 (G6).  
What do you think about having the same number of eras in every group? 1-25 (G1), 26-50 (G2) …

Or even more, having the same number of rows in every group? First eras have less rows, thus, G1-G2 groups could contain more eras than G3-G4 groups, but the number of rows will be close enough between groups.

Regards,  
Mark

---

### Post #5 — **nyuton** | 2021-05-02 08:56 UTC _(reply to #4)_

Hi JackerParker,

my splits are somewhat arbitrary, you are right. I wanted to split the validation eras into different splits, so that I have a score on the numerai validation set. That’s the reason, why I chose these splits.

More gouprs would give better granuality, but this is already too time consuming. CV with random forests can run for hours on my computer.

Feel free to tweak it!  
I wanted to share the idea and the base code, but there is certainly some room for improvement!
