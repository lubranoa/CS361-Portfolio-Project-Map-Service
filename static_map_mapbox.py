# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description: This program
#
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv

load_dotenv()
mapbox_key = os.getenv('MAPBOX_KEY')


def get_map_req_url(coord_data):
    """Does this"""
    print('Generating a static map URL for these coordinates:', coord_data)
    url_components = [
        'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/',
        '',
        ',',
        '',
        ',15,0/400x300?access_token=',
        mapbox_key
    ]

    url_components[1] = coord_data[1]
    url_components[3] = coord_data[0]

    req_url = ''.join(url_components)
    return req_url


if __name__ == '__main__':

    lat_lon = ['33.5277', '-112.262608']
    req_url_map = get_map_req_url(lat_lon)
    print(req_url_map)
