---
title: "Teach Your Neural Net to Minimize Risk with Lagrangian Dynamics"
category: Data Science
url: https://forum.numer.ai/t/teach-your-neural-net-to-minimize-risk-with-lagrangian-dynamics/2219
created_at: 2021-03-07T19:17:00.068000+00:00
last_posted_at: 2021-03-25T21:35:14.064000+00:00
posts_count: 13
views: 2270
tags: []
---

# Teach Your Neural Net to Minimize Risk with Lagrangian Dynamics

---

### Post #1 — **lackofintelligence** | 2021-03-07 19:17 UTC

What a Financial Physicist would like to do is find a symmetry principle that governs risk and probable gain; a loss function that incorporates the Lagrangian Dynamics of Finance might help decide the ultimate question: When is Feature Exposure an acceptable risk? What is that mysterious symmetry principle that we have been searching for? Here I will scratch the surface of this topic with an ansatz and suggest a very simple way that it could be explored further if Numer.ai data were simply augmented!

Let us suppose the Hamiltonian H of the system to be a prediction of the target y. Let us associate risk with a potential V = A \cdot X where X is the data. When we perform Feature Neutralization we are reducing this potential. A neural net gives nonlinear output M(\dot{X}) that we associate with the kinetic energy of the Hamiltonian.

Then the Hamiltonian is H \equiv M(\dot{X}) + A\cdot X while the Lagrangian is \mathcal{L} = M(\dot{X}) - A\cdot X.

Substituting into the Euler Equations:

\frac{\partial \mathcal{L}}{ \partial X} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{X}} \rightarrow A - \Delta\left( \frac{\partial M(\dot{X})}{\partial \dot{X}} \right)

The \Delta represents a finite difference which is to be defined. The partial derivative in the brackets can be determined automatically through the usual software interfaces like pytorch.

The square of the Euler-Lagrange equation can then be used as the loss function to train the neural network.

The idea is that we train the neural network to specifically adjust for the feature exposure assuming that such a conservation law exists between linear (risky) and nonlinear outputs.

What is missing from Numer.ai data to explore this idea? \dot{X}. What is _not_ needed is the identification of a row from one era to another. Although people _want_ to do a proper time series analysis its actually not necessary with this approach. The differences in the values of the variables \dot{X} from one time step to the next (from one week to the next) can be safely encoded and scaled without fear of undermining the integrity of the data.

I believe this is the single easiest augmentation of Numer.ai data possible. It could open up a new way to reduce risk. Open questions are things like should the neural network be trained on \dot{X} or \dot{X}^2 in analogy with kinetic energy and further distinguishing the neural net input from risky features.

---

### Post #2 — **lackofintelligence** | 2021-03-08 02:07 UTC

Some additional information:

  1. Some people might think that Numer.ai already utilizes \dot{X} values buried in X because a lot of financial data is not stationary. In order to transform the data into the obfuscated range zero to one, the data must first be made stationary. As is discussed in Marcos Lopez de Prado’s book, some form of derivative is taken. MLDP suggests the fractional derivative. The fractional derivative computation involves finite differences of the data to various orders. But whatever form of derivative is used to bring some parts of the data to stationarity, this is not what we are looking for. We identify any value first brought to stationarity as X and the first difference to be \dot{X}. Doing so allows much more powerful theoretical treatment of the data. Even if Numer.ai has already computed actual \dot{X} values as I have here defined, they cannot be used in a Lagrangian treatment without being explicitly identified as first order derivatives.
  2. There is a typo after the arrow in the Euler-Lagrange equation above.
  3. It would take less than a line of code to compute the \dot{X} s, if they have not yet already be computed in the data stream.
  4. One could also consider using M(\dot{X}, X) or just M(X) in the Lagrangian. Up to now I have attempted to use the latter form but that formulation is lacking from a dynamical standpoint. To do this right we really need to know which values in the data are the \dot{X} if they are there or they need to be computed if they are not.
  5. Besides the normal process of obfuscation the other reason that it would be very difficult to reconstitute the time series of the rows is that it is not necessary to identify which columns of the \dot{X} s belong to which columns of the X s but only that the columns of data be identified as X s and \dot{X} s.

---

### Post #3 — **succulent** | 2021-03-09 08:18 UTC

I don’t follow your argument in point 5, are you saying you only want the delta X' per X rather than the additional information telling us which rows the delta came from?

I agree that this information would be extremely valuable, for many other types of models as well. I assume it is already encoded as some form of equivalent indicator.

---

