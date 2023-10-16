import pandas as pd 

# read the amenities csv file
df = pd.read_csv('csv_files/amenities.csv')

# retrieve town values from postal code input
def getTown(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    town = row['town'].iloc[0]
    return town

# retrieve block and flat values from postal code input
def getFlat(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    flat = row['flat'].iloc[0]
    return flat

# retrieve nearest park from postal code input
def getPark(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    park = row['park'].iloc[0]
    return park

# retrieve nearest park distance from postal code input
def getParkDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    parkDist = row['park_dist'].iloc[0]
    return parkDist

# retrieve how many park within 2km radius from postal code input
def getNumPark(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numPark = row['num_park_2km'].iloc[0]
    return numPark

# retrieve nearest shopping mall from postal code input
def getMall(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mall = row['mall'].iloc[0]
    return mall

# retrieve nearest shopping mall distance from postal code input
def getMallDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mallDist = row['mall_dist'].iloc[0]
    return mallDist

# get how many shopping mall within 2km radius from postal code input
def getNumMall(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numMall = row['num_mall_2km'].iloc[0]
    return numMall

# retrieve any nearest top 50 schools from postal code input
def getTopSchool(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    topSchool = row['top_school'].iloc[0]
    return topSchool

# retrieve distance from any top 50 schools to postal code inputs
def getTopSchoolDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    topSchoolDist = row['top_school_dist'].iloc[0]
    return topSchoolDist

# retrieve how many top 50 schools nearby within 2km radius from postal code input
def getNumTopSchool(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    getNumTopSchool = row['num_top_school_2km'].iloc[0]
    return getNumTopSchool

# retrieve nearest hawker center from postal code input
def getHawker(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawker = row['hawker'].iloc[0]
    return hawker

# retrieve distance from nearest hawker center to postal code input
def getHawkerDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawkerDist = row['hawker_dist'].iloc[0]
    return hawkerDist

# retrieve how many hawker centers are there within 2km radius from postal code input
def getNumHawker(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numHawker = row['num_hawker_2km'].iloc[0]
    return numHawker

# retrieve nearest MRT station from postal code input
def getStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    stationName = row['station_name'].iloc[0]
    return stationName

# retrieve distance from nearest MRT station to postal code input
def getStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    stationDist = row['station_dist'].iloc[0]
    return stationDist

# retrieve number of MRT stations within 2km radius of postal code input
def getNumStation(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numStation = row['num_station_2km'].iloc[0]
    return numStation

# retrieve any upcoming MRT station from postal code input
def getUpcomingStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcomingStationName = row['station_name_2027_onwards'].iloc[0]
    return upcomingStationName

# retrieve distance from any upcoming MRT stations to postal code input
def getUpcomingStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcomingStationDist = row['station_dist_2027_onwards'].iloc[0]
    return upcomingStationDist

# retrieve number of upcoming MRT stations within 2km radius of postal code input
def getNumUpcomingStation(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numUpcomingStation = row['num_station_2km_2027_onwards'].iloc[0]
    return numUpcomingStation

# retrieve number of MRT station added within 2km radius of postal code input
def getNumStationsAdded(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numStationsAdded = row['num_of_new_stations_added_here'].iloc[0]
    return numStationsAdded

# retrieve resale price of any flat based on postal code input 
def getResalePrice(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    resalePrice = row['resale_price'].iloc[0]
    return resalePrice