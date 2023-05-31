import pandas as pd
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
print(df['DATE'][2])
# - alternatively
print(df.DATE[1])

# - To inspect the datatype of an entry
print(type(df['DATE'][1]))

# - We see that our entry is of type string.
# - To convert to a date-time object
print(type(pd.to_datetime(df.DATE[1])))