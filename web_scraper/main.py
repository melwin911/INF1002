import pandas as pd
import requests
import json
from geopy.distance import geodesic
import school_scraper , hdb_scraper , station_scraper , park_scraper , mall_scraper , hawker_scraper

def find_postal(lst, filename):  
    for index,add in enumerate(lst):
        url= "https://developers.onemap.sg/commonapi/search?returnGeom=Y&getAddrDetails=Y&pageNum=1&searchVal="+ add        
        # Retrieve information from website
        response = requests.get(url)
        try:
            data = json.loads(response.text) 
        except ValueError:
            pass
    
        temp_df = pd.DataFrame.from_dict(data["results"])
        # The "add" is the address that was used to search in the website
        temp_df["flat"] = add
        
        # Create the file with the first row that is read in 
        if index == 0:
            file = temp_df
        else:
            file = pd.concat([file, temp_df], ignore_index=True)
    file.to_csv(filename + '.csv')

def find_nearest(house, amenity, radius=2):
    results = {}
    for index,flat in enumerate(house.iloc[:,0]):
        flat_loc = (house.iloc[index,1],house.iloc[index,2])
        flat_amenity = ['','',100,0]
        for ind, eachloc in enumerate(amenity.iloc[:,0]):
            amenity_loc = (amenity.iloc[ind,1],amenity.iloc[ind,2])
            distance = geodesic(flat_loc,amenity_loc)
            distance = float(str(distance)[:-3]) # convert to float

            if distance <= radius:   # compute number of amenities in 2km radius
                flat_amenity[3] += 1
            if distance < flat_amenity[2]: # find nearest amenity
                flat_amenity[0] = flat
                flat_amenity[1] = eachloc
                flat_amenity[2] = distance
        results[flat] = flat_amenity
    return results

#this will find the geospatial data using ONEMAP API
find_postal(hdb_scraper.get_hdb_list(), 'web_scraper/Data/Coordinates/hdb_coordinates')
find_postal(mall_scraper.get_mall_list(), 'web_scraper/Data/Coordinates/mall_coordinates')
find_postal(school_scraper.get_school_list(), 'web_scraper/Data/Coordinates/School_coordinates')
find_postal(park_scraper.get_park_list(), 'web_scraper/Data/Coordinates/park_coordinates')
find_postal(station_scraper.get_new_stations_list(), 'web_scraper/Data/Coordinates/stations_coordinates')
find_postal(station_scraper.get_current_stations_list(), 'web_scraper/Data/Coordinates/current_station_coordinates')



def find_nearest_school_hdb():
    nearest_school = find_nearest(hdb_scraper.get_hdb_coordinates(), school_scraper.get_school_coordinates())
    flat_top_school = pd.DataFrame.from_dict(nearest_school).T
    flat_top_school = flat_top_school.rename(columns={0: 'flat', 1: 'top_school', 2: 'top_school_dist', 3: 'num_top_school_2km'}).reset_index().drop(['index'], axis=1)
    flat_top_school.to_csv('web_scraper/Data/Flat_amenities/hdb_top_schools.csv' , index=False)

def find_nearest_park_hdb():
    nearest_park = find_nearest(hdb_scraper.get_hdb_coordinates(), park_scraper.get_park_coordinates())
    flat_park = pd.DataFrame.from_dict(nearest_park).T
    flat_park = flat_park.rename(columns={0: 'flat', 1: 'park', 2: 'park_dist', 3: 'num_park_2km'}).reset_index().drop(['index'], axis=1)
    flat_park.to_csv('web_scraper/Data/Flat_amenities/hdb_park.csv' , index=False)

def find_nearest_mall_hdb():
    nearest_mall = find_nearest(hdb_scraper.get_hdb_coordinates(), mall_scraper.get_mall_coordinates())
    flat_mall = pd.DataFrame.from_dict(nearest_mall).T
    flat_mall = flat_mall.rename(columns={0: 'flat', 1: 'mall', 2: 'mall_dist', 3: 'num_mall_2km'}).reset_index().drop(['index'], axis=1)
    flat_mall.to_csv('web_scraper/Data/Flat_amenities/hdb_mall.csv' , index=False)

