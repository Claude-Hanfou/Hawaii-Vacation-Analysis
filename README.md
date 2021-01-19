# Sqlalchemy-Analysis


![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/surfs-up.png "Daily Normals")
## Background
This is a deatiled analysis of holiday vacation in Honolulu, Hawaii! To help with thisntrip planning, some climate analysis on the area were done done prior to the trip.

### Precipitation Analysis
This process involves finding the most recent date in the data setand then using this date to retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. The date and prcp values were used to plot the below graph

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_1.png "Precipitation")

### Station Analysis
A query was designed to calculate the total number of stations in the dataset and find the most active stations.Using the most active station id, calculate the lowest, highest, and average temperature. A query was designed to retrieve the last 12 months of temperature observation data (TOBS), and then filtered by the station with the highest number of observation. The last 12 months of temperature observation data for this station were ploted in the histogram below.

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_2.png "Temp obs")


![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_3.png "Avg Temp")

![alt text](https://github.com/Claude-Hanfou/Sqlalchemy-Analysis/blob/main/Image/figure_4.png "Daily Normals")
