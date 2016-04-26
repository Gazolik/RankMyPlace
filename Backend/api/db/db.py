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
# Retourne un tuple contenant la densité, le record le plus proche et sa distance à la coordonnée
#
def density_around(records, coord, radius):
    closest = None
    density = 0
    min_dist = 100000000000000000.0 + radius # meters
    for record in records:
        dist = 1000 * geo_dist(coord, record['coordinates'])
        if dist < radius:
            density += 1
            if dist < min_dist:
                min_dist = dist
                closest = record
    # finally return record
    return (density, closest, min_dist)

#
# Retourne tous les records compris dans un rayon (radius) autour de coord
#
def records_around(records, coord, radius):
    recs = []
    for record in records:
        dist = 1000 * geo_dist(coord, record['coordinates'])
        if dist < radius:
            recs.append(record)
    # finally return records
    return recs

