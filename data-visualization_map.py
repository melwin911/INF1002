import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from folium import IFrame

# Read the CSV file
# df = pd.read_csv("sorted_output.csv")

# View the first 5 rows
# print(df.head())

# check for null values
# print(df.isnull().sum())

# Bar graph showing count of 'town'
# sns.countplot(x='town', data = df)
# plt.title('Count of Town')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_type'
# sns.countplot(x='flat_type', data = df)
# plt.title('Count of Flat Type')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_model'
# sns.countplot(x='flat_model', data = df)
# plt.title('Count of Flat Model')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'storey_range'
# sns.countplot(x='storey_range', data = df)
# plt.title('Count of Storey Range')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'year'
# sns.countplot(x=df['year'], data = df)
# plt.title('Count of Year')
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'street_name'
# requires one hot encoding to categorize streets
# sns.countplot(x='street_name', data = df)
# plt.title('Count of Street Name')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'storey_range'
# sns.countplot(x='storey_range', data = df)
# plt.title('Count of Storey Range')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'floor_area_sqm'
# sns.countplot(x='floor_area_sqm', data = df)
# plt.title('Count of Floor Area Sqm')
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'lease_commence_date'
# sns.countplot(x='lease_commence_date', data = df)
# plt.title('Count of Lease Commence Date')
# plt.xticks(rotation=90)
# plt.show()

# running slow, requires optimization (sub-categorize resale price)
# Bar graph showing count of 'resale_price'
# sns.countplot(x='resale_price', data = df)
# plt.title('Count of Resale Price')
# plt.xticks(rotation=90)
# plt.show()

# running slow, requires optimization (sub-categorize year and resale price)
# Scatter Plot showing y = 'resale_price', x = 'year' 

# x_axis = df['year']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price over years')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing y = 'resale_price 'x = 'lease_commence_date', 

# x_axis = df['lease_commence_date']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and lease commencement date')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing y = 'resale_price 'x = 'flat_type', 

# x_axis = df['flat_type']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and flat type')
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.ylabel('Resale Price')

# # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# Scatter Plot showing x = 'resale_price 'x = 'floor_area_sqm', 

# x_axis = df['floor_area_sqm']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price and floor area sqm')
# plt.xlabel('Floor Area Sqm')
# plt.ylabel('Resale Price')

# # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

df = pd.read_csv("2012_onwards_sorted_output.csv")

# merging the block and street name column in csv file to 'address' for geolocator to work
df['address'] = df['block'].map(str) + ',' + df['street_name'].map(str) + ', Singapore'

# created a variable towns to store all the 26 unique towns names and created lat long as empty array
towns = [x for x in df['town'].unique().tolist() if type(x) == str]
latitude = []
longitude = []

# this just find the location of the towns
geolocator = Nominatim(user_agent="ny_explorer")

# this for loop will find each town's lat long and store them in the arrays
for town in towns:
    try:
        loc = geolocator.geocode(town + ', Singapore')
        if loc:
            latitude.append(loc.latitude)
            longitude.append(loc.longitude)
            #print('Geographical coordinates for {}: {}, {}'.format(town, loc.latitude, loc.longitude))
        else:
            latitude.append(np.nan)
            longitude.append(np.nan)
            print('Geographical coordinates for {} not found.'.format(town))
    except Exception as e:
        print('Error geocoding {}: {}'.format(town, str(e)))
        latitude.append(np.nan)
        longitude.append(np.nan)

# created a DataFrame to work for the map with markers
df2 = pd.DataFrame({'town': towns, 'latitude': latitude, 'longitude': longitude})

# created a DataFrame to work for the heatmap - resale prices of each town are aggregated
resale_price_data = pd.DataFrame({
    'town':['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH',
            'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG',
            'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'],
    'resale_price': [473870.284, 473900.502, 473949.592, 473940.662, 474010.543, 473973.073, 473978.389, 473994.141,
                     474027.733, 474043.643, 474084.002, 474094.283, 474120.195, 474170.685, 474180.104, 474188.309,
                     474220.112, 474215.923, 474235.162, 474267.183, 474267.895, 474294.323, 474318.580, 474338.803,
                     474404.5732]
})

