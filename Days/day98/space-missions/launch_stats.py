import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import iso3166

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('mission_launches.csv')
# pd.set_option('display.max_columns', None)

################################################################

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
# print(df_data.head())
# print(df_data.shape)
# print(df_data.info())
# print(f'This data frame has {len(df_data)} rows and {len(df_data.columns)}')
# print(f'Missing/NaN values for Mission Launch data?: {df_data.isna().values.any()}')
# duplicated_rows = df_data[df_data.duplicated()]
# print(f'Duplicated values for Mission Launch data?: {len(duplicated_rows) > 0}')
# print(f'Duplicated values for Mission Launch data?: {df_data.duplicated().values.any()}')

################################################################
 
'''
Data Cleaning

Consider removing columns containing junk data. 
'''
# df_data.dropna(inplace=True)
# print(df_data.head())
df_data.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)
df_data.drop_duplicates(inplace=True)

################################################################

'''
Descriptive Statistics
'''


# print(df_data.head())

#print(df_data.describe())

# print(df_data[df_data["Price"].notna()]["Price"].str.replace(',', '').astype(float).describe())

################################################################


'''
Create a chart that shows the number of space mission launches by organisation.
'''


# print(df_data[['Organisation']].groupby('Organisation').count())
print(df_data['Organisation'].count())

# df_data['Organisation'].value_counts(sort=True).plot.bar()

# or

# df_data["Organisation"].value_counts().plot()

# plt.show()

################################################################

'''
How many rockets are active compared to those that are 
decomissioned?

'''

# print(df_data['Rocket_Status'].value_counts())
retired_rockets = df_data['Rocket_Status'].value_counts()['StatusRetired']
active_rockets = df_data['Rocket_Status'].value_counts()['StatusActive']
print(f'There are {retired_rockets} retired_rockets' +
      f' and {active_rockets} active rockets.')

# print(df_data["Rocket_Status"].value_counts())

# df_data["Rocket_Status"].value_counts().sort_values().plot(kind="barh")

# plt.show()

################################################################


'''How many missions were successful?
How many missions failed?'''


# df_data['Mission_Status'].value_counts().plot.pie(autopct='%1.1f%%')

# plt.show()

# print(df_data["Mission_Status"].value_counts())

print(df_data.groupby("Mission_Status").agg({"Mission_Status":pd.Series.count}))

################################################################


'''
How Expensive are the Launches? 
Create a histogram and visualise the distribution. The price column is given
 in USD millions (careful of missing values)
'''

df_data.dropna(inplace=True)
print(df_data['Price'].isna().values.any())


print(df_data.Price.describe())

# Generate data on commute times.
# f = lambda x: "%.2f" % x
# df_data['Price'] = df_data['Price'].apply(lambda x: f(float(x.replace(',', ''))))


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



# plt.show()



################################################################


# Use a Choropleth Map to Show the Number of Launches by Country


'''
Create a choropleth map using the plotly documentation
Experiment with plotly's available colours.
You'll need to extract a country feature as well as change 
the country names that no longer exist.
Wrangle the Country Names

You'll need to use a 3 letter country code for each country.
You might have to change some country names.

Russia is the Russian Federation
New Mexico should be USA
Yellow Sea refers to China
Shahrud Missile Test Site should be Iran
Pacific Missile Range Facility should be USA
Barents Sea should be Russian Federation
Gran Canaria should be USA
You can use the iso3166 package to convert the country names
to Alpha3 format.
'''


df_data["Country"] = df_data["Location"].str.split(", ").str[-1]

