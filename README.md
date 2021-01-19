# Surf Up


![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/surfs-up.png "Daily Normals")
## Background
This is a deatiled analysis of holiday vacation in Honolulu, Hawaii! To help with this trip planning, some climate analysis on the area were done done prior to the trip.

### Precipitation Analysis
This process involves finding the most recent date in the data setand then using this date to retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. The date and prcp values were used to plot the below graph

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_1.png "Precipitation")

### Station Analysis
A query was designed to calculate the total number of stations in the dataset and find the most active stations.Using the most active station id, calculate the lowest, highest, and average temperature. A query was designed to retrieve the last 12 months of temperature observation data (TOBS), and then filtered by the station with the highest number of observation. The last 12 months of temperature observation data for this station were ploted in the histogram below.

### Climate App
A Flask API based on the queries from the climate notebook.
Available Routes:
Return the JSON representation for precipitation data. * /api/v1.0/precipitationReturn a JSON list of stations from the dataset.
Return a JSON list of stations from the dataset.* /api/v1.0/stations
Return a JSON list of stations from the dataset.
* /api/v1.0/tobs
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date.
* /api/v1.0/<start>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end date range.
* /api/v1.0/<start>/<end>

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_2.png "Temp obs")

### Temperature Analysis I
A range of dates were selected for the a potential trip from August first to August seventh of this year to check what previous year temperatures were for those matching dates. The historical data in the dataset was used to find what the the temperature has previously looked like.In the temperature analysis notebook a function called calc_temps that accepts a start date and end date in the format %Y-%m-%d returned the minimum, average, and maximum temperatures for the range of dates selected.

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_3.png "Avg Temp")

### Temperature Analysis II
 In the CLIMATEnotebook a function called daily_normals that accepts a day and moth in the format %m-%d returned the minimum, average, and maximum precipitation for the range of dates selected.
 
![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_4.png "Daily Normals")
