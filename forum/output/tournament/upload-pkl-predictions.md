---
title: "Upload pkl predictions"
category: Tournament
url: https://forum.numer.ai/t/upload-pkl-predictions/7005
created_at: 2024-01-31T14:50:26.068000+00:00
last_posted_at: 2024-04-20T16:10:30.278000+00:00
posts_count: 5
views: 601
tags: []
---

# Upload pkl predictions

---

### Post #1 — **marc_gg** | 2024-01-31 14:50 UTC

Hi people!

I am trying to upload a prediction function using cloudpickle. It works fine if all the code is in the same file, but when creating a folder structure, the pkl is uploaded but it can not be extracted correctly as it miss modules. If the main file is like:

from my_module import my_func  
…  
def predict(live_features: pd.DataFrame) → pd.DataFrame:  
features = my_func(live_features)  
live_predictions = model.predict(lfeatures)  
submission = pd.Series(live_predictions, index=live_features.index)  
return submission.to_frame(“prediction”)

In this case how I should proceed? Numerai tells me “my_module” is not found

Thanks in advance

---

### Post #2 — **shatteredx** | 2024-01-31 20:53 UTC

I think you have to keep all the code in the same file. Maybe someone can prove me wrong?

---

### Post #3 — **rpica** | 2024-04-18 07:29 UTC _(reply to #2)_

This is really frustrating ![:pensive:](http://forum.numer.ai/images/emoji/twitter/pensive.png?v=12), I think it’s the first time I’m punished for giving code some structure…

Did someone find a solution or we have to copy paste all related code into a single python module to make cloudpickle work? (and hence, model uploads, which is an amazing feature)

---

### Post #4 — **marc_gg** | 2024-04-18 10:54 UTC _(reply to #3)_

Completly agree, it is frustrating. It did not manage to solve the issue, I finally decided to make the training, evaluation and some other stuff with a code using structure, but when submitting I have a single code that loads the models and the feature list, the only issue I have to copy-paste the same code to recreate the generated-variables, as importing the code does not work, but importing list and models it does.

---

### Post #5 — **0xleo** | 2024-04-20 16:10 UTC

It’s marked as experimental, but have you tried marking your module to be picked by value instead of by reference?

[github.com](<https://github.com/cloudpipe/cloudpickle#overriding-pickles-serialization-mechanism-for-importable-constructs>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9c3f78ead3e9022a888636bfa520f27b5b0a9752_2_690x344.png)

### [GitHub - cloudpipe/cloudpickle: Extended pickling support for Python objects](<https://github.com/cloudpipe/cloudpickle#overriding-pickles-serialization-mechanism-for-importable-constructs>)

Extended pickling support for Python objects
    
    
    import cloudpickle
    import my_module
    cloudpickle.register_pickle_by_value(my_module)
    cloudpickle.dumps(my_module.my_function)  # my_function is pickled by value
    cloudpickle.unregister_pickle_by_value(my_module)
    cloudpickle.dumps(my_module.my_function)  # my_function is pickled by reference
