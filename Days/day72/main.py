import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# - Get the first and last 5 rows of the dataframe
# print(df.head())
# print(df.tail())

# - Get dimension (row x column) of dataframe
# print(df.shape)

# - Get the number of non-NaN-valued entries for each column in our dataframe
# print(df.count())

# - To see how many post each programming language has
# - What is going on behind the scenes is that we're
#  grouping by tag (programming language) and then taking the total
# number of rows that is associated with that tag. We then sum up
# the values in these rows and return it as a single row.
# The data frame does this for all categories under 'TAG'
# print(df.groupby('TAG').sum())


# - To see how many entries we have of each category of 'TAG'
# print(df.groupby('TAG').count())

# - We can use square brackets to access an entry in a column
# print(df['DATE'][2])
# - alternatively
# print(df.DATE[1])

# - To inspect the datatype of an entry
# print(type(df['DATE'][1]))

# - We see that our entry is of type string.
# - To convert to a date-time object
print(pd.to_datetime(df.DATE[1]))
print(type(pd.to_datetime(df.DATE[1])))

# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)
print(df.head())


test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)

# - If we want to convert our dataframe such that each category of actor has his own column: 
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

# - To pivot the df DataFrame so that each row is a date and each column is a programming language:
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# print(reshaped_df)

# - To substitute all values that have NaN with 0:
reshaped_df = reshaped_df.fillna(0) 
# print(reshaped_df.head())

# - To check if there are any NaN values left in the entire DataFrame:
is_nan_left = reshaped_df.isna().values.any()
# print(is_nan_left)

# - show a line chart for the popularity of a programming language
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)
# - To show results for Java and Python
# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df.python)

# To plot all languages using a for loop:
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column])

# - To plot all languages using a for loop with a legend:
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], 
#              linewidth=3, label=reshaped_df[column].name)

# plt.legend(fontsize=16)


# To plot an average number of observations (rolling mean):

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)


plt.show()

