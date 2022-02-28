# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description: This module generates a Mapbox Static Images API request URL
#     when called by another program and returns it to the calling program. The
#     URL should be placed in an HTML img element as a src property to display
#     a static satellite map image of the sent coordinates. Mapbox API key does
#     not need to be hidden because it has been restricted to specific URLs.
#
# -----------------------------------------------------------------------------

mapbox_key = 'pk.eyJ1IjoibHVicmFub2EiLCJhIjoiY2wwNXVqM3lvMDRpeDNvcnVwazJrZXlobyJ9.DgD1j9mF8jELE7_CJ_vKcw '


def get_map_req_url(coord_data: list):
    """
    Takes a latitude and a longitude and generates a Mapbox Static Images API
    request URL to be added as a src property to an HTML img element on a web
    page

    :param coord_data: list containing [lat, long]
    :return: string - API request URL
    """

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
