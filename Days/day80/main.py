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

# river_access = data['CHAS'].value_counts()

# bar = px.bar(x=['No', 'Yes'],
#              y=river_access.values,
#              color=river_access.values,
#              color_continuous_scale=px.colors.sequential.haline,
#              title='Next to Charles River?')

# bar.update_layout(xaxis_title='Property Located Next to the River?', 
#                   yaxis_title='Number of Homes',
#                   coloraxis_showscale=False)
# bar.show()


# Understand the Relationships in the Data

'''**Challenge**

There might be some relationships in the data that we should know about. Before you run the code, make some predictions:

* What would you expect the relationship to be between pollution (NOX) and the distance to employment (DIS)? 
* What kind of relationship do you expect between the number of rooms (RM) and the home value (PRICE)?
* What about the amount of poverty in an area (LSTAT) and home prices? '''


# sns.pairplot(data)

# # You can even include a regression line
# # sns.pairplot(data, kind='reg', plot_kws={'line_kws':{'color': 'cyan'}})
# plt.show()


# **Challenge**

'''Use Seaborn's .jointplot() to look at some of the relationships 
in more detail. Create a jointplot for:

* DIS and NOX
* INDUS vs NOX
* LSTAT vs RM
* LSTAT vs PRICE
* RM vs PRICE

Try adding some opacity or `alpha` to the scatter plots using keyword
 arguments under `joint_kws`.
 
 '''

# with sns.axes_style('darkgrid'):
#   sns.jointplot(x=data['DIS'], 
#                 y=data['NOX'], 
#                 height=8, 
#                 kind='scatter',
#                 color='deeppink', 
#                 joint_kws={'alpha':0.5})

# plt.show()

# with sns.axes_style('darkgrid'):
#   sns.jointplot(x=data.NOX, 
#                 y=data.INDUS, 
#                 # kind='hex', 
#                 height=7, 
#                 color='darkgreen',
#                 joint_kws={'alpha':0.5})
# plt.show()




#### % of Lower Income Population vs Average Number of Rooms


'''

*Challenge** 

Compare LSTAT (proportion of lower-income population)
with RM (number of rooms) using Seaborn's `.jointplot()`.
How does the number of rooms per dwelling vary with the
 poverty of area? Do homes have more or fewer rooms when LSTAT is low?

'''


# with sns.axes_style('darkgrid'):
#   sns.jointplot(x=data['LSTAT'], 
#                 y=data['RM'], 
#                 # kind='hex', 
#                 height=7, 
#                 color='orange',
#                 joint_kws={'alpha':0.5})
# plt.show()


'''**Challenge**

Compare LSTAT with PRICE using Seaborn's `.jointplot()`. How does the
 proportion of the lower-income population in an area affect home prices?'''


# with sns.axes_style('darkgrid'):
#   sns.jointplot(x=data.LSTAT, 
#                 y=data.PRICE, 
#                 # kind='hex', 
#                 height=7, 
#                 color='crimson',
#                 joint_kws={'alpha':0.5})
# plt.show()

#### Number of Rooms versus Home Value

'''**Challenge** 

Compare RM (number of rooms) with PRICE using Seaborn's `.jointplot()`.
 You can probably guess how the number of rooms affects home prices. 😊 '''


# with sns.axes_style('whitegrid'):
#   sns.jointplot(x=data.RM, 
#                 y=data.PRICE, 
#                 height=7, 
#                 color='darkblue',
#                 joint_kws={'alpha':0.5})
# plt.show()


# Split Training & Test Dataset

'''

**Challenge**

* Import the `train_test_split()` function from sklearn
* Create 4 subsets: X_train, X_test, y_train, y_test
* Split the training and testing data roughly 80/20. 
* To get the same random split every time you run your 
notebook use `random_state=10`. This helps us get the same results
 every time and avoid confusion while we're learning. 

'''

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, 
                                                    target, 
                                                    test_size=0.2, 
                                                    random_state=10)


# % of training set
train_pct = 100*len(X_train)/len(features)
print(f'Training data is {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100*X_test.shape[0]/features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')



# Multivariable Regression

'''
**Challenge**

Use sklearn to run the regression on the training dataset.
 How high is the r-squared for the regression on the training data?
'''