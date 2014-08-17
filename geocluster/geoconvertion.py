# -*- coding: utf-8 -*-
# Geocluster - A simple and naive geo cluster
# (c) Régis FLORET 2014 and later
#


def convert_lat_from_gps(value):
    """
    Convert a lattitude from GPS coordinate to decimal degrees
    :param value: The lattitude as a float between 0 and -90
    :return: The lattitude in decimal degrees
    """
    assert(isinstance(value, (int, float)))

    return value if value > 0 else 90 + abs(value)


def convert_lng_from_gps(value):
    """
    Convert a longitude from GPS coordinate to decimal degrees
    :param value: The longitude as a float
    :return: The longitude in decimal degrees
    """
    assert(isinstance(value, (int, float)))
    return value if value > 0 else 180 + abs(value)


def convert_lat_from_degrees(value):
    """
    Convert a longitude from decimal degrees to GPS coordinate
    :param value: The longitude as a float
    :return: The longitude in GPS coordinate
    """
    assert(isinstance(value, (int, float)))

    if value > 180:
        raise ValueError("Lattitude in degrees can't be greater than 180")
    elif value < 0:
        raise ValueError("Lattitude in degrees can't be lesser than 0")

    return value if value < 90 else 90 - value


def convert_lng_from_degrees(value):
    """
    Convert a longitude from decimal degrees to GPS coordinate
    :param value: The longitude as a float
    :return: The longitude in GPS coordinate
    """
    assert(isinstance(value, (int, float)))

    if value > 180:
        raise ValueError("Lattitude in degrees can't be greater than 180")
    elif value < 0:
        raise ValueError("Lattitude in degrees can't be lesser than 0")

    return value if value < 180 else 180 - value
