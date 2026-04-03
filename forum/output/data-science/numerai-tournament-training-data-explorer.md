---
title: "Numerai Tournament Training Data Explorer"
category: Data Science
url: https://forum.numer.ai/t/numerai-tournament-training-data-explorer/1200
created_at: 2020-11-18T18:14:17.952000+00:00
last_posted_at: 2021-12-02T21:26:54.862000+00:00
posts_count: 2
views: 1347
tags: []
---

# Numerai Tournament Training Data Explorer

---

### Post #1 — **theomniacs** | 2020-11-18 18:14 UTC

# Numerai Tournament Training Data Explorer

> R Shiny Web Interface for Exploring Numerai Tournament Training Data

Numerai is a crowdsourced hedgefund that hosts machine learning tournaments which attract thousands of data scientists around the world to compete for Numeraire cryptocurrency. The company provides clean, regularized, and obfuscated data, where anyone with expertise in machine learning can freely participate.

You can use this app to explore the data before diving into any model! Here is a snapshot of what the app looks like in action:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/057bec5368a71d6a0adf95894ff0cc19ab343a67.png)](<https://crypto.omnianalytics.io/apps/numerai/>)

# Running the App

We are hosting our own instance of the app at the following URL:

<https://crypto.omnianalytics.io/apps/numerai/>

For optimal performance, you can run your own instance of the app. This requires R 4.3.x and associated R packages.

## Installing Dependencies
    
    
    ## Install CRAN dependencies
    install.packages("shiny")
    install.packages("shinyWidgets")
    install.packages("shinythemes")
    install.packages("shinycssloaders")
    install.packages("dplyr")
    install.packages("ggfortify")
    install.packages("DT")
    install.packages("stringr")
    

## Running with RStudio

If you use RStudio, you can clone or download the repository, and open the app.R file. A “Run App” button will appear at the top of RStudio. Clicking this will run the app. Note that by default, the app will open in a small pop-up window. You can click the Open in Browser link at the top to open it in your browser of choice, instead.

## Running with R

If you use R or another R GUI other than RStudio, run the following lines to execute the dashboard:
    
    
    ## Set the working directory containing the folder of the app code
    setwd("~/Work")
    
    ## Run the app using the name of the folder containing the app code 
    runApp("numerai")

---

### Post #2 — **theomniacs** | 2021-12-02 21:26 UTC

Our Numerai Tournament Training Data Explorer App has been updated to be compatible with the new “Super Massive Dataset”.

Code: [GitHub - OmniacsDAO/numerai-explorer](<https://github.com/Omni-Analytics-Group/numerai-explorer>)  
App: <https://crypto.omnianalytics.io/apps/numerai/>

Screenshots:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/38fb063e4c4d181549c112a62c96eb93b570506b_2_690x310.png)image1882×848 113 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/38fb063e4c4d181549c112a62c96eb93b570506b.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/af202096773d66b5973d403dabd5577c15b20a23_2_690x330.png)image1825×875 68.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/af202096773d66b5973d403dabd5577c15b20a23.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d6e350120577249ee1aebaaa0ba99df7b4a235e9_2_560x500.png)image815×727 25.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d6e350120577249ee1aebaaa0ba99df7b4a235e9.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/675cb78370a1176e68de7c614d2e966e5d1fa833_2_690x363.png)image1171×617 37.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/675cb78370a1176e68de7c614d2e966e5d1fa833.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/728729910d840f92ca3620e510c9d283dea939f6_2_690x381.png)image1222×675 59.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/728729910d840f92ca3620e510c9d283dea939f6.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4768d823a26beea127c4cabad8c50e984c313ff1_2_577x500.png)image1035×896 93.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4768d823a26beea127c4cabad8c50e984c313ff1.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/48688ecc42df32e775b55aacec42f1dcfccc6938_2_689x360.png)image1374×718 88.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/48688ecc42df32e775b55aacec42f1dcfccc6938.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6f765f03f1a43ec07237c4e83324c588ef3f8831_2_690x355.jpeg)image1376×709 152 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6f765f03f1a43ec07237c4e83324c588ef3f8831.jpeg> "image")
