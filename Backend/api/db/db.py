#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------- IMPORT
from ..py_geo.geo import geo_dist

# ------------------------------- FUNCTIONS

#
#
#
def n_closest_records(records, coord, n):
    pass
    #record = None
    #min_dist = 100000000000000000.0 # meters
    #for record in records:
    #    dist = geo_dist(coord, record['coordinates'])
    #    if dist < min_dist:
    #        min_dist = dist
    #        closest = record
    # finally return record
    #return record

#
#
#
def closest_record(records, coord):
    return n_closest_records(records, coord, 1)

#
#
#
def density_around(records, coord, age, time):
    pass
