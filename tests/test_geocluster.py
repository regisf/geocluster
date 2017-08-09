# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

import unittest

import geocluster

__author__ = 'Régis FLORET'


class GeoclusterTest(unittest.TestCase):
    def test_geocluster(self):
        cluster = geocluster.GeoCluster()
        self.assertIn('rectangles', dir(cluster))
        self.assertEqual(cluster.rectangles, [])

    def test_set_grid(self):
        cluster = geocluster.GeoCluster()
        north = -20.849968961968585
        south = -21.39184466348015
        east = 55.99046983169558
        west = 55.064185041656515

        cluster.set_bounds(north=north, south=south, east=east, west=west)
        cluster.set_grid(10, 10)
        self.assertEqual(len(cluster.rectangles), 10)

        lat = geocluster.convert_lat_from_gps(north)

        for rect in cluster.rectangles:
            self.assertEqual(len(rect), 10)
            lat += rect[0].get_height()
            lng = geocluster.convert_lng_from_gps(west)
            for r in rect:
                lng += r.get_width()
                self.assertIsInstance(r, geocluster.GeoBound)
            self.assertEqual(lng, geocluster.convert_lng_from_gps(east))

        self.assertEqual(lat, geocluster.convert_lat_from_gps(south))

    def test_populate(self):
        pass

    def test_to_json(self):
        pass
