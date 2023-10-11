from flask import Flask, jsonify, request, render_template, render_template_string, redirect, url_for
from flask_cors import CORS
import requests
from predict import predictPrice

import pandas as pd 
import csv
import json
from getAmenities import*

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# dummy hdb data 
HDBs = []

Ammenities = []


@app.route('/town', methods=['GET'])
def town():
    df = pd.read_csv("2012_onwards_sorted_output.csv")

    data = df.to_dict(orient='records')
    town_column = df["town"].tolist()

    return jsonify(town_column)

@app.route('/resale', methods=['GET'])
def resale_by_town():
    selected_town = request.args.get('town')
    df = pd.read_csv("2012_onwards_sorted_output.csv")

    filtered_data = df[df['town'] == selected_town]

    # data = df.to_dict(orient='records')
    # resaleprice_column = df["resale_price"].tolist()
    # year_column = df["year"].tolist()
    
    # Group by year and calculate the average resale price
    aggregated_data = filtered_data.groupby('year')['resale_price'].mean().reset_index()

    # Convert the aggregated data to a list of dictionaries
    aggregated_data_list = aggregated_data.to_dict(orient='records')

    return jsonify(aggregated_data_list)

    # return jsonify(variable1=resaleprice_column, variable2=year_column)


global_postal_code = None



def get_latlng_from_postal_code(postal_code):
    google_maps_api_key = 'AIzaSyC6v4STqhDYCRcc9afAiHh3RglCTCPNjbU'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={postal_code}&key={google_maps_api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK' and len(data['results']) > 0:
            location = data['results'][0]['geometry']['location']
            print(location)
            return {'lat': location['lat'], 'lng': location['lng']}
        else:
            print('Geocoding API request failed.')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error in Geocoding API request: {e}')
        return None


@app.route('/ammenities', methods=['GET', 'POST'])
def all_ammenities():

    global global_postal_code
    response_object = {'status': 'success'}
    postal_code = None
    latitude = None
    longitude = None

    if request.method == 'POST':

        post_data = request.get_json()
        postal_code = post_data.get('postal')

        """df = pd.read_csv('Data/final_sorted.csv')
        data = df.loc[df['postal'] == post_data.get('postal')]
        def get_amenities(): 
            amenities = [] 
            for col in data.columns: 
                amenities.append(data[col].tolist()) 
            myIndices = [3,4,6,7,9,10,12,13,15,16,18,19] 
            flattened = [val for sublist in amenities for val in sublist] 
            flattened = [flattened[i] for i in myIndices] 
            grouped_list = [flattened[i:i+2] for i in range(0, len(flattened), 2)] 
            return [{"amenity": item[0], "distance": item[1] * 1000} for item in grouped_list]"""


        Ammenities.append({

            'town': 'TownPlaceholder',

            'flat':  getFlat(int(post_data.get('postal'))),

            'postal': post_data.get('postal'),

            'park': getPark(int(post_data.get('postal'))),

            'park_dist': getParkDist(int(post_data.get('postal'))),

            'num_park_2km': 'TownPlaceholder',

            'mall': getMall(int(post_data.get('postal'))),

            'mall_dist': getMallDist(int(post_data.get('postal'))),

            'num_mall_2km': 'TownPlaceholder',
            
            'top_school': getTopSchool(int(post_data.get('postal'))),
            
            'top_school_dist': getTopSchoolDist(int(post_data.get('postal'))),

            'num_top_school_2km': 'TownPlaceholder',

            'hawker': getHawker(int(post_data.get('postal'))),

            'hawker_dist': getHawkerDist(int(post_data.get('postal'))),

            'num_hawker_2km': 'TownPlaceholder',

            'station_name': getStationName(int(post_data.get('postal'))),

            'station_dist': getStationDist(int(post_data.get('postal'))),

            'num_station_2km': 'TownPlaceholder',

            'station_name_2027_onwards': getUpcomingStationName(int(post_data.get('postal'))),

            'station_dist_2027_onwards': getUpcomingStationDist(int(post_data.get('postal'))),

            'num_station_2km_2027_onwards': 'TownPlaceholder',

            'num_of_new_stations_added_here': 'TownPlaceholder',

            'resale_price': 'TownPlaceholder',

        })

        # Call the function to get latitude and longitude

        latlng_data = get_latlng_from_postal_code(postal_code)
        print(latlng_data)

        if latlng_data:
            latitude = latlng_data['lat']
            longitude = latlng_data['lng']

            # Redirect to the map route with latitude and longitude as parameters
            return redirect(url_for('map', latitude=latitude, longitude=longitude))

        response_object['message'] = 'Priced!'
    else:
        response_object['latitude'] = latitude
        response_object['longitude'] = longitude
        response_object['Ammenities'] = Ammenities

    return jsonify(response_object)

@app.route('/hdbs', methods=['GET', 'POST'])
def all_hdbs():

    response_object = {'status': 'success'}

    if request.method == 'POST':

        post_data = request.get_json()
        
        HDBs.append({

            'town': post_data.get('town'),

            'flat_type': post_data.get('flat_type'),

            'storey_range': post_data.get('storey_range'),

            'floor_area_sqm': post_data.get('floor_area_sqm'),

            'lease_commence_date': post_data.get('lease_commence_date'),

            # 'resale_price': "test",

            'resale_price': round(predictPrice( town=post_data.get('town'),
                                                flat_type=post_data.get('flat_type'),
                                                storey_range=post_data.get('storey_range'),
                                                floor_area_sqm=post_data.get('floor_area_sqm'),
                                                lease_commence_date=post_data.get('lease_commence_date'))*1.01),
            # To return from model
        })

        response_object['message'] = 'Priced!'

    else:

        response_object['hdbs'] = HDBs

    return jsonify(response_object)


# Heat Map Route
@app.route('/map', methods=['GET'])
def map():
    latitude = float(request.args.get('latitude', 1.3521))  # Default latitude if not provided
    longitude = float(request.args.get('longitude', 103.8198))  # Default longitude if not provided

    return render_template('map.html', latitude=latitude, longitude=longitude)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()