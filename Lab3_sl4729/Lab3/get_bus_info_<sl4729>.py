from __future__ import print_function
import json
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib
import os
import sys

import pandas as pd

apikey = sys.argv[1]  #"b40ed1fc-a440-430c-995c-ed98906d8d52"
bus_line= sys.argv[2] #'M10'
file_name = sys.argv[3]


#bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey +'&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

print (bus_url)
response = urllib.urlopen(bus_url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)


VehicleActivity = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]

VehicleActivity = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]
numbers = len(VehicleActivity)

la= []
lo= []
sn= []
ss= []

count = 0
for vehicle in VehicleActivity:
	Location = VehicleActivity[count]['MonitoredVehicleJourney']['VehicleLocation']
	latitude = Location['Latitude']
	longitude = Location['Longitude']
	StopStatus = VehicleActivity[0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['Extensions']['Distances']['PresentableDistance']
	StopName = VehicleActivity[0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['StopPointName']
	la.append(latitude)
	lo.append(longitude)
	sn.append(StopName)
	ss.append(StopStatus)

	print(latitude)
	print(longitude)
	print(StopName)
	print(StopStatus)
	count += 1
d = {'latitude':la, 'longitude':lo, 'Stop Name': sn, 'Stop Status':ss}
dt = pd.dataFrame(d) 

# dt.to_csv('/Users/songjianli/Downloads/PUI2018/PUI2018_sl4729/Lab3_sl4729/Lab3/output.csv')

# you need to change the path when you are running it on a different laptop
path = '/Users/songjianli/Downloads/PUI2018/PUI2018_sl4729/Lab3_sl4729/Lab3/'

dt.to_csv(path+file_name)

