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

# Histograms of price_twd_msq with 10 bins, split by the age of each house
sns.displot(data=taiwan_real_estate,
         x='price_twd_msq',
         col='house_age_years',
         col_wrap=3,
         bins=10)

# Show the plot
plt.show()

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


# Calculate the mean of price_twd_msq, grouped by house age
mean_price_by_age = taiwan_real_estate.groupby('house_age_years')['price_twd_msq'].mean()

# Print the result
print(mean_price_by_age)



'''


house_age_years
0 to 15     12.637
15 to 30     9.877
30 to 45    11.393
Name: price_twd_msq, dtype: float64

'''

from statsmodels.formula.api import ols

# Create the model, fit it
mdl_price_vs_age = ols('price_twd_msq ~ house_age_years', data=taiwan_real_estate).fit()

# Print the parameters of the fitted model
print(mdl_price_vs_age.params)


# you need the intercept to have a working model

# Update the model formula to remove the intercept
mdl_price_vs_age0 = ols("price_twd_msq ~ house_age_years + 0", data=taiwan_real_estate).fit()

# Print the parameters of the fitted model
print(mdl_price_vs_age0.params)

'''

# Linear regression with a categorical explanatory variable
house_age_years[0 to 15]     12.637
house_age_years[15 to 30]     9.877
house_age_years[30 to 45]    11.393

look at the mean, I still have a vague understanding of this here.

'''

