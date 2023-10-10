from flask import Flask, jsonify, request, render_template, render_template_string
from flask_cors import CORS
import pandas as pd 
import csv
import json
from getAmenities import*

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



#HDB data 
with open('final_sorted.csv') as f:
    HDBs = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]



@app.route('/hdbs', methods=['GET', 'POST'])
def all_hdbs():

    response_object = {'status': 'success'}

    if request.method == 'POST':

        post_data = request.get_json()

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


        HDBs.append({

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

        response_object['message'] = 'Priced!'
    else:

        response_object['hdbs'] = HDBs

    return jsonify(response_object)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


#Heat Map Route
@app.route('/map')
def map():
    return render_template('heatmap_map.html')

if __name__ == '__main__':
    app.run()