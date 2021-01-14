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


#Precipitation :Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Last 12 months ago
    prec_result = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= last_twelve_months).order_by(Measurement.date).all()
    return jsonify(prec_result)



#Precipitation :Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/stations")
def stations():
    sta_result = session.query(Station.name,Station.station).all()
    return jsonify(sta_result)






if __name__ == "__main__":
    app.run(debug=True)
