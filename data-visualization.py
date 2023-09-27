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

# Histogram plot showing count of 'town'
# sns.histplot(x='town', data = df)
# plt.title('Count of Towns')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'flat_type'
# sns.histplot(x='flat_type', data = df)
# plt.title('Count of Flat Type')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'flat_model'
# sns.histplot(x='flat_model', data = df)
# plt.title('Count of Flat Model')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'storey_range'
# sns.histplot(x='storey_range', data = df)
# plt.title('Count of Storey Range')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'year'
# sns.histplot(x=df['year'], data = df)
# plt.title('Count of Year')
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'street_name'
# sns.countplot(x='street_name', data = df)
# plt.title('Count of Street Name')
# plt.xticks(rotation=90)
# plt.show()

# Histogram plot showing count of 'floor_area_sqm'
# sns.histplot(x='floor_area_sqm', data = df)
# plt.title('Count of Floor Area Sqm')
# plt.xticks(rotation=90)
# plt.show()

# Histogram Plot showing count of 'lease_commence_date'
# sns.histplot(x='lease_commence_date', data = df)
# plt.title('Count of Lease Commence Date')
# plt.xticks(rotation=90)
# plt.show()

# Histplot showing count of 'resale_price'
# sns.histplot(df["resale_price"])
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing y = 'resale_price', x = 'year' 
# sns.scatterplot(data=df, x="year", y="resale_price")
# plt.title('Resale Price over years')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing y = 'resale_price', x = 'floor_area_sqm' 
# sns.scatterplot(data=df, x="floor_area_sqm", y="resale_price")
# plt.title('Resale Price and floor area sqm')
# plt.xlabel('floor area sqm')
# plt.ylabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()


# df = pd.read_csv("2012_onwards_sorted_output.csv")

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
# labelEncoder = LabelEncoder()
# df["le_town"] = labelEncoder.fit_transform(df["town"])
# le_df = 'le_df.csv'
# df.to_csv(le_df, index=False)
# print('Merged CSV file saved at:', le_df)

df = pd.read_csv("ouput.csv")

# Correlation matrix and heatmap
# corr_matrix = df.corr(numeric_only=True)
# k = 7
# cols = corr_matrix.nlargest(7, 'resale_price')['resale_price'].index
# cm = np.corrcoef(df[cols].values.T)
# sns.set(font_scale=1.25)
# hm = sns.heatmap(cm,  fmt='.2f', annot=True, annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
# plt.show()