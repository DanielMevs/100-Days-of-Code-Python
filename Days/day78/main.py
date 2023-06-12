import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('nobel_prize_data.csv')

# Challenge 1: Preliminary data exploration

'''
What is the shape of df_data? How many rows and columns?

What are the column names and what kind of data is inside of them?

In which year was the Nobel prize first awarded?

Which year is the latest year included in the dataset?
'''
# print(df_data.shape)
# print(df_data.tail())
# print(df_data.head())
# print(df_data.info())


# Challenge 2

'''
Are there any duplicate values in the dataset?

Are there NaN values in the dataset?

Which columns tend to have NaN values?

How many NaN values are there per column?

Why do these columns have NaN values?
'''

# print(f'Any duplicates? {df_data.duplicated().values.any()}')

# print(f'Any NaN values among the data? {df_data.isna().values.any()}')

# print(df_data.isna().sum())

# col_subset = ['year','category', 'laureate_type',
#               'birth_date','full_name', 'organization_name']
# print(df_data.loc[df_data.birth_date.isna()][col_subset])

# col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
# print(df_data.loc[df_data.organization_name.isna()][col_subset])

# Challenge 3

'''
Convert the birth_date column to Pandas Datetime objects

Add a Column called share_pct which has the laureates' share as a

percentage in the form of a floating-point number.
'''

df_data.birth_date = pd.to_datetime(df_data.birth_date)

separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

# print(df_data.info())


# plotly Bar & Donut Charts: Analyse Prize Categories & Women Winning Prizes

# Challenge 1: 
'''
Come up with 3 Questions
Write down at least 3 questions that you'd like to explore as part of this analysis
'''

# 1) How many prizes were given out in the Literature category?

# 2) What would a donut chart with the percentage of laureates
#  in each category look like?

# 3) How many Nobel laureates have a birth country of US?

# Challenge 2: 
'''
Create a donut chart using plotly which shows how many 
# prizes went to men compared to how many prizes went to women. 

What percentage of all the prizes went to women?
'''

biology = df_data.sex.value_counts()
fig = px.pie(labels=biology.index, 
             values=biology.values,
             title="Percentage of Male vs. Female Winners",
             names=biology.index,
             hole=0.4,)
 
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
 
# fig.show()

# Challenge 3:

'''
What are the names of the first 3 female Nobel laureates?

What did the win the prize for?

What do you see in their birth_country? Were they part of an organisation?
'''

df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

# Challenge 4:
'''
Did some people get a Nobel Prize more than once? If so, who were they?
'''

is_winner = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner]
# print(f'There are {multiple_winners.full_name.nunique()}' \
#       ' winners who were awarded the prize more than once.')


col_subset = ['year', 'category', 'laureate_type', 'full_name']
# print(multiple_winners[col_subset])

# Challenge 5:
'''
In how many categories are prizes awarded?

Create a plotly bar chart with the number of prizes awarded by category.

Use the color scale called Aggrnyl to colour the chart, but don't show a color axis.

Which category has the most number of prizes awarded?

Which category has the fewest number of prizes awarded?

'''

df_data.category.nunique()


prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
        x = prizes_per_category.index,
        y = prizes_per_category.values,
        color = prizes_per_category.values,
        color_continuous_scale='Aggrnyl',
        title='Number of Prizes Awarded per Category')
 
