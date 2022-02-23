# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/23/2022
# Description:
#
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serp_key = os.getenv('SERP_KEY')
GoogleSearch.SERP_API_KEY = serp_key

search = GoogleSearch({
    "engine": "google_maps",
    "type": "search",
    "q": "houston texans stadium",
    "google-domain": "google.com",
    "hl": "en"
  })
result = search.get_dict()

poi_name = result["place_results"]["title"]

print(poi_name)
