import pandas as pd

#combine the address, names , street name into 1
def get_hdb_list():
    df = pd.read_csv('web_scraper/Data/2012_merged.csv')
    all_hdb_names = list(df['flat'])
    return all_hdb_names


def get_hdb_coordinates():
    #filter to address, X ,Y and remove duplicates
    hdb_coord = pd.read_csv('web_scraper/Data/Coordinates/hdb_coordinates.csv')
    hdb_coord = hdb_coord[['flat','LATITUDE','LONGITUDE']]
    hdb_coord = hdb_coord.drop_duplicates(subset=['flat'])
    hdb_coord = hdb_coord.reset_index(drop=True)
    return hdb_coord

def get_hdb_postal():
    hdb_postal = pd.read_csv('web_scraper/Data/Coordinates/hdb_coordinates.csv')
    hdb_postal = hdb_postal[['flat','POSTAL']]
    hdb_postal = hdb_postal.drop_duplicates(subset=['flat'])
    hdb_postal = hdb_postal.reset_index(drop=True)
    return hdb_postal.pop('POSTAL')