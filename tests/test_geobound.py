# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

__author__ = 'Régis FLORET'

import unittest
import geocluster


class GeoBoundTest(unittest.TestCase):
    def test_geobound_convert_point(self):
        """
        Bounds must be converted into radian
        """
        north=-20.849968961968585
        south=-21.39184466348015
        east=55.99046983169558
        west=55.064185041656515

        bound = geocluster.GeoBound(north=north, south=south, east=east, west=west)
        bound_dir = dir(bound)
        self.assertIn('points', bound_dir)
        self.assertIsInstance(bound.points, list)
        self.assertEqual(bound.points, [])

    def test_contains(self):
        """
        Test if a point is inside a bound
        """
        p = geocluster.GeoPoint(-21, 55.5)

        bound = geocluster.GeoBound(north=-20.849968961968585, south=-21.39184466348015,
                                    east=55.99046983169558, west=55.064185041656515)

        self.assertTrue(bound.contains(p))

    def test_not_contains(self):
        bound = geocluster.GeoBound(north=-20.849968961968585, south=-21.39184466348015,
                                    east=55.99046983169558, west=55.064185041656515)

        point = geocluster.GeoPoint(0,0)
        self.assertFalse(bound.contains(point))

        # If the point is on the south border or the east border, it's not inside
        point = geocluster.GeoPoint(-20.849968961968585, -21.39184466348015)
        self.assertFalse(bound.contains(point))

        point = geocluster.GeoPoint(-21, 0)
        self.assertFalse(bound.contains(point))

        point = geocluster.GeoPoint(0, 55.5)
        self.assertFalse(bound.contains(point))

    def test_append(self):
        """
        Append a point in the bound
        """
        p = geocluster.GeoPoint(-21, 55.5)

        bound = geocluster.GeoBound(north=-20.849968961968585, south=-21.39184466348015,
                                    east=55.99046983169558, west=55.064185041656515)
        bound.append(p)
        self.assertEqual(len(bound.points), 1)

    def test_append_not_inside(self):
        p = geocluster.GeoPoint(-21, 55)

        bound = geocluster.GeoBound(north=-20.849968961968585, south=-21.39184466348015,
                                    east=55.99046983169558, west=55.064185041656515)
        bound.append(p)
        self.assertEqual(len(bound.points), 0)

    def test_to_json(self):
        pass
