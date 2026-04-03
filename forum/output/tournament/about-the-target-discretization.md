---
title: "About the target discretization"
category: Tournament
url: https://forum.numer.ai/t/about-the-target-discretization/7081
created_at: 2024-03-06T17:00:45.690000+00:00
last_posted_at: 2024-03-08T17:09:27.560000+00:00
posts_count: 6
views: 605
tags: []
---

# About the target discretization

---

### Post #1 — **rpica** | 2024-03-06 17:00 UTC

Hello! I’m trying to understand the target and how our predictions are scored. If I understand right, it will be better to discretize the predictions into 5 buckets, just as targets are given. Or the score is against a non-discretized version of the target?

If so, giving it discretized so heavily makes it artificially hard to get good predictions, doesn’t it?

Here is a bit of code to show how having many equal target values but a prediction that is a float number (so even if we have almost perfect predictions, it’s still a dense cloud around the target bucket) leads to a pretty bad score:
    
    
    import numpy as np
    import pandas as pd
    from numerai_tools.scoring import numerai_corr
    
    def compare(pred, target):
        pred = pd.DataFrame({'predictions': pred})
        target = pd.DataFrame({'target': target})['target']
        return numerai_corr(pred, target)
    
    # 1
    out1 = compare([1,2,3,4,5],
                   [1,2,3,4,5])
    # 2
    out2 = compare([1,2,3,4,5],
                   [0,.25,.5,.75,1])
    
    # Now a "similar" target distribution to the actual targets:
    # many points at the center. 
    target = [1] + [50]*100 + [100]
    
    # 3 shorted list
    pred = list(range(len(target)))
    out3 = compare(pred, target)
    
    # 4 problem: very dense but ordered around that middle point
    # Still pretty bad score
    pred = [0] + list(np.linspace(0.45,0.55,len(target)-2)) + [1]
    out4 = compare(pred, target)
    
    # 5 should we just discretize our output to 5 values for increased scoring? 
    # This can't be good for the hedge fund using the output, can it? 
    # A lot of info is being dropped
    # Here is the max score again.
    pred = target.copy()
    out5 = compare(pred, target)
    
    print(f'output 1: {out1[0]}')
    print(f'output 2: {out2[0]}')
    print(f'output 3: {out3[0]}')
    print(f'output 4: {out4[0]}')
    print(f'output 5: {out5[0]}')
    

The output:
    
    
    output 1: 0.9964884741438282
    output 2: 0.9964884741438282
    output 3: 0.4684796965347025
    output 4: 0.4684796965347025
    output 5: 0.9998918220813134

---

### Post #2 — **rpica** | 2024-03-07 09:03 UTC

Another view of the same thing: We can have really good predictions, but either because it’s a float number (almost never exactly the very same value as the target), it doesn’t matter the order (rank) to get a better corr as I have always understood that numerai does:
    
    
    import numpy as np
    import pandas as pd
    from numerai_tools.scoring import numerai_corr
    
    def compare(pred, target):
        pred = pd.DataFrame({'predictions': pred})
        target = pd.DataFrame({'target': target})['target']
        return numerai_corr(pred, target)
    
    target = [0] + [.5]*100 + [1]
    pred = [0] + list(np.linspace(0.45,0.55,len(target)-2)) + [1]
    out = compare(pred, target)
    print(f'output: {out[0]:.3f}')
    
    for _ in range(10):
        pred = [0] + list(np.random.uniform(low=0.45, high=0.55, size=100)) + [1]
        out = compare(pred, target)
        print(f'output: {out[0]:.3f}')
    

Output
    
    
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    output: 0.468
    

So, the order around that 0.5 value of the target, does not make a difference (here a random cloud of points near the target value was generated each time).

I must be misunderstanding something, I suspect:

  1. That the actual score is done against a non-discretized version of the target, which would mean that we have an artificially difficult target (bad for everyone, isn’t it?)
  2. Maybe I’m simplifying the example too much? But the target is 5 buckets… I’m working around one. I think even if the “output” changes in value, the effect is the same.



