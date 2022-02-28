# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description: This program
#
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv
import http.client
import urllib.parse
import json

load_dotenv()
positionstack_key = os.getenv('POSITIONSTACK_KEY')
mapbox_key = os.getenv('MAPBOX_KEY')


def get_map_req_url(place_data):
    """Does this"""
    url_components = [
        'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/',
        '',
        ',',
        '',
        ',15,0/400x300?access_token=',
        mapbox_key
    ]
    poi_coord = get_coordinates(place_data)
    print(poi_coord)
    print(type(poi_coord['lon']))

    url_components[1] = str(poi_coord['lon'])
    url_components[3] = str(poi_coord['lat'])

    req_url = ''.join(url_components)
    return req_url


def get_coordinates(place_data: dict):
    """Does this"""
    params = {
        'access_key': positionstack_key,
        'query': place_data['poi_name'],
        'region': place_data['location'],
        'limit': 1
    }

    conn = http.client.HTTPConnection('api.positionstack.com')

    send_params = urllib.parse.urlencode(params)

    conn.request('GET', '/v1/forward?{}'.format(send_params))

    res = conn.getresponse()
    received = res.read()

    print(received.decode('utf-8'))
    rec = json.loads(received.decode('utf-8'))

    lon_lat = {}

    lat = rec['data'][0]['latitude']
    lon = rec['data'][0]['longitude']
    lon_lat['lon'] = lon
    lon_lat['lat'] = lat

    return lon_lat


if __name__ == '__main__':

    data = {
        'poi_name': 'AT&T Stadium',
        'location': 'Arlington, Texas, United States'
    }
    req_url_map = get_map_req_url(data)
    print(req_url_map)
