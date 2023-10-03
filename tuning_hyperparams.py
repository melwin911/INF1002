# This file uses GridSearchCV to obtain the best hyperparams

import warnings
warnings.simplefilter('ignore')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
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
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("le_df.csv")

df = df.drop('street_name',axis=1)
df = df.drop('flat_model',axis=1)
df = df.drop('block',axis=1)

x = df.drop('resale_price',axis =1).values
y = df['resale_price'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

models = []
# models.append(('KNN', KNeighborsRegressor()))
# models.append(('MLR', LinearRegression()))
models.append(('XGB', XGBRegressor()))
# models.append(('LSO', Lasso()))
# models.append(('RDG', Ridge()))

# 1st iteration training and testing
for name, model in models:
    model.fit(x_train, y_train)
    test_predictions = model.predict(x_test)
    rmse = (MSE(y_test, test_predictions)) ** (1/2)

    # Root mean squared error
    print(f"First Iteration {name} RMSE:% f" %(rmse))

# xgb1 = XGBClassifier(
#  learning_rate =0.1,
#  n_estimators=1000,
#  max_depth=5,
#  min_child_weight=1,
#  gamma=0,
#  subsample=0.8,
#  colsample_bytree=0.8,
#  objective= 'binary:logistic',
#  nthread=4,
#  scale_pos_weight=1,
#  seed=27)
# modelfit(xgb1, train, predictors)

# XGB Tuning
param_grid = {
    'fit_intercept': (True, False), 
    'copy_X':(True, False),
    'n_jobs':(None, 50, 100),
    'positive':(True, False)}
xgb = XGBRegressor()
gs_xgb = GridSearchCV(xgb, param_grid)
gs_xgb.fit(x_train, y_train)
best_hyperparams = gs_xgb.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_xgb.best_estimator_

# Tuned XGB model
# best_xgb = XGBRegressor()
# best_xgb.fit(x_train, y_train)
# test_predictions = best_xgb.predict(x_test)
# rmse = (MSE(y_test, test_predictions)) ** (1/2)
# print(f"Second Iteration {name} RMSE:% f" %(rmse))

# MLR Tuning
# param_grid = {
#     'fit_intercept': (True, False), 
#     'copy_X':(True, False),
#     'n_jobs':(None, 50, 100),
#     'positive':(True, False)}
# mlr = LinearRegression()
# gs_mlr = GridSearchCV(mlr, param_grid)
# gs_mlr.fit(x_train, y_train)
# best_hyperparams = gs_mlr.best_params_
# print('Best hyerparameters:\n', best_hyperparams)
# best_model = gs_mlr.best_estimator_

# Tuned MLR model
# best_mlr = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, positive=False)
# best_mlr.fit(x_train, y_train)
# test_predictions = best_mlr.predict(x_test)
# rmse = (MSE(y_test, test_predictions)) ** (1/2)

# KNN Tuning
# param_grid = {
#     'weights': ('uniform', 'distance'), 
#     'algorithm':('auto', 'ball_tree', 'kd_tree','brute')}
# knn = KNeighborsRegressor()
# gs_knn = GridSearchCV(knn, param_grid)
# gs_knn.fit(x_train, y_train)
# best_hyperparams = gs_knn.best_params_
# print('Best hyerparameters:\n', best_hyperparams)
# best_model = gs_knn.best_estimator_

# Tuned KNN model
# best_knn = KNeighborsRegressor(algorithm='auto', weights='distance')
# best_knn.fit(x_train, y_train)
# test_predictions = best_knn.predict(x_test)
# rmse = (MSE(y_test, test_predictions)) ** (1/2)
# print(f"Second Iteration {name} RMSE:% f" %(rmse))

