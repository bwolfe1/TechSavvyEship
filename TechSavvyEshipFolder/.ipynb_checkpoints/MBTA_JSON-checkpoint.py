import requests
from urllib.request import urlopen
import json

def get_json(url):
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

api_key= "172ce4d9fbbe422496368d3b1ead4e18"

start_of_url= 'https://api-v3.mbta.com'

ROUTE_ID= "Orange"

url= "https://api-v3.mbta.com/predictions?filter[route]=" + ROUTE_ID + "&key=" + api_key

def get_vote(url, api_key):
    headers={'x-api-key': api_key}
    data = get_json(url)
    
    return data
        
    
Orange_line = get_vote(url, api_key)
print(Orange_line)
