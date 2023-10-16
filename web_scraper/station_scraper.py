from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

def station_to_csv():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'

    url = 'https://propertyreviewsg.com/complete-singapore-mrt-list-english-and-chinese-station-names/'
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    soup = BeautifulSoup(data)
    table = soup.find_all('table')[0]
    table_titles = table.find_all('th')
    station_table_titles = [title.text for title in table_titles]

    df = pd.DataFrame(columns=station_table_titles)

    column_data = table.find_all('tr')

    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text for data in row_data]
        length = len(df)
        df.loc[length] = individual_row_data


    df.to_csv('web_scraper/Data/allStationNames.csv' , index=False)

#read the csv and filter out new stations
#return new stations name

def get_new_stations_list():
    all_stations = pd.read_csv("web_scraper/Data/allStationNames.csv")
    all_stations_names = list(all_stations['MRT Station English Name'])
    new_staions = set(all_stations_names)
    return list(new_staions)

def get_new_station_coordinates():
    #filter to address , X , Y and remove duplicates
    station_coord = pd.read_csv('web_scraper/Data/Coordinates/stations_coordinates.csv')
    station_coord = station_coord[['address','LATITUDE','LONGITUDE']]
    station_coord = station_coord.drop_duplicates(subset=['address'])
    station_coord = station_coord.reset_index(drop=True)
    return station_coord

def get_current_stations_list():
    current_stations = pd.read_csv("web_scraper/Data/CurrentStations.csv")
    current_stations_names = list(current_stations['mrt_station_english'])
    current_staions = set(current_stations_names)
    return list(current_staions)

def get_current_station_coordinates():
    station_coord = pd.read_csv('web_scraper/Data/Coordinates/current_stations_coordinates.csv')
    station_coord = station_coord[['address','LATITUDE','LONGITUDE']]
    station_coord = station_coord.drop_duplicates(subset=['address'])
    station_coord = station_coord.reset_index(drop=True)
    return station_coord