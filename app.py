from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from predict import predictPrice
from getAmenities import*

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# dummy hdb data 
HDBs = []

Amenities = []


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


@app.route('/amenities', methods=['GET', 'POST'])
def all_amenities():

    response_object = {'status': 'success'}

    if request.method == 'POST':

        post_data = request.get_json()
        postal_code = post_data.get('postal')

        """Append values from datafile selected by postal code input to a dictionary in Amenities[]. 
        Values are gotten from passing the postal code input to its relevant getter function, from the getter function file, getAmenities.py. 
        Placeholders are used for the values which will not be displayed on the frontend Accordion.vue page.
        """

        Amenities.append({

            'town': 'TownPlaceholder',

            'flat':  getFlat(int(postal_code)),

            'postal': postal_code,

            'park': getPark(int(postal_code)),

            'park_dist': getParkDist(int(postal_code)),

            'num_park_2km': 'NumParkPlaceholder',

            'mall': getMall(int(postal_code)),

            'mall_dist': getMallDist(int(postal_code)),

            'num_mall_2km': 'NumMallPlaceholder',
            
            'top_school': getTopSchool(int(postal_code)),
            
            'top_school_dist': getTopSchoolDist(int(postal_code)),

            'num_top_school_2km': 'NumTopSchoolPlaceholder',

            'hawker': getHawker(int(postal_code)),

            'hawker_dist': getHawkerDist(int(postal_code)),

            'num_hawker_2km': 'NumHawkerPlaceholder',

            'station_name': getStationName(int(postal_code)),

            'station_dist': getStationDist(int(postal_code)),

            'num_station_2km': 'NumStationPlaceholder',

            'station_name_2027_onwards': getUpcomingStationName(int(postal_code)),

            'station_dist_2027_onwards': getUpcomingStationDist(int(postal_code)),

            'num_station_2km_2027_onwards': 'NumUpcomingStationPlaceholder',

            'num_of_new_stations_added_here': 'NumStationsAddedPlaceholder',

            'resale_price': 'ResalePricePlaceholder',
        })

        # Call the function to get latitude and longitude

        response_object['message'] = 'Amenities Displayed!'
    else:

        response_object['amenities'] = Amenities

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
                                                lease_commence_date=post_data.get('lease_commence_date')*1.01))
            # To return from model
        })

        response_object['message'] = 'Priced!'

    else:

        response_object['hdbs'] = HDBs

    return jsonify(response_object)


# Heat Map Route
@app.route('/map', methods=['GET'])
def map():

    return render_template('heatmap_map.html')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()