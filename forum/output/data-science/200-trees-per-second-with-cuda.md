---
title: "200 Trees Per Second with Cuda"
category: Data Science
url: https://forum.numer.ai/t/200-trees-per-second-with-cuda/7823
created_at: 2024-10-31T03:34:37.033000+00:00
last_posted_at: 2025-12-30T16:35:44.513000+00:00
posts_count: 13
views: 2967
tags: []
---

# 200 Trees Per Second with Cuda

---

### Post #1 — **murkyautomata** | 2024-10-31 03:34 UTC

You can build 200 trees per second on v5-all with my cuda extra tree booster (on an A100,) and it can fit a dataset several times larger.

<https://drive.google.com/file/d/1EU0a4mMLyUBCBLdjIS3_qEM85bHERtKi/view?usp=sharing>

It uses some obvious optimizations like bit-packing and quantized gradients, but the more interesting one is that it builds layers (of different trees) at each depth simultaneously allowing for efficient packing of node index bits and full utilization of shared memory to accomplish more per global memory read.

This strategy requires layer-wise feature sampling which tends to prefer fewer features per layer than tree-wise sampling as trees see a greater variety of features overall than they do in one layer. My guess is that layer-wise sampling should perform better as it enables greater variety in trees.

This is the validation diagnostic when I attempt to reproduce the procedure of Numerai’s example preds with an ensemble of Teager and Cyrus and retraining at eras 470, 626, 783, 939, and 1078 (no neutralization).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f77425fdd8e2163ac99e77ad296a8095d9094961_2_690x406.png)image1053×620 43.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f77425fdd8e2163ac99e77ad296a8095d9094961.png> "image")

You can verify the result with this script that runs in about an hour:

<https://drive.google.com/file/d/1xG0oEprBKI4hikY1xGdze2HVNI4sicWi/view?usp=sharing>

This is still a fairly rough draft; it doesn’t support sample weight and won’t support depths greater than 7 until I re-write it in pycuda or find a way to adjust the shared memory carve-out in numba.

---

### Post #2 — **andralienware** | 2024-10-31 04:57 UTC

Thanks a ton for sharing the code. The quantization of the dataset allows for many optimizations without much prediction performance loss, so it’s nice to see that you’ve built code that exploits that. From reading into the code it seems like `nfeatsets` is the number of subsets of features used to train the different trees. I figure that `trees_per_layer` is the number of trees being created in parallel, but I’m not so sure. If you could clarify what `trees_per_layer` is that would be great. I also can’t quite figure out what `nsets`–is it the number of trees?

---

### Post #3 — **murkyautomata** | 2024-10-31 05:35 UTC _(reply to #2)_

trees_per_layer x max_depth is the number of layers built in one round, each belonging to a different trees. Handling layers at each depth in parallel is more efficient and handling multiple such sets at once allows this to be done without making trees that see the same feature subsets in the same order (by creating a larger feature subset for a round that layer groups sample from). nsets is the number of such rounds the booster is trained on (and the number of round feature sets that need to be preselected). nfeatsets is the number of 32 feature subsets that will each be distributed to a group of max_depth layers in a round.

---

### Post #4 — **mdo** | 2024-10-31 17:51 UTC

Very cool Murky! One thing I’m not clear on is how building “layers (of different trees) at each depth simultaneously” is compatible with boosting as each tree is trained on gradients calculated using the full ensemble up to that point. Probably not a huge deal tbh if the gradients are a bit stale as they don’t change too rapidly with a small step size, but just want to understand what the tradeoffs are. Also IME tree-wise sampling (eg colsample_bytree) works better than layer-wise sampling (eg colsample_bylevel) because the learnable representation for each tree is more constrained because they see fewer features and thus the tree predictions are more diverse than is the case in layer-wise sampling. Also, have you tried implementing in Triton, it seems like it would be quite similar implementation but has some nice interfaces to pytorch.

---

