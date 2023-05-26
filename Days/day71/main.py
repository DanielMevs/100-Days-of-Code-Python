import pandas as pd
df = pd.read_csv('./salaries_by_college_major.csv')
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())
clean_df = df.dropna()
# print(clean_df.tail())

# # - Access a particular column
# print(clean_df["Starting Median Salary"])

# # - To find the highest starting salary
# print(clean_df["Starting Median Salary"].max())

# # - To find the index of the highest starting salary
max_sal_index = clean_df["Starting Median Salary"].idxmax()
# print(max_sal_index)

# - To find the major of the highest starting salary by using the index
most_lucrative_major = clean_df['Undergraduate Major'].loc[max_sal_index]
print(most_lucrative_major)

# - alternatively
most_lucrative_major = clean_df['Undergraduate Major'][max_sal_index]
print(most_lucrative_major)

print(clean_df['Mid-Career Median Salary'].max())
min_mid_car_sal = clean_df["Mid-Career Median Salary"].idxmin()
print(f'Index for the max mid career salary: {min_mid_car_sal}')
print(f'Undergraduate major for minimum mid career salary: {clean_df["Undergraduate Major"]}')

min_starting_med_sal = clean_df['Starting Median Salary'].min()
min_starting_med_sal_idx = clean_df['Starting Median Salary'].idxmin()
print(min_starting_med_sal)
print(clean_df['Undergraduate Major'].loc[min_starting_med_sal_idx])


min_mid_car_sal_idx = clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df.loc[min_mid_car_sal_idx])