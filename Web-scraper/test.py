import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('Data/final_sorted.csv')
df2 = pd.read_csv('Data/test_data.csv')
# #user input
# postal = input("type postal here :")

# data = df.loc[df['postal'] == postal]

# def get_amenities():
#     amenities = []
#     for col in data.columns:
#         amenities.append(data[col].tolist())
#     myIndices = [3,4,6,7,9,10,12,13,15,16,18,19]
#     flattened = [val for sublist in amenities for val in sublist]
#     flattened = [flattened[i] for i in myIndices]
#     grouped_list = [flattened[i:i+2] for i in range(0, len(flattened), 2)]
#     return tuple([[item[0], item[1] * 1000] for item in grouped_list])

# sorted_df = df.sort_values(by='street_name', ascending=True)
# sorted_df = sorted_df.reset_index(drop=True)
# df['street_name'] = df['block'] + ' ' + df['street_name']
# # Drop column B if needed
# columns_to_drop = ['year','town','lease_commence_date','block']
# df = df.drop(columns=columns_to_drop)
# df.to_csv('Data/test_data.csv',index=False)

# merged_df = pd.merge(df, df2, on='ID', how='inner')
df2 = df2.rename(columns={'street_name': 'flat'})
df = df.drop(columns='resale_price')
merged_df = pd.merge(df, df2, on='flat', how='inner')
merged_df.to_csv('Data/merged_2012_amenities.csv',index=False)