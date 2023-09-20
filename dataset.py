import pandas as pd

df = pd.concat(map(pd.read_csv, ['ResaleFlatPricesBasedonApprovalDate19901999.csv',
                                 'ResaleFlatPricesBasedonApprovalDate19901999.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv',
                                 'ResaleFlatPricesBasedonregistrationdatefromJan2017onwards.csv']))

column_to_sort_by = 'town'

sorted_df = df.sort_values(by=column_to_sort_by)

sorted_csv_file = 'sorted_output.csv'

df.to_csv(sorted_csv_file, index=False)

print('Merged CSV file saved at:', sorted_csv_file)


