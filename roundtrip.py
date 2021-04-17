#!/usr/bin/python3

from datetime import datetime
import os
import sys

import googlemaps


DEFAULT_ORIGIN = "9402 Meadow Crossing Way, Fairfax Station, VA 22039"


def get_origin():
    return DEFAULT_ORIGIN


def get_destinations():
    return [
        "774a walker road, Great Falls, VA",
        ]


def get_api_key():
    return os.environ.get('GOOGLE_API_KEY')


def print_round_trips(client, origin, destinations):
    for destination in destinations:
        now = datetime.now()
        result_routes = client.directions(
            origin, destination, mode="driving", departure_time=now)
        distance = result_routes[0]['legs'][0]['distance']['value']
        trip = round(distance * 2 / 1609.34, 2)
        print('{}:\t{}'.format(destination, trip))


def main():
    API_KEY = get_api_key()
    if not API_KEY:
        print('source/export GOOGLE_API_KEY before running script.')
        sys.exit(1)

    client = googlemaps.Client(key=API_KEY)
    origin = get_origin()
    destinations = get_destinations()
    print_round_trips(client, origin, destinations)


if __name__ == '__main__':
    main()
