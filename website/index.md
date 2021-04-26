---
title: Modeling Animal Migration Routes with Machine Learning

---

# Why use machine learning to investigate animal migration routes?
Environmental conditions have changed significantly in the past few decades. Many species are sensitive to climate change and alter their migration pathways by long distances or change their migration  timing in  response  to changing  temperatures. Using historic species geolocation and weather data we can predict future movement, including anticipating migration path and timing shifts. It  is  particularly  challenging  and  time-consuming  to  manually  analyze  the  geolocator  data. Machine  learning  algorithms are  crucial  to  bridge  this  gap  and create  accurate  and  informative migration models. 

The overarching goal of this project is to create an easy-to-implement tool that can predict the future migration routes of any animal with historic tracking data using an automated machine learning process. 


# Data selection
Among all the migratory animals, we are interested in waterflow near the Arctic area because: (1) they have less interactions with human beings; (2) the bird migration in the Arctic area is one of the most important events in the natural world [5]; (3) the climate changing speed in the Arctic area is the fastest on Earth [6]; and (4) previous research indicated that climate change in Arctic area is affecting animals’ migration [7].

**Click on each image below for a detailed study of these animals**


[<img src="https://github.com/JSRist0028/animalmigration/blob/57e907a53538094c530b101bd2f4b9d25f7831d8/website/goose_thumbnail.PNG?raw=true" width="400" >](https://jsrist0028.github.io/animalmigration/website/barnaclegeese)


[<img src="https://github.com/JSRist0028/animalmigration/blob/57e907a53538094c530b101bd2f4b9d25f7831d8/website/swan_thumbnail.PNG?raw=true" width="400" >](https://jsrist0028.github.io/animalmigration/website/swan)


# Methodology 
<img src="https://github.com/JSRist0028/animalmigration/blob/beccd0e282fd6a8da0bf041d68d46f3bb8175931/website/ProcessFlow.PNG?raw=true" width="800" >

This project uses Python's Keras package to create a neural network for prediction. Inputs to the model include the date and location (latitudue and longitude) of the animal and the location's weather conditions on the current day. The target is animal location on the next day. Our neural network is trained using the first (by date) 75% of the dataset. The network predicts the next day location of the animal after the last date of the training set. It continues determining next day location based off of previous day prediction, building a migration path for the final 25% of the dataset. This process is repeated for every unique animal in the species dataset.

# Results
Using barnacle geese data from the Movebank Data Repository, we found that the model to predict the next day migration routes fitted better than the one to predict year-long migration routes. After including temperature as a predictor, the model prediction loss decreased, which indicates that temperature had an impact on barnacle geese’s migration routes. 

Similar to the barnacle geese’s result, the model of predicting tundra swans’ next day migration fitted better than the model of predicting year-long migration routes. However, models with temperature had worse accuracy than those without temperature. Previous research has also suggested that the migration speed and route of tundra swans were consistent across years.[4]


# Takeaways
This project demonstrates that a neural network framework is an efficient way to predict the migration routes of animals. Although this tool is less accurate than prediction methods on induvidual speicies, it is general and does not require extensive background knowledge in animal behavior in order to be implemented. However, to ensure valid results we do recommend doing research on migration patterns for a particular animal species in parallel with use of the model, ensuring that the model results will be valid. Applying this model will help researchers and policy makers better understand animal migration patterns so that these animal species will not be harmed with future climate change and infastructure development. We welcome you to give the code an animal species of interest and hope to update and improve the model in future studies! 

# Contact us
Justin Rist (<a href="jsr5605@psu.edu">jsr5605@psu.edu</a>)

Junyan Tian (<a href="jxt717@psu.edu">jxt717@psu.edu</a>)

Christine Cummings (<a href="cmc6720@psu.edu">cmc6720@psu.edu</a>)

# References
1. Trinder, Mark N., Hassell, David and Votier, Stephen. “Reproductive performance in arctic‐nesting geese is influenced by environmental conditions during the wintering, breeding and migration seasons.” Oikos Vol. 118 No. 7 (2009): pp. 1093-1101. DOI: 10.1111/j.1600-0706.2009.17429.x 

2. Shariati-Najafabadi, Mitra, Darvishzadeh, Roshanak, Skidmore, Andrew K., Kölzsch, Andrea, Exo, Klaus-Michael, Nolet, Bart A., ... and Toxopeus, Albertus G. “Environmental parameters linked to the last migratory stage of barnacle geese en route to their breeding sites.” Animal behaviour Vol. 118 (2016): pp. 81-95. DOI: 10.1016/j.anbehav.2016.05.018 

3. Hupp, Jerry W., Ward, David H., Soto, David X. and Hobson, Keith A. “Spring temperature, migration chronology, and nutrient allocation to eggs in three species of arctic‐nesting geese: Implications for resilience to climate warming.” Global Change Biology Vol. 24 No. 11 (2018): pp. 5056-5071. DOI: 10.1111/gcb.14418 

4. Nuijten, Rascha. J. "Bewick's Swans in a Changing World: Species Responses and the Need for Dynamic Nature Conservation. Universiteit van Amsterdam." Universiteit van Amsterdam (2020).
