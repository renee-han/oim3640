import requests
import os
from dotenv import load_dotenv
load_dotenv() #goes into env file and loads the API key and the variable its assigned to into Python memory
MAPBOX_KEY = os.getenv("MAPBOX_KEY")
MBTA_KEY = os.getenv("MBTA_KEY")


#API Pipeline Dev

#Function for taking location name and returning long/lat 
#How it all works: When I request from MapBox, I'm saying here's the location name w/ my API key. That request hits their servers i.e. computers+datbase w/ all this info and they verify my API key, takes in that location name, recognizes it bcz they already have associated location names and coordinates in their system+external data they used 

def long_lat(place_name):
    url = "https://api.mapbox.com/search/searchbox/v1/forward"
    params = {"q": place_name, "access_token": MAPBOX_KEY, "limit": 1}
    response = requests.get(url, params = params) #sends request to MapBox for data 
    data = response.json()#converts data into dict/JSON form 
    print(data) #this is a list of dicts
    lng, lat = data["features"][0]["geometry"]["coordinates"] #tuple = unpacking/packing: assigning the first value to lng and second to lat
    return lat, lng
print(long_lat("Newbury Street"))

#data is a dictionary bcz you converted it into JSON
#'features': [{'type': 'Feature', 'geometry': {'coordinates': [-71.0795, 42.349516]
#features is a key and its value is that entire list 
#data[features] gets back the list
#data["features"][0] is getting the first value in the list which is {'type': 'Feature', 'geometry': {'coordinates': [-71.0795, 42.349516]
#data["features"][0]["geometry"] is getting {'coordinates': [-71.0795, 42.349516]
#data["features"][0]["geometry"]["coordinates"] getting [-71.0795, 42.349516]


#Second Function (MBTA + Wheelchair)
def mbta_stop(lat, lng):
    url = "https://api-v3.mbta.com/stops"
    params = {"api_key": MBTA_KEY, "filter[latitude]": lat,"filter[longitude]": lng, "sort": "distance",
    "page[limit]": 1} #filter[lat] and filter[long] are defined by MBTA, NOT PYTHON = this is a rule/condition you set i.e. here are my coordinates and based on them, get the closest station
    #sort distance is getting the closest stop and limiting to 1 result
    response = requests.get(url, params = params)  
    data = response.json()
    stop = data["data"][0]["attributes"]
    name = stop["name"]
    wheelchair = stop["wheelchair_boarding"] == 1
    return name, wheelchair
print(mbta_stop(42.349516, -71.0795))
    
