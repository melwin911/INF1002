import pandas as pd
import numpy as np

def get_hawker_coordinates():
    hawker_coord = pd.read_csv('Data/Downloaded_data/HawkerCentresKML.csv')
    hawker_coord = hawker_coord[['Name','Y','X']]
    hawker_coord = hawker_coord.rename(columns={'Name':'Name','Y':'LATITUDE','X':'LONGTITUDE'})
    return hawker_coord