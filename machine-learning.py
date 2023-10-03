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
# df = pd.read_csv("2012_onwards_sorted_output.csv")

# peek unique town values
# print(df['town'].unique())
# print(len(df['town'].unique()))

# One Hot Encoding produces +26 columns. High dimensionality not suitable for ML.
# Label encoding does not produce new features unlike OHE, but ML models may misinterpret numbers for hierachy.
# labelEncoder = LabelEncoder()
# df["town"] = labelEncoder.fit_transform(df["town"])
# df["storey_range"] = labelEncoder.fit_transform(df["storey_range"])
# df["flat_type"] = labelEncoder.fit_transform(df["flat_type"])
# df["flat_model"] = labelEncoder.fit_transform(df["flat_model"])

# le_df = 'le_df.csv'
# df.to_csv(le_df, index=False)
# print('Encoded CSV file saved at:', le_df)

df = pd.read_csv("le_df.csv")

# Correlation matrix and heatmap
# corr_matrix = df.corr(numeric_only=True)
# k = 7
# cols = corr_matrix.nlargest(k, 'resale_price')['resale_price'].index
# cm = np.corrcoef(df[cols].values.T)
# sns.set(font_scale=1.25)
# hm = sns.heatmap(cm,  fmt='.2f', annot=True, annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
# plt.show()
# print(df)

# drop some unnecessary columns
df = df.drop('street_name',axis=1)
df = df.drop('flat_model',axis=1)
df = df.drop('block',axis=1)


from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

x = df.drop('resale_price',axis =1).values
y = df['resale_price'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

# not using standardization scaler for better accuracy

# Multiple Liner Regression
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(x_train, y_train)
# predictions = regressor.predict(x_test)

# Root mean squared error
# mse = MSE(y_test, predictions)
# rmse = mse ** (1/2)
# print("RMSE : % f" %(rmse))

# Visualizing predictions
# fig = plt.figure(figsize=(10,5))
# plt.scatter(y_test,predictions)
# plt.plot(y_test,y_test,'r')
# plt.show()

# user_input = input().split()
# unit, height, weight = user_input


# KNN
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(algorithm='brute')
knn.fit(x_train,y_train)
predictions = knn.predict(x_test)

# Root mean squared error
mse = MSE(y_test, predictions)
rmse = mse ** (1/2)
print("RMSE : % f" %(rmse))

# Visualizing predictions
# fig = plt.figure(figsize=(10,5))
# plt.scatter(y_test,predictions)
# plt.plot(y_test,y_test,'r')
# plt.show()

# import xgboost as xg
# xgb_r = xg.XGBRegressor(objective ='reg:linear', n_estimators = 10, seed = 123)
# xgb_r.fit(x_train, y_train)
# predictions = xgb_r.predict(x_test)

# # Root mean squared error
# mse = MSE(y_test, predictions)
# rmse = mse ** (1/2)
# print("RMSE : % f" %(rmse))

# # Visualizing predictions
# fig = plt.figure(figsize=(10,5))
# plt.scatter(y_test,predictions)
# plt.plot(y_test,y_test,'r')
# plt.show()

# from sklearn.linear_model import Lasso
# lasso = Lasso()
# lasso.fit(x_train, y_train)
# predictions = lasso.predict(x_test)

# # Root mean squared error
# mse = MSE(y_test, predictions)
# rmse = mse ** (1/2)
# print("RMSE : % f" %(rmse))

# # Visualizing predictions
# fig = plt.figure(figsize=(10,5))
# plt.scatter(y_test,predictions)
# plt.plot(y_test,y_test,'r')
# plt.show()

# from sklearn.linear_model import Ridge
# ridge = Ridge()
# ridge.fit(x_train, y_train)
# predictions = ridge.predict(x_test)

# # Root mean squared error
# mse = MSE(y_test, predictions)
# rmse = mse ** (1/2)
# print("RMSE : % f" %(rmse))

# # Visualizing predictions
# fig = plt.figure(figsize=(10,5))
# plt.scatter(y_test,predictions)
# plt.plot(y_test,y_test,'r')
# plt.show()

# changes made from reference: label encoded more columns and removed scaling for higher accuracy