If it is none of those, I wonder if this message still applies:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png)[Are predictions discrete or continuous?](<http://forum.numer.ai/t/are-predictions-discrete-or-continuous/1157/2>)

> Nevertheless, your predictions should be real valued and ideally not contain any ties (they will be broken by row order, i.e. essentially randomly).

Because according to my analysis, breaking the tie drops the corr from that 0.9ish to 0.5ish values (again in this example).

Any idea of what I’m missing? ![:sweat:](http://forum.numer.ai/images/emoji/twitter/sweat.png?v=12)

---

### Post #3 — **shatteredx** | 2024-03-07 18:38 UTC _(reply to #2)_

I could be wrong here, but I don’t think you’re missing anything. 0.468 is probably about the highest numerai_corr score possible (in-sample) and that’s around what I get from diagnostics when I train on validation.

---

### Post #4 — **wigglemuse** | 2024-03-07 19:30 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/rpica/48/2776_2.png) rpica:

> `target = [1] + [50]*100 + [100]`

The problem is your target^ is not like the actual target. Use the real distribution of  
5,20,50,20,5 and you’ll see a max score of .94 something on a set of predictions with no ties. It appears they no longer break ties, btw. (That previous comment was about the old scoring system.)

Also keep in mind that with 0.5xCORR + 2xMMC, the corr component is not that important anyway – mainly you want to focus on beating the competition as much and and often as possible. Actual score corr values only matter by how better they are compared to others.

---

### Post #5 — **rpica** | 2024-03-08 10:52 UTC _(reply to #4)_

Thank you both! I see that the difference making an example closer to the actual distribution of targets massively changes the outcome, making it useless to return values rounded to the target values as I was suggesting instead of the float that a regression will return.

What is mildly concerning to me is that, then, the order that I thought was the main thing here is not that important, being the main goal to make each sample fall into the corresponding bucket (bucket being the range of values nearer to each of the 5 possible target values).

The code modified below shows this as the difference between example 4 and 5: it doesn’t matter the fine order of the predictions as long as they fall near the target value (nearer than to the other 4 possible values of the target).

It changes a bit respect to order / rank being the main thing, doesn’t it?
    
    
    import numpy as np
    import pandas as pd
    from numerai_tools.scoring import numerai_corr
    
    def compare(pred, target):
        pred = pd.DataFrame({'predictions': pred})
        target = pd.DataFrame({'target': target})['target']
        return numerai_corr(pred, target)
    
    # 1
    out1 = compare([1,2,3,4,5],
                   [1,2,3,4,5])
    # 2
    out2 = compare([1,2,3,4,5],
                   [0,.25,.5,.75,1])
    
    # Now a "similar" target distribution to the actual targets:
    # many points at the center. 
    target = [0]*5 + [25]*20 + [50]*50 + [75]*20 + [100]*5
    
    # 3 shorted list
    pred = list(range(len(target)))
    out3 = compare(pred, target)
    
    # 4 very dense but ordered around that middle point
    centers = [0, 25, 50, 75, 100]
    sizes = [5, 20, 50, 20, 5]
    alpha = 5
    pred = sum([
                list(np.linspace(center-alpha,center+alpha,size_)) 
                for center,size_ in zip(centers, sizes)
                ], [])
    out4 = compare(pred, target)
    
    # 5 same as #4 but randomly sorted around each target value
    pred = sum([
                list(np.random.uniform(low=center-alpha, high=center+alpha, size=size_)) 
                for center,size_ in zip(centers, sizes)
                ], [])
    out5 = compare(pred, target)
    
    # 6 should we just discretize our output to 5 values for increased scoring? 
    # This can't be good for the hedge fund using the output, can it? 
    # A lot of info is being dropped
    # Here is the max score again.
    pred = target.copy()
    out6 = compare(pred, target)
    
    print(f'output 1: {out1[0]}')
    print(f'output 2: {out2[0]}')
    print(f'output 3: {out3[0]}')
    print(f'output 4: {out4[0]}')
    print(f'output 5: {out5[0]}')
    print(f'output 6: {out6[0]}')
    
    >>>
    output 1: 0.9964884741438282
    output 2: 0.9964884741438282
    output 3: 0.9479180288841879
    output 4: 0.9479180288841879
    output 5: 0.9479180288841879
    output 6: 0.999195322883508

---

### Post #6 — **wigglemuse** | 2024-03-08 17:09 UTC _(reply to #5)_

Yes, the way it shakes out is that your ordering for rows with the same target doesn’t really matter because there is nothing to compare against – they all have the same target. So what is important is that your predictions for the rows with targets 1 are lower than the rows with targets 2,3,4,5 and the predictions for the rows with targets 2 are higher than 1 and lower than 3,4,5, and so on. So ordering within buckets doesn’t matter at all, only differences between buckets. And of course you’ll never get anywhere near .94 or even .44 in the real competition. (In fact, if you get an 0.04 is a round that usually means you’re in the top 1%.) In practical terms, if you can just classify top half vs bottom half better than most you’ll be doing quite well.