### Post #5 — **murkyautomata** | 2024-11-01 00:09 UTC _(reply to #4)_

> One thing I’m not clear on is how building “layers (of different trees) at each depth simultaneously” is compatible with boosting as each tree is trained on gradients calculated using the full ensemble up to that point.

Node values are decided at the time of their layer’s creation with the gradient at that round, so I don’t think one can accurately call the gradient out of date. Maybe you could say that the splits above leaves are, but I can’t imagine that mattering with the learning rates we’re dealing with.

> Also IME tree-wise sampling (eg colsample_bytree) works better than layer-wise sampling (eg colsample_bylevel) because the learnable representation for each tree is more constrained because they see fewer features and thus the tree predictions are more diverse than is the case in layer-wise sampling

Whether trees see more total features under layer-wise sampling is a matter of the respective sample rates. To the extent that I tested it in xgboost, layer-wise sampling outperformed tree-wise sampling when each were given their best performing rates.

If we consider the limit of the gradient boosting process as the learning rate approaches zero and the number of trees approaches infinity, the features sampling scheme becomes a weighting scheme: the weight of each possible leaf at some point in training being the probability that a random tree will include it which is the product of the probabilities of each ancestor node’s split provided that the splits that lead to them were taken.

Under a layer sampling scheme, the probability that a node splits on a feature is entirely independent of the splits taken to reach that node and simply the probability that the feature will be the best scoring cut in a random feature sub-sample. This is simply a function of the rank order of that feature’s cut score against all others. The relative weights of all trees that include each cut are given by this function in the limit case. This is what that function which relates cut score rank to cuts’ trees’ relative weights looks like given a couple different sampling rates:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7d4ce7412bd36295c2490b34a300198cedcebce6.png)image556×413 19.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7d4ce7412bd36295c2490b34a300198cedcebce6.png> "image")

Tree-wise sampling complicates this in two ways: first cuts cannot exist at a node if cuts on that feature would have scored better on the ancestor cuts than the feature-cut-path taken to reach the node. Second, features used in previous cuts must necessarily be available to the node and thus have a higher probability (and therefore weight) than they would otherwise. I think it would be very difficult to argue that the first condition is beneficial as it appears to punish features for being good, and it weights some good cuts to zero which doubtlessly hurts variety. If good cuts are too high weighted, it make more sense to gently adjust the weight of all good cuts by reducing the sample rate than to set some good cuts to zero by using tree-level sampling. The second effect is less easy to judge, but it can be reproduced in a layer sampling scheme by adding just those few features used in parent cuts to a layer’s feature set without the side effect of the first, or at least it could if I wasn’t using an extra trees scheme to begin with.

Taking this limit might seem overly theoretical, but learning rates below a certain rate seem to see drastically diminishing returns in terms of improvement which makes me think the limit is relevant.

> have you tried implementing in Triton, it seems like it would be quite similar implementation but has some nice interfaces to pytorch

Briefly looking at Triton, I don’t think it’s suitable as it appears to abstract away shared memory and warp boundaries. This is probably fine for basic tensor manipulation, but building trees with the highest efficiency requires manipulating shared memory and the distribution of data to warps carefully.

---

### Post #6 — **mdo** | 2024-11-03 07:08 UTC _(reply to #5)_

What I mean by stale is just that from the perspective of the traditional algorithm where trees are built serially so each tree sees a different gradient, where you are building trees in batches so all trees within a batch see the same gradient. You’re essentially using a small random forest rather than a single tree as your weak learner for boosting, which seems to me a perfectly fine thing to do.  
I admittedly haven’t tested layer-wise sampling in a long time, so I will revisit especially around the very low sampling rate it looks like you’re using.

> If we consider the limit of the gradient boosting process as the learning rate approaches zero

I don’t really know if this limit is super meaningful in the context of boosting. How does it differ from a random forest, which is equivalent to a learning rate of 0? Empirically GBM outperforms similarly configured random forests so theoretical limits that blur the distinction between the two aren’t particularly convincing.

