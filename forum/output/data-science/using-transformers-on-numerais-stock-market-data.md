---
title: "Using Transformers on Numerai's stock market data"
category: Data Science
url: https://forum.numer.ai/t/using-transformers-on-numerais-stock-market-data/6003
created_at: 2023-01-05T13:17:38.676000+00:00
last_posted_at: 2023-12-22T13:58:40.980000+00:00
posts_count: 23
views: 6041
tags: []
---

# Using Transformers on Numerai's stock market data

---

### Post #1 — **richai** | 2023-01-05 13:17 UTC

In the first Quant Club with our chief scientist Michael Oliver, [@jrb](</u/jrb>) talked about how he used transformers on the Numerai data ([Numerai Quant Club with Michael Oliver - YouTube](<https://youtu.be/eLIxarbDXuQ?t=860>)). I was curious how [@jrb](</u/jrb>) and other Numerai data scientists have set up the problem to work with transformer architectures.

---

### Post #2 — **jrb** | 2023-01-05 15:17 UTC

I started experimenting with Transformers with the v3 data. `jrb20` was my first transformer model. It’s just a [vanilla](<https://arxiv.org/abs/1706.03762>) 4 layer transformer that takes embeddings of the 1050 features as a sequence and the model just has a single linear neuron at the end on the concatenated sequence output from the transformer. My newer models are bigger mixture of experts of small transformer like models and the routing model is a hypernetwork. These things are much trickier to train, but the results seem quite promising. I believe the hard routing (and the softmax attention in the transformers) give these models GBDT like properties, with the flexibility of NNs (pre-training, better loss functions, better optimizers, architectural tricks, etc).

---

### Post #3 — **danzell** | 2023-01-06 07:56 UTC

To me it was clear from the beginning that I have to use NNs to be “different” - anyone can use Trees.  
My models are multilevel and I use transformers to generate different features/ data representations for 2nd level models.

---

### Post #4 — **surajp** | 2023-03-14 03:45 UTC

How about using the era as a sequence to the Transformer with some hacks for long sequences (~6k)?  
It should help with synthetic era generation and with self supervised learning as well. Can also be trained on multiple targets with custom losses.

The current rough implementation seem to struggle a little with longer sequences. Having more number of layers help.

[Colab: NumeraiTransformerEra.ipynb](<https://colab.research.google.com/drive/1W90xCrRE0_MWVvK-wugDM_HhkjgGNXDa?usp=sharing>)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d95584263dd3711b1a5b922af46aca20fc669263_2_690x214.png)image2422×752 89.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d95584263dd3711b1a5b922af46aca20fc669263.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2b5ffb86aa5730cc40296862730b23ea1cab5dcb_2_690x211.png)image2448×752 93.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2b5ffb86aa5730cc40296862730b23ea1cab5dcb.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b7520d716effefa7533858821d236ec1cf7e61ae_2_690x261.png)image880×334 21.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b7520d716effefa7533858821d236ec1cf7e61ae.png> "image")

[![Screenshot 2023-03-17 at 01-46-45 Google Colaboratory](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0eb4b86027fd7c293fe123e0ffc8fb878da130ad_2_690x283.jpeg)Screenshot 2023-03-17 at 01-46-45 Google Colaboratory1794×738 78.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0eb4b86027fd7c293fe123e0ffc8fb878da130ad.jpeg> "Screenshot 2023-03-17 at 01-46-45 Google Colaboratory")

---

### Post #5 — **olivepossum** | 2023-03-14 10:14 UTC

I’ve tried a hacked implementation of [TabTransformers](<https://github.com/lucidrains/tab-transformer-pytorch>) and treated features as categorical (so not using continuous features).

Currently:

  * Just using the small dataset to avoid running out of memory on GPU.
  * Using pearson corr as loss function applying penalization to feature exposure
  * Using eras as batch sizes
  * Predict all targets at once and rank and average them



No relevant results worth sharing so far. A draft of the code looks like this:
    
    
    # helpers
    def exists(val):
        return val is not None
    
    def default(val, d):
        return val if exists(val) else d
    
    # classes
    class Residual(nn.Module):
        def __init__(self, fn):
            super().__init__()
            self.fn = fn
    
        def forward(self, x, **kwargs):
            return self.fn(x, **kwargs) + x
    
    class PreNorm(nn.Module):
        def __init__(self, dim, fn):
            super().__init__()
            self.norm = nn.LayerNorm(dim)
            self.fn = fn
    
        def forward(self, x, **kwargs):
            return self.fn(self.norm(x), **kwargs)
    
    # attention
    class GEGLU(nn.Module):
        def forward(self, x):
            x, gates = x.chunk(2, dim = -1)
            return x * F.gelu(gates)
    
    class FeedForward(nn.Module):
        def __init__(self, dim, mult = 4, dropout = 0.):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(dim, dim * mult * 2),
                GEGLU(),
                nn.Dropout(dropout),
                nn.Linear(dim * mult, dim)
            )
    
        def forward(self, x, **kwargs):
            return self.net(x)
    
    class Attention(nn.Module):
        def __init__(
            self,
            dim,
            heads = 8,
            dim_head = 16,
            dropout = 0.
        ):
            super().__init__()
            inner_dim = dim_head * heads
            self.heads = heads
            self.scale = dim_head ** -0.5
    
            self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)
            self.to_out = nn.Linear(inner_dim, dim)
    
            self.dropout = nn.Dropout(dropout)
    
        def forward(self, x):
            h = self.heads
            q, k, v = self.to_qkv(x).chunk(3, dim = -1)
            q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), (q, k, v))
            sim = einsum('b h i d, b h j d -> b h i j', q, k) * self.scale
    
            attn = sim.softmax(dim = -1)
            attn = self.dropout(attn)
    
            out = einsum('b h i j, b h j d -> b h i d', attn, v)
            out = rearrange(out, 'b h n d -> b n (h d)', h = h)
            return self.to_out(out)
    
    # transformer
    class Transformer(nn.Module):
        def __init__(self, num_tokens, dim, depth, heads, dim_head, attn_dropout, ff_dropout):
            super().__init__()
            self.embeds = nn.Embedding(num_tokens, dim)
            self.layers = nn.ModuleList([])
    
            for _ in range(depth):
                self.layers.append(nn.ModuleList([
                    Residual(PreNorm(dim, Attention(dim, heads = heads, dim_head = dim_head, dropout = attn_dropout))),
                    Residual(PreNorm(dim, FeedForward(dim, dropout = ff_dropout))),
                ]))
    
        def forward(self, x):
            x = self.embeds(x)
    
            for attn, ff in self.layers:
                x = attn(x)
                x = ff(x)
    
            return x
    # mlp
    class MLP(nn.Module):
        def __init__(self, dims, act = None):
            super().__init__()
            dims_pairs = list(zip(dims[:-1], dims[1:]))
            layers = []
            for ind, (dim_in, dim_out) in enumerate(dims_pairs):
                is_last = ind >= (len(dims_pairs) - 1)
                linear = nn.Linear(dim_in, dim_out)
                layers.append(linear)
    
                if is_last:
                    continue
    
                act = default(act, nn.ReLU())
                layers.append(act)
                layers.append(nn.Dropout(p=.3))
    
            self.mlp = nn.Sequential(*layers)
    
        def forward(self, x):
            return self.mlp(x)
    
    # main class
    class TabTransformer(nn.Module):
        def __init__(
            self,
            *,
            categories,
            dim,
            depth,
            heads,
            dim_head = 16,
            dim_out = 1,
            mlp_hidden_mults = (4, 2),
            mlp_act = None,
            num_special_tokens = 2,
            attn_dropout = 0.,
            ff_dropout = 0.
        ):
            super().__init__()
            assert all(map(lambda n: n > 0, categories)), 'number of each category must be positive'
    
            # categories related calculations
            self.num_categories = len(categories)
            self.num_unique_categories = sum(categories)
    
            # create category embeddings table
            self.num_special_tokens = num_special_tokens
            total_tokens = self.num_unique_categories + num_special_tokens
    
            # for automatically offsetting unique category ids to the correct position in the categories embedding table
            categories_offset = F.pad(torch.tensor(list(categories)), (1, 0), value = num_special_tokens)
            categories_offset = categories_offset.cumsum(dim = -1)[:-1]
            self.register_buffer('categories_offset', categories_offset)
    
            # transformer
            self.transformer = Transformer(
                num_tokens = total_tokens,
                dim = dim,
                depth = depth,
                heads = heads,
                dim_head = dim_head,
                attn_dropout = attn_dropout,
                ff_dropout = ff_dropout
            )
    
            # mlp to logits
            input_size = (dim * self.num_categories)
            l = input_size // 8
    
            hidden_dimensions = list(map(lambda t: l * t, mlp_hidden_mults))
            all_dimensions = [input_size, *hidden_dimensions, dim_out]
    
            self.mlp = MLP(all_dimensions, act = mlp_act)
    
        def forward(self, x_categ):
            assert x_categ.shape[-1] == self.num_categories, f'you must pass in {self.num_categories} values for your categories input'
            x_categ += self.categories_offset
            
            x = self.transformer(x_categ)
    
            flat_categ = x.flatten(1)
    
            x = flat_categ
            return self.mlp(x)
    
    #main
    categories_unique_values = []
    i = 0
    while i < FEATURE_LEN: #len of the small feature dataset
        categories_unique_values.append(5)
        i+=1
    categories_unique_values = tuple(categories_unique_values)
    
    model = TabTransformer(
        categories = categories_unique_values,      
        dim = 32,                           
        dim_out = TARGET_LEN, #len of all targets                       
        depth = 6,                          
        heads = 8,                          
        attn_dropout = 0.1,                 
        ff_dropout = 0.1,                   
        mlp_hidden_mults = (4, 2),          
        mlp_act = nn.ReLU()                
    )

---

### Post #6 — **olivepossum** | 2023-04-12 16:06 UTC _(reply to #5)_

An update on [Tab Transformers](<https://github.com/lucidrains/tab-transformer-pytorch>). Inspired by what [@surajp](</u/surajp>) mentioned, tried [Linear Attention](<https://github.com/lucidrains/linear-attention-transformer>) with a Tab Transformer and managed to run it with the medium dataset, a bunch of targets and splitting the data a bit (with vanilla Attention and a RTX 3090 just could manage the small dataset).

Metrics are a bit more decent than with the small one. Would have expected lower feature exposure (as I’m penalizing it in the loss function, clearly not enough) and lower corr with the example predictions. Anyways, haven’t tuned anything yet as training takes quite a while.

Sharing here code with the Linear Attention.

Any feedback is welcome!
    
    
    # helpers
    def exists(val):
        return val is not None
    
    def default(val, d):
        return val if exists(val) else d
    
    # classes
    class Residual(nn.Module):
        def __init__(self, fn):
            super().__init__()
            self.fn = fn
    
        def forward(self, x, **kwargs):
            return self.fn(x, **kwargs) + x
    
    class PreNorm(nn.Module):
        def __init__(self, dim, fn):
            super().__init__()
            self.norm = nn.LayerNorm(dim)
            self.fn = fn
    
        def forward(self, x, **kwargs):
            return self.fn(self.norm(x), **kwargs)
    
    # attention
    class GEGLU(nn.Module):
        def forward(self, x):
            x, gates = x.chunk(2, dim = -1)
            return x * F.gelu(gates)
    
    class FeedForward(nn.Module):
        def __init__(self, dim, mult = 4, dropout = 0.):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(dim, dim * mult * 2),
                GEGLU(),
                nn.Dropout(dropout),
                nn.Linear(dim * mult, dim)
            )
    
        def forward(self, x, **kwargs):
            return self.net(x)
        
    def linear_attn(q, k, v):
        dim = q.shape[-1]
    
        q = q.softmax(dim=-1)
        k = k.softmax(dim=-2)
    
        q = q * dim ** -0.5
    
        context = einsum('bhnd,bhne->bhde', k, v)
        attn = einsum('bhnd,bhde->bhne', q, context)
        return attn.reshape(*q.shape)
    
    class LinearAttention(nn.Module):
        def __init__(self, dim, heads, dim_head = None, dropout = 0.):
            super().__init__()
            assert dim_head or (dim % heads) == 0, 'embedding dimension must be divisible by number of heads'
            d_heads = default(dim_head, dim // heads)
            self.heads = heads
            self.d_heads = d_heads
            self.global_attn_fn = linear_attn
    
            self.to_q = nn.Linear(dim, d_heads * heads, bias = False)
            self.to_k = nn.Linear(dim, d_heads * heads, bias = False)
            self.to_v = nn.Linear(dim, d_heads * heads, bias = False)
            self.to_out = nn.Linear(d_heads * heads, dim)
            self.dropout = nn.Dropout(dropout)
    
        def forward(self, x, **kwargs):
            q, k, v = (self.to_q(x), self.to_k(x), self.to_v(x))
            b, t, e, h, dh = *q.shape, self.heads, self.d_heads
            merge_heads = lambda x: x.reshape(*x.shape[:2], -1, dh).transpose(1, 2)
            q, k, v = map(merge_heads, (q, k, v))
    
            out = []
            global_out = self.global_attn_fn(q, k, v)
            out.append(global_out)
            attn = torch.cat(out, dim=1)
            attn = attn.transpose(1, 2).reshape(b, t, -1)
            return self.dropout(self.to_out(attn))
    
    # transformer
    class Transformer(nn.Module):
        def __init__(self, num_tokens, dim, depth, heads, dim_head, attn_dropout, ff_dropout):
            super().__init__()
            self.embeds = nn.Embedding(num_tokens, dim)
            self.layers = nn.ModuleList([])
    
            for _ in range(depth):
                self.layers.append(nn.ModuleList([
                    Residual(PreNorm(dim, LinearAttention(dim, heads, dim_head = dim_head, dropout = attn_dropout))),
                    Residual(PreNorm(dim, FeedForward(dim, dropout = ff_dropout))),
                ]))
    
        def forward(self, x):
            x = self.embeds(x)
    
            for attn, ff in self.layers:
                x = attn(x)
                x = ff(x)
    
            return x
    # mlp
    class MLP(nn.Module):
        def __init__(self, dims, act = None):
            super().__init__()
            dims_pairs = list(zip(dims[:-1], dims[1:]))
            layers = []
            for ind, (dim_in, dim_out) in enumerate(dims_pairs):
                is_last = ind >= (len(dims_pairs) - 1)
                linear = nn.Linear(dim_in, dim_out)
                layers.append(linear)
    
                if is_last:
                    continue
    
                act = default(act, nn.ReLU())
                layers.append(act)
                layers.append(nn.Dropout(p=.3))
    
            self.mlp = nn.Sequential(*layers)
    
        def forward(self, x):
            return self.mlp(x)
    
    # main class
    class TabTransformer(nn.Module):
        def __init__(
            self,
            *,
            categories,
            dim,
            depth,
            heads,
            dim_head = 16,
            dim_out = 1,
            mlp_hidden_mults = (4, 2),
            mlp_act = None,
            num_special_tokens = 2,
            attn_dropout = 0.,
            ff_dropout = 0.
        ):
            super().__init__()
            assert all(map(lambda n: n > 0, categories)), 'number of each category must be positive'
    
            # categories related calculations
            self.num_categories = len(categories)
            self.num_unique_categories = sum(categories)
    
            # create category embeddings table
            self.num_special_tokens = num_special_tokens
            total_tokens = self.num_unique_categories + num_special_tokens
    
            # for automatically offsetting unique category ids to the correct position in the categories embedding table
            categories_offset = F.pad(torch.tensor(list(categories)), (1, 0), value = num_special_tokens)
            categories_offset = categories_offset.cumsum(dim = -1)[:-1]
            self.register_buffer('categories_offset', categories_offset)
    
            # transformer
            self.transformer = Transformer(
                num_tokens = total_tokens,
                dim = dim,
                depth = depth,
                heads = heads,
                dim_head = dim_head,
                attn_dropout = attn_dropout,
                ff_dropout = ff_dropout
            )
    
            # mlp to logits
            input_size = (dim * self.num_categories)
            l = input_size // 8
    
            hidden_dimensions = list(map(lambda t: l * t, mlp_hidden_mults))
            all_dimensions = [input_size, *hidden_dimensions, dim_out]
    
            self.mlp = MLP(all_dimensions, act = mlp_act)
    
        def forward(self, x_categ):
            assert x_categ.shape[-1] == self.num_categories, f'you must pass in {self.num_categories} values for your categories input'
            x_categ += self.categories_offset
            
            x = self.transformer(x_categ)
    
            flat_categ = x.flatten(1)
    
            x = flat_categ
            return self.mlp(x)
    
    #main
    categories_unique_values_list = []
    i = 0
    while i < FEATURE_LEN:
        categories_unique_values_list.append(5)
        i+=1
    
    categories_unique_values = tuple(categories_unique_values_list)
    
    model_transformer = TabTransformer(
        categories = categories_unique_values,      
        dim = 16,                           
        dim_out = TARGET_LEN,                        
        depth = 3,                          
        heads = 4,                          
        attn_dropout = 0.1,                 
        ff_dropout = 0.1,                   
        mlp_hidden_mults = (4, 2),          
        mlp_act = nn.ReLU()                
    )
    

[![performance](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c17204f3f9e1418cb784ac41bedaf523a25225ab.png)performance742×473 36 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c17204f3f9e1418cb784ac41bedaf523a25225ab.png> "performance")

---

### Post #7 — **autratec** | 2023-04-15 06:52 UTC

Considering openai providing a foundation of neural network with transformer , is it feasible to use their model to handle our trading needs directly. For example, convert our signal to serially inputs with expected out. This is similar to the llm token prediction. And figure out the relationship between those key input - transformer concept. We might use our data, load to openai to fine tune and get it to do classification work - buy/sell. Pls share your thoughts or experiment being done.

---

### Post #8 — **surajp** | 2023-04-17 18:24 UTC _(reply to #7)_

Yep, Working on something like that for signals.

Idea is to feed all the stocks at once and then use decoder to forecast all stocks together. This would allow the model to understand the interactions between stocks. Also allows for country and sector to be embedded into the data. Instead of OpenAI, I am trying to build a Transformer from scratch for this flexibility.

---

### Post #9 — **surajp** | 2023-04-30 00:20 UTC _(reply to #7)_

you mean converting daily changes into timeseries? Like 0.01% change as “u” and 0.02% change as token “uu”, -0.06% as “dddddd” and so on? and then training a transformer for forecasting next day’s returns from a dictionary ranging form [“u” or “d”]_100_ 100 (assuming 0.01 as base) and thus treating the daily pct changes as natural (language) sequences? Seems doable

---

### Post #10 — **autratec** | 2023-05-01 00:09 UTC _(reply to #9)_

Yes. Close. Basically, treat singal as a language

---

### Post #11 — **surajp** | 2023-05-19 05:17 UTC _(reply to #4)_

Just adding a reference to my post that explains this approach better [“Eras” of Transformers](<https://parmarsuraj99.medium.com/era-of-transformers-792e5960e287>)

[![eraFormer](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/668210fbfc59e5986cbf92fa12d76c4d420ec38c_2_690x354.webp)eraFormer1400×719 29.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/668210fbfc59e5986cbf92fa12d76c4d420ec38c.webp> "eraFormer")

---

### Post #12 — **pumplerod** | 2023-10-19 16:44 UTC _(reply to #11)_

These examples appear to be using the Transformer model as engineered for LLMs. I’m curious if anyone has experimented with more of a Vision Transformer model. I’ve been exploring this, with no significant results as of yet, but I could also be doing something wildly wrong with my architecture. I’d love to connect with anyone who’s given this a shot.

---

### Post #13 — **surajp** | 2023-10-20 16:08 UTC _(reply to #12)_

I guess the underlying idea or architecture of transformer encoders stays same, both for langugae and vision encoding, It’s just the way we encode images and text to feed to the modle that is different

---

### Post #14 — **jrb** | 2023-10-24 10:30 UTC _(reply to #13)_

Yes tokenization in ViTs is a lot simpler. We just cut up the image into patches, linearly project them and then add position embeddings before feeding them into a cascade of transformer encoder layers. It’s regrettable that we don’t have end to end learning of tokenization in text transformers (text tokenizers are pre-trained or trained before the transformer), although IIRC there have been some attempts at it.

---

### Post #15 — **pumplerod** | 2023-10-26 00:41 UTC _(reply to #14)_

I’m still experimenting with the transformer process. I’m finding that there isn’t a direct relationship to what the model learns on training data and how it performs on validation. At least it doesn’t seem as directly correlated as when training a random forest or GBT. I’ve read that transformers require a significant amount of training data, and I’m wondering if this is part of the reason. [@jrb](</u/jrb>) , do you have a sense for how the main transformer parameters relate to our data? For example, number of layers vs number of heads per layer vs embedding deminsion? I’d like to formulate some general understanding for what impact each of these values has on the learning/generalization of the model.

---

### Post #16 — **jrb** | 2023-11-01 12:54 UTC _(reply to #15)_

You can create a near infinite amount of training data by masking features. I’m not training any new transformer based models because the incentives of the tournament are now tilted towards training tree based models with feature engineering. Also, I don’t have any intuitive sense of what hyperparameters works best with transformers for this data. I’d recommend starting small and experimenting. Almost all of the recieved wisdom from using transformers in the fields of NLP and CV is applicable here.

---

### Post #17 — **jeremy_berros** | 2023-11-06 13:59 UTC _(reply to #16)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) jrb:

> the incentives of the tournament are now tilted towards training tree based models with feature engineering

Curious about what makes you say that [@jrb](</u/jrb>) ?

---

### Post #18 — **jrb** | 2023-11-06 14:24 UTC _(reply to #17)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jeremy_berros/48/3025_2.png) jeremy_berros:

> Curious about what makes you say that [@jrb](</u/jrb>) ?

TC incentivises novel predictions and CORR incentivises maximising CORR. With 2xCORR and 1xTC, the incentives are tilted towards maximising CORR at the cost of everything else. And if you’re after the highest CORR, it’s hard to beat gradient boosted tree ensembles.

---

### Post #19 — **f58c** | 2023-11-07 20:35 UTC _(reply to #2)_

any thoughts on why positive corr20v2 may also have negative tc? e.g. jrb46D: corr20v2 0.0061, tc -0.0009. while another model jrb19 has less positive corr20v2 (0.0036) and positive tc (0.0154)?

i’ve noticed a similar pattern in some of my own models (9111953: pos tc, low corr20v2, 10122004: neg tc, higher corr20v2).

adjusting the 20corrv2 and tc multipliers can compensate for this behavior, however 20corrv2 mult 2 is needed to stake a model.

---

### Post #20 — **surajp** | 2023-11-09 01:54 UTC _(reply to #16)_

The GBDTs are indeed hard to beat, I am training training Transformers specifically to extract values over the example model, barely getting anything (ofc, my implementation isn’t perfect). While the GBDTs seem highly overfitted on training set, when the NNs reach that level, they often hit saturation and validation CORR starts decreasing. The discrete boundaries of 20k trees is nice generalization which gets robust and smoother with 20k trees, NN on the other hand, generate smoother and continuous boundaries (planes), making them susceptible to smaller changes in inputs. My endeavour now is to look at what can help the NN in generalizing well. Ensemble of NN is nice idea but, then it’s better to go with trees.

---

### Post #21 — **jrb** | 2023-11-09 10:16 UTC _(reply to #19)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/f/779978/48.png) f58c:

> any thoughts on why positive corr20v2 may also have negative tc? e.g. jrb46D: corr20v2 0.0061, tc -0.0009. while another model jrb19 has less positive corr20v2 (0.0036) and positive tc (0.0154)?

`jrb46` \- `jrb46d` predictions are from two tree based models (XGBoost), one trained to predict the target another trained to predict the meta model.`jrb46` is just the target model and `jrb46d` is just a model of the meta model (meta-model model?). And everything in between is interpolating between various proportions of meta-model model subtraction. The base model hasn’t been updated in over a year now, and the meta model model was trained in January. IMO, it’s a failed experiment, nothing of value there, except the negative result. Surprising how well you can do on corr by just predicting the averages. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

`jrb19` OTOH is a mixture of hypernetworks jointly trained on all the targets in the `v4` dataset with a custom loss to maximise `fncv3`. Another relic from the 3x TC era.

EDIT: I just took a look at the code and it turns out that `jrb46` is a LightGBM model and not an XGBoost model. The other model (meta-model model) is XGBoost.

---

### Post #22 — **edubergeek** | 2023-11-11 04:18 UTC _(reply to #18)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) jrb:

> rb

On the other hand …  
My [Andro_M31](<https://numer.ai/andro_m31>) model is a NN and has done pretty well on CORR20V2 (as well as TC).

---

### Post #23 — **f58c** | 2023-12-22 13:58 UTC _(reply to #22)_

Yeah, NN’s are universal functions. I wasn’t sure if their tendency to over-fit would be a problem. Looks like it’s not a problem! ![:smile:](http://forum.numer.ai/images/emoji/twitter/smile.png?v=12)
