
import pandas as pd

sp500_yearly_returns = pd.read_csv('Resources/sp500_yearly_returns.csv', index_col=[0])

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

%matplotlib

'''
    symbol  return_2018  return_2019
0     AAPL       -0.054        0.890

trying to predict...

but the values come to be : 

   return_2018  return_2018_values
0         -0.2            0.317307
1          0.0            0.321321
2          0.2            0.325334


'''


# Import numpy with alias np
import numpy as np

from statsmodels.formula.api import ols

# Create the model, fit it
return_2018_vs_r_2019 = ols('return_2019 ~ return_2018', data=sp500_yearly_returns).fit()

#extrapolation / prediction

# Define a DataFrame impossible
return_2018_values = pd.DataFrame({'return_2018': [-0.2, 0, 0.2]})

pred_2019_values = return_2018_values.assign(return_2018_values=return_2018_vs_r_2019.predict(return_2018_values))

print(pred_2019_values)

'''
Incredible investment predictions! 
Investments that gained a lot in value in 2018 on average gained only a small amount in 2019. 
Similarly, investments that lost a lot of value in 2018 on average also gained a small amount in 2019.


and graphing:

# Create a new figure, fig
fig = plt.figure()

# Plot the first layer: y = x
plt.axline(xy1=(0,0), slope=1, linewidth=2, color="green")

# Add scatter plot with linear regression trend line
sns.regplot(x='return_2018',
            y='return_2019', 
        data=sp500_yearly_returns)

# Set the axes so that the distances along the x and y axes look the same
plt.axis('equal')

# Show the plot
plt.show()

see 11-graph.jpg
'''