### Post #4 — **lackofintelligence** | 2021-03-09 08:35 UTC _(reply to #3)_

I agree that the entire methodology that I have identified should work for any type of ML algorithm, not just Neural Networks. Whether \dot{X} already exists in the data or not does not matter if dual variables are not identified as such. Only when the variables are separately identified do theoretical Lagrangian treatments become possible to utilize.

Point 5 asserts that you do not have to know which column of X is dual to which column of \dot{X} in order to write down or code up the Lagrangians. I believe that is what you are rephrasing.

---

### Post #5 — **lackofintelligence** | 2021-03-09 08:53 UTC

TL;DR:

  * Identify stationary features of the data and identify them with X. If needed utilize the fractional derivative to create stationary features.
  * For each stationary feature calculate its dual, the derivative \dot{X}.
  * Identify which columns are X and which columns are the \dot{X}.
  * Utilizing X and \dot{X}, train machine learning algorithms with Lagrangian dynamical loss functions that encode theoretical financial conservation principles to make predictions about the future.
  * Theoretical treatments are ONLY possible by identification of these dual variables.
  * Find through theoretical justification and through experiment up-to-now completely unknown new formulas that describe the evolution of financial systems, optimize risk against gain, explain the role of Feature Neutralization and provide superior buy and sell signals.



I can understand how a lot of the pure data scientists and finance folks are puzzled by these discussions of Lagrangian Dynamics. But I am also willing to bet that there are enough Numerati who are physicists for whom these dual variables and classical mechanics ideas will all make a lot of sense as they remember back to their undergraduate or even graduate days and will probably even get a kick out of the fact that it might be possible to apply these ideas in such a field far far way.

---

### Post #6 — **gammarat** | 2021-03-09 10:03 UTC _(reply to #5)_

Isn’t the sort of information you need built into, or extractable from, the Signals competition? I don’t participate in that (and I’ve just gotten started in the Tournament competition), but Signals is based on pretty standard info, iirc.

FWIW, 15-20 years ago I was having fun putting Kalman type filters onto Forex feeds, so I would be interested in how you progress.

---

### Post #7 — **minou** | 2021-03-09 12:21 UTC _(reply to #5)_

Interesting posts. The maths is well above what I studied in my maths A levels many years ago, but has sparked some interesting reading, and finding out or relearning things that I probably should already know such as that some functions can be continuous everywhere and differentiable nowhere (e.g. Weierstrass function).

---

### Post #8 — **lackofintelligence** | 2021-03-09 18:19 UTC _(reply to #6)_

Yes. I am hoping I don’t have to head over there. I’ll give [@richai](</u/richai>) and [@mdo](</u/mdo>) time to ponder this, but I am hoping that they at least do me the favor to shoot the darn idea down instead of letting it list away.

---

### Post #9 — **gammarat** | 2021-03-09 18:43 UTC _(reply to #8)_

I do think though that one of the most interesting aspects of the Tournament is the way the.data has been severely abstracted. I think the idea behind the tournament is, more or less, to create a _maybe_ solvable problem while exploring all sorts of interesting approaches. So they move as far away from the market as they can. I find it pretty neat, just as it is.