# this drops any towns with NA values for lat and long - "CENTRAL AREA" so the code won't break
df2 = df2.dropna(subset=['latitude', 'longitude'])

# merged the previous dataframe with town, lat, long with resale price for heatmap data
merged_data = df2.merge(resale_price_data, on='town', how='left')

# this section creates the map with markers and print it to test_map1
test_map = folium.Map(location=[1.3521, 103.8198], zoom_start=13)
marker_cluster = MarkerCluster().add_to(test_map)

for index, row in df2.iterrows():
    popup_info = f"<strong>{row['town']}</strong><br>Lat: {row['latitude']},Lon: {row['longitude']}",
    tooltip_info = f"Click for more info about {row['town']}",
    folium.Marker(
        location=(row['latitude'], row['longitude']),
        popup=popup_info,
        icon=folium.Icon(color='blue',icon='info-sign'),
        tooltip=tooltip_info,
    ).add_to(marker_cluster)

test_map.save("test_map1.html")
print("test_map created")


heat_data = merged_data[['latitude', 'longitude', 'resale_price']]

# this is to normalise the prices of each towns to display them as a spectrum
min_price = heat_data['resale_price'].min()
max_price = heat_data['resale_price'].max()
print(min_price)
print(max_price)
heat_data['normalized_price'] = (heat_data['resale_price'] - min_price) / (max_price - min_price)

# to create the colour gradient for the spectrum
gradient = {0.0: '#00008b', 0.5: '#008000', 1.0: '#8b0000'}

# this section creates the heatmap and print it out
heatmap_map = folium.Map(location=[1.3521, 103.8198], zoom_start=12)
heat_data_list = heat_data[['latitude', 'longitude', 'normalized_price']].values.tolist()
HeatMap(heat_data_list,
        radius=20,
        blur=25,
        gradient=gradient,
        max_opacity=0.8,
        scale_radius=True,
        overlay=True,
        control=True,
        show=True).add_to(heatmap_map)

# to create the colour gradient legend for the heatmap
legend_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 300px; background-color: rgba(255, 255, 255, 0.5);
     z-index:9999; font-size:14px; border-radius: 5px; padding: 10px;">
     <p><strong>Resale Price per sqm in thousands</strong></p>
     <div style="background: linear-gradient(to right, #00008b, #008000, #8b0000); height: 10px;"></div>
     <p style="margin-top: 5px;">Low: 4,738 | Medium: 4,741 | High: 4,744</p>
     </div>
     '''

# add the legend to the map
heatmap_map.get_root().html.add_child(folium.Element(legend_html))

heatmap_map.save("heatmap_map.html")
print("Heatmap map created")

# running slow, requires optimization (sub-categorize year and resale price)
# Scatter Plot showing y = 'resale_price', x = 'year' 

# x_axis = df['year']

# y_axis = df['resale_price']
# plt.scatter(x_axis, y_axis)

# plt.title('Resale Price over years')
# plt.xlabel('Year')
# plt.ylabel('Resale Price')

# # # # remove scientific notation
# plt.ticklabel_format(style='plain', axis='y')
# plt.show()

# print(df['town'].unique())
# print(len(df['town'].unique()))

# One Hot Encoding produces +26 columns. High dimensionality not suitable for ML.
# ohe_town = pd.get_dummies(df["town"]).astype(int)

# df = pd.concat([df, ohe_town], axis="columns")

# print(df)

# ohe_df = 'ohe_df.csv'

# df.to_csv(ohe_df, index=False)

# print('Merged CSV file saved at:', ohe_df)

# Label encoding does not produce new features unlike OHE, but ML models may misinterpret numbers for hierachy.

# print('Merged CSV file saved at:', le_df)

# labelEncoder = LabelEncoder()
# df["le_town"] = labelEncoder.fit_transform(df["town"])
# le_df = 'le_df.csv'
# df.to_csv(le_df, index=False)'''

# corr_matrix = df1.corr(numeric_only=True)
# k = 7
# cols = corr_matrix.nlargest(k, 'resale_price')['resale_price'].index
# cm = np.corrcoef(df1[cols].values.T)
# sns.set(font_scale=1.25)
# hm = sns.heatmap(cm,  fmt='.2f', annot=True, annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

# plt.show()

