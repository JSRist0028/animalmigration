---
title: Modeling Animal Migration Routes with Machine Learning

description: Justin Rist (<a href="jsr5605@psu.edu">jsr5605@psu.edu</a>), Junyan Tian (<a href="jxt717@psu.edu">jxt717@psu.edu</a>), Christine Cummings (<a href="cmc6720@psu.edu">cmc6720@psu.edu</a>)

---
# Why we use machine learning to investigate animal migration routes?
Environmental conditions have changed significantly in the past few decades. Many species are sensitive to climate change and alter their migration pathways by long distances or change their migration  timing in  response  to changing  temperatures. Using historic species geolocation and weather data we can predict future movement, including anticipating migration path and timing shifts. It  is  particularly  challenging  and  time-consuming  to  manually  analyze  the  geolocator  data. Machine  learning  algorithms are  crucial  to  bridge  this  gap  and create  accurate  and  informative migration models. 

The overarching goal of this project is to create an easy-to-implement tool that can predict the future migration routes of any animal with historic tracking data using an automated machine learning process. 

**Click on each image below for a detailed study of these animals**

# Barnacle geese

[<img src="https://media.gettyimages.com/photos/flock-of-barnacle-geese-taking-off-from-lake-picture-id584682566?s=2048x2048" width="400" >](https://github.com/JSRist0028/animalmigration/blob/7324f5a948200a7842793bcefd7c7b6b646f21e3/website/barnaclegeese.md)

# Whales
[<img src="https://media.gettyimages.com/photos/humpback-whale-and-calf-in-the-waters-of-tonga-picture-id936167240?s=612x612" width="400" >](https://github.com/JSRist0028/animalmigration/blob/7c6138fdd1d20d9bc6fd85e556bda8b0b13058b2/website/whale.md)


# Methodology 
This project uses Python's Keras package to create a neural network for prediction. Inputs to the model include the date and location (latitudue and longitude) of the animal and the location's weather conditions on the current day. The target is animal location on the next day. Our neural network is trained using the first (by date) 70% of the dataset. The network predicts the next day location of the animal after the last date of the training set. It continues determining next day location based off of previous day prediction, building a migration path for the final 30% of the dataset. This process is repeated for every unique animal in the species dataset.

# Results

# Takeaways

# References
