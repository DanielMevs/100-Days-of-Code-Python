import pandas as pd

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
print(sets[sets['year'] == 1949])