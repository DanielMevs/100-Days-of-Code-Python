import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
# print(colors.head())

# - To find the number of unique colors
# print(colors['name'].nunique())

# - Find the number of transparent colours
# print(colors.groupby('is_trans').count())

# alternatively
# print(colors.is_trans.value_counts())

# - Challenge: Find the Oldest and Largest LEGO Sets using the sets.csv lego dataset
sets = pd.read_csv('data/sets.csv')
# print(sets.head())
# print(sets.tail())

# - To find the year when the first Lego sets were released
# print(sets.sort_values('year').head())


# - To find how many different Lego sets were sold in their first year
# print(sets[sets['year'] == 1949])

# - To find the LEGO set with the largest number of parts
# print(sets.sort_values('num_parts', ascending=False).head())


# - Challenge: create a new Series called sets_by_year which has the years as the index 
# and the number of sets as the value
sets_by_year = sets.groupby('year').count()
# print(sets_by_year['set_num'].head())
# print(sets_by_year['set_num'].tail())

# - To plot this data:
# plt.plot(sets_by_year.index, sets_by_year.set_num)
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()

# - To calculate the number of diifferent thems by calendar year
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
# - To rename a column(s)
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
# print(themes_by_year.head())
# print(themes_by_year.tail())


# - Challenge: create a line plot of the number of themes released year-on-year
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# - To configure and plot our data on two separate axes on the same chart
# ax1 = plt.gca()
# ax2 = ax1.twinx()

# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')

# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')


# plt.show()

# - Challenge: create a Pandas Series called parts_per_set that has the year 
# as the index and contains the average number of parts per LEGO set in that year
# - To work out the average number of parts per LEGO set
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
# print(parts_per_set.head())
# print(parts_per_set.tail())

# - To generate a scatter plot
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()


set_theme_count = sets["theme_id"].value_counts()
# print(set_theme_count[:5])

# - From the above's first column, we can't tell the name, just the theme id
# - The themes.csv file has the actual theme names
# - Challenge: Search for 'Star Wars'. 
# How many id's correspond to the 'Star Wars' name in the themes.csv?

themes = pd.read_csv('data/themes.csv')
# print(themes.head())
# print(themes[themes.name == 'Star Wars'])
# print(sets[sets.theme_id == 18])
# print(sets[sets.theme_id == 209])


# - To combine our data on theme names with the number sets per theme,
# use the .merge() method to combine two separate Dataframes into one.
# set_theme_count = sets["theme_id"].value_counts()
# print(set_theme_count[:5]) -> Let's give these guys a name

set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})
# print(set_theme_count.head())
# - To .merge() two DataFrames along a particular column, we need to 
# provide our two DataFrames and then the column name on which to merge
merged_df = pd.merge(set_theme_count, themes, on='id')
# print(merged_df[:3])

# - To create a bar graph of our data:
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.show()