> I think it would be very difficult to argue that the first condition is beneficial as it appears to punish features for being good, and it weights some good cuts to zero which doubtlessly hurts variety.

I think I see what you’re getting at, but I don’t think this statement makes a lot of sense. A cut is good only in the contest of the data its being evaluated on. If you’ve already split the data at a particular value of a feature earlier in the tree it doesn’t make sense to say later in the tree that it’s a good place to cut again as all the data on the other side of that split is on the other side of the tree. The good feature isn’t being punished at all, it’s just used higher up in the tree and a different cut of the same feature can be used lower down in the tree if useful. Now a point you could make about the tree-wise sampling is that when a good feature is sampled for a tree it will usually end up high up in the tree, and rarely lower down in the tree. I could see layer wise sampling increasing diversity in that respect. It’s an empirical question what kind of difference this makes. I wasn’t clear, was a technical issue that makes tree-wise sampling difficult? It seems like it should be easier, no?

---

### Post #7 — **murkyautomata** | 2024-11-04 00:07 UTC _(reply to #6)_

> you are building trees in batches so all trees within a batch see the same gradient.

Sure, but I think the benefit of very low learning rates comes from building more trees rather than having smaller learning increments. With thousands of boosting rounds, the difference in gradient from round to round is going to be pretty trivial compared to the difference in behavior of trees with different feature sets.

> How does it differ from a random forest, which is equivalent to a learning rate of 0?

It’s the limit as the learning rate approaches zero and the number of trees approaches infinity such that the sum learning rate remains constant: an integral over the infinite random forest function. In the limit we form an infinite forest before the learning progresses, but we can define the total tree number to be a greater infinity such that learning does still progress. The main point here being to recognize that as sampling approaches infinity, sample probabilities begin to act like weights.

> The good feature isn’t being punished at all, it’s just used higher up in the tree and a different cut

Well no, I’m specifically considering nodes that do not have the cut in their ancestors. The problem is not that the cut was already used, but that it would have been if it were in the tree’s feature set.

I’m talking about the probability of a cut at a node when we do not presuppose a given feature set. We have to apply Bayes theorem then and consider the probability that a feature is in the feature set given the path to the node, and this probability is zero if we have tree level sampling and the presence of that feature would necessarily cause the tree to make different splits that don’t lead to the node (by “node” I mean a node with a particular set of train samples and particular cut history, not just a position in the tree.)

If each possible node has less variety in its possible splits, we can expect less variety in the trees overall.

> I wasn’t clear, was a technical issue that makes tree-wise sampling difficult? It seems like it should be easier, no?

Each histogram warp works on max_depth tree layers belonging to different trees and a feature subset of 32 features. If that feature set needed to be used for every layer of a tree, it would have to keep being used in subsequent iterations because the shallowest tree won’t be completed until max_depth rounds have elapsed and at that point a new set of unfinished trees will have begun being built on the feature subset meaning it would have to remain for the whole boosting process.

I could still make feature subsets persist over multiple rounds, but it would make the trees I’m building have more overlap in their feature sets and reduce the variety I gain per tree.

---

### Post #8 — **jmnum** | 2024-11-10 17:32 UTC

Hello Murky, you might have an edge case, allocating  
self.dV = cuda.to_device(np.zeros([rounds, self.nfolds, 2*(2**self.max_depth - 1)], dtype=np.int32 ))  
In _advance_and_predict_offline (easier to check) V[tree_set, tree_fold, 2 _lo + 1 + x ], 2_ lo+1+x might reach the upper bound ?

---

### Post #9 — **halsmith99** | 2024-12-12 11:55 UTC

is this or anything like it in a live model? curious how its handling current burn.

---

### Post #10 — **shatteredx** | 2024-12-14 07:18 UTC _(reply to #9)_

I have two of these models running live:

