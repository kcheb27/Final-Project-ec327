
import requests
import math

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    latitude = response.get("latitude")
    longitude = response.get("longitude")
    location_data =[longitude,latitude]
    return location_data

def get_distance(x,y):
    loc = get_location
    return (math.acos(math.sin(y)*math.sin(loc[1])+math.cos(y)*math.cos(loc[1])*math.cos(loc[0]-x))*6371 )


def get_closest(building):
    indeces = []
    values = []
    for i in range(len(building)):
        values.append(get_distance(building[i].x,building[i].y))
        



