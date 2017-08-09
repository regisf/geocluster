# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

from .geoconvertion import *
from .geoboundbase import GeoBoundBase
from .geobound import GeoBound
from .geopoint import GeoPoint


class GeoCluster(GeoBoundBase):
    def __init__(self):
        super(GeoCluster, self).__init__()
        self.rectangles = []

    def __repr__(self):
        return '<GeoCluster(north={north}, west={west}, south={south}, east={east})>'.format(
            north=self.north,
            south=self.south,
            east=self.east,
            west=self.west
        )

    def set_grid(self, size_lng, size_lat):
        """
        Set the grid parameters
        :param size_lng: How many
        :param size_lat:
        :return: None
        """
        assert (isinstance(size_lng, int))
        assert (isinstance(size_lat, int))

        inc_lng = self.get_width() / size_lng
        inc_lat = self.get_height() / size_lat

        lat = self.north
        lng = self.west

        for width in xrange(size_lng):
            r = []
            for height in xrange(size_lat):
                r.append(GeoBound(lat, lng, lat + inc_lat, lng + inc_lng))
                lat += inc_lat
            self.rectangles.append(r)
            lat = self.north
            lng += inc_lng

    def populate(self, data, lat_name='latti', lng_name='longi'):
        """
        Add data a list of dictionnaries
        :param data: A dictionnary
        :param lat_name: A string for the lattitude key
        :param lng_name: A string for the longitude key
        :return: None
        """
        assert (isinstance(data, list))
        assert (isinstance(lat_name, str))
        assert (isinstance(lng_name, str))

        while len(data):
            d = data[0]
            assert (isinstance(d, dict))

            p = GeoPoint(d[lat_name], d[lng_name])
            del d[lat_name]
            del d[lng_name]

            if len(d):
                p.set_extra_data(d)

            for rectangle in self.rectangles:
                for rect in rectangle:
                    if rect.append(p):
                        break
            # remove d to be faster (the more the loop iterate, the less there's data)
            data.pop(0)

    def clear_population(self):
        for rectangle in self.rectangles:
            for rect in rectangle:
                rect.clear()

    def to_json(self):
        """
        Prepare the
        :return: The list containing all bounds in an array of array
        """
        ret = []
        ret_append = ret.append
        for rectangle in self.rectangles:
            r = []
            r_append = r.append
            for rect in rectangle:
                rect.use_clustering(self.clustering)
                r_append(rect.to_json())
            ret_append(r)

        return ret

    def get_bounds(self):
        """
        Get all bounds of the cluster.
        :return:  A list of list of dict
        """
        ret = []
        for rectangle in self.rectangles:
            r = []
            for rect in rectangle:
                r.append({
                    'north': convert_lat_from_degrees(rect.north),
                    'south': convert_lat_from_degrees(rect.south),
                    'east': convert_lng_from_degrees(rect.east),
                    'west': convert_lng_from_degrees(rect.west)
                })
            ret.append(r)

        return ret


if __name__ == '__main__':
    """
    Perform tests if the file is started as shell script
    However, it must be started with the "test" argument
    $ python geocluster.py test
    """

    import sys  # Don't pollute the namespace

    if len(sys.argv) != 2:
        sys.exit("Usage : \n    python geocluster.py test")

    import unittest

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests")
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(loader.discover(start_dir="tests")))