df_data.loc[(df_data["Country"] == 'Russia'), "Country"] = "Russian Federation"
df_data.loc[(df_data["Country"] == 'New Mexico'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Yellow Sea'), "Country"] = "China"
df_data.loc[(df_data["Country"] == 'Shahrud Missile Test Site'), "Country"] = "Iran"
df_data.loc[(df_data["Country"] == 'Pacific Missile Range Facility'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Barents Sea'), "Country"] = "Russian Federation"
df_data.loc[(df_data["Country"] == 'Gran Canaria'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Iran'), "Country"] = "Iran, Islamic Republic of"
df_data.loc[(df_data["Country"] == 'South Korea'), "Country"] = "Korea, Republic of"
df_data.loc[(df_data["Country"] == 'North Korea'), "Country"] = "Korea, Democratic People's Republic of"
df_data.loc[(df_data["Country"] == 'Kazakhstan'), "Country"] = "Russian Federation"

countries = {country.name: key for key, country in iso3166.countries_by_alpha3.items()}
df_data = df_data.replace({"Country": countries})

launches = df_data["Country"].value_counts().rename_axis("Country").reset_index(name='counts')
# print(launches.head())
# world_map = px.choropleth(launches, locations="Country", color="counts", color_continuous_scale=px.colors.sequential.matter)
# world_map.update_layout(coloraxis_showscale=True)
# world_map.show()
# print(df_data.head())

# for country in countries: 
#     print(country)


################################################################

'''
Use a Choropleth Map to Show the Number of Failures by Country
'''

statuses = df_data.groupby("Country")["Mission_Status"].value_counts().rename_axis(["Country", "Status"]).reset_index(name='counts')
failures = statuses[statuses["Status"].str.contains("Fail")].groupby("Country").sum()

# world_map = px.choropleth(failures, locations=failures.index, color="counts", color_continuous_scale=px.colors.sequential.matter)
# world_map.update_layout(coloraxis_showscale=True) 
# world_map.show()

################################################################

'''
Create a Plotly Sunburst Chart of the countries, organisations, and mission status.
'''

sunburst = df_data.groupby(by=["Country", "Organisation", "Mission_Status"], as_index=False).size()
sunburst = sunburst.sort_values("size", ascending=False)
# print(sunburst.head())
# px.sunburst(sunburst, path=["Country", "Organisation", "Mission_Status"], values="size", title="Missions By Country").show()

################################################################

'''
Analyse the Total Amount of Money Spent by Organisation on Space Missions
'''

money_spent = df_data[df_data["Price"].notna()]

money_spent["Price"] = money_spent["Price"].str.replace(',', '').astype(float)

total_money_spent = money_spent.groupby("Organisation")["Price"].sum().reset_index()
total_money_spent.sort_values(by="Price", ascending=False)
# print(total_money_spent.head())

###############################################################

'''
Analyse the Amount of Money Spent by Organisation per Launch
'''
organisation_expense = money_spent.groupby("Organisation")["Price"].mean().reset_index()
organisation_expense.sort_values("Price", ascending=False)
# print(organisation_expense.head())

###############################################################

'''
Chart the Number of Launches per Year
'''

# df_data['date'] = pd.to_datetime(df_data['Date'], format='mixed')
# df_data['year'] = df_data['date'].apply(lambda datetime: datetime.year)

# ds = df_data['year'].value_counts().reset_index()
# ds.columns = [
#     'year', 
#     'count'
# ]
# fig = px.bar(
#     ds, 
#     x='year', 
#     y="count", 
#     orientation='v', 
#     title='Missions number by year' 
# )
# fig.show()

###############################################################

'''
Chart the Number of Launches Month-on-Month until the Present
'''

# df_data['date'] = pd.to_datetime(df_data['Date'], format='mixed')
# df_data['month'] = df_data['date'].apply(lambda datetime: datetime.month)

# ds = df_data['month'].value_counts().reset_index()
# ds.columns = [
#     'month', 
#     'count'
# ]
# fig = px.bar(
#     ds, 
#     x='month', 
#     y="count", 
#     orientation='v', 
#     title='Missions number by month' 
# )
# fig.show()

###############################################################

'''
Launches per Month: Which months are most popular and least popular for launches?
'''

# most_launches = ds['count'].max()
# print('-'*20)
# print(f"Most launches in a month = {most_launches}")
# print('-'*20)
# ds.sort_values(by="count", ascending=False)
# print(ds.max())
# print('-'*20)

# least_launches = ds['count'].min()
# print(f"Least launches in a month = {least_launches}")
# print(ds.min())

###############################################################

'''
How has the Launch Price varied Over Time?
'''

# avg_price = df_data[df_data["Price"].notna()]
# pd.options.mode.chained_assignment = None
# avg_price["Price"] = avg_price["Price"].str.replace(',', '').astype(float)

# avg_price.groupby("year").mean().plot(figsize=(12, 8))

###############################################################

'''
Chart the Number of Launches over Time by the Top 10 Organisations.

How has the dominance of launches changed over time between the different players?
'''

# top_10=pd.DataFrame(columns=df_data.columns)
# for val in df_data.groupby("Organisation").count().sort_values("Date",ascending=False)[:10].index:
#   print(val)
#   org=df_data[df_data.Organisation==val]
# #   pd.concat([top_10, org], ignore_index=False, verify_integrity=False, sort=None)
#   top_10=top_10.append(org,ignore_index=False, verify_integrity=False, sort=None)

# df_data[df_data.Organisation=="CASC"]

# top_10.groupby("Organisation").count().sort_values("Date",ascending=False)[:10].index


# px.histogram(top_10.sort_values(by=["Organisation", "Date"], ascending=[True, False]), x="Organisation",nbins=10).show()


###############################################################

'''
Cold War Space Race: USA vs USSR
'''
# Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]

# cold_war_years = Or_df.sort_values("year")

# print(cold_war_years[(cold_war_years.year <= 1991)])



###############################################################

'''
Create a Plotly Pie Chart comparing the total number of launches of the USSR and the USA
'''

# Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]
# print(Or_df.head())

# launches = Or_df["Country"].value_counts().rename_axis("Country").reset_index(name='counts')
# print(launches.head())


# colors = ["#1f77b4", "#ff7f0e"]
# grouping = Or_df.groupby("Country").count().reset_index()
# sizes = grouping['Mission_Status']
# labels = grouping['Country']

# plt.pie(sizes, labels = labels, colors = colors)

# plt.show()

###############################################################

'''
Create a Chart that Shows the Total Number of Launches Year-On-Year by the Two Superpowers
'''

# Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]
# Or_df.groupby(["year", "Country"]).size().unstack().plot()

###############################################################


'''
Chart the Total Number of Mission Failures Year on Year.
'''
Or_df = df_data[df_data['Mission_Status'].str.contains("Failure")]
# print(Or_df.head())

# yearly_failures = px.data.tips()
# fig = px.sunburst(Or_df, path=["year", "Mission_Status"])
# fig.show()

###############################################################

'''
Chart the Percentage of Failures over Time

Did failures go up or down over time? Did the countries get better 
at minimising risk and improving their chances of success over time?
'''

# grouping = Or_df.groupby("year").count().reset_index()
# sizes = grouping['Mission_Status']
# labels = grouping['year']

# plt.pie(sizes, labels = labels)
# fig = plt.gcf()
# fig.set_size_inches(15,15)
# plt.show()

###############################################################

'''
For Every Year Show which Country was in the Lead in
 terms of Total Number of Launches up to and including
2020)
'''

# country_launches = df_data.groupby("year")["Country"].value_counts().rename_axis(["year", "Country"]).reset_index(name='counts')

# country_launches.loc[country_launches.groupby("year")["counts"].idxmax()]
# print(country_launches.head())

###############################################################


'''Create a Year-on-Year Chart Showing the Organisation Doing the Most Number of Launches
Which organisation was dominant in the 1970s and 1980s? Which organisation was dominant in 2018, 2019 and 2020?
'''
# org_launches = df_data.groupby("year")["Organisation"].value_counts().rename_axis(["year", "Organisation"]).reset_index(name='counts')

# org_launches.loc[org_launches.groupby("year")["counts"].idxmax()]
# org_launches.head()

# org_launches = df_data.groupby("year")["Organisation"].value_counts().rename_axis(["year", "Organisation"]).reset_index(name='counts')

# org_launches.loc[org_launches.groupby("year")["counts"].idxmax()]
# org_launches.head()