import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
pd.set_option('display.max_columns', None)

# - Explore and Clean the Data

# Challenge 1 
'''
How many rows and columns does the dataset contain?

Are there any NaN values present?

Are there any duplicate rows?

What are the data types of the columns?
'''

# Challenge 2
'''
Convert the USD_Production_Budget, USD_Worldwide_Gross, 
and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
'''

# Challenge 3
'''
Convert the Release_Date column to a Pandas Datetime type.
'''

data = pd.read_csv('cost_revenue_dirty.csv')

# print(data.shape)
# print(data.head())
# print(data.tail())
# print(data.info())
# print(data.sample())

# print(f'Any NaN values among the data? {data.isna().values.any()}')
# print(f'Any duplicates? {data.duplicated().values.any()}')
# duplicated_rows = data[data.duplicated()]
# print(f'Number of duplicates: {len(duplicated_rows)}')

# print(data.info())

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']
 
for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

# print(data.head())
data.Release_Date = pd.to_datetime(data.Release_Date)
# print(data.head())
# print(data.info())

# print(data.describe())
# print(data[data.USD_Production_Budget == 1100.00])
# print(data[data.USD_Production_Budget == 425000000.00])
# zero_domestic = data[data.USD_Domestic_Gross == 0]
# print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
# print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))

# zero_worldwide = data[data.USD_Worldwide_Gross == 0]
# print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
# print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))


# Filter on Multiple Conditions: International Films
# - Challenge: Find which films made money internationally, but had
# zero box office revenue in the United States
bool_list1 = [True, True, False, False]
bool_list2 = [False, True, True, False]
print(np.array(bool_list1 & np.array(bool_list2)))

international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]

# print(f'Number of international releases: {len(international_releases)}')
# print(international_releases.head())

# - Challenge: use the Pandas .query() function to accomplish the same thing
international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
# print(international_releases.tail())

# - Singularity and Aquaman had zero revenue because they were
# not released at the time the data was collected.


# - Challenge
'''
Identify which films were not released yet as of the time of data collection (May 1st, 2018).

How many films are included in the dataset that have not yet had a chance to be screened in the box office? 

Create another DataFrame called data_clean that does not include these films.
'''

scrape_date = pd.Timestamp('2018-5-1')

future_releases = data[data.Release_Date >= scrape_date]
# print(f'Number of unreleased movies: {len(future_releases)}')
# print(future_releases)

data_clean = data.drop(future_releases.index)


# Bonus Challenge: Films that Lost Money
# calculate the percentage of films that did not break even at the box office
# what is the percentage of films where the costs exceed the worldwide gross revenue

money_losing = data_clean.loc[
    data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]

# print(len(money_losing)/len(data_clean))


money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
# print(money_losing.shape[0]/data_clean.shape[0])


#  Seaborn Data Visualisation: Bubble Charts
# sns.scatterplot(data=data_clean,
#                 x='USD_Production_Budget', 
#                 y='USD_Worldwide_Gross')

# plt.figure(figsize=(8, 4), dpi=200)

# # set styling on a single chart
# with sns.axes_style('darkgrid'):
#   ax = sns.scatterplot(data=data_clean,
#                        x='USD_Production_Budget', 
#                        y='USD_Worldwide_Gross',
#                        hue='USD_Worldwide_Gross',
#                        size='USD_Worldwide_Gross')
 
#   ax.set(ylim=(0, 3000000000),
#         xlim=(0, 450000000),
#         ylabel='Revenue in $ billions',
#         xlabel='Budget in $100 millions')

# # plt.show()

# Challenge: Movie Budgets Over Time

# plt.figure(figsize=(8,4), dpi=200)
 
# with sns.axes_style("darkgrid"):
#     ax = sns.scatterplot(data=data_clean, 
#                     x='Release_Date', 
#                     y='USD_Production_Budget',
#                     hue='USD_Worldwide_Gross',
#                     size='USD_Worldwide_Gross',)
 
#     ax.set(ylim=(0, 450000000),
#            xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
#            xlabel='Year',
#            ylabel='Budget in $100 millions')
 
# plt.show()


# Floor Division: A Trick to Convert Years to Decades
# Challenge: : Use Floor Division to Convert Years to Decades
# create a column in data_clean that has the decade of the movie release

'''
Create a DatetimeIndex object from the Release_Date column.


Grab all the years from the DatetimeIndex object using the .year property.

Use floor division // to convert the year data to the decades of the films.

Add the decades as a Decade column to the data_clean DataFrame.
'''

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

decades = years//10*10
data_clean['Decade'] = decades


# Challenge: Create two new DataFrames: old_films and new_films
'''
old_films should include all the films before 1970 (up to and including 1969)

new_films should include all the films from 1970 onwards

How many of our films were released prior to 1970?

What was the most expensive film made prior to 1970?
'''

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]


# print(old_films.describe())

# Plotting Linear Regressions with Seaborn

# Goal: visualise the relationship between the movie 
# budget and the worldwide revenue using linear regression

# sns.regplot(data=old_films, 
#             x='USD_Production_Budget',
#             y='USD_Worldwide_Gross')

# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#   sns.regplot(data=old_films, 
#             x='USD_Production_Budget', 
#             y='USD_Worldwide_Gross',
#             scatter_kws = {'alpha': 0.4},
#             line_kws = {'color': 'black'})

# plt.show()

# Challenge: Use Seaborn's .regplot() to show the
#  scatter plot and linear regression line against the new_films.

'''
Style the chart

Put the chart on a 'darkgrid'.

Set limits on the axes so that they don't show negative values.

Label the axes on the plot "Revenue in $ billions" and "Budget in $ millions".

Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).

Interpret the chart

Do our data points for the new films align better or worse with the linear regression than for our older films?

Roughly how much would a film with a budget of $150 million make according to the regression line?
'''

# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style('darkgrid'):
#   ax = sns.regplot(data=new_films,
#                    x='USD_Production_Budget',
#                    y='USD_Worldwide_Gross',
#                    color='#2f4b7c',
#                    scatter_kws = {'alpha': 0.3},
#                    line_kws = {'color': '#ff7c43'})
  
#   ax.set(ylim=(0, 3000000000),
#          xlim=(0, 450000000),
#          ylabel='Revenue in $ billions',
#          xlabel='Budget in $100 millions') 
  
# plt.show()

# Use scikit-learn to Run Your Own Regression

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

# Find the best-fit line
regression.fit(X, y)

# # Theta zero
# print(regression.intercept_)

# # Theta one
# print(regression.coef_)

# R-Squared: Goodness of Fit
'''
One measure of figuring out how well our model
 fits our data is by looking at a metric called r-squared
'''

# This means that our model explains about 56% of the variance in movie revenue# 
# print(regression.score(X, y)) # 0.558


# Challenge: Run a linear regression for the old_films. Calculate the
#  intercept, slope and r-squared. How much of the variance in movie
#  revenue does the linear model explain in this case?

print(f'The slope coefficient is: {regression.coef_[0]}')
print(f'The intercept is: {regression.intercept_[0]}')
print(f'The r-squared is: {regression.score(X, y)}')


# Challenge: You've just estimated the intercept and slope for 
# the Linear Regression model. Now we can use it to 
# make a prediction! For example, how much global revenue does our model
#  estimate for a film with a budget of $350 million?

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')