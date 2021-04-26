# Barnacle Geese Results 

We analyzed barnacle geese data near the Barents Sea from the [Movebank database repository](www.movebank.org) across four years. Barnacle geese predominately live in the Arctic area and migrate every year. A previous simulation study has found that increasing temperatures correlate to and can predict increases in the barnacle goose population.[4] Various indicators of climate change, such as mean daily air temperature, wind, low-altitude cloud cover and timing of spring, have also been associated with barnacle geese’s migration route.[5,6]

![alt="Geese tracks" width="240", height="180" border="10"](https://github.com/JSRist0028/animalmigration/blob/3bc2be85841a5446790dae1d9d96fb33ac6c8285/website/barnaclegeesetracks.png?raw=true)

**Tracked movements of 14 barnacle geese over 4 years (January 2008 - April 2011)**


We modeled and predicted where each tracked bird was expected to be the next day and traced year-long migration routes. We trained our model with the first 75% (or 3 years) of our tracked data and compared our results using only the bird's location data to our results using the bird's location data and daily weather data. We looked at the accuracy for our model predicting the next location in our "training data" (the first 75% of data), the next day location of our "testing data" (the remaining 25% of data), and the locations of each bird continuously for a future year of data (tested using the final 25% of data). The loss for each prediction type is shown in the figure below. While our next day predictions were fairly accurate, predicting the geese's location far in the future was less accurate. 

An interesting observation the team noticed is that inclusion of temperature data increased the model prediction accuracy. This implies barnacle geese migration is impacted by temperature. The model can then be used with simulated temperatures to forecast how barnacle gees migration could be impacted by global increases in temperature.


|    | Training data loss | Next day prediction loss | Year-long prediction loss |
| --- | --- | --- | --- |
| Without Temperature | 0.70 | 0.72 | 12.16 |
| With Temperature | 0.67 | 0.67 | 8.2 | 


![alt="Geese results" width="880" border="10"](https://github.com/JSRist0028/animalmigration/blob/94fd4e5fd2e6634fae69666f3989a87153fb50b7/website/goose_results.PNG?raw=true)

<img src="https://github.com/JSRist0028/animalmigration/blob/cf88cd2bc6fd08950ad5a01aeafcb75bb0c46602/animations/GooseNoTemp.gif?raw=true" width="500" />
<img src="https://github.com/JSRist0028/animalmigration/blob/cf88cd2bc6fd08950ad5a01aeafcb75bb0c46602/animations/GooseTemp.gif?raw=true" width="500" /> 

# How will Global Warming likely affect goose migration?
<img src="https://github.com/JSRist0028/animalmigration/blob/c672b258604944b464d091141b3f5f34360dd60d/animations/GooseGW.gif?raw=true" width="500" /> 

In this figure, 'GW' indicates that the datapoints are related to the prediction with a two degree celsius temperature increase, while 'no GW' indicates the path with the actual temperature values. A a temperature increase is predicted to cause the geese the migrate sooner and migrate farther south. 
