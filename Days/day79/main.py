import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis


from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv('monthly_deaths.csv', 
                      parse_dates=['date'])


# Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital

# - Challenge 1: Preliminary Data Exploration

'''
What is the shape of df_yearly and df_monthly? How many rows and columns?

What are the column names?

Which years are included in the dataset?

Are there any NaN values or duplicates?

What were the average number of births that took place per month?

What were the average number of deaths that took place per month?
'''

# print(df_yearly.shape)
# print(df_yearly)
# print(df_monthly.shape)
# print(df_monthly.tail())

# print(df_yearly.info())
# print(df_yearly.isna().values.any())

# print(f'Any yearly duplicates? {df_yearly.duplicated().values.any()}')
# print(f'Any monthly duplicates? {df_monthly.duplicated().values.any()}')

# print(df_monthly.describe())
# print(df_yearly.describe())

# Challenge 2: Percentage of Women Dying in Childbirth

'''
Using the annual data, calculate the percentage
 of women giving birth who died throughout the 1840s at the hospital.
'''
# prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
# print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')


# Challenge 3: Visualise the Total Number of Births and Deaths over Time

'''
Format the x-axis using locators for the years and months (Hint: we did this in the Google Trends notebook)

Set the range on the x-axis so that the chart lines touch the y-axes

Add gridlines

Use skyblue and crimson for the line colours

Use a dashed line style for the number of deaths

Change the line thickness to 3 and 2 for the births and deaths respectively.

'''
# Create locators for ticks on the time axis
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y') 

# plt.figure(figsize=(14,8), dpi=200)
# plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('Births', color='skyblue', fontsize=18)
# ax2.set_ylabel('Deaths', color='crimson', fontsize=18)
 
# # Use Locators
# ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.grid(color='grey', linestyle='--')
 
# ax1.plot(df_monthly.date, 
#          df_monthly.births, 
#          color='skyblue', 
#          linewidth=3)
 
# ax2.plot(df_monthly.date, 
#          df_monthly.deaths, 
#          color='crimson', 
#          linewidth=2, 
#          linestyle='--')
 
# plt.show()

'''
From the graph, we see that after 1847, the total number of deaths
 dropped, despite an increasing number of births
'''
