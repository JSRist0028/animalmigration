---
title: Modeling Animal Migration Routes with Machine Learning

---

# Why use machine learning to investigate animal migration routes?
Environmental conditions have changed significantly in the past few decades. Many species are sensitive to climate change and alter their migration pathways by long distances or change their migration  timing in  response  to changing  temperatures. Using historic species geolocation and weather data we can predict future movement, including anticipating migration path and timing shifts. It  is  particularly  challenging  and  time-consuming  to  manually  analyze  the  geolocator  data. Machine  learning  algorithms are  crucial  to  bridge  this  gap  and create  accurate  and  informative migration models. 

The overarching goal of this project is to create an easy-to-implement tool that can predict the future migration routes of any animal with historic tracking data using an automated machine learning process. 

**Click on each image below for a detailed study of these animals**


[<img src="https://github.com/JSRist0028/animalmigration/blob/57e907a53538094c530b101bd2f4b9d25f7831d8/website/goose_thumbnail.PNG?raw=true" width="400" >](https://jsrist0028.github.io/animalmigration/website/barnaclegeese)


[<img src="https://github.com/JSRist0028/animalmigration/blob/57e907a53538094c530b101bd2f4b9d25f7831d8/website/swan_thumbnail.PNG?raw=true" width="400" >](https://jsrist0028.github.io/animalmigration/website/swan)


# Methodology 
<img src="https://github.com/JSRist0028/animalmigration/blob/beccd0e282fd6a8da0bf041d68d46f3bb8175931/website/ProcessFlow.PNG?raw=true" width="800" >

This project uses Python's Keras package to create a neural network for prediction. Inputs to the model include the date and location (latitudue and longitude) of the animal and the location's weather conditions on the current day. The target is animal location on the next day. Our neural network is trained using the first (by date) 70% of the dataset. The network predicts the next day location of the animal after the last date of the training set. It continues determining next day location based off of previous day prediction, building a migration path for the final 30% of the dataset. This process is repeated for every unique animal in the species dataset.

# Results
Using barnacle geese data from the Movebank Data Repository, we found that the model to predict the next day migration routes fitted better than the one to predict year-long migration routes. After including temperature as a predictor, the model prediction loss decreased, which indicates that temperature had an impact on barnacle geese’s migration routes. 

Similar to the barnacle geese’s result, the model of predicting tundra swans’ next day migration fitted better than the model of predicting year-long migration routes. However, models with temperature had worse accuracy than those without temperature. Previous research has also suggested that the migration speed and route of tundra swans were consistent across years.


# Takeaways
This project demonstrates that a neural network framework is an efficient way to predict the migration routes of animals. Although this tool is less accurate than prediction methods on induvidual speicies, it is general and does not require extensive background knowledge in animal behavior in order to be implemented. However, to ensure valid results we do recommend doing research on migration patterns for a particular animal species in parallel with use of the model, ensuring that the model results will be valid. Applying this model will help researchers and policy makers better understand animal migration patterns so that these animal species will not be harmed with future climate change and infastructure development. We welcome you to give the code an animal species of interest and hope to update and improve the model in future studies! 

# Contact us
Justin Rist (<a href="jsr5605@psu.edu">jsr5605@psu.edu</a>)

Junyan Tian (<a href="jxt717@psu.edu">jxt717@psu.edu</a>)

Christine Cummings (<a href="cmc6720@psu.edu">cmc6720@psu.edu</a>)

# References
