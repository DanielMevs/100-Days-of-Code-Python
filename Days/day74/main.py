import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')


# print(df_tesla.shape)
# print(df_tesla.head())

# print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
# print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

# print(df_tesla.describe())

# - Let's explore unemployment benefits data
# print(df_unemployment.shape)
# print(df_unemployment.head())

# print(f'Smallest value for "Unemployment Benefits" '
#       f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.min()}')

# print(df_btc_price.shape)
# print(df_btc_price.head())
# print(df_btc_search.shape)
# print(df_btc_search.head())

print(f'largest BTC News Search {df_btc_search.BTC_NEWS_SEARCH.max()}')

# Challenge: investigate all 4 DataFrames and find if there are any missing values

# print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
# print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
# print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
# print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')

# print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
# print(df_btc_price[df_btc_price.CLOSE.isna()])

# df_btc_price2 = df_btc_price.dropna(inplace=True)
# print(df_btc_price.isna().values.any())
# df_btc_price2 = df_btc_price.dropna(inplace=False)
# print(df_btc_price.isna().values.any())

df_btc_price.dropna(inplace=True)
print(df_btc_price.isna().values.any())


# - Challenge: Convert any strings you find in all 4 DataFrames to Datetime objects.

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# - To convrt daily data into monthly data, we use .resample()
# Specify the column to use and the sample frequency('M': month, 'Y': year, etc...)

df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()

# print(df_btc_monthly.head())

# - Challenge: Plot the Tesla stock price against the Tesla search
#  volume using a line chart and two different axes

# ax1 = plt.gca() # get current axis
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('TSLA Stock Price')
# ax2.set_ylabel('Search Trend')
 
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)

# plt.show()

# - Challenge: Style the chart

# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('TSLA Stock Price', color='#E6232E') # can use a HEX code
# ax2.set_ylabel('Search Trend', color='skyblue') # or a named colour
 
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

# plt.show()

# - Challenge: 

'''Increase the figure size (e.g., to 14 by 8).

Increase the font sizes for the labels and the ticks on the x-axis to 14.

Rotate the text on the x-axis by 45 degrees.

Add a title that reads 'Tesla Web Search vs Price'

Make the lines on the chart thicker.

Keep the chart looking sharp by changing the dots-per-inch or DPI value.

Set minimum and maximum values for the y and x-axis. Hint: check out methods like set_xlim().

Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.'''


# plt.figure(figsize=(14,8), dpi=120)
# plt.title('Tesla Web Search vs Price', fontsize=18)
 
# # Increase the size and rotate the labels on the x-axis
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# # Set the minimum and maximum values on the axes
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
 
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
# plt.show()


# - Using Locators and DateFormatters to generate Tick Marks on a Time Line

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
# plt.show()


# - Challenge
'''
Modify the chart title to read 'Bitcoin News Search vs Resampled Price'

Change the y-axis label to 'BTC Price'

Change the y- and x-axis limits to improve the appearance

Investigate the linestyles to make the BTC closing price a dashed line

Investigate the marker types to make the search datapoints little circles

Were big increases in searches for Bitcoin accompanied by big increases in the price?
'''

# plt.figure(figsize=(14,8), dpi=120)
 
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
 
# # Experiment with the linestyle and markers
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, 
#          color='#F08F2E', linewidth=3, linestyle='--')
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, 
#          color='skyblue', linewidth=3, marker='o')

# plt.show()

# - Data Visualisation - Unemployment: How to use Grids
# - Challenge:
'''
Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate

Change the y-axis label to: FRED U/E Rate

Change the axis limits

Add a grey grid to the chart to better see the years and the U/E rate values. Use dashed lines for the line style.

Can you discern any seasonality in the searches? Is there a pattern?
'''

# plt.figure(figsize=(14,8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
 
# # Show the grid lines as dark grey lines
# ax1.grid(color='grey', linestyle='--')
 
# # Change the dataset used
# ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 
#          color='purple', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 
#          color='skyblue', linewidth=3)
 
# plt.show()

# - Challenge: Calculate the 3-month or 6-month rolling average for the web searches
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
# plt.figure(figsize=(14,8), dpi=120)
# plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
 
# # Calculate the rolling average over a 6 month window
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
 
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
 
# plt.show()


# - Data Visualisation - Unemployment: The Effect of New Data

# - Challenge: Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv'
#  into a DataFrame. onvert the MONTH column to Pandas Datetime objects
#  and then plot the chart.

df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14,8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])
 
ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
 
plt.show()