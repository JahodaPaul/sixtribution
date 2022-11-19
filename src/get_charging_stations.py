
import requests
import json
overpass_url = "http://overpass-api.de/api/interpreter"

# area["ISO3166-1"="DE"][admin_level=2];

overpass_query = """
[out:json];
area["name:en"="Munich"][admin_level=6];
(node["amenity"="charging_station"](area);
 way["amenity"="charging_station"](area);
 rel["amenity"="charging_station"](area);
);
out center;
"""
response = requests.get(overpass_url, 
                        params={'data': overpass_query})
print('test')
data = response.json()

import numpy as np
import matplotlib.pyplot as plt# Collect coords into list
coords = []
capacities = []
nodes = []

class Node():
  def __init__(self, lon, lat, capacity, station_id):
    self.lon = lon
    self.lat = lat
    self.capacity = capacity
    self.station_id = station_id 

for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    station_id = element['id']
    if 'capacity' in element['tags'].keys():
      capacity = element['tags']['capacity']
    else:
      capacity = 1
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    station_id = element['center']['id']
    capacity = element['center']['capacity']
    coords.append((lon, lat))# Convert coordinates into numpy array
  n = Node(lon,lat,int(capacity),int(station_id))
  capacities.append(int(capacity))
  nodes.append(n)
  
X = np.array(coords)

 

print(len(X[:, 0]),len(capacities))
plt.plot(X[:, 0], X[:, 1],'o')
plt.title('Charging stations in Munich')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()

# written in csv format id, lat, lon, capacity
with open('stations.txt', 'w') as f:
  for item in nodes:
    result = str(item.station_id)+','+str(item.lat)+','+','+str(item.lon)+','+str(item.capacity)+'\n'
    f.write(result)
