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
df = pd.read_csv("final_sorted.csv")

# View the first 5 rows
# print(df.head())

# see df info
# print(df.info())

# Scatter Plot showing x = 'resale_price', y = 'top_school_dist' 
# sns.scatterplot(data=df, x="resale_price", y="top_school_dist")
# plt.title('Resale Price and top school distance')
# plt.ylabel('Top School Distance')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'park_dist' 
# sns.scatterplot(data=df, x="resale_price", y="park_dist")
# plt.title('Resale Price and park distance')
# plt.ylabel('Park Distance')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'mall_dist' 
# sns.scatterplot(data=df, x="resale_price", y="mall_dist")
# plt.title('Resale Price and mall distance')
# plt.ylabel('Mall Distance')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'hakwer_dist' 
# sns.scatterplot(data=df, x="resale_price", y="hakwer_dist")
# plt.title('Resale Price and hawker distance')
# plt.ylabel('Hawker Distance')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'station_dist' 
# sns.scatterplot(data=df, x="resale_price", y="station_dist")
# plt.title('Resale Price and station distance')
# plt.ylabel('Station Distance')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'num_station_2km_2027_onwards' 
# sns.scatterplot(data=df, x="resale_price", y="num_station_2km_2027_onwards")
# plt.title('Resale Price and Number of new stations 2027 onwards')
# plt.ylabel('Number of new stations 2027 onwards')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()

# Scatter Plot showing x = 'resale_price', y = 'num_of_new_stations_added_here' 
# sns.scatterplot(data=df, x="resale_price", y="num_of_new_stations_added_here")
# plt.title('Resale Price and Number of new stations 2027 onwards')
# plt.ylabel('Number of new stations added here')
# plt.xlabel('Resale Price')
# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='x')
# plt.show()