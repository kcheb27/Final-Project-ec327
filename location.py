
import requests


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





