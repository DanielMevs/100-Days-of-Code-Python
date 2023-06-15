import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('boston.csv', index_col=0)


# Preliminary Data Exploration 🔎

''' 
**Challenge**

* What is the shape of `data`? 
* How many rows and columns does it have?
* What are the column names?
* Are there any NaN values or duplicates?

'''


# print(data.shape)

# print(data.columns)

# print(data.head())

# print(data.tail())

# print(data.count())


## Data Cleaning - Check for Missing Values and Duplicates

# print(data.info())

# print(f'Any NaN values? {data.isna().values.any()}')

# print(f'Any duplicates? {data.duplicated().values.any()}')


## Descriptive Statistics

'''
**Challenge**

* How many students are there per teacher on average?
* What is the average price of a home in the dataset?
* What is the `CHAS` feature? 
* What are the minimum and the maximum value of the `CHAS` and why?
* What is the maximum and the minimum number of rooms per dwelling in the dataset?

'''

# print(data.describe())

'''
`CHAS` shows whether the home is next to the Charles River or not. 
As such, it only has the value 0 or 1. This kind of feature is also
 known as a dummy variable. 

The average price of a Boston home in the 1970s was 22.53 or $22,530.
 We've experienced a lot of inflation and house price appreciation since then!
'''


## Visualise the Features

'''

**Challenge**: Having looked at some descriptive statistics, visualise the data for your model. Use [Seaborn's `.displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot) to create a bar chart and superimpose the Kernel Density Estimate (KDE) for the following variables: 
* PRICE: The home price in thousands.
* RM: the average number of rooms per owner unit.
* DIS: the weighted distance to the 5 Boston employment centres i.e., the estimated length of the commute.
* RAD: the index of accessibility to highways. 

Try setting the `aspect` parameter to `2` for a better picture. 

What do you notice in the distributions of the data? 

'''

# sns.displot(data['PRICE'], 
#             bins=50, 
#             aspect=2,
#             kde=True, 
#             color='#2196f3')

# plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
# plt.xlabel('Price in 000s')
# plt.ylabel('Nr. of Homes')

# plt.show()

#### Distance to Employment - Length of Commute

# sns.displot(data.DIS, 
#             bins=50, 
#             aspect=2,
#             kde=True, 
#             color='darkblue')

# plt.title(f'Distance to Employment Centres. Average: {(data.DIS.mean()):.2}')
# plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
# plt.ylabel('Nr. of Homes')

# plt.show()

#### Number of Rooms

# sns.displot(data.RM, 
#             aspect=2,
#             kde=True, 
#             color='#00796b')

# plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}')
# plt.xlabel('Average Number of Rooms')
# plt.ylabel('Nr. of Homes')

# plt.show()


# plt.figure(figsize=(10, 5), dpi=200)

# plt.hist(data['RAD'], 
#          bins=24, 
#          ec='black', 
#          color='#7b1fa2', 
#          rwidth=0.5)

# plt.xlabel('Accessibility to Highways')
# plt.ylabel('Nr. of Houses')
# plt.show()

#### Next to the River? ⛵️

'''

**Challenge**

Create a bar chart with plotly for CHAS to show many more homes 
are away from the river versus next to it. 

You can make your life easier by providing a list of 
values for the x-axis (e.g., `x=['No', 'Yes']`)
'''

river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
             y=river_access.values,
             color=river_access.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Next to Charles River?')

bar.update_layout(xaxis_title='Property Located Next to the River?', 
                  yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()
