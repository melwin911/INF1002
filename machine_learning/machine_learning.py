import warnings
warnings.simplefilter('ignore')
import pandas as pd
from xgboost import XGBRegressor
import datetime

# Encodes string value to a label
def encode(value):
    df = pd.read_csv("csv_files/encoded_labels.csv")

    for row in df.iterrows():
        town = row["VALUE"]
        label = row["LABEL"]
        if value == town:
            return label

df = pd.read_csv("csv_files/label_encoded_dataset.csv")

# Drop some unnecessary columns
df = df.drop('street_name',axis=1)
df = df.drop('block',axis=1)

x = df.drop('resale_price',axis =1).values
y = df['resale_price'].values

def predictPrice(town,flat_type,storey_range,floor_area_sqm,flat_model,lease_commence_date):
    current_year = datetime.datetime.now().year

    u_test = []
    u_test.append(current_year)
    u_test.append(encode(town))
    u_test.append(encode(flat_type))
    u_test.append(encode(storey_range))
    u_test.append(int(floor_area_sqm))
    u_test.append(encode(flat_model))
    u_test.append(lease_commence_date)

    # User predictions using best model (XGBoost)
    # Refer to tuning_hyperparams.py to see how best hyperparams were derived
    u_model = XGBRegressor(colsample_bytree=0.5, gamma=0, learning_rate=0.3, max_depth=10, min_child_weight=1, subsample=1)
    u_prediction = u_model.predict([u_test])
    print("Prediction is " + str(u_prediction[0]))
    return u_prediction[0]
