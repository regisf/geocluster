# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

import random
from .geoboundbase import GeoBoundBase
from .geopoint import GeoPoint
from .geoconvertion import *

class GeoBound(GeoBoundBase):
    """ A Geobound is in fact a rectangle
    """
    def __init__(self, north, west, south, east):
        """
        Create the bound
        :param north: The top of the bound as a float
        :param west: The left of the bound as a float
        :param south: The bottom of the bound as a float
        :param east: The right of the bound as a float
        """
        super(GeoBound, self).__init__()
        self.set_bounds(north=north, west=west, south=south, east=east)
        self.center_lat = self.north + (self.south - self.north)/2.0
        self.center_lng = self.west + (self.east - self.west)/2.0

        self.points = []

    def contains(self, point):
        """
        Compute if a point is inside the bound
        :param point:
        :return: True if inside, False elsewhere
        """
        assert(isinstance(point, GeoPoint))
        return self.north <= point.lat < self.south and self.west <= point.lng < self.east

    def append(self, point):
        """
        Add a point into the GeoBound.
        :type point: GeoPoint
        :param point: The point to add
        """
        assert(isinstance(point, GeoPoint))
        if not self.contains(point):
            return False

        self.points.append(point)
        return True

    def get_center(self):
        """
        Get the center of the bound
        :return: lattitude and longitude of the center as a tuple
        """
        self.compute_center()
        return self.center_lat, self.center_lng


    def __repr__(self):
        return '<GeoBound({}, {}, {}, {})>'.format(self.north, self.west, self.south, self.east)

    def __len__(self):
        """
        How many point does the bound got
        :return: The number of points inside
        """
        return len(self.points)

    def to_json(self):
        ret = {}
        if self.clustering:
            if not len(self.points):
                ret['count'] = 0
                return

            if len(self.points) == 1:
                ret = self.points[0].to_json()
                ret.update({
                    'count': 1
                })
            else:
                lat, lng = self.get_center()
                ret.update({
                    'count': len(self.points),
                    'lat': convert_lat_from_degrees(lat),
                    'lng': convert_lng_from_degrees(lng)
                })
        else:
            ret.update({
                'points': [p.to_json() for p in self.points]
            })

        return ret

    def clear(self):
        self.points = []

    def compute_center(self):
        """
        Compute the global center of a bound
        """
        avg_lat = 0
        avg_lng = 0
        for p in self.points:
            avg_lat += p.lat
            avg_lng += p.lng
        size = len(self.points) or 1
        self.center_lat = avg_lat / size
        self.center_lng = avg_lng / size
