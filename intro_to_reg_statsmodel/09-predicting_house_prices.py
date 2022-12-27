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
print(mdl_price_vs_age.params)


# Create explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)

# Create prediction_data
prediction_data = explanatory_data.assign(price_twd_msq = mdl_price_vs_conv.predict(explanatory_data))

# Print the result
print(prediction_data)



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

#visualizing the data


# Create a new figure, fig
fig = plt.figure()

sns.regplot(x="n_convenience",
            y="price_twd_msq",
            data=taiwan_real_estate,
            ci=None)
# Add a scatter plot layer to the regplot
sns.scatterplot(x='n_convenience', y='price_twd_msq', data=prediction_data, color='red')

# Show the layered plot
plt.show()

'''
   **                         
  /**                         
 ****** ******  *****   ******
///**/ //**//* **///** **//// 
  /**   /** / /*******//***** 
  /**   /**   /**////  /////**
  //** /***   //****** ****** 
   //  ///     ////// //////  
'''

#extrapolation

# Define a DataFrame impossible
impossible = pd.DataFrame({'n_convenience': [-1, 2.5]})

pred_impossible = impossible.assign(price=mdl_price_vs_conv.predict(impossible))

print(pred_impossible)

"""

   ...: print(pred_impossible)
   n_convenience      price
0           -1.0   7.426158
1            2.5  10.219437

Legendary limit detection! Linear models don't know what is possible or not in real life. 
That means that they can give you predictions that don't make any sense when applied to your data. 
You need to understand what your data means in order to determine whether a prediction is nonsense or not.

""""