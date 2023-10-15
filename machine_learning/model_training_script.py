import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from geopy.geocoders import Nominatim
from sklearn.neighbors import KNeighborsRegressor
import pickle


def train():
    # Dataset from https://data.gov.sg/dataset/resale-flat-prices
    file_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8OfO82KXoRmO0E6c58MdwsOSc8ns5Geme87SiaiqTUrS_hI8u8mYE5KIOfQe4m2m3GGf9En22xuXx/pub?gid=382289391&single=true&output=csv"
    data = pd.read_csv(file_url)

    dataframe = data.copy()

    # let's break date to years, months
    dataframe['date'] = pd.to_datetime(dataframe['month'])
    dataframe['month'] = dataframe['date'].apply(lambda date:date.month)
    dataframe['year'] = dataframe['date'].apply(lambda date:date.year)

    # Get number of years left on lease as a continuous number (ignoring months)
    dataframe['remaining_lease'] = dataframe['remaining_lease'].apply(lambda remaining_lease:remaining_lease[:2])

    # Get storey range as a continuous number
    dataframe['storey_range'] = dataframe['storey_range'].apply(lambda storey_range:storey_range[:2])

    # Concat address
    dataframe['address'] = dataframe['block'].map(str) + ', ' + dataframe['street_name'].map(str) + ', Singapore' 

    # Geocode by town (Singapore is so small that geocoding by addresses might not make much difference compared to geocoding to town)
    town = [x for x in dataframe['town'].unique().tolist() 
                if type(x) == str]
    latitude = []
    longitude = []
    for i in range(0, len(town)):
        # remove things that does not seem useful here
        try:
            geolocator = Nominatim(user_agent="ny_explorer")
            loc = geolocator.geocode(town[i])
            latitude.append(loc.latitude)
            longitude.append(loc.longitude)
        except:
            # in the case the geolocator does not work, then add nan element to list
            # to keep the right size
            latitude.append(np.nan)
            longitude.append(np.nan)
    # create a dataframe with the location, latitude and longitude
    df_ = pd.DataFrame({'town': town,
                        'latitude': latitude,
                        'longitude': longitude})
    # merge on Restaurant_Location with rest_df to get the column 
    dataframe = dataframe.merge(df_, on='town', how='left')

    # label encode the categorical values and convert them to numbers

    townDict = {'ANG MO KIO': 1,'BEDOK': 2,'BISHAN': 3,'BUKIT BATOK': 4,'BUKIT MERAH': 5,'BUKIT PANJANG': 6,'BUKIT TIMAH': 7,'CENTRAL AREA': 8,'CHOA CHU KANG': 9,'CLEMENTI': 10,'GEYLANG': 11,'HOUGANG': 12,'JURONG EAST': 13,'JURONG WEST': 14,'KALLANG/WHAMPOA': 15,'MARINE PARADE': 16,'PASIR RIS': 17,'PUNGGOL': 18,'QUEENSTOWN': 19,'SEMBAWANG': 20,'SENGKANG': 21,'SERANGOON': 22,'TAMPINES': 23,'TOA PAYOH': 24,'WOODLANDS': 25,'YISHUN': 26,}
    flat_typeDict = {'1 ROOM': 1,'2 ROOM': 2,'3 ROOM': 3,'4 ROOM': 4,'5 ROOM': 5,'EXECUTIVE': 6,'MULTI-GENERATION': 7,}

    dataframe['town'] = dataframe['town'].replace(townDict, regex=True)
    dataframe['flat_type'] = dataframe['flat_type'].replace(flat_typeDict, regex=True)

    # drop some unnecessary columns
    dataframe = dataframe.drop('date',axis=1)

    dataframe = dataframe.drop('block',axis=1)
    dataframe = dataframe.drop('month',axis=1)
    dataframe = dataframe.drop('street_name',axis=1)
    dataframe = dataframe.drop('address',axis=1)
    dataframe = dataframe.drop('flat_model',axis=1)
    dataframe = dataframe.drop('year',axis=1)
    dataframe = dataframe.drop('remaining_lease',axis=1)

    X = dataframe.drop('resale_price',axis =1)
    y = dataframe['resale_price']
    X = X.values
    y = y.values
    # splitting Train and Test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


    s_scaler = StandardScaler()
    X_train = s_scaler.fit_transform(X_train.astype(np.float))
    X_test = s_scaler.transform(X_test.astype(np.float))

    knn = KNeighborsRegressor(algorithm='brute')

    knn.fit(X_train,y_train)

    # save model
    filename = 'hdbknn.sav'
    scalername = 'scaler.sav'
    pickle.dump(knn, open(filename, 'wb'))
    pickle.dump(s_scaler, open(scalername, 'wb'))

    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(X_test, y_test)
    print(result)
    return result