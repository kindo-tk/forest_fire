import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize Flask application
application = Flask(__name__)
app = application

# Load models and scalers
try:
    with open('models/ridge.pkl', 'rb') as model_file:
        ridge_model = pickle.load(model_file)
    with open('models/scaler.pkl', 'rb') as scaler_file:
        standard_scaler = pickle.load(scaler_file)
except Exception as e:
    raise

# Route for home page and prediction
@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Extract form data
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Scale the input data
            new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

            # Make prediction
            result = ridge_model.predict(new_data_scaled)

            return render_template('index.html', result=result[0])
        except Exception as e:
            return render_template('index.html', result="Error: Unable to make prediction.")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
