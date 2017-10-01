#!/usr/bin/python

from __future__ import print_function
from __future__ import division

from datetime import datetime
import os
import sys

import googlemaps


API_KEY = os.environ.get('GOOGLE_API_KEY')
if not API_KEY:
    print('source/export GOOGLE_API_KEY before running script.')
    sys.exit(1)

maps = googlemaps.Client(key=API_KEY)
now = datetime.now()
origin = "9402 Meadow Crossing Way, Fairfax Station, VA 22039"
destination = "12193 Fair Lakes Promenade Dr, Fairfax, VA 22033"
destinations = [destination]
for destination in destinations:
    result_routes = maps.directions(
        origin, destination, mode="driving", departure_time=now)
    distance = result_routes[0]['legs'][0]['distance']['value']
    trip = round(distance * 2 / 5280, 2)
    print('{}:\t{}'.format(destination, trip))
