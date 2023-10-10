import pandas as pd 
 
df = pd.read_csv('final_sorted.csv') 
#user input 
#postal = input("type postal here :") 
 
#data = df.loc[df['postal'] == 760868]
 
"""def get_amenities(): 
    amenities = [] 
    for col in data.columns: 
        amenities.append(data[col].tolist()) 
    myIndices = [3,4,6,7,9,10,12,13,15,16,18,19] 
    flattened = [val for sublist in amenities for val in sublist] 
    flattened = [flattened[i] for i in myIndices] 
    grouped_list = [flattened[i:i+2] for i in range(0, len(flattened), 2)] 
    return [{"amenity": item[0], "distance": item[1] * 1000} for item in grouped_list]

park = get_amenities()
print(park)"""


#getFlat
def getFlat(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['flat'].iloc[0]
    return park_value

#getPark
def getPark(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['park'].iloc[0]
    return park_value

#getParkDist
def getParkDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['park_dist'].iloc[0]
    return park_value

#getMall
def getMall(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['mall'].iloc[0]
    return park_value

#getMallDist
def getMallDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['mall_dist'].iloc[0]
    return park_value

#getTopSchool
def getTopSchool(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['top_school'].iloc[0]
    return park_value

#getTopSchoolDistance
def getTopSchoolDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['top_school_dist'].iloc[0]
    return park_value

#getHawker
def getHawker(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['hawker'].iloc[0]
    return park_value

#getHawkerDist
def getHawkerDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['hawker_dist'].iloc[0]
    return park_value

#getStationName
def getStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['station_name'].iloc[0]
    return park_value

#getStationDist
def getStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['station_dist'].iloc[0]
    return park_value

#getUpcomingStationName
def getUpcomingStationName(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['station_name_2027_onwards'].iloc[0]
    return park_value

#getUpcomingStationDist
def getUpcomingStationDist(intPostal):
    postal = str(intPostal)
    row = df.loc[df['postal'] == postal]
    if row.empty:
        return "Postal code not found"
    park_value = row['station_dist_2027_onwards'].iloc[0]
    return park_value