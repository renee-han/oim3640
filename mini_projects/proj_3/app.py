import requests
import os
from dotenv import load_dotenv
load_dotenv() #goes into env file and loads the API key and the variable its assigned to into Python memory
from flask import Flask, render_template, request
MAPBOX_KEY = os.getenv("MAPBOX_KEY")
MBTA_KEY = os.getenv("MBTA_KEY")


#API Pipeline Dev

#Function for taking location name and returning long/lat 
#How it all works: When I request from MapBox, I'm saying here's the location name w/ my API key. That request hits their servers i.e. computers+datbase w/ all this info and they verify my API key, takes in that location name, recognizes it bcz they already have associated location names and coordinates in their system+external data they used 

def long_lat(place_name):
    url = "https://api.mapbox.com/search/searchbox/v1/forward"
    params = {"q": place_name, "access_token": MAPBOX_KEY, "limit": 1, "proximity": "-71.0589,42.3601", "bbox": "-71.9,42.0,-70.5,42.9"} #Error handling: keeps inputs to the nearby downton Boston region in case someone intputs somewhere not in MA 
    response = requests.get(url, params = params) #sends request to MapBox for data
    response.raise_for_status() #handles api errors 
    data = response.json()#converts data into dict/JSON form 
    if not data["features"]:
        raise ValueError(f"Could not find location: {place_name}")
    print(data) #this is a list of dicts
    lng, lat = data["features"][0]["geometry"]["coordinates"]
     #tuple = unpacking/packing: assigning the first value to lng and second to lat
    return lat, lng


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
    response.raise_for_status() #handles api errors
    data = response.json()
    print(data)
    if not data["data"]:  
        return "No MBTA stops found. Please enter a location in the Boston area!", False #error handling for if someone types an input that's not in MA
    stop = data["data"][0]["attributes"]
    name = stop["name"] #getting you 'name': 'Ring Rd @ Boylston St'
    wheelchair = stop["wheelchair_boarding"] == 1
    stop_lat = stop["latitude"]
    stop_lng = stop["longitude"]
    return name, wheelchair, stop_lat, stop_lng 


#data holds the entire dict 
#data[data] gets you the entire list i.e. [{'attributes': {'address': None, 'at_street': 'Boylston Street', 'description': None, 'latitude': 42.348825, 'location_type': 0, 'longitude': -71.080571, 'municipality': 'Boston', 'name': 'Ring Rd @ Boylston St', 'on_street': 'Ring Road', 'platform_code': None, 'platform_name': None, 'vehicle_type': 3, 'wheelchair_boarding': 1}, 'id': '174', 'links': {'self': '/stops/174'}, 'relationships': {'facilities': {'links': {'related': '/facilities/?filter[stop]=174'}}, 'parent_station': {'data': None}, 'zone': {'data': {'id': 'LocalBus', 'type': 'zone'}}}, 'type': 'stop'}]

#data["data"][0] gets you first value in list which is {'address': None, 'at_street': 'Boylston Street', 'description': None, 'latitude': 42.348825, 'location_type': 0, 'longitude': -71.080571, 'municipality': 'Boston', 'name': 'Ring Rd @ Boylston St', 'on_street': 'Ring Road', 'platform_code': None, 'platform_name': None, 'vehicle_type': 3, 'wheelchair_boarding': 1}

#data["data"][0]["attributes"] gets you 'attributes': {'address': None, 'at_street': 'Boylston Street', 'description': None, 'latitude': 42.348825, 'location_type': 0, 'longitude': -71.080571, 'municipality': 'Boston', 'name': 'Ring Rd @ Boylston St'}

#Calling both functions together 
def find_stop_near(place_name):
    lat, lng = long_lat(place_name)
    stop_name, wheelchair, stop_lat, stop_lng = mbta_stop(lat, lng)
    return stop_name, wheelchair, lat, lng, stop_lat, stop_lng



#Flask Section
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nearest", methods=["POST"])
def nearest():
    place = request.form["place"]
    try:
        stop_name, wheelchair, place_lat, place_lng, stop_lat, stop_lng = find_stop_near(place)
        if "No MBTA stops" in stop_name:
            return render_template("index.html", error=stop_name)
        return render_template("mbta-results.html", 
            stop_name=stop_name, 
            wheelchair=wheelchair, 
            place=place,
            place_lat=place_lat,
            place_lng=place_lng,
            stop_lat=stop_lat,
            stop_lng=stop_lng,
            mapbox_token=MAPBOX_KEY)
    except Exception as e:
        return render_template("index.html", error=f"Something went wrong: {e}")

if __name__ == "__main__":
    app.run(debug=True)








    
