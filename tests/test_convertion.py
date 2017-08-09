# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#


import unittest

from geocluster import convert_lng_from_gps, convert_lng_from_degrees, convert_lat_from_gps, convert_lat_from_degrees

__author__ = 'Régis FLORET'


class ConvertionTest(unittest.TestCase):
    def test_type(self):
        lat_f = 10.0
        lat_i = 10
        lat_s = '10'

        lng_f = 10.0
        lng_i = 10
        lng_s = '10'

        # Test correct arguments type
        convert_lat_from_gps(lat_f)
        convert_lat_from_gps(lat_i)
        convert_lng_from_gps(lng_f)
        convert_lng_from_gps(lng_i)

        # Test wrong argument type
        with self.assertRaises(AssertionError):
            convert_lat_from_gps(lat_s)

        with self.assertRaises(AssertionError):
            convert_lng_from_gps(lng_s)

        convert_lat_from_degrees(lat_f)
        convert_lat_from_degrees(lat_i)
        convert_lng_from_degrees(lng_f)
        convert_lng_from_degrees(lng_i)

        # Test wrong argument type
        with self.assertRaises(AssertionError):
            convert_lat_from_degrees(lat_s)

        with self.assertRaises(AssertionError):
            convert_lng_from_degrees(lng_s)

    def test_lat_from_gps(self):
        lat = 10
        response = convert_lat_from_gps(lat)
        self.assertEqual(response, lat)

        lat = -1
        response = convert_lat_from_gps(lat)
        self.assertNotEqual(response, lat)
        self.assertEqual(response, 91)

    def test_lat_from_degrees(self):
        lat = 10
        response = convert_lat_from_degrees(lat)
        self.assertEqual(response, lat)

        lat = 91
        response = convert_lat_from_degrees(lat)
        self.assertNotEqual(response, lat)
        self.assertEqual(response, -1)

        lat = -1
        with self.assertRaises(ValueError):
            convert_lat_from_degrees(lat)

        lat = 181
        with self.assertRaises(ValueError):
            convert_lat_from_degrees(lat)

    def test_lng_from_gps(self):
        lng = 10
        response = convert_lat_from_gps(lng)
        self.assertEqual(response, lng)

        lng = -1
        response = convert_lat_from_gps(lng)
        self.assertNotEqual(response, lng)
        self.assertEqual(response, 91)

    def test_lng_from_degrees(self):
        lng = 10
        response = convert_lat_from_degrees(lng)
        self.assertEqual(response, lng)

        lng = 91
        response = convert_lat_from_degrees(lng)
        self.assertNotEqual(response, lng)
        self.assertEqual(response, -1)

        lng = -1
        with self.assertRaises(ValueError):
            response = convert_lat_from_degrees(lng)

        lng = 181
        with self.assertRaises(ValueError):
            response = convert_lat_from_degrees(lng)
