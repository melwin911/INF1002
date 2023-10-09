import pandas as pd
import csv

df = pd.concat(map(pd.read_csv, ['ResaleFlatPricesBasedonApprovalDate19901999.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv',
                                 'ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv',
                                 'ResaleFlatPricesBasedonregistrationdatefromJan2017onwards.csv']))

df.fillna(0, inplace=True)

df['year'] = df['year'].str.replace('-01','')
df.drop_duplicates(inplace=True)
df['flat'] = df['block'].astype(str) + df['street_name'].astype(str)

column_to_sort_by = 'town'

sorted_df = df.sort_values(by=column_to_sort_by)

df = sorted_df.groupby(['town', 'flat']).agg({'resale_price': 'mean'}).reset_index()


def merge_csv(file1, file2, common_column, output_file):
    # Read data from the first CSV file and create a dictionary based on the common column
    data_dict = {}
    with open(file1, 'r', newline='') as csv_file:
        reader1 = csv.DictReader(csv_file)
        for row in reader1:
            key = row[common_column]
            data_dict[key] = row

    # Merge data from the second CSV file into the dictionary based on the common column
    with open(file2, 'r', newline='') as csv_file:
        reader2 = csv.DictReader(csv_file)
        for row in reader2:
            key = row[common_column]
            if key in data_dict:
                data_dict[key].update(row)

    # Write the merged data to a new CSV file
    header = data_dict[next(iter(data_dict))].keys()
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for row in data_dict.values():
            writer.writerow(row)


# Specify the file paths and common column
file1 = 'merged.csv'
file2 = 'final_hdb_mrt.csv'
common_column = 'flat'  # Change this to the appropriate common column
output_file = 'final_merged.csv'

# Merge the CSV files and write to the output file
merge_csv(file1, file2, common_column, output_file)
print('csv file printed')