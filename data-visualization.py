import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Read the CSV file
# df = pd.read_csv("sorted_output.csv")

# View the first 5 rows
# print(df.head())

# check for null values
# print(df.isnull().sum())

# Bar graph showing count of 'town'
# sns.countplot(x='town', data = df)
# plt.title('Count of Town')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_type'
# sns.countplot(x='flat_type', data = df)
# plt.title('Count of Flat Type')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_model'
# sns.countplot(x='flat_model', data = df)
# plt.title('Count of Flat Model')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'storey_range'
# sns.countplot(x='storey_range', data = df)
# plt.title('Count of Storey Range')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'year'
# sns.countplot(x=df['year'], data = df)
# plt.title('Count of Year')
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'street_name'
# requires one hot encoding to categorize streets
# sns.countplot(x='street_name', data = df)
# plt.title('Count of Street Name')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'storey_range'
# sns.countplot(x='storey_range', data = df)
# plt.title('Count of Storey Range')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'floor_area_sqm'
# sns.countplot(x='floor_area_sqm', data = df)
# plt.title('Count of Floor Area Sqm')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'lease_commence_date'
# sns.countplot(x='lease_commence_date', data = df)
# plt.title('Count of Lease Commence Date')
# plt.xticks(rotation=90)
# plt.show()

# running slow, requires optimization (sub-categorize resale price)
# Bar graph showing count of 'resale_price'
# sns.countplot(x='resale_price', data = df)
# plt.title('Count of Resale Price')
# plt.xticks(rotation=90)
# plt.show()

# running slow, requires optimization (sub-categorize year and resale price)
# Scatter Plot showing y = 'resale_price', x = 'year' 

# x_axis = df['year']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price over years')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing y = 'resale_price 'x = 'lease_commence_date', 

# x_axis = df['lease_commence_date']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and lease commencement date')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing y = 'resale_price 'x = 'flat_type', 

# x_axis = df['flat_type']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and flat type')
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.ylabel('Resale Price')

# # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing x = 'resale_price 'x = 'floor_area_sqm', 

# x_axis = df['floor_area_sqm']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and floor area sqm')
# plt.xlabel('Floor Area Sqm')
# plt.ylabel('Resale Price')

# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()


df = pd.read_csv("2012_onwards_sorted_output.csv")

# running slow, requires optimization (sub-categorize year and resale price)
# Scatter Plot showing y = 'resale_price', x = 'year' 

# x_axis = df['year']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price over years')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# print(df['town'].unique())
# print(len(df['town'].unique()))

# One Hot Encoding produces +26 columns. High dimensionality not suitable for ML.
# ohe_town = pd.get_dummies(df["town"]).astype(int)

# df = pd.concat([df, ohe_town], axis="columns")

# print(df)

# ohe_df = 'ohe_df.csv'

# df.to_csv(ohe_df, index=False)

# print('Merged CSV file saved at:', ohe_df)

# Label encoding does not produce new features unlike OHE, but ML models may misinterpret numbers for hierachy.
labelEncoder = LabelEncoder()
df["le_town"] = labelEncoder.fit_transform(df["town"])
le_df = 'le_df.csv'
df.to_csv(le_df, index=False)
# print('Merged CSV file saved at:', le_df)

df = pd.read_csv("le_df.csv")
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True)
plt.show()
