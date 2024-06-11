from flask import Flask, request, render_template, redirect, url_for
import pyttsx3
from pathlib import Path
import pickle
import numpy as np

app = Flask(__name__)

def predict_price(under_construction, rera, bhk_no, bhk_or_rk, square_ft, resale, longitude, latitude, posted_by):
    
    under_construction = under_construction.lower()
    valid_inputs_for_under_construction = ['yes', 'no']
    if under_construction not in valid_inputs_for_under_construction:
        print("invalid input for under_construction: please insert either 'yes' or 'no' ")
        return 
    else:
        if under_construction == 'yes':
            under_construction = 1
        else: 
            under_construction = 0

    rera = rera.lower()
    valid_inputs_for_rera = ['yes', 'no']
    if rera not in valid_inputs_for_rera:
        print("invalid input for rera: please insert either 'yes' or 'no' ")
        return 
    else:
        if rera == 'yes':
            rera = 1
        else: 
            rera = 0

    try:
        bhk_no = int(bhk_no)
    except ValueError:
        return "Please insert an integer value for BHK_NO between 1 and 6."

    if not (1 <= bhk_no <= 6):
        return "Please insert an integer value for BHK_NO between 1 and 6."

    bhk_or_rk = bhk_or_rk.lower()
    valid_inputs_for_bhk_or_rk = ['bhk', 'rk']
    if bhk_or_rk not in valid_inputs_for_bhk_or_rk:
        print("invalid input for bhk_or_rk: please insert either 'bhk' or 'rk' ")
        return
    else:
        if bhk_or_rk == 'bhk':
            bhk_or_rk = 1
        else: 
            bhk_or_rk = 0

    resale = resale.lower()
    valid_inputs_for_resale = ['yes', 'no']
    if resale not in valid_inputs_for_resale:
        print("invalid input for resale: please insert either 'yes' or 'no' ")
        return
    else:
        if resale == 'yes':
            resale = 1
        else: 
            resale = 0

    posted_by = posted_by.lower()
    valid_inputs_for_posted_by = ['builder', 'owner', 'dealer']
    if posted_by not in valid_inputs_for_posted_by:
        print("invalid input for posted by: please insert 'builder' or 'owner' or 'dealer' ")
        return

    try:
        longitude = float(longitude)
        latitude = float(latitude)
        square_ft = float(square_ft)
    except ValueError:
        return "Please ensure area, longitude, and latitude are numeric."

    if not ((68 < longitude < 97) and (8 < latitude < 37)):
        print("please insert co-ordinate which is in India")
        return

    pyttsx3.speak('successfully entered the data')
    if posted_by == 'builder':
        array = [under_construction, rera, bhk_no, bhk_or_rk, square_ft, resale, latitude, longitude, 1, 0]
    elif posted_by == 'dealer':
        array = [under_construction, rera, bhk_no, bhk_or_rk, square_ft, resale, latitude, longitude, 0, 1]
    else:
        array = [under_construction, rera, bhk_no, bhk_or_rk, square_ft, resale, latitude, longitude, 0, 0]

    # load the MinMaxScaler
    file_name = Path.cwd() / 'minmaxscaler' / 'MinMaxScaler.pkl'
    minmax = pickle.load(open(file_name, 'rb'))

    # convert 1D array to 2D array (model requirement)
    array = np.expand_dims(array, axis = 0)

    # transform 2D array using MinMaxScaler
    transformed_array = minmax.transform(array)

    # load the model
    model_name = 'stacked_model'
    model_path = Path.cwd() / 'saved_model' / f"{model_name}.h5"
    model = pickle.load(open(model_path,'rb'))

    # predict the price
    predicted_price = model.predict(transformed_array)[0]
    pyttsx3.speak(f"The predicte price is {round(predicted_price,3)} lacs")
    return predicted_price


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
     # Set default values
    default_values = {
        'latitude': 19.08,
        'longitude': 72.88,
        "area": 1000,
        "bhk_number": 3
        # Add more default values here if needed
    }
    if request.method == 'POST':
        under_construction = request.form.get('under_construction')
        rera = request.form.get('rera')
        bhk_no = request.form.get('bhk_number')
        bhk_or_rk = request.form.get('bhk_or_rk')
        area = request.form.get('area')
        resale = request.form.get('resale')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        posted_by = request.form.get('posted_by')

        result = predict_price(under_construction, rera, bhk_no, bhk_or_rk, area, resale, longitude, latitude, posted_by)
        # Redirect to the 'price' URL with the result
        return redirect(url_for('price', result=result))
    
    return render_template('index.html', defaults=default_values)

@app.route('/price')
def price():
    # Get the result from the query parameters
    result = request.args.get('result')
    return render_template('price.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)