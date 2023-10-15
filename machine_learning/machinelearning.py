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
    df = pd.read_csv("csv_files/label_encoded_dataset.csv")

    df = df.drop('street_name',axis=1)
    df = df.drop('block',axis=1)

    x = df.drop('resale_price',axis =1).values
    y = df['resale_price'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)


    current_year = datetime.datetime.now().year

    u_test = []
    u_test.append(current_year)
    u_test.append(Encode(town))
    u_test.append(Encode(flat_type))
    u_test.append(Encode(storey_range))
    u_test.append(int(floor_area_sqm))
    u_test.append(Encode(flat_model))
    u_test.append(lease_commence_date)

    # User predictions using best model (XGBoost)
    # Refer to tuning_hyperparams.py to see how best hyperparams were derived
    u_model = XGBRegressor(colsample_bytree=0.5, gamma=0, learning_rate=0.3, max_depth=10, min_child_weight=1, subsample=1)
    u_model.fit(x_train, y_train)

    u_prediction = u_model.predict([u_test])
    print("Prediction is " + str(u_prediction[0]))
    return u_prediction[0]
