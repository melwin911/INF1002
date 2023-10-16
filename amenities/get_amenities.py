import pandas as pd 

# read the amenities csv file
df = pd.read_csv('csv_files/amenities.csv')

# retrieve town values from postal code input
def get_town(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    town = row['town'].iloc[0]
    return town

# retrieve block and flat values from postal code input
def get_flat(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    flat = row['flat'].iloc[0]
    return flat

# retrieve nearest park from postal code input
def get_park(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    park = row['park'].iloc[0]
    return park

# retrieve nearest park distance from postal code input
def get_park_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    park_dist = row['park_dist'].iloc[0]
    return park_dist

# retrieve how many park within 2km radius from postal code input
def get_num_park(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_park = row['num_park_2km'].iloc[0]
    return num_park

# retrieve nearest shopping mall from postal code input
def get_mall(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mall = row['mall'].iloc[0]
    return mall

# retrieve nearest shopping mall distance from postal code input
def get_mall_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mall_dist = row['mall_dist'].iloc[0]
    return mall_dist

# get how many shopping mall within 2km radius from postal code input
def get_num_mall(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_mall = row['num_mall_2km'].iloc[0]
    return num_mall

# retrieve any nearest top 50 schools from postal code input
def get_top_school(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    top_school = row['top_school'].iloc[0]
    return top_school

# retrieve distance from any top 50 schools to postal code inputs
def get_top_school_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    top_school_dist = row['top_school_dist'].iloc[0]
    return top_school_dist

# retrieve how many top 50 schools nearby within 2km radius from postal code input
def get_num_top_school(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_top_school = row['num_top_school_2km'].iloc[0]
    return num_top_school

# retrieve nearest hawker center from postal code input
def get_hawker(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawker = row['hawker'].iloc[0]
    return hawker

# retrieve distance from nearest hawker center to postal code input
def get_hawker_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawker_dist = row['hawker_dist'].iloc[0]
    return hawker_dist

# retrieve how many hawker centers are there within 2km radius from postal code input
def get_num_hawker(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_hawker = row['num_hawker_2km'].iloc[0]
    return num_hawker

# retrieve nearest MRT station from postal code input
def get_station_name(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    station_name = row['station_name'].iloc[0]
    return station_name

# retrieve distance from nearest MRT station to postal code input
def get_station_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    station_dist = row['station_dist'].iloc[0]
    return station_dist

# retrieve number of MRT stations within 2km radius of postal code input
def get_num_station(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_station = row['num_station_2km'].iloc[0]
    return num_station

# retrieve any upcoming MRT station from postal code input
def get_upcoming_station_name(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcoming_station_name = row['station_name_2027_onwards'].iloc[0]
    return upcoming_station_name

# retrieve distance from any upcoming MRT stations to postal code input
def get_upcoming_station_dist(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcoming_station_dist = row['station_dist_2027_onwards'].iloc[0]
    return upcoming_station_dist

# retrieve number of upcoming MRT stations within 2km radius of postal code input
def get_num_upcoming_station(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_upcoming_station = row['num_station_2km_2027_onwards'].iloc[0]
    return num_upcoming_station

# retrieve number of MRT station added within 2km radius of postal code input
def get_num_stations_added(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    num_stations_added = row['num_of_new_stations_added_here'].iloc[0]
    return num_stations_added

# retrieve resale price of any flat based on postal code input 
def get_resale_price(int_postal):
    postal = str(int_postal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    resale_price = row['resale_price'].iloc[0]
    return resale_price