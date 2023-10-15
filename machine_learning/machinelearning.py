import warnings
warnings.simplefilter('ignore')
import pandas as pd
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import datetime


# Encodes string value to a label
def Encode(value):
    df = pd.read_csv("csv_files/encoded_labels.csv")

    for index,row in df.iterrows():
        town = row["VALUE"]
        label = row["LABEL"]
        if value == town:
            return label


def predictPrice(town,flat_type,storey_range,floor_area_sqm,flat_model,lease_commence_date):
    # Read the CSV file, save as dataframe (df)

    df = pd.read_csv("csv_files/label_encoded_dataset.csv")

    # Drop some unnecessary columns
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

        # Root mean squared error and report
        print(f"1st Iteration {name} RMSE:% f" %(rmse))

    # Refer to tuning_hyperparams.py to see how best hyperparams were derived
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

    current_year = datetime.datetime.now().year

    u_test = []
    u_test.append(current_year)
    u_test.append(Encode(town))
    u_test.append(Encode(flat_type))
    u_test.append(Encode(storey_range))
    u_test.append(int(floor_area_sqm))
    u_test.append(Encode(flat_model))
    u_test.append(lease_commence_date)

    prediction = 0

    # User predictions using all tuned models
    for name, model in tuned_models:
        u_prediction = model.predict([u_test])
        # print(u_prediction[0]
        print(f"Tuned {name} prediction: {u_prediction[0]}")

        if name == "XGB":
            prediction = u_prediction[0]

    print("Prediction is " + str(prediction))
    return prediction
