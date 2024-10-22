import warnings
warnings.simplefilter('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap

df = pd.read_csv("csv_files/resale_price_data.csv")

df['address'] = df['block'].map(str) + ',' + df['street_name'].map(str) + ', Singapore'

towns = [x for x in df['town'].unique().tolist() if type(x) == str]
latitude = []
longitude = []
geolocator = Nominatim(user_agent="ny_explorer")

for town in towns:
    try:
        loc = geolocator.geocode(town + ', Singapore')
        if loc:
            latitude.append(loc.latitude)
            longitude.append(loc.longitude)
        else:
            latitude.append(np.nan)
            longitude.append(np.nan)
            print('Geographical coordinates for {} not found.'.format(town))
    except Exception as e:
        print('Error geocoding {}: {}'.format(town, str(e)))
        latitude.append(np.nan)
        longitude.append(np.nan)

df2 = pd.DataFrame({'town': towns, 'latitude': latitude, 'longitude': longitude})

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

dataframe = df.merge(df2, on='town', how='left')

df2 = df2.dropna(subset=['latitude', 'longitude'])
merged_data = df2.merge(resale_price_data, on='town', how='left')

heat_data = merged_data[['latitude', 'longitude', 'resale_price']]

min_price = heat_data['resale_price'].min()
max_price = heat_data['resale_price'].max()
print(min_price)
print(max_price)
heat_data['normalized_price'] = (heat_data['resale_price'] - min_price) / (max_price - min_price)

gradient = {0.0: '#00008b', 0.5: '#008000', 1.0: '#8b0000'}

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

legend_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 300px; background-color: rgba(255, 255, 255, 0.5);
     z-index:9999; font-size:14px; border-radius: 5px; padding: 10px;">
     <p><strong>Resale Price per sqm in thousands</strong></p>
     <div style="background: linear-gradient(to right, #00008b, #008000, #8b0000); height: 10px;"></div>
     <p style="margin-top: 5px;">Low: 4,738 | Medium: 4,741 | High: 4,744</p>
     </div>
     '''
toggle_heatmap_js = """
function toggleHeatmap() {
    var heatmapLayer = heatmap_map.getLayers()[0];
    heatmapLayer.options.show = !heatmapLayer.options.show;
    if (heatmapLayer.options.show) {
        heatmapLayer.addTo(heatmap_map);
    } else {
        heatmapLayer.removeFrom(heatmap_map);
    }
}
"""

heatmap_map.save("heatmap_map.html")
print("Heatmap map created")

# Histogram plot showing count of 'town'
sns.histplot(x='town', data = df)
plt.title('Count of Towns')
plt.xticks(rotation=90)
plt.show()

# Line graph showing y='resale_price', x='year' 
plt.figure(figsize=(14,5))
sns.set_style("ticks")
sns.lineplot(data=df,x="year",y='resale_price',color='firebrick')
plt.xlabel('Year')
plt.ylabel('Resale Price')
sns.despine()
plt.title("Resale price over time",size='x-large')
plt.show()

# Scatter Plot showing y = 'resale_price', x = 'floor_area_sqm' 
sns.scatterplot(data=df, x="floor_area_sqm", y="resale_price")
plt.title('Resale Price and floor area sqm')
plt.xlabel('floor area sqm')
plt.ylabel('Resale Price')
# remove scientific notation
plt.ticklabel_format(style='plain', axis='y')
plt.show()