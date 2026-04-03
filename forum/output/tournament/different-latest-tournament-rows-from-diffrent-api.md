---
title: "Different latest tournament rows from diffrent api?"
category: Tournament
url: https://forum.numer.ai/t/different-latest-tournament-rows-from-diffrent-api/1062
created_at: 2020-10-13T03:00:29.484000+00:00
last_posted_at: 2020-10-13T03:54:56.047000+00:00
posts_count: 2
views: 630
tags: []
---

# Different latest tournament rows from diffrent api?

---

### Post #1 — **wentixiaogege** | 2020-10-13 03:00 UTC

**API one:**  
the code is from:  
https://www.kaggle.com/carlolepelaars/how-to-get-started-with-numerai  
def download_current_data(directory: str):  
“”"  
Downloads the data for the current round  
:param directory: The path to the directory where the data needs to be saved  
“”"  
current_round = NAPI.get_current_round()  
if os.path.isdir(f’{directory}/numerai_dataset_{current_round}/’):  
print(f"You already have the newest data! Current round is: {current_round}")  
else:  
print(f"Downloading new data for round: {current_round}!")  
NAPI.download_current_dataset(dest_path=directory, unzip=True)  
**API two:**  
tournament_data = pd.read_csv(“<https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz>”)

before monday 2:00utc pm, they have differenct rows,but after that time, I download the latest data again ,they are match? cause using API one I tried many times, always got “invilad match ids include the order issue”, can’t be wrong~~;

---

### Post #2 — **wentixiaogege** | 2020-10-13 03:54 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5ab8538472794cb0303c1b54c3e44bc1065c4cff.png)image611×136 8.42 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5ab8538472794cb0303c1b54c3e44bc1065c4cff.png> "image")

  
this is my previous rows difference~~!!!