def find_nearest_hawker_hdb():
    nearest_hawker = find_nearest(hdb_scraper.get_hdb_coordinates(), hawker_scraper.get_hawker_coordinates())
    flat_hawker = pd.DataFrame.from_dict(nearest_hawker).T
    flat_hawker = flat_hawker.rename(columns={0: 'flat', 1: 'hawker', 2: 'hakwer_dist', 3: 'num_hawker_2km'}).reset_index().drop(['index'], axis=1)
    flat_hawker.to_csv('web_scraper/Data/Flat_amenities/hdb_hawker.csv', index=False)

#for all stations including new plans
def find_nearest_station_hdb_new():
    nearest_station_new = find_nearest(hdb_scraper.get_hdb_coordinates(), station_scraper.get_new_station_coordinates())
    flat_station_new= pd.DataFrame.from_dict(nearest_station_new).T
    flat_station_new = flat_station_new.rename(columns={0: 'flat', 1: 'station_name_2027_onwards', 2: 'station_dist_2027_onwards', 3: 'num_station_2km_2027_onwards'}).reset_index().drop(['index'], axis=1)
    flat_station_new.to_csv('web_scraper/Data/Flat_amenities/hdb_stations_new.csv' , index=False)

def find_nearest_station_hdb_current():
    nearest_station = find_nearest(hdb_scraper.get_hdb_coordinates(), station_scraper.get_current_station_coordinates())
    flat_station_current = pd.DataFrame.from_dict(nearest_station).T
    flat_station_current = flat_station_current.rename(columns={0: 'flat', 1: 'station_name', 2: 'station_dist', 3: 'num_station_2km'}).reset_index().drop(['index'], axis=1)
    flat_station_current.to_csv('web_scraper/Data/Flat_amenities/hdb_stations_current.csv' , index=False)

#this is the function calling to find the distance between the hdb flats to the respective types of amenities
find_nearest_school_hdb()
find_nearest_park_hdb()
find_nearest_mall_hdb()
find_nearest_hawker_hdb()
find_nearest_station_hdb_current()
find_nearest_station_hdb_new()

def merge_stations():
    current_mrt_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_stations_current.csv')
    new_mrt_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_stations_new.csv')
    hdb_station = current_mrt_hdb.merge(new_mrt_hdb, on='flat', how='outer')
    hdb_station['num_of_new_stations_added_here'] = hdb_station['num_station_2km_2027_onwards']-hdb_station['num_station_2km']
    hdb_station['num_of_new_stations_added_here'] = hdb_station['num_of_new_stations_added_here'].clip(lower=0)
    hdb_station.to_csv('web_scraper/Data/Flat_amenities/hdb_final_stations.csv' , index=False)

def merge_amenities():
    park_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_park.csv')
    mall_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_mall.csv')
    school_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_top_schools.csv')
    hawker_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_hawker.csv')
    station_hdb = pd.read_csv('web_scraper/Data/Flat_amenities/hdb_final_stations.csv')
    hdb_amenities = park_hdb.merge(mall_hdb , on='flat', how='outer')
    hdb_amenities = hdb_amenities.merge(school_hdb , on='flat', how='outer')
    hdb_amenities = hdb_amenities.merge(hawker_hdb , on='flat', how='outer')
    hdb_amenities = hdb_amenities.merge(station_hdb , on='flat', how='outer')
    columns_to_round = [col for col in hdb_amenities.columns if 'dist' in col]
    hdb_amenities[columns_to_round] = hdb_amenities[columns_to_round].round(2)
    hdb_amenities.to_csv('web_scraper/Data/Flat_amenities/final_amenities_merged.csv',index=False)

#merge station data first
merge_stations()
#merge everything together
merge_amenities()