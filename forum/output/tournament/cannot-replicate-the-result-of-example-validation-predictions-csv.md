---
title: "Cannot replicate the result of example_validation_predictions.csv"
category: Tournament
url: https://forum.numer.ai/t/cannot-replicate-the-result-of-example-validation-predictions-csv/5146
created_at: 2022-03-24T02:09:55.304000+00:00
last_posted_at: 2022-03-27T03:10:01.041000+00:00
posts_count: 2
views: 545
tags: []
---

# Cannot replicate the result of example_validation_predictions.csv

---

### Post #1 — **omegaz** | 2022-03-24 02:09 UTC

Running the example script example_model.py does not give the same result as example_validation_predictions.csv.

This is the command I used:
    
    
    pip3 install -r requirements.txt
    python3 example_model.py
    

And below is the difference:
    
    
    $ head example_validation_predictions.csv
    id,prediction
    n000777698096000,0.22826
    n0009793a3b91c27,0.73120
    n00099ccd6698ab0,0.84688
    n0019e36bbb8702b,0.84971
    n0028cb874439df8,0.17504
    n002ff30f2ccd7e0,0.46245
    n00310da5e169a35,0.41654
    n003fa83b4f2f608,0.44718
    n004af567f93ca2c,0.59547
    
    $ head validation_predictions_308.csv
    id,prediction
    n000777698096000,0.4399175033076504
    n0009793a3b91c27,0.30779678981873704
    n00099ccd6698ab0,0.7927576353913034
    n0019e36bbb8702b,0.6281682102368538
    n0028cb874439df8,0.124921709675387
    n002ff30f2ccd7e0,0.6480622913030104
    n00310da5e169a35,0.27058618606598994
    n003fa83b4f2f608,0.4535094448706403
    n004af567f93ca2c,0.5285866233799925
    

I am using the 308 era data. Any idea about the difference?

---

### Post #2 — **jefferythewind** | 2022-03-27 03:10 UTC

I actually recently had the same question. You can see a big difference submitting to the diagnostics as well. The downloaded file has .25 corr with .95 sharpe but the file produced from the `example_model.py` is much worse than that.
