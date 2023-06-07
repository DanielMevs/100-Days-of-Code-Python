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
print(themes_by_year.tail())