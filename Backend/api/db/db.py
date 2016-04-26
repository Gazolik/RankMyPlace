#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------- IMPORT
from ..py_geo.geo import geo_dist

# ------------------------------- FUNCTIONS

#
# Récupère les N records les plus proches géographiquement de la coordonnée passée en paramètre
#
def n_closest_records(records, coord, n):
    recs = []
    for record in records:
        dist = 1000 * geo_dist(coord, record['coordinates'])
        recs.append((dist, record))
    # sort records
    sorted_recs = sorted(recs, key=lambda r: r[0])
    # finally return n first records
    return sorted_recs[:n]

#
# Récupère le record le plus proche de la coordonnée géographiquement
#
def closest_record(records, coord):
    return n_closest_records(records, coord, 1)

#
#
#
def density_around(records, coord, age, time):
    pass
