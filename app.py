# 1. import Dependencies
from flask import Flask,jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,inspect

import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

#Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite",connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# last 12 months variable
last_twelve_months = '2016-08-23'


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    print(latest_date)
    return (
        f"Welcome to the Hawaii weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        
    )

#Last 12 months ago
prec_result = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= last_twelve_months).order_by(Measurement.date).all()

#Precipitation :Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitaton_data = []
    for prc_data in prec_result:
        prec_dict = {}
        prec_dict['Date']= prc_data.date
        prec_dict['Precipitation'] = prc_data.prcp
        precipitaton_data.append(prec_dict)

    return jsonify(precipitaton_data)


#Query all stations 
sta_result = session.query(Station.name,Station.station,Station.latitude,Station.longitude,Station.elevation).all()

#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station_list = []
    sta_dict = {}
    for stats in sta_result:
      sta_dict['Station'] = stats.station
      sta_dict['Name'] = stats.name
      sta_dict['Latitude'] = stats.latitude
      sta_dict['Longitude'] = stats.longitude
      sta_dict['Elevation'] = stats.elevation
      station_list.append(sta_dict)


    return jsonify(station_list )






if __name__ == "__main__":
    app.run(debug=True)
