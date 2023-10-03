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
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xg
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

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

x = df.drop('resale_price',axis =1).values
y = df['resale_price'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

models = []
models.append(('KNN', KNeighborsRegressor(algorithm='brute')))
models.append(('MLR', LinearRegression()))
models.append(('XGB', xg.XGBRegressor(objective ='reg:linear', n_estimators = 10, seed = 123)))
models.append(('LSO', Lasso()))
models.append(('RDG', Ridge()))

# training and testing
for name, model in models:
    model.fit(x_train, y_train)
    test_predictions = model.predict(x_test)
    rmse = (MSE(y_test, test_predictions)) ** (1/2)

    # Root mean squared error
    print(f"{name} RMSE:% f" %(rmse))

    # Visualizing predictions
    # fig = plt.figure(figsize=(10,5))
    # plt.scatter(y_test,test_predictions)
    # plt.plot(y_test,y_test,'r')
    # plt.ticklabel_format(style='plain', axis='y')
    # plt.ticklabel_format(style='plain', axis='x')
    # plt.show()

# prediction using user inputs

# some dummy data:
# 2012, 0, 1, 3, 45, 1986
# 2012, 0, 1, 1, 44, 1980

# 2023, 0, 1, 3, 45, 1986
# 2023, 0, 1, 1, 44, 1980

u_input = input('Enter the year, town, flat type, storey range, floor area sqm and lease commence year:').split(",")
u_year, u_town, u_flat_type, u_storey_range, u_floor_area_sqm, u_lease_commence_year = u_input

u_test = []
u_test.append(int(u_year))
u_test.append(int(u_town))
u_test.append(int(u_flat_type))
u_test.append(int(u_storey_range))
u_test.append(float(u_floor_area_sqm))
u_test.append(int(u_lease_commence_year))


# user predictions using all models
for name, model in models:
    u_prediction = model.predict([u_test])
    print(u_prediction[0])

# changes made from references: 
# 1) label encoded more columns
# 2) removed scaling for higher accuracy