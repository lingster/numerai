---
title: "Automating Rust"
category: Tournament
url: https://forum.numer.ai/t/automating-rust/6642
created_at: 2023-09-02T07:53:15.856000+00:00
last_posted_at: 2023-09-05T03:12:09.996000+00:00
posts_count: 5
views: 607
tags: []
---

# Automating Rust

---

### Post #1 — **liborty** | 2023-09-02 07:53 UTC

I have been running Rust since the beginning. I have shell script cron automation on my local machine but sometimes deadlines get missed, for example because of internet connection problems. I wonder if there is any way of making use of the compute lite beta? It can be done. I am able to run Rust securely for example on github actions. All the instructions on numerai, however, seem to assume that we run interpreted (slow) Python.

---

### Post #2 — **numerologist** | 2023-09-03 17:48 UTC

I don’t think you’ll get a good response here, the dominant majority uses Python with some using R too.

But if you are determined, [GitHub - PyO3/pyo3: Rust bindings for the Python interpreter](<https://github.com/PyO3/pyo3>) might be worth looking into. No guarantees that it will work out the way you expect though.

Also, note that compute-lite is currently not well supported. See [Discord](<https://discord.com/channels/894652647515226152/1145904192553226351/1146504225858265250>)

---

### Post #3 — **liborty** | 2023-09-04 02:16 UTC _(reply to #2)_

I am more likely to go the other way and to use Parquet reader etc. directly from Rust. Still no server automation though.

---

### Post #4 — **quantverse** | 2023-09-04 16:30 UTC

Kudos for trying to use Rust to implement Numerai pipeline! I develop in Rust on a daily basis yet I still use Python for Numerai mainly for historical and compatibility reasons. But for instance [polars](<https://www.pola.rs/>) looks to be a great replacement for pandas (and it should handle reading parquet files natively), so maybe I will move to Rust with my pipelines as well one day…

About automation - I would just pack your whole pipeline as a simple docker image (so compiling your Rust binaries will be part of the Dockerfile) and then use Amazon ECS & Fargate to schedule and run the container appropriately.

Some example how you could containerize your Rust programs: [Getting Started with Rust and Docker – Collabnix](<https://collabnix.com/getting-started-with-rust-and-docker/>)

Good luck!

---

### Post #5 — **liborty** | 2023-09-05 03:12 UTC _(reply to #4)_

Thanks for the headsup about polars. They look promising, I will try them.  
If I can avoid going through all those python pyrotechnics just to convert .parquet to .csv,  
then my pipeline will be so much simpler and faster!
