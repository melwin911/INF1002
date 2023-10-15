import pandas as pd

# Reading the csv files and merging them into one dataframe
df = pd.concat(map(pd.read_csv, ['ResaleFlatPricesBasedonApprovalDate19901999.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv',
                                 'ResaleFlatPricesBasedonregistrationdatefromJan2017onwards.csv']))

# Dropping duplicate entries that are not needed and filling NaN values with 0
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

# Columns and values are reorganised and formatted to be consistent
df['year'] = df['year'].str.replace('-01', '')
df['flat'] = df['block'].astype(str) + df['street_name'].astype(str)

# Data to be sorted to facilitate the comparison of housing costs across Singapore
column_to_sort_by = 'town'

sorted_df = df.sort_values(by=column_to_sort_by)

# Aggregating data to enhance data quality
df = sorted_df.groupby(['town', 'flat']).agg({'resale_price': 'mean'}).reset_index()

# Exporting the dataframe to a csv file
df.to_csv('csv_files/resale_price_data.csv', index=False)
