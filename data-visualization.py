import warnings
warnings.simplefilter('ignore')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Read the CSV file, save as dataframe (df)
# data taken from 2012 onwards as earlier years contain missing data
df = pd.read_csv("2012_onwards_sorted_output.csv")

# View the first 5 rows
# print(df.head())

# see df info
# print(df.info())

# Histogram plot showing count of 'town'
sns.histplot(x='town', data = df)
plt.title('Count of Towns')
plt.xticks(rotation=90)
plt.show()

# Histogram plot showing count of 'flat_type'
sns.histplot(x='flat_type', data = df)
plt.title('Count of Flat Type')
plt.xticks(rotation=90)
plt.show()

# Histogram plot showing count of 'flat_model'
sns.histplot(x='flat_model', data = df)
plt.title('Count of Flat Model')
plt.xticks(rotation=90)
plt.show()

# Histogram plot showing count of 'storey_range'
sns.histplot(x='storey_range', data = df)
plt.title('Count of Storey Range')
plt.xticks(rotation=90)
plt.show()

# Histogram plot showing count of 'year'
sns.histplot(x=df['year'], data = df)
plt.title('Count of Year')
plt.xlabel('Year')
plt.xticks(rotation=90)
plt.show()

# Histogram plot showing count of 'floor_area_sqm'
sns.histplot(x='floor_area_sqm', data = df)
plt.title('Count of Floor Area Sqm')
plt.xticks(rotation=90)
plt.show()

# Histogram Plot showing count of 'lease_commence_date'
sns.histplot(x='lease_commence_date', data = df)
plt.title('Count of Lease Commence Date')
plt.xticks(rotation=90)
plt.show()

# Histplot showing count of 'resale_price'
sns.histplot(df["resale_price"])
plt.ticklabel_format(style='plain', axis='x')
plt.show()

# Line graph showing y='resale_price', x='year' 
plt.figure(figsize=(14,5))
sns.set_style("ticks")
sns.lineplot(data=df,x="year",y='resale_price',color='firebrick')
plt.xlabel('Year')
plt.ylabel('Resale Price')
sns.despine()
plt.title("Resale price over time",size='x-large')
plt.show()

# Scatter Plot showing y = 'resale_price', x = 'floor_area_sqm' 
# sns.scatterplot(data=df, x="floor_area_sqm", y="resale_price")
# plt.title('Resale Price and floor area sqm')
# plt.xlabel('floor area sqm')
# plt.ylabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

