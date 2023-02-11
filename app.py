from flask import Flask, jsonify, request
from keras.models import load_model
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)

model = load_model('model.h5')

@app.route("/")
def hello():
    return "<h1>Hello world</h1>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame.from_records(data)
    
    # df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(x//1000))
    df.sort_values(by='time', inplace=True)
    
    df['energy'] = df[['global energy', 'diffusive energy']].mean(axis=1)
    df.drop(columns=['global energy', 'diffusive energy'], inplace=True)
    df = df.interpolate(method='linear')

    scaler = joblib.load('scaler.save')
    stevilski = ['mean T', 'min T', 'max T', 'mean rel. hum.', 'min rel. hum.', 'max rel. hum.', 'T', 'rel. hum.', 'wind speed', 'wind direction', 'max gust', 'energy']
    df[stevilski] = scaler.transform(df[stevilski])

    xtest = df.drop(['precipitation','time'], axis=1)

    lookback = 24*6

    temparray = []
    for i in range (len(xtest)-lookback-1):
        a = xtest.iloc[i:(i+lookback)]
        temparray.append(a.to_numpy())
    xtest = np.array(temparray)

    predictions = model.predict(xtest)
    predictions = predictions[0].tolist()
    prediction = predictions[0]
    rounded_prediction = round(prediction, 2)
    return {'prediction': rounded_prediction}

if __name__ == '__main__':
    app.run(debug=True)

# py -m flask --app app run