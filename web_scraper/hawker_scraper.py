import pandas as pd

def get_hawker_coordinates():
    hawker_coord = pd.read_csv('web_scraper/Data/Downloaded_data/HawkerCentresKML.csv')
    hawker_coord = hawker_coord[['Name','Y','X']]
    hawker_coord = hawker_coord.rename(columns={'Name':'Name','Y':'LATITUDE','X':'LONGTITUDE'})
    return hawker_coord