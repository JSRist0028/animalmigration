# Swan Results 

We analyzed Tundra swan migration data from the [Movebank database repository](www.movebank.org) across four years. These swans migrate across the northern United States and Canada every year. They live on the north east and west coasts of the United States. They migrate to the artic coastal areas of Canada and Alaska to breed.

![alt="Swan tracks" width="240", height="180" border="10"](https://github.com/JSRist0028/animalmigration/blob/0938bff04f6a34bd25397906360ec90793c9fe77/website/swan_tracks.PNG?raw=true)

Tracked movements of swans over 5 years (July 2008 - Feburary 2012)

We modeled and predicted where each tracked bird was expected to be the next day and traced year-long migration routes. We trained our model with the first 75% (or 3 years) of our tracked data and compared our results using only the bird's location data to our results using the bird's location data and daily weather data. We looked at the accuracy for our model predicting the next location in our "training data" (the first 75% of data), the next day location of our "testing data" (the remaining 25% of data), and the locations of each bird continuously for a future year of data (tested using the final 25% of data). The loss for each prediction type is shown in the figure below. While our next day predictions were fairly accurace, predicting the swan's location far in the future was less accurate. 


|    | Training data loss | Next day prediction loss | Year-long prediction loss |
| --- | --- | --- | --- |
| Without Temperature | 1.9 | 2.0 | 11.6 |
| With Temperature | 2.4 | 2.4 | 15.2 | 


![alt="Swan results" width="880" border="10"](https://github.com/JSRist0028/animalmigration/blob/94fd4e5fd2e6634fae69666f3989a87153fb50b7/website/swan_results.PNG?raw=true)


<img src="https://github.com/JSRist0028/animalmigration/blob/be52614bc1b553311ed2855c2c19466238182d2e/animations/SwanNoTemp.gif?raw=true" width="500" />
<img src="https://github.com/JSRist0028/animalmigration/blob/be52614bc1b553311ed2855c2c19466238182d2e/animations/SwanTemp.gif?raw=true" width="500" /> 
