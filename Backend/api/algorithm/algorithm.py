#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------- IMPORT

from ..printer.printer import print_progress, print_over
import math

# ------------------------------- CONFIGURATION

EARTH_RADIUS = 6367.0

# ------------------------------- FUNCTIONS
#
#   
#
def coord_dist(ori, dest, geodist=True):
    res = None
    dlat = math.radians(dest['lat']-ori['lat'])
    dlon = math.radians(dest['lon']-ori['lon'])
    if geodist:
        a = math.pow(
            math.sin(dlat / 2.0), 2) + math.cos(
            math.radians(ori['lat'])) * math.cos(
            math.radians(dest['lat'])) * math.pow(
            math.sin(dlon / 2.0), 2)
        res = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    else:
        d = math.sqrt(math.pow(dlat,2) + math.pow(dlon,2))
        res = math.tan(d)
    return 1000 * EARTH_RADIUS * res
#
# Récupère les N records les plus proches géographiquement de la coordonnée passée en paramètre
#
def n_closest_records(records, coord, n):
    recs = []
    for record in records:
        dist = coord_dist(coord, record['coordinates'])
        recs.append((dist, record))
    # sort records
    sorted_recs = sorted(recs, key=lambda r: r[0])
    # finally return n first records
    return sorted_recs[:n]
#
# Récupère le record le plus proche de la coordonnée géographiquement
#
def closest_record(records, coord):
    cr = n_closest_records(records, coord, 1)[0]
    return cr
#
# Retourne un tuple contenant la densité, le record le plus proche et sa distance à la coordonnée
#
def density_around(records, coord, radius):
    closest = None
    density = 0
    min_dist = 100000000000000000.0 + radius # meters
    for record in records:
        dist = coord_dist(coord, record['coordinates'])
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
        dist = coord_dist(coord, record['coordinates'])
        if dist < radius:
            recs.append(record)
    # finally return records
    return recs
#
#   Fonction de réduction de la granularité de la grille
#
def reduce_precision(grid, precision, determinist=True):
    grid_len = len(grid)
    removed_idx = []
    # calcul des points à supprimer
    for i in range(grid_len):
        print_progress(i, grid_len)
        if not i in removed_idx:
            o = { 'lon':grid[i][0], 'lat':grid[i][1] }
            for j in range(grid_len):
                if not j in removed_idx:
                    if i != j:
                        p = { 'lon':grid[j][0], 'lat':grid[j][1] }
                        if coord_dist(o, p) < precision:
                            removed_idx.append(j)
    # suppression des points en trop
    for idx in removed_idx:
        del grid[idx]
    # retour du ratio
    ratio = float(len(removed_idx))/grid_len
    return (ratio, len(removed_idx), grid_len)
#
#
#
def avg_geo_delta(grid):
    dlat = []
    dlon = []
    k=0
    for i in grid:
        k = k+1
        print_progress(k,len(grid))
        for j in grid:
            dlat.append(abs(i[0]-j[0]))
            dlon.append(abs(i[1]-j[1]))
    return (sum(dlat)/len(dlat),sum(dlon)/len(dlon))

