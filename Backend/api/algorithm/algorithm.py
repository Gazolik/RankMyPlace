#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------- IMPORT
from ..py_geo.geo import geo_dist
from ..printer.printer import print_progress

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
    cr = n_closest_records(records, coord, 1)[0]
    return cr

#
# Retourne un tuple contenant la densité, le record le plus proche et sa distance à la coordonnée
#
def density_around(records, coord, radius):
    closest = None
    density = 0
    min_dist = 100000000000000000.0 + radius # meters
    total = len(records)
    for i in range(total):
        if i%1000 == 0 :
            print_progress(i, total)
        dist = 1000 * geo_dist(coord, records[i]['coordinates'])
        if dist < radius:
            density += 1
            if dist < min_dist:
                min_dist = dist
                closest = records[i]
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

#
#   Fonction de réduction de la granularité de la grille
#
def reduce_precision(grid, precision, determinist=True):
    grid_len = len(grid)
    removed_idx = []
    # calcul des points à supprimer
    for i in range(grid_len):
        if not i in removed_idx:
            o = { 'lon':grid[i][0], 'lat':grid[i][1] }
            for j in range(grid_len):
                if not j in removed_idx:
                    if i != j:
                        p = { 'lon':grid[j][0], 'lat':grid[j][1] }
                        if 1000 * geo_dist(o, p) < precision:
                            removed_idx.append(j)
    # suppression des points en trop
    for idx in removed_idx:
        del grid[idx]
    # retour du ratio
    ratio = float(len(removed_idx))/grid_len
    return (ratio, len(removed_idx), grid_len)

