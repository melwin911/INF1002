from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from machine_learning.machine_learning import predictPrice
from amenities.get_amenities import*

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

HDBs = []

Amenities = []

selected_town = 0


@app.route('/town', methods=['GET'])
def town():
    df = pd.read_csv("csv_files/resale_price_data.csv")

    data = df.to_dict(orient='records')
    town_column = df["town"].tolist()

    return jsonify(town_column)


@app.route('/selectedtown', methods=['GET'])
def selectedt_town():

    return jsonify(selected_town)


@app.route('/resale', methods=['GET'])
def resale_by_town():

    selected_town = (request.args.get('town'))

    df = pd.read_csv("csv_files/resale_price_data.csv")

    filtered_data = df[df['town'] == selected_town]

    aggregated_data = filtered_data.groupby('year')['resale_price'].mean().reset_index()

    aggregated_data_list = aggregated_data.to_dict(orient='records')

    return jsonify(aggregated_data_list)

    # return jsonify(variable1=resaleprice_column, variable2=year_column)


@app.route('/resale_floorarea', methods=['GET'])
def resale_by_floorarea():

    selected_town = (request.args.get('town'))

    df = pd.read_csv("csv_files/resale_price_data.csv")

    filtered_data = df[df['town'] == selected_town]

    aggregated_data = filtered_data.groupby('floor_area_sqm')['resale_price'].mean().reset_index()

    aggregated_data_list = aggregated_data.to_dict(orient='records')

    return jsonify(aggregated_data_list)


@app.route('/amenities', methods=['GET', 'POST'])
def all_amenities():

    response_object = {'status': 'success'}

    if request.method == 'POST':

        post_data = request.get_json()
        postal_code = post_data.get('postal')

        """Append values from datafile selected by postal code input to a dictionary in Amenities[]. 
         Values are gotten from passing the postal code input to its relevant getter function, from the getter function 
         file, getAmenities.py. Placeholders are used for the values which will not be displayed on the frontend 
         Accordion.vue page.
         """

        Amenities.append({

            'town': 'TownPlaceholder',

            'flat':  get_flat(int(postal_code)),

            'postal': postal_code,

            'park': get_park(int(postal_code)),

            'park_dist': get_park_dist(int(postal_code)),

            'num_park_2km': 'NumParkPlaceholder',

            'mall': get_mall(int(postal_code)),

            'mall_dist': get_mall_dist(int(postal_code)),

            'num_mall_2km': 'NumMallPlaceholder',
            
            'top_school': get_top_school(int(postal_code)),
            
            'top_school_dist': get_top_school_dist(int(postal_code)),

            'num_top_school_2km': 'NumTopSchoolPlaceholder',

            'hawker': get_hawker(int(postal_code)),

            'hawker_dist': get_hawker_dist(int(postal_code)),

            'num_hawker_2km': 'NumHawkerPlaceholder',

            'station_name': get_station_name(int(postal_code)),

            'station_dist': get_station_dist(int(postal_code)),

            'num_station_2km': 'NumStationPlaceholder',

            'station_name_2027_onwards': get_upcoming_station_name(int(postal_code)),

            'station_dist_2027_onwards': get_upcoming_station_dist(int(postal_code)),

            'num_station_2km_2027_onwards': 'NumUpcomingStationPlaceholder',

            'num_of_new_stations_added_here': 'NumStationsAddedPlaceholder',

            'resale_price': 'ResalePricePlaceholder',
        })

        response_object['message'] = 'Amenities Displayed!'
    else:

        response_object['amenities'] = Amenities

    return jsonify(response_object)


@app.route('/hdbs', methods=['GET', 'POST'])
def all_hdbs():

    response_object = {'status': 'success'}

    if request.method == 'POST':

        post_data = request.get_json()
        
        if(len(HDBs) == 0):
            HDBs.append({

                'town': post_data.get('town'),

                'flat_type': post_data.get('flat_type'),

                'storey_range': post_data.get('storey_range'),

                'floor_area_sqm': post_data.get('floor_area_sqm'),

                'flat_model': post_data.get('flat_model'),

                'lease_commence_date': post_data.get('lease_commence_date'),

                'resale_price': round(predictPrice( town = post_data.get('town'),
                                                    flat_type = post_data.get('flat_type'),
                                                    storey_range = post_data.get('storey_range'),
                                                    floor_area_sqm = post_data.get('floor_area_sqm'),
                                                    flat_model = post_data.get('flat_model'),
                                                    lease_commence_date = post_data.get('lease_commence_date')*1.01))
                # To return from model
            })

            response_object['message'] = 'Priced!'
        else:
            HDBs[0] = {

                'town': post_data.get('town'),

                'flat_type': post_data.get('flat_type'),

                'storey_range': post_data.get('storey_range'),

                'floor_area_sqm': post_data.get('floor_area_sqm'),

                'flat_model': post_data.get('flat_model'),

                'lease_commence_date': post_data.get('lease_commence_date'),

                'resale_price': round(predictPrice( town = post_data.get('town'),
                                                    flat_type = post_data.get('flat_type'),
                                                    storey_range = post_data.get('storey_range'),
                                                    floor_area_sqm = post_data.get('floor_area_sqm'),
                                                    flat_model = post_data.get('flat_model'),
                                                    lease_commence_date = post_data.get('lease_commence_date')*1.01))
                # To return from model
            }

            response_object['message'] = 'Priced!'

    else:

        response_object['hdbs'] = HDBs

    return jsonify(response_object)


@app.route('/map', methods=['GET'])
def map():

    return render_template('heatmap_map.html')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
