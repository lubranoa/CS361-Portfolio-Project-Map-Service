# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/24/2022
# Description: This program
#
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv
import http.client
import urllib.parse
import json

load_dotenv()
opencage_key = os.getenv('POSITIONSTACK_KEY')
mapbox_key = os.getenv('MAPBOX_KEY')


def get_static_map_request(place_data):
    """Does this"""
    adjustable_comp = {'sat': 1, 'longi': 3, 'lati': 5, 'zoom': 7, 'size': 10}
    url_components = [
        'https://api.mapbox.com/styles/v1/mapbox/',
        'satellite-streets-v11',
        '/static/',
        '',
        ',',
        '',
        ',',
        '15'
        ',',
        '0/',
        '400x300',
        '?access_token=',
        mapbox_key
    ]
    poi_coord = get_coordinates(place_data)
    print(poi_coord)
    print(type(poi_coord['lon']))

    url_components[adjustable_comp['longi']] = str(poi_coord['lon'])
    url_components[adjustable_comp['lati']] = str(poi_coord['lat'])

    req_url = ''.join(url_components)
    return req_url


def get_coordinates(place_data: dict):
    """Does this"""
    params = {
        'access_key': opencage_key,
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
    req_url_map = get_static_map_request(data)
    print(req_url_map)
