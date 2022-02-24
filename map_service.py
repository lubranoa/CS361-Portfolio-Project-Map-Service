# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/24/2022
# Description: This program uses the SerpApi to scrape Google Maps for the name
#      of a point of interest. Returns the first result of a Google Maps search
#      for the point of interest.
#
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serp_key = os.getenv('SERP_KEY')
GoogleSearch.SERP_API_KEY = serp_key


def poi_search(params: dict):
    """Does this"""
    result = GoogleSearch(params).get_dict()

    poi_name = result["place_results"]["title"]

    return poi_name


if __name__ == "__main__":

    query_params = {
        "engine": "google_maps",
        "type": "search",
        "q": "houston texans stadium",
        "google-domain": "google.com",
        "hl": "en"
    }

    print(poi_search(query_params))
