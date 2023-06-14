import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats as stats


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
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y') 

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

# Analysing the Yearly Data Split By Clinic

# Challenge 1: The Yearly Data Split by Clinic

'''

Which clinic is bigger or more busy judging by the number of births?

Has the hospital had more patients over time?

What was the highest number of deaths recorded in clinic 1 and clinic 2?

'''

# line = px.line(df_yearly, 
#                x='year', 
#                y='births',
#                color='clinic',
#                title='Total Yearly Births by Clinic')
 
# line.show()

# line = px.line(df_yearly, 
#                x='year', 
#                y='deaths',
#                color='clinic',
#                title='Total Yearly Deaths by Clinic')
 
# line.show()

# Challenge 2: Calculate the Proportion of Deaths at Each Clinic

'''
Work out the percentage of deaths for each row in the df_yearly DataFrame by adding a column called "pct_deaths".

Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the total number of births).

Create another plotly line chart to see how the percentage varies year over year with the two different clinics.

Which clinic has a higher proportion of deaths?

What is the highest monthly death rate in clinic 1 compared to clinic 2?
'''

# df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births


# clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
# avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
# print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')


# clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
# avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
# print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')


# line = px.line(df_yearly, 
#                x='year', 
#                y='pct_deaths',
#                color='clinic',
#                title='Proportion of Yearly Deaths by Clinic')
 
# line.show()

# The Effect of Handwashing

# Challenge 1: The Effect of Handwashing

'''
Add a column called "pct_deaths" to df_monthly that has the percentage of deaths per birth for each row.

Create two subsets from the df_monthly data: before and after Dr Semmelweis ordered washing hand.

Calculate the average death rate prior to June 1846.

Calculate the average death rate after June 1846.
'''

# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

df_monthly['pct_deaths'] = df_monthly.deaths/df_monthly.births

before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]

bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
print(f'Average death rate before 1847 was {bw_rate:.4}%')
print(f'Average death rate AFTER 1847 was {aw_rate:.3}%')

# Challenge 2: Calculate a Rolling Average of the Death Rate

'''
Create a DataFrame that has the 6-month rolling average
 death rate prior to mandatory handwashing.
'''

roll_df = before_washing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()


# Challenge 3: Highlighting Subsections of a Line Chart

'''
Add 3 separate lines to the plot: the death rate before handwashing, after handwashing, and the 6-month moving average before handwashing.

Show the monthly death rate before handwashing as a thin dashed black line.

Show the moving average as a thicker, crimson line.

Show the rate after handwashing as a skyblue line with round markers.

Look at the code snippet in the documentation to see how you can add a legend to the chart.

'''


# plt.figure(figsize=(14,8), dpi=200)
# plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)
 
# ax = plt.gca()
# ax.xaxis.set_major_locator(years)
# ax.xaxis.set_major_formatter(years_fmt)
# ax.xaxis.set_minor_locator(months)
# ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
 
# plt.grid(color='grey', linestyle='--')
 
# ma_line, = plt.plot(roll_df.index, 
#                     roll_df.pct_deaths, 
#                     color='crimson', 
#                     linewidth=3, 
#                     linestyle='--',
#                     label='6m Moving Average')
# bw_line, = plt.plot(before_washing.date, 
#                     before_washing.pct_deaths,
#                     color='black', 
#                     linewidth=1, 
#                     linestyle='--', 
#                     label='Before Handwashing')
# aw_line, = plt.plot(after_washing.date, 
#                     after_washing.pct_deaths, 
#                     color='skyblue', 
#                     linewidth=3, 
#                     marker='o',
#                     label='After Handwashing')
 
# plt.legend(handles=[ma_line, bw_line, aw_line],
#            fontsize=18)
 
# plt.show()



# Visualising Distributions and Testing for Statistical Significance

# Challenge 1: Calculate the Difference in the Average Monthly Death Rate

'''
What was the average percentage of monthly deaths before handwashing (i.e., before June 1847)?

What was the average percentage of monthly deaths after handwashing was made obligatory?

By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?

How do these numbers compare to the average for all the 1840s that we calculated earlier?

How many times lower are the chances of dying after handwashing compared to before?

'''

# avg_prob_before = before_washing.pct_deaths.mean() * 100
# print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')
 
# avg_prob_after = after_washing.pct_deaths.mean() * 100
# print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')
 
# mean_diff = avg_prob_before - avg_prob_after
# print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')
 
# times = avg_prob_before / avg_prob_after
# print(f'This is a {times:.2}x improvement!')


# Challenge 2: Using Box Plots to Show How the Death Rate Changed 
# Before and After Handwashing

'''
Use NumPy's .where() function to add a column to df_monthly that shows if a particular date was before or after the start of handwashing.

Then use plotly to create box plot of the data before and after handwashing.

How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy

'''

# df_monthly['washing_hands'] = np.where(df_monthly.date < handwashing_start, 'No', 'Yes')
# box = px.box(df_monthly, 
#              x='washing_hands', 
#              y='pct_deaths',
#              color='washing_hands',
#              title='How Have the Stats Changed with Handwashing?')
 
# box.update_layout(xaxis_title='Washing Hands?',
#                   yaxis_title='Percentage of Monthly Deaths',)
 
# box.show()


# Challenge 3: Use Histograms to Visualise the Monthly Distribution of Outcomes

'''
Use docs to check out the available parameters. Use the color parameter to display two overlapping histograms.

The time period of handwashing is shorter than not handwashing. Change histnorm to percent to make the time periods comparable.

Make the histograms slightly transparent

Experiment with the number of bins on the histogram. Which number works well in communicating the range of outcomes?

Just for fun, display your box plot on the top of the histogram using the marginal parameter

'''

# hist = px.histogram(df_monthly, 
#                    x='pct_deaths', 
#                    color='washing_hands',
#                    nbins=30,
#                    opacity=0.6,
#                    barmode='overlay',
#                    histnorm='percent',
#                    marginal='box',)
 
# hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
#                    yaxis_title='Count',)
 
# hist.show()

# Challenge 4: Use a Kernel Density Estimate (KDE) to visualise a smooth distribution

'''
Use Seaborn's .kdeplot() to create two kernel density estimates of the
 pct_deaths, one for before handwashing and one for after.

Use the shade parameter to give your two distributions different colours.

What weakness in the chart do you see when you just use the default parameters?

Use the clip parameter to address the problem.

'''

# plt.figure(dpi=200)
# # By default the distribution estimate includes a negative death rate!
# sns.kdeplot(before_washing.pct_deaths, shade=True)
# sns.kdeplot(after_washing.pct_deaths, shade=True)
# plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
# plt.show()


# The solution is to specify a lower bound of 0 for the death rate.

# plt.figure(dpi=200)
# sns.kdeplot(before_washing.pct_deaths, 
#             shade=True,
#             clip=(0,1))
# sns.kdeplot(after_washing.pct_deaths, 
#             shade=True,
#             clip=(0,1))
# plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
# plt.xlim(0, 0.40)
# plt.show()


# Challenge 5: Use a T-Test to Show Statistical Significance

'''
Import stats from scipy

Use the .ttest_ind() function to calculate the t-statistic and the p-value

Is the difference in the average proportion of monthly deaths
 statistically significant at the 99% level?

'''

t_stat, p_value = stats.ttest_ind(a=before_washing.pct_deaths, 
                                  b=after_washing.pct_deaths)
print(f'p-palue is {p_value:.10f}')
print(f't-statstic is {t_stat:.4}')

