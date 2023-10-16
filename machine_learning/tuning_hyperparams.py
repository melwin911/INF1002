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

df = pd.read_csv("csv_files/label_encoded_dataset.csv")

df = df.drop('street_name',axis=1)
df = df.drop('block',axis=1)

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

    # Root mean squared error
    print(f"First Iteration {name} RMSE:% f" %(rmse))

# RDG Tuning
param_grid = {
    'alpha':(1.0, 2.0, 3.0),
    'fit_intercept':(True, False),
    'copy_X':(True, False),
    'max_iter':(1000, 500, 2000),
    'positive':(True, False),
    'solver': ('auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga', 'lbfgs')}
rdg = Ridge()
gs_rdg = GridSearchCV(rdg, param_grid)
gs_rdg.fit(x_train, y_train)
best_hyperparams = gs_rdg.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_rdg.best_estimator_

# Tuned RDG model
best_rdg = Ridge(alpha=2.0, copy_X=False, fit_intercept=True, max_iter=500, positive=False, solver='sag')
best_rdg.fit(x_train, y_train)
test_predictions = best_rdg.predict(x_test)
rmse = (MSE(y_test, test_predictions)) ** (1/2)
print(f"Second Iteration RDG RMSE:% f" %(rmse))

# LSO Tuning
param_grid = {
    'alpha':(1.0, 2.0, 3.0),
    'fit_intercept':(True, False),
    'precompute':(True, False),
    'copy_X':(True, False),
    'max_iter':(1000, 500, 2000),
    'warm_start':(True, False),
    'positive':(True, False)}
lso = Lasso()
gs_lso = GridSearchCV(lso, param_grid)
gs_lso.fit(x_train, y_train)
best_hyperparams = gs_lso.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_lso.best_estimator_

# Tuned LSO model
best_lso = Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000, positive=False, precompute=False, warm_start=True)
best_lso.fit(x_train, y_train)
test_predictions = best_lso.predict(x_test)
rmse = (MSE(y_test, test_predictions)) ** (1/2)
print(f"Second Iteration LSO RMSE:% f" %(rmse))

# XGB Tuning
param_grid = {
    'learning_rate':(0.1, 0.3),
    'max_depth':(3,6,10),
    'min_child_weight':(1,5,10),
    'gamma':(0,5,10),
    'subsample':(0.5, 1),
    'colsample_bytree':(0.5,1)}
xgb = XGBRegressor()
gs_xgb = GridSearchCV(xgb, param_grid)
gs_xgb.fit(x_train, y_train)
best_hyperparams = gs_xgb.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_xgb.best_estimator_

# Tuned XGB model
best_xgb = XGBRegressor(colsample_bytree=0.5, gamma=0, learning_rate=0.3, max_depth=10, min_child_weight=1, subsample=1)
best_xgb.fit(x_train, y_train)
test_predictions = best_xgb.predict(x_test)
rmse = (MSE(y_test, test_predictions)) ** (1/2)
print(f"Second Iteration XGB RMSE:% f" %(rmse))


# MLR Tuning
param_grid = {
    'fit_intercept': (True, False), 
    'copy_X':(True, False),
    'n_jobs':(None, 50, 100),
    'positive':(True, False)}
mlr = LinearRegression()
gs_mlr = GridSearchCV(mlr, param_grid)
gs_mlr.fit(x_train, y_train)
best_hyperparams = gs_mlr.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_mlr.best_estimator_

# Tuned MLR model
best_mlr = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, positive=False)
best_mlr.fit(x_train, y_train)
test_predictions = best_mlr.predict(x_test)
rmse = (MSE(y_test, test_predictions)) ** (1/2)
print(f"Second Iteration MLR RMSE:% f" %(rmse))

# KNN Tuning
param_grid = {
    'weights': ('uniform', 'distance'), 
    'algorithm':('auto', 'ball_tree', 'kd_tree','brute')}
knn = KNeighborsRegressor()
gs_knn = GridSearchCV(knn, param_grid)
gs_knn.fit(x_train, y_train)
best_hyperparams = gs_knn.best_params_
print('Best hyerparameters:\n', best_hyperparams)
best_model = gs_knn.best_estimator_

# Tuned KNN model
best_knn = KNeighborsRegressor(algorithm='auto', weights='distance')
best_knn.fit(x_train, y_train)
test_predictions = best_knn.predict(x_test)
rmse = (MSE(y_test, test_predictions)) ** (1/2)
print(f"Second Iteration KNN RMSE:% f" %(rmse))

tuned_models = []
tuned_models.append(('KNN', KNeighborsRegressor(algorithm='auto', weights='distance')))
tuned_models.append(('MLR', LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, positive=False)))
tuned_models.append(('XGB', XGBRegressor(colsample_bytree=0.5, gamma=0, learning_rate=0.3, max_depth=10, min_child_weight=1, subsample=1)))
tuned_models.append(('LSO', Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000, positive=False, precompute=False, warm_start=True)))
tuned_models.append(('RDG', Ridge(alpha=2.0, copy_X=False, fit_intercept=True, max_iter=500, positive=False, solver='sag')))

# 2nd iteration training and testing
for name, model in tuned_models:
    model.fit(x_train, y_train)
    test_predictions = model.predict(x_test)
    rmse = (MSE(y_test, test_predictions)) ** (1/2)
    
    # Root mean squared error and report
    print(f"2nd Iteration {name} RMSE:% f" %(rmse))