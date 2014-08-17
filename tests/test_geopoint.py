# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#

__author__ = 'Régis FLORET'

import unittest
import geocluster


class GeoPointTest(unittest.TestCase):
    def test_point(self):
        point = geocluster.GeoPoint(10, 10)
