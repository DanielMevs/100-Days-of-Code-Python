import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
pd.set_option('display.max_columns', None)

# - Explore and Clean the Data

# Challenge 1 
'''
How many rows and columns does the dataset contain?

Are there any NaN values present?

Are there any duplicate rows?

What are the data types of the columns?
'''

# Challenge 2
'''
Convert the USD_Production_Budget, USD_Worldwide_Gross, 
and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
'''

# Challenge 3
'''
Convert the Release_Date column to a Pandas Datetime type.
'''

data = pd.read_csv('cost_revenue_dirty.csv')

# print(data.shape)
# print(data.head())
# print(data.tail())
# print(data.info())
# print(data.sample())

# print(f'Any NaN values among the data? {data.isna().values.any()}')
# print(f'Any duplicates? {data.duplicated().values.any()}')
# duplicated_rows = data[data.duplicated()]
# print(f'Number of duplicates: {len(duplicated_rows)}')

# print(data.info())

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']
 
for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

# print(data.head())
data.Release_Date = pd.to_datetime(data.Release_Date)
# print(data.head())
# print(data.info())

# print(data.describe())
# print(data[data.USD_Production_Budget == 1100.00])
# print(data[data.USD_Production_Budget == 425000000.00])
zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))


