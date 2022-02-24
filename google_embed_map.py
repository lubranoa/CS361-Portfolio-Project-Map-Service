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
positionstack_key = os.getenv('POSITIONSTACK_KEY')
google_key = os.getenv('GOOGLE_KEY')


def get_map_request(place_data):
    """Does this"""
    adjustable_comp = {'lati': 3, 'longi': 5, 'zoom': 7, 'sat': 9}
    url_components = [
        'https://www.google.com/maps/embed/v1/view?key=',
        google_key,
        '&center=',
        '',
        ',',
        '',
        '&zoom=',
        '16'
        '&maptype=',
        'satellite'
    ]
    poi_coord = get_coordinates(place_data)
    print(poi_coord)

    url_components[adjustable_comp['lati']] = str(poi_coord['lat'])
    url_components[adjustable_comp['longi']] = str(poi_coord['lon'])

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
    req_url_map = get_map_request(data)
    print(req_url_map)