no feature neutralization: [Numerai](<https://numer.ai/shatt101>)  
feature neutralization: [Numerai](<https://numer.ai/shatt102>)

---

### Post #11 — **jefferythewind** | 2024-12-17 15:46 UTC

I’ve been uploading the predictions from one model I used to this slot: [Numerai](<https://numer.ai/jefferythewind3>)

One bottleneck I ran into on my GPU hardware is that I prefer to retrain the models on all the data before deploying, and in my case the memory was exhausted and I could not do a final train based on the best parameters from the cross validation. I’m still meaning to go back to this though, because it is incredibly fast.

It is getting more and more like we’re mining for corr.

---

### Post #12 — **shatteredx** | 2024-12-26 16:59 UTC _(reply to #10)_

Since model uploads doesn’t have numba I asked Claude to make me an inference function compatible with murky’s trees. It produces predictions that are very close but not exactly the same as murky’s inference function (~0.99 correlation). Here is the code if anyone is interested:
    
    
    def pack_cuts_32(X, n):
    
      Xo = np.zeros( ( n*X.shape[0],  ( X.shape[1]+ 31 )>>5 )  , np.uint32)
    
      for f in range( X.shape[0] ):
        for k in range( X.shape[1] ):
    
          x = X[f, k]
    
          for s in range(n):
    
            Xo[n*f + s, k>>5] |=  ( 1 << ( k&31 ) ) * ( x > s )
    
    
      return Xo
    
    class NumpyOfflineBooster:
        def __init__(self, path):
            data = np.load(path)
            self.V = data['V']
            self.I = data['I']
            self.max_depth = int.bit_count(self.I.shape[-1])
    
        def predict(self, X, n=None):
            if n is None:
                n = 32 * X.shape[1]
    
            predictions = np.zeros(n, dtype=np.int32)
            L_old = np.zeros((self.I.shape[1], self.max_depth-1, n), dtype=np.uint16)
            L_new = np.zeros((self.I.shape[1], self.max_depth-1, n), dtype=np.uint16)
    
            # For each boosting round
            for tree_set in range(self.I.shape[0]):
                max_depth_round = min(tree_set + 1, self.max_depth)
    
                # Process each depth level
                for depth in range(max_depth_round):
                    # For each tree in the fold
                    for tree_fold in range(self.I.shape[1]):
                        # Get sample indices for this batch
                        sample_indices = np.arange(n)
    
                        # Get current leaves for all samples
                        leaf = np.uint16(L_old[tree_fold, depth-1, :] if depth > 0 else 0)
    
                        # Calculate node offset
                        lo = leaf + (1 << depth) - 1
    
                        # Get feature indices
                        li = self.I[tree_set, tree_fold, lo]
    
                        # Extract bits
                        word_indices = sample_indices >> 5
                        bit_shifts = sample_indices & 31
                        x = np.uint8((X[li, word_indices] >> bit_shifts) & 1)
    
                        # Update leaf indices
                        leaf = np.uint16(2 * leaf + x)
    
                        # Store new leaves if not at max depth
                        if depth < L_new.shape[1]:
                            L_new[tree_fold, depth, :] = leaf
    
                        # Calculate value indices with bounds checking
                        value_idx = np.minimum(2 * lo + 1 + x, self.V.shape[2] - 1)
    
                        # Add prediction values
                        predictions += self.V[tree_set, tree_fold, value_idx]
    
                # Swap buffers for next round
                L_old, L_new = L_new, L_old
    
            return predictions

---

### Post #13 — **jmnum** | 2025-12-30 16:35 UTC

Hello [@murkyautomata](</u/murkyautomata>) ,

It looks like your histogram H stores the values above the thresold. Then, in __cut_ _cuda, you use it in the left split (vls) but it should be the right one ? So in advance_and_predict, you swap the branchs with the formula 2*_lo+1+x . However, this overflows (hidden by njit) and you never use the value at indice 0. So the correct formula should be 2_ *lo+1-x ?
