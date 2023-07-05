import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('mission_launches.csv')

'''

* What is the shape of `df_data`? 
L> (4324, 9)

* How many rows and columns does it have?
L> 9 columns and 4324 rows (2 columns are junk)

* What are the column names?
L> Organisation, Location, 
Date, Detail, Rocket_Status, Price, Mission_Status

* Are there any NaN values or duplicates?

'''

# print(df_data.shape)
# print(df_data.info())
# print(f'This data frame has {len(df_data)} rows and {len(df_data.columns)}')
# print(f'Missing/NaN values for Mission Launch data?: {df_data.isna().values.any()}')
# duplicated_rows = df_data[df_data.duplicated()]
# print(f'Duplicated values for Mission Launch data?: {len(duplicated_rows) > 0}')
# print(f'Duplicated values for Mission Launch data?: {df_data.duplicated().values.any()}')

'''
Data Cleaning

Consider removing columns containing junk data. 
'''

# print(df_data.head())
df_data.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)


# print(df_data.head())

'''
Create a chart that shows the number of space mission launches by organisation.
'''

# print(df_data[['Organisation']].groupby('Organisation').count())
print(df_data['Organisation'].count())

# df_data['Organisation'].value_counts(sort=True).plot.bar()

# plt.show()
# print(df_data['Rocket_Status'].value_counts())
retired_rockets = df_data['Rocket_Status'].value_counts()['StatusRetired']
active_rockets = df_data['Rocket_Status'].value_counts()['StatusActive']
print(f'There are {retired_rockets} retired_rockets' +
      f' and {active_rockets} active rockets.')


'''How many missions were successful?
How many missions failed?'''
# df_data['Mission_Status'].value_counts().plot.pie(autopct='%1.1f%%')

# plt.show()


'''
How Expensive are the Launches? 
Create a histogram and visualise the distribution. The price column is given
 in USD millions (careful of missing values)
'''

df_data.dropna(inplace=True)
print(df_data['Price'].isna().values.any())


print(df_data.Price.describe())

# Generate data on commute times.
f = lambda x: "%.2f" % x
df_data['Price'] = df_data['Price'].apply(lambda x: f(float(x.replace(',', ''))))


# sns.set_style('darkgrid')
# sns.distplot(df_data.Price)
# plt.show()

# alternatively

# df_data.Price.hist(grid=True, bins=56, rwidth=0.9,
#                    color='#607c8e')
# plt.title('Distribution of Price of each Space Launch')
# plt.xticks(rotation=90)
# plt.xlabel('Price in USD millions', fontweight='bold')
# plt.ylabel('Counts', fontweight='bold')
# plt.grid(axis='y', alpha=0.75)


# plt.subplots_adjust(bottom=0.200)

# N = 150
# plt.gca().margins(x=0)
# plt.gcf().canvas.draw()
# tl = plt.gca().get_xticklabels()
# maxsize = max([t.get_window_extent().width for t in tl])
# m = 0.2 # inch margin
# s = maxsize/plt.gcf().dpi*N+2*m
# margin = m/plt.gcf().get_size_inches()[0]

# plt.gcf().subplots_adjust(left=margin, right=1.-margin)
# plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
# plt.show()