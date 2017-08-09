# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

from .geoconvertion import *


class GeoBoundBase(object):
    def __init__(self):
        """
        Predeclare the object variables
        """
        self.north, self.south, self.west, self.east = None, None, None, None
        self.clustering = True

    def set_bounds(self, north, west, south, east):
        """
        Set the global bounds
        :param north: The top of the bound as a float
        :param west: The left of the bound as a float
        :param south: The bottom of the bound as a float
        :param east: The right of the bound as a float
        """
        assert (isinstance(north, (float, int)))
        assert (isinstance(west, (float, int)))
        assert (isinstance(south, (float, int)))
        assert (isinstance(east, (float, int)))

        if north < 0:
            north = convert_lat_from_gps(north)

        if south < 0:
            south = convert_lat_from_gps(south)

        if east < 0:
            east = convert_lng_from_gps(east)

        if west < 0:
            west = convert_lng_from_gps(west)

        self.north = min(north, south)
        self.south = max(north, south)
        self.west = min(east, west)
        self.east = max(east, west)

    def get_width(self):
        """
        Return the width size of the bound
        It don't return the REAL size but the approximative size (see README.md)
        :rtype float
        :return: the width
        """
        return abs(self.east - self.west)

    def get_height(self):
        """
        Return the height size of the bound
        It don't return the REAL size but the approximative size (see README.md)
        :rtype float
        :return: the height
        """
        return abs(self.south - self.north)

    def use_clustering(self, clustering):
        """
        Aggregate data or not
        :param clustering: a boolean to indicate if we use aggregation or not
        """
        assert (isinstance(clustering, bool))
        self.clustering = clustering
