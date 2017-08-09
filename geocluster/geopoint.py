# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

from .geoconvertion import *


class GeoPoint(object):
    def __init__(self, lat, lng):
        assert (isinstance(lat, (int, float)))
        assert (isinstance(lng, (int, float)))

        self.lat = convert_lat_from_gps(lat)
        self.lng = convert_lng_from_gps(lng)
        self.extra_data = {}

    def __repr__(self):
        return '<GeoPoint({}, {})>'.format(self.lat, self.lng)

    def set_extra_data(self, data):
        """
        Add data to the point to retrieve them easily
        :type data: dict
        :param data: A dictionnary of extra data
        :return: None
        """
        assert (isinstance(data, dict))
        self.extra_data.update(data)

    def to_json(self):
        self.extra_data.update({
            'lat': convert_lat_from_degrees(self.lat),
            'lng': convert_lng_from_degrees(self.lng)
        })

        return self.extra_data
