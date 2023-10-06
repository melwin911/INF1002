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
from xgboost import XGBRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

# Read the CSV file, save as dataframe (df)
# Data taken from final csv file
df = pd.read_csv("final_sorted.csv")

# Correlation matrix and heatmap
# corr_matrix = df.corr(numeric_only=True)
# k = 23
# cols = corr_matrix.nlargest(k, 'resale_price')['resale_price'].index
# cm = np.corrcoef(df[cols].values.T)
# sns.set(font_scale=1.25)
# hm = sns.heatmap(cm,  fmt='.2f', annot=True, annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
# plt.show()

# Drop some unnecessary columns
df = df.drop('town',axis=1)
df = df.drop('flat',axis=1)
df = df.drop('park',axis=1)
df = df.drop('mall',axis=1)
df = df.drop('top_school',axis=1)
df = df.drop('hawker',axis=1)
df = df.drop('station_name',axis=1)
df = df.drop('station_name_2027_onwards',axis=1)







x = df.drop('resale_price',axis =1).values
y = df['resale_price'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

models = []
models.append(('KNN', KNeighborsRegressor()))
models.append(('MLR', LinearRegression()))
models.append(('XGB', XGBRegressor()))
models.append(('LSO', Lasso()))
models.append(('RDG', Ridge()))

# 1st iteration training and testing
for name, model in models:
    model.fit(x_train, y_train)
    test_predictions = model.predict(x_test)
    rmse = (MSE(y_test, test_predictions)) ** (1/2)

    # Root mean squared error and report
    print(f"1st Iteration {name} RMSE:% f" %(rmse))

    # Visualizing predictions
    fig = plt.figure(figsize=(10,5))
    plt.scatter(y_test,test_predictions)
    plt.plot(y_test,y_test,'r')
    plt.ticklabel_format(style='plain', axis='y')
    plt.ticklabel_format(style='plain', axis='x')
    plt.show()

# Refer to tuning_hyperparams.py to see how best hyperparams were derived
# tuned_models = []
# tuned_models.append(('KNN', KNeighborsRegressor(algorithm='auto', weights='distance')))
# tuned_models.append(('MLR', LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, positive=False)))
# tuned_models.append(('XGB', XGBRegressor(colsample_bytree=0.5, gamma=0, learning_rate=0.3, max_depth=10, min_child_weight=1, subsample=1)))
# tuned_models.append(('LSO', Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000, positive=False, precompute=False, warm_start=True)))
# tuned_models.append(('RDG', Ridge(alpha=2.0, copy_X=False, fit_intercept=True, max_iter=500, positive=False, solver='sag')))

# 1st iteration training and testing
# for name, model in tuned_models:
#     model.fit(x_train, y_train)
#     test_predictions = model.predict(x_test)
#     rmse = (MSE(y_test, test_predictions)) ** (1/2)

    # Root mean squared error and report
    # print(f"2nd Iteration {name} RMSE:% f" %(rmse))

    # Visualizing predictions
    # fig = plt.figure(figsize=(10,5))
    # plt.scatter(y_test,test_predictions)
    # plt.plot(y_test,y_test,'r')
    # plt.ticklabel_format(style='plain', axis='y')
    # plt.ticklabel_format(style='plain', axis='x')
    # plt.show()

# prediction using user inputs

# Some dummy data:
# 2012,0,1,3,45,1986
# 2012,0,1,1,44,1980

# 2023,0,1,3,45,1986
# 2023,0,1,1,44,1980

# u_input = input('Enter the year, town, flat type, storey range, floor area sqm and lease commence year:').split(",")
# u_year, u_town, u_flat_type, u_storey_range, u_floor_area_sqm, u_lease_commence_year = u_input

# u_test = []
# u_test.append(int(u_year))
# u_test.append(int(u_town))
# u_test.append(int(u_flat_type))
# u_test.append(int(u_storey_range))
# u_test.append(float(u_floor_area_sqm))
# u_test.append(int(u_lease_commence_year))

# User predictions using all tuned models
# for name, model in tuned_models:
#     u_prediction = model.predict([u_test])
#     # print(u_prediction[0]
#     print(f"Tuned {name} prediction: {u_prediction[0]}")


# Changes made from references: 
# 1) Label encoded more features
# 2) Removed scaling for higher accuracy
# 3) Tuned models for improved performance