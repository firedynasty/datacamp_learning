'''
prices:

based on the distance from the metro:

You transform like a robot in disguise! By transforming the explanatory variable, 
the relationship with the response variable became linear, and so a linear regression
 became an appropriate model.

'''



import pandas as pd

taiwan_real_estate = pd.read_csv('Resources/taiwan_real_estate.csv', index_col=[0])

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

%matplotlib


taiwan_real_estate


'''

categorical value for the house age in years.


  dist_to_mrt_m    n_convenience  house_age_years      price_twd_msq
        84.8788               10  30 to 45                  11.4675
       306.595                 9  15 to 30                  12.7685
       561.985                 5  0 to 15                   14.3116
       561.985                 5  0 to 15                   16.5809
       390.568                 5  0 to 15                   13.0408


                          
                          
  ******  *******   ***** 
 **////**//**///** **///**
/**   /** /**  /**/*******
/**   /** /**  /**/**//// 
//******  ***  /**//******
 //////  ///   //  ////// 

'''

# Import numpy with alias np
import numpy as np

from statsmodels.formula.api import ols

# Create the model, fit it
mdl_price_vs_conv = ols('price_twd_msq ~ n_convenience', data=taiwan_real_estate).fit()

# Print the parameters of the fitted model
print(mdl_price_vs_conv.params)


# Create explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)


'''
   **                      
  /**                      
 ****** ***     **  ****** 
///**/ //**  * /** **////**
  /**   /** ***/**/**   /**
  /**   /****/****/**   /**
  //**  ***/ ///**//****** 
   //  ///    ///  //////  
'''



# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

plt.figure()

# Plot using the transformed variable
sns.regplot(x='sqrt_dist_to_mrt_m', y='price_twd_msq', data=taiwan_real_estate, ci=None)
plt.show()

'''

next

'''


# run a linear regression : price_twd_msq vs sqrt(dist_to_mrt_m)

# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. square root of dist_to_mrt_m using taiwan_real_estate
mdl_price_vs_dist = ols('price_twd_msq ~ sqrt_dist_to_mrt_m', data=taiwan_real_estate).fit()

# Print the parameters
print(mdl_price_vs_dist.params)

'''

next

'''

import pandas as pd

taiwan_real_estate = pd.read_csv('Resources/taiwan_real_estate.csv', index_col=[0])

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

%matplotlib


taiwan_real_estate

import numpy as np

from statsmodels.formula.api import ols


# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. sqrt_dist_to_mrt_m
mdl_price_vs_dist = ols("price_twd_msq ~ sqrt_dist_to_mrt_m", data=taiwan_real_estate).fit()

explanatory_data = pd.DataFrame({"sqrt_dist_to_mrt_m": np.sqrt(np.arange(0, 81, 10) ** 2),
                                "dist_to_mrt_m": np.arange(0, 81, 10) ** 2})

# goes from 0,10,20,30,40,50,60,70,80

# Create prediction_data by adding a column of predictions to explantory_data
prediction_data = explanatory_data.assign(
    price_twd_msq = mdl_price_vs_dist.predict(explanatory_data)
)

# Print the result
print(prediction_data)

'''
Using matplotlib backend: MacOSX
   sqrt_dist_to_mrt_m  dist_to_mrt_m  price_twd_msq
0                 0.0              0      16.709799
1                10.0            100      14.881370
2                20.0            400      13.052942
3                30.0            900      11.224513
4                40.0           1600       9.396085
5                50.0           2500       7.567656
6                60.0           3600       5.739227
7                70.0           4900       3.910799
8                80.0           6400       2.082370

'''


''' next:

add a layer to the plot

Add a layer to your plot containing points from prediction_data, colored "red".




'''

fig = plt.figure()
sns.regplot(x="sqrt_dist_to_mrt_m", y="price_twd_msq", data=taiwan_real_estate, ci=None)

# Add a layer of your prediction points
sns.scatterplot(x='sqrt_dist_to_mrt_m', y='price_twd_msq', data=prediction_data, color='red')
plt.show()