Of course if I do get something working (I’m about ½ way there, I think), I hope to run off and use it on the markets, and lose even more money even faster ![:crazy_face:](http://forum.numer.ai/images/emoji/twitter/crazy_face.png?v=9) .

ETA: Below is a link to a paper (PDF) I read about 15 years ago that’s quite influenced my ideas of how to approach a problem like this one. It’s much more directed at target location, tracking, and identification (which was the field I was working in). It might be of interest to you as well, if you are interested in looking at the markets in a more dynamic manner.

<https://www.ee.cuhk.edu.hk/~wkma/publications/gmphd_2col.pdf>

---

### Post #10 — **lackofintelligence** | 2021-03-11 08:40 UTC

## Conserved Currents in Finance

Numerati (and others) are _convinced_ that its possible to estimate the future of the stock market. The proof of that statement, which is just a proof about the sentiment of data scientists in the present epoch in the evolution of humankind and not about the nature of reality, is that there are hundreds of data scientists staking their cash in the Numer.ai tournament.

Predictability is only possible if something that happens now, something that we know, continues to persist for some amount of time into the future. Physicists describe this situation by saying that there is a _conserved current_. This current is physical. By the word physical we mean _everything_ that occurs in nature. For example, peoples opinions are physical in the sense that they are real and they persist for some time into the future.

In the following I am going to write down an elementary proof about the nature of that current. This is really about the way we must calculate it, assuming that it exists. But I have argued that everybody agrees that it does.

I will have to use a little bit of math for this proof. But it’s so little that by now I think everybody can follow along.

### Set Up

Normally we train a model H to try to estimate y. One of the reasons that we use black box estimators is that we know that human biases are generally inferior to unemotional machine learning estimators. But instead of training any model, let’s start with the best minimum biased estimator, a linear model (OLS) and in the boosting sense, go from there:

H = A \cdot X + \ldots \tag{1} 

We also know that we can reduce the variance of our estimate by introducing some bias into our estimate of y. There are many ways to express this situation, but now we want to express this in a way that makes our linear model and its associated risk explicit. Doing so will lead to some interesting properties of the equations. Therefore, we say that we start with a minimum biased model and add to it another model, say a neural network M(\cdot), that compensates for that risk. In more data sciency terms the neural network applies the biases that reduce variances of the linear model:

H = A \cdot X+ M(\cdot) \tag{2}

Here the center dot in the argument of M explicitly indicates that we don’t know what that argument consists of in a world where the choices are the features X and their first derivatives \dot{X}.

### Definitions

We call H the Hamiltonian of a real physical dynamical financial system. Our model of it is the predictor we are after.

The linear predictor A\cdot X with features X and coefficients A is associated with the potential for gain or loss in such a real physical dynamical system. In classical mechanical terms we would call it the potential energy.

The Lagrangian of this dynamical system is:

\mathcal{L} = M(\cdot) - A\cdot X \tag{3}

The equation that describes the persistence of conserved currents into the future is called the Euler-Lagrange equation:

0 = \frac{d}{dt} \frac{\partial \mathcal{L} }{\partial \dot{X} } - \frac{\partial \mathcal{L} }{ \partial X} \tag{4} 

The universe of possible variables consist _any_ kind of features X and their duals, the first derivative of the features, \dot{X}.

### Theorem

In summary, _a biasing neural network cannot only be a function of the features in real physical systems with conserved currents_.

If A\cdot X is the minimum biased estimator of a target y associated with a dynamical potential of the above Hamiltonian that conserves a Noetherian current into the future, then no matter what the variables are for X, a compensating neural network _cannot_ only be a function of X.

#### Proof

As usual the proof begins by assuming the opposite, namely that the biasing neural network is only a function of X. Then the Langrangian is obtained by replacing the dot in Eq. 3 with X:

\mathcal{L} = M(X) - A \cdot X \tag{5}

Plugging this into the Euler-Lagrange Equation (Eq. 4) and rearranging, we trivially obtain that the derivative of the biasing neural network with respect to the features X is identically the coefficients of the linear model:

A = \frac{dM}{dX} \tag{6}

In other words the neural network tries to predict the linear model. Clearly the linear model and therefore the neural network fails to bias the estimator H.

\square

### Corollary

A neural network that correctly persists a compensating bias for a linear model must be a function of the derivatives of the features.

#### Proof

The proof follows from considering the math that led to the Theorem: Only expressions that are functions of the first derivative lead to a non-zero first term in the Euler-Lagrange equation (Eq.~4). But any function that does so leads to anything other than the linear model. Since any model that is not the linear model is more biased than OLS, then biasing can persist according to real causal physical laws.

\square

### Notes

The above theorem does not state that we cannot bias our estimate of y with only X available. For better or worse, we, _obviously_ , can always do that.

The statement about conserved currents relates directly to the question of generalizability in data science; do my biases help at the appearance of previously unseen data? The assertion is that if there exists some real dynamical quantity that persists when really new conditions arise (something real out in the world), then a compensating neural network cannot be a function of X only in order to be able to model that persisting dynamical quantity and therefore to correctly bias the linear model into the future.

The Theorem does not say we cannot get improved estimates of y by adding all kinds of new features to the linear predictor but only that risk minimizing bias cannot correctly be propagated into the future using only a bias function of the features in X even if those features consist of derivatives of stationary features themselves!

Stop pulling your hair out. When in doubt identify the derivative.

---

### Post #11 — **lackofintelligence** | 2021-03-11 09:02 UTC _(reply to #9)_

I see that paper uses transition probabilities which are closely related to derivatives.

---

### Post #12 — **linello** | 2021-03-25 20:37 UTC _(reply to #10)_

Could you please fix the math formulas? I believe some symbol are not interpreted correctly.

---

### Post #13 — **lackofintelligence** | 2021-03-25 21:35 UTC _(reply to #12)_

Just reloading the page should fix that.