v_bar.update_layout(xaxis_title='Nobel Prize Category', 
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
# v_bar.show()


# Challenge 6:
'''
When was the first prize in the field of Economics awarded?

Who did the prize go to?


'''

# print(df_data[df_data.category == 'Economics'].sort_values('year')[:3])

# Challenge  7:
'''
Create a plotly bar chart that shows the split between men and women by category.

Hover over the bar chart. How many prizes went to women in Literature

 compared to Physics?
'''

cat_men_women = df_data.groupby(['category', 'sex'], 
                               as_index=False).agg({'prize': pd.Series.count})
cat_men_women.sort_values('prize', ascending=False, inplace=True)

v_bar_split = px.bar(x = cat_men_women.category,
                     y = cat_men_women.prize,
                     color = cat_men_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')
 
v_bar_split.update_layout(xaxis_title='Nobel Prize Category', 
                          yaxis_title='Number of Prizes')
# v_bar_split.show()


# Using Matplotlib to Visualise Trends over Time

# Challenge 1

'''
Count the number of prizes awarded every year.

Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).

Using Matplotlib superimpose the rolling average on a scatter plot.

Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?

What could be the reason for the trend in the chart?

'''

prize_per_year = df_data.groupby(by='year').count().prize 

moving_average = prize_per_year.rolling(window=5).mean()

# plt.scatter(x=prize_per_year.index, 
#            y=prize_per_year.values, 
#            c='dodgerblue',
#            alpha=0.7,
#            s=100,)
 
# plt.plot(prize_per_year.index, 
#         moving_average.values, 
#         c='crimson', 
#         linewidth=3,)
 
# plt.show()

# plt.figure(figsize=(16,8), dpi=200)
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(ticks=np.arange(1900, 2021, step=5), 
#            fontsize=14, 
#            rotation=45)
 
# ax = plt.gca() # get current axis
# ax.set_xlim(1900, 2020)
 
# ax.scatter(x=prize_per_year.index, 
#            y=prize_per_year.values, 
#            c='dodgerblue',
#            alpha=0.7,
#            s=100,)
 
# ax.plot(prize_per_year.index, 
#         moving_average.values, 
#         c='crimson', 
#         linewidth=3,)
 
# plt.show()


# Challenge 2

'''
Investigate if more prizes are shared than before.

Calculate the average prize share of the winners on a year by year basis.

Calculate the 5 year rolling average of the percentage share.

Copy-paste the cell from the chart you created above.

Modify the code to add a secondary axis to your Matplotlib chart.

Plot the rolling average of the prize share on this chart.

See if you can invert the secondary y-axis to make the relationship even more clear.


'''

yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()


# plt.figure(figsize=(16,8), dpi=200)
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(ticks=np.arange(1900, 2021, step=5), 
#            fontsize=14, 
#            rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx() # create second y-axis
# ax1.set_xlim(1900, 2020)
 
# ax1.scatter(x=prize_per_year.index, 
#            y=prize_per_year.values, 
#            c='dodgerblue',
#            alpha=0.7,
#            s=100,)
 
# ax1.plot(prize_per_year.index, 
#         moving_average.values, 
#         c='crimson', 
#         linewidth=3,)
 
# # Adding prize share plot on second axis
# ax2.plot(prize_per_year.index, 
#         share_moving_average.values, 
#         c='grey', 
#         linewidth=3,)
 
# plt.show()

# plt.figure(figsize=(16,8), dpi=200)
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(ticks=np.arange(1900, 2021, step=5), 
#            fontsize=14, 
#            rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax1.set_xlim(1900, 2020)
 
# # Can invert axis
# ax2.invert_yaxis()
 
# ax1.scatter(x=prize_per_year.index, 
#            y=prize_per_year.values, 
#            c='dodgerblue',
#            alpha=0.7,
#            s=100,)
 
# ax1.plot(prize_per_year.index, 
#         moving_average.values, 
#         c='crimson', 
#         linewidth=3,)
 
# ax2.plot(prize_per_year.index, 
#         share_moving_average.values, 
#         c='grey', 
#         linewidth=3,)
 
# plt.show()



# A Choropleth Map and the Countries with the Most Prizes

# Challenge 1: Top 20 Country Ranking

'''
Create a Pandas DataFrame called top20_countries that has the two columns. 
The prize column should contain the total number of prizes won.

Is it best to use birth_country, birth_country_current or organization_country?

What are some potential problems when using birth_country or any of the others? Which column is the least problematic?

Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what you're after:

What is the ranking for the top 20 countries in terms of the number of prizes?
'''

top_countries = df_data.groupby(['birth_country_current'], 
                                  as_index=False).agg({'prize': pd.Series.count})
 
top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]


h_bar = px.bar(x=top20_countries.prize,
               y=top20_countries.birth_country_current,
               orientation='h',
               color=top20_countries.prize,
               color_continuous_scale='Viridis',
               title='Top 20 Countries by Number of Prizes')
 
h_bar.update_layout(xaxis_title='Number of Prizes', 
                    yaxis_title='Country',
                    coloraxis_showscale=False)
# h_bar.show()


# Challenge 2: Choropleth Map

'''
Create a Choropleth Map based on Nobel prize distribution
'''

df_countries = df_data.groupby(['birth_country_current', 'ISO'], 
                               as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)

world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize', 
                          hover_name='birth_country_current', 
                          color_continuous_scale=px.colors.sequential.matter)
 
world_map.update_layout(coloraxis_showscale=True,)
 
# world_map.show()

# Challenge 3: Country Bar Chart with Prize Category

'''
In which category are Germany and Japan the weakest compared to the United States?

In which category does Germany have more prizes than the UK?

In which categories does France have more prizes than Germany?

Which category makes up most of Australia's Nobel prizes?

Which category makes up half of the prizes in the Netherlands?

Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?

'''

cat_country = df_data.groupby(['birth_country_current', 'category'], 
                               as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values(by='prize', ascending=False, inplace=True)

merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')
# change column names
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize'] 
merged_df.sort_values(by='total_prize', inplace=True)

# cat_cntry_bar = px.bar(x=merged_df.cat_prize,
#                        y=merged_df.birth_country_current,
#                        color=merged_df.category,
#                        orientation='h',
#                        title='Top 20 Countries by Number of Prizes and Category')
 
# cat_cntry_bar.update_layout(xaxis_title='Number of Prizes', 
#                             yaxis_title='Country')
# cat_cntry_bar.show()

# Challenge 4: Prizes by Country over Time

'''
When did the United States eclipse every other country in terms of the number of prizes won?

Which country or countries were leading previously?

Calculate the cumulative number of prizes won by each country in every year. Again, use the birth_country_current of the winner to calculate this.

Create a plotly line chart where each country is a coloured line.


'''

# prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
# prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]


# cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
#                                               'year']).sum().groupby(level=[0]).cumsum()
# cumulative_prizes.reset_index(inplace=True) 


# l_chart = px.line(cumulative_prizes,
#                   x='year', 
#                   y='prize',
#                   color='birth_country_current',
#                   hover_name='birth_country_current')
 
# l_chart.update_layout(xaxis_title='Year',
#                       yaxis_title='Number of Prizes')
 
# l_chart.show()


# Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations

# Challenge 1

# Create a bar chart showing the organisations affiliated with the Nobel laureates.

'''
Which organisations make up the top 20?

How many Nobel prize winners are affiliated with the University of 
Chicago and Harvard University?

'''

top20_orgs = df_data.organization_name.value_counts()[:20]
top20_orgs.sort_values(ascending=True, inplace=True)

org_bar = px.bar(x = top20_orgs.values,
                 y = top20_orgs.index,
                 orientation='h',
                 color=top20_orgs.values,
                 color_continuous_scale=px.colors.sequential.haline,
                 title='Top 20 Research Institutions by Number of Prizes')
 
org_bar.update_layout(xaxis_title='Number of Prizes', 
                      yaxis_title='Institution',
                      coloraxis_showscale=False)
# org_bar.show()


# Challenge 2

'''
Create another plotly bar chart graphing the top 20 organisation cities of the research institutions associated with a Nobel laureate.

Where is the number one hotspot for discoveries in the world?

Which city in Europe has had the most discoveries?
'''

top20_org_cities = df_data.organization_city.value_counts()[:20]
top20_org_cities.sort_values(ascending=True, inplace=True)
city_bar2 = px.bar(x = top20_org_cities.values,
                  y = top20_org_cities.index,
                  orientation='h',
                  color=top20_org_cities.values,
                  color_continuous_scale=px.colors.sequential.Plasma,
                  title='Which Cities Do the Most Research?')
 
city_bar2.update_layout(xaxis_title='Number of Prizes', 
                       yaxis_title='City',
                       coloraxis_showscale=False)
# city_bar2.show()

# Challenge 3

'''
Create a plotly bar chart graphing the top 20 birth cities of Nobel laureates.

Use a named colour scale called Plasma for the chart.

What percentage of the United States prizes came from Nobel laureates born in New York?

How many Nobel laureates were born in London, Paris and Vienna?

Out of the top 5 cities, how many are in the United States?

'''

top20_cities = df_data.birth_city.value_counts()[:20]
top20_cities.sort_values(ascending=True, inplace=True)
city_bar = px.bar(x=top20_cities.values,
                  y=top20_cities.index,
                  orientation='h',
                  color=top20_cities.values,
                  color_continuous_scale=px.colors.sequential.Plasma,
                  title='Where were the Nobel Laureates Born?')
 
city_bar.update_layout(xaxis_title='Number of Prizes', 
                       yaxis_title='City of Birth',
                       coloraxis_showscale=False)
# city_bar.show()

# Challenge 4
'''
Create a DataFrame that groups the number of prizes by organisation.

Then use the plotly documentation to create a sunburst chart

Click around in your chart, what do you notice about Germany and France?
'''

country_city_org = df_data.groupby(by=['organization_country', 
                                       'organization_city', 
                                       'organization_name'], as_index=False).agg({'prize': pd.Series.count})
 
country_city_org = country_city_org.sort_values('prize', ascending=False)

burst = px.sunburst(country_city_org, 
                    path=['organization_country', 'organization_city', 'organization_name'], 
                    values='prize',
                    title='Where do Discoveries Take Place?',
                   )
 
burst.update_layout(xaxis_title='Number of Prizes', 
                    yaxis_title='City',
                    coloraxis_showscale=False)
 
# burst.show()



# Unearthing Patterns in the Laureate Age at the Time of the Award

# Challenge 1
'''
Calculate the age of the laureate in the year of the ceremony and add this 
as a column called winning_age to the df_data DataFrame.
'''

birth_years = df_data.birth_date.dt.year

df_data['winning_age'] = df_data.year - birth_years

# Challenge 2

'''
What are the names of the youngest and oldest Nobel laureate?

What did they win the prize for?

What is the average age of a winner?

75% of laureates are younger than what age when they receive the prize?

Use Seaborn to create histogram to visualise the distribution of laureate age 
at the time of winning. Experiment with the number of bins to 
see how the visualisation changes.

'''

# print(df_data.nlargest(n=1, columns='winning_age'))
# print(df_data.nsmallest(n=1, columns='winning_age'))

# Challenge 3

'''
Calculate the descriptive statistics for the age at the time of the award.

Then visualise the distribution in the form of a histogram using Seaborn's .histplot() function.

Experiment with the bin size. Try 10, 20, 30, and 50.

'''

print(df_data.winning_age.describe())

# plt.figure(figsize=(8, 4), dpi=200)
# sns.histplot(data=df_data,
#              x=df_data.winning_age,
#              bins=30)
# plt.xlabel('Age')
# plt.title('Distribution of Age on Receipt of Prize')
# plt.show()

# Challenge 4

'''
Use Seaborn to create a .regplot with a trendline.

Set the lowess parameter to True to show a moving average of the linear fit.

According to the best fit line, how old were Nobel laureates in the years 1900-1940 when they were awarded the prize?

According to the best fit line, what age would it predict for a Nobel laureate in 2020?

'''

# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#     sns.regplot(data=df_data,
#                 x='year',
#                 y='winning_age',
#                 lowess=True, 
#                 scatter_kws = {'alpha': 0.4},
#                 line_kws={'color': 'black'})
 
# plt.show()

# Challenge 5

'''
Use Seaborn's .boxplot() to show how the mean, quartiles, max, and minimum values vary across categories. Which category has the longest "whiskers"?

In which prize category are the average winners the oldest?

In which prize category are the average winners the youngest?

You can also use plotly to create the box plot if you like.

'''

# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#     sns.boxplot(data=df_data,
#                 x='category',
#                 y='winning_age')
 
# plt.show()

# Challenge 6

'''
Now use Seaborn's .lmplot() and the row parameter to create 6 separate charts for each prize category. Again set lowess to True.

What are the winning age trends in each category?

Which category has the age trending up and which category has the age trending down?

Is this .lmplot() telling a different story from the .boxplot()?

Create a third chart with Seaborn. This time use .lmplot() to put all 6 categories on the same chart using the hue parameter.

'''

# with sns.axes_style('whitegrid'):
#     sns.lmplot(data=df_data,
#                x='year', 
#                y='winning_age',
#                row = 'category',
#                lowess=True, 
#                aspect=2,
#                scatter_kws = {'alpha': 0.6},
#                line_kws = {'color': 'black'},)

with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               hue='category',
               lowess=True, 
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})
 
plt.show()