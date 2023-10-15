import pandas as pd 

"""This is a function file containing the getter for each column of the finalised data.csv file for the Amenities portion of the Accordion.vue.
Each function takes in the postal code input, selects the row which matches the postal code, and retrieves the value of the column name specified.
E.g. getTown retrieves the value of the column name "Town" where the postal code matches the input. Otherwise, it returns an error message.
Note: it does not get the postal code value because the postal code has already been entered by the user."""


df = pd.read_csv('final_sorted.csv') 


# getTown
def getTown(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    town = row['town'].iloc[0]
    return town


# getFlat
def getFlat(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    flat = row['flat'].iloc[0]
    return flat


# getPark
def getPark(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    park = row['park'].iloc[0]
    return park


# getParkDist
def getParkDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    parkDist = row['park_dist'].iloc[0]
    return parkDist


# getNumPark
def getNumPark(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numPark = row['num_park_2km'].iloc[0]
    return numPark


# getMall
def getMall(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mall = row['mall'].iloc[0]
    return mall


# getMallDist
def getMallDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    mallDist = row['mall_dist'].iloc[0]
    return mallDist


# getNumMall
def getNumMall(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numMall = row['num_mall_2km'].iloc[0]
    return numMall


# getTopSchool
def getTopSchool(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    topSchool = row['top_school'].iloc[0]
    return topSchool


# getTopSchoolDistance
def getTopSchoolDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    topSchoolDist = row['top_school_dist'].iloc[0]
    return topSchoolDist


# getNumTopSchool
def getNumTopSchool(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    getNumTopSchool = row['num_top_school_2km'].iloc[0]
    return getNumTopSchool


# getHawker
def getHawker(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawker = row['hawker'].iloc[0]
    return hawker


# getHawkerDist
def getHawkerDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    hawkerDist = row['hawker_dist'].iloc[0]
    return hawkerDist


# getNumHawker
def getNumHawker(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numHawker = row['num_hawker_2km'].iloc[0]
    return numHawker


# getStationName
def getStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    stationName = row['station_name'].iloc[0]
    return stationName


# getStationDist
def getStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    stationDist = row['station_dist'].iloc[0]
    return stationDist


# getNumStation
def getNumStation(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numStation = row['num_station_2km'].iloc[0]
    return numStation


# getUpcomingStationName
def getUpcomingStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcomingStationName = row['station_name_2027_onwards'].iloc[0]
    return upcomingStationName


# getUpcomingStationDist
def getUpcomingStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    upcomingStationDist = row['station_dist_2027_onwards'].iloc[0]
    return upcomingStationDist


# getNumUpcomingStation
def getNumUpcomingStation(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numUpcomingStation = row['num_station_2km_2027_onwards'].iloc[0]
    return numUpcomingStation


# getNumStationsAdded
def getNumStationsAdded(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    numStationsAdded = row['num_of_new_stations_added_here'].iloc[0]
    return numStationsAdded


# getResalePrice
def getResalePrice(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Error: Postal code not found"
    resalePrice = row['resale_price'].iloc[0]
    return resalePrice
