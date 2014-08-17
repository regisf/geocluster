# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

__author__ = 'Régis FLORET'

import unittest
import geocluster


class GeoboundBaseTest(unittest.TestCase):
    def test_geoboundbase(self):
        cluster = geocluster.GeoBoundBase()
        cluster_dir = dir(cluster)

        self.assertIn('north', cluster_dir)
        self.assertIsNone(cluster.north)

        self.assertIn('south', cluster_dir)
        self.assertIsNone(cluster.south)

        self.assertIn('west', cluster_dir)
        self.assertIsNone(cluster.west)

        self.assertIn('east', cluster_dir)
        self.assertIsNone(cluster.east)

    def test_set_bounds(self):
        bound = geocluster.GeoBoundBase()

        north=-20.849968961968585
        south=-21.39184466348015
        east=55.99046983169558
        west=55.064185041656515

        bound.set_bounds(north=south, south=north, east=west, west=east)

        self.assertGreater(bound.south, bound.north)
        self.assertGreater(bound.east, bound.west)

        bound_dir = dir(bound)
        self.assertIn('north', bound_dir)
        self.assertEqual(bound.north, geocluster.convert_lat_from_gps(north))

        self.assertIn('south', bound_dir)
        self.assertEqual(bound.south, geocluster.convert_lat_from_gps(south))

        self.assertIn('west', bound_dir)
        self.assertEqual(bound.west, geocluster.convert_lng_from_gps(west))

        self.assertIn('east', bound_dir)
        self.assertEqual(bound.east, geocluster.convert_lng_from_gps(east))


    def test_get_width(self):
        bound = geocluster.GeoBoundBase()

        north=-20.849968961968585
        south=-21.39184466348015
        east=55.99046983169558
        west=55.064185041656515

        bound.set_bounds(north=north, south=south, east=east, west=west)
        self.assertEqual(bound.get_height(), geocluster.convert_lat_from_gps(south) - geocluster.convert_lat_from_gps(north))

    def test_get_height(self):
        bound = geocluster.GeoBoundBase()

        north=-20.849968961968585
        south=-21.39184466348015
        east=55.99046983169558
        west=55.064185041656515

        bound.set_bounds(north=north, south=south, east=east, west=west)
        self.assertEqual(bound.get_width(), geocluster.convert_lng_from_gps(east) - geocluster.convert_lng_from_gps(west))

