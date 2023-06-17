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

regr = LinearRegression()
regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

print(f'Training data r-squared: {rsquared:.2}')


### Evaluate the Coefficients of the Model


'''

**Challenge** Print out the coefficients (the thetas in the equation above)
 for the features. Hint: You'll see a nice table if you stick the coefficients 
 in a DataFrame. 

'''

regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
print(regr_coef)


# Premium for having an extra room
premium = regr_coef.loc['RM'].values[0] * 1000  # i.e., ~3.11 * 1000
print(f'The price premium for having an extra room is ${premium:.5}')


### Analyse the Estimated Values & Regression Residuals

# **Challenge**: Create two scatter plots.

predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)


# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()


'''

**Challenge**

* Calculate the mean and the skewness of the residuals. 
* Again, use Seaborn's `.displot()` to create a histogram and superimpose the Kernel Density Estimate (KDE)
* Is the skewness different from zero? If so, by how much? 
* Is the mean different from zero?

'''


# Residual Distribution Chart
resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()

'''

**Challenge**

Investigate if the target `data['PRICE']` could be a suitable candidate for
 a log transformation. 

* Use Seaborn's `.displot()` to show a histogram and KDE of the price data. 
* Calculate the skew of that distribution.

* Plot the log prices using Seaborn's `.displot()` and calculate the skew. 
* Which distribution has a skew that's closer to zero? 


'''


tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title(f'Normal Prices. Skew is {tgt_skew:.3}')
plt.show()

y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title(f'Log Prices. Skew is {y_log.skew():.3}')
plt.show()


plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()


## Regression using Log Prices

'''

**Challenge**: 

* Use `train_test_split()` with the same random state as before to make the results comparable. 
* Run a second regression, but this time use the transformed target data. 
* What is the r-squared of the regression on the training data? 
* Have we improved the fit of our model compared to before based on this measure?

'''


new_target = np.log(data['PRICE']) # Use log prices
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features, 
                                                    new_target, 
                                                    test_size=0.2, 
                                                    random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')


## Evaluating Coefficients with Log Prices

'''

**Challenge**: Print out the coefficients of the new regression model. 

* Do the coefficients still have the expected sign? 
* Is being next to the river a positive based on the data?
* How does the quality of the schools affect property prices? What happens to prices 
as there are more students per teacher? 

'''


df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
print(df_coef)


## Regression with Log Prices & Residual Plots

'''

**Challenge**: 

* Copy-paste the cell where you've created scatter plots of the actual 
versus the predicted home prices as well as the residuals versus the predicted values. 
* Add 2 more plots to the cell so that you can compare the regression outcomes with the 
log prices side by side. 
* Use `indigo` as the colour for the original regression and `navy` for the color 
using log prices.

'''

# Graph of Actual vs. Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Prediced Log Prices $\hat y _i$', fontsize=14)
plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=17)
plt.xlabel('Predicted Log Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()


'''

**Challenge**: 

Calculate the mean and the skew for the residuals using log prices. 
Are the mean and skew closer to 0 for the regression using log prices?

'''


# Distribution of Residuals (log prices) - checking for normality
log_resid_mean = round(log_residuals.mean(), 2)
log_resid_skew = round(log_residuals.skew(), 2)

sns.displot(log_residuals, kde=True, color='navy')
plt.title(f'Log price model: Residuals Skew ({log_resid_skew}) Mean ({log_resid_mean})')
plt.show()

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Original model: Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()



# Compare Out of Sample Performance

'''

**Challenge**

Compare the r-squared of the two models on the test dataset. Which model does 
better? Is the r-squared higher or lower than for the training dataset? Why?

'''

print(f'Original Model Test Data r-squared: {regr.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')


# Predict a Property's Value using the Regression Coefficients


# Starting Point: Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)), 
                              columns=features.columns)
print(property_stats)

'''

**Challenge**

Predict how much the average property is worth using the stats above. 

'''

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
# or use
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')


'''

**Challenge**

Keeping the average values for CRIM, RAD, INDUS and others, value a property
 with the following characteristics:

'''

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20 
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty =  data.LSTAT.quantile(q=0.25) # low

 
 
# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty


# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')