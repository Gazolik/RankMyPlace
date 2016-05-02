#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------- IMPORT

from ..printer.printer import print_progress
from ..printer.printer import print_over
from ..fs.fs import load_heatmap_grid
from ..fs.fs import load_heatmap
import math

# ------------------------------- CONFIGURATION

EARTH_RADIUS = 6367.0

# ------------------------------- FUNCTIONS


def isobarycenter(coordinates):
    """
        Barycentre en coordonnées géographiques
    """
    n = len(coordinates)
    sumlat = 0.0
    sumlon = 0.0
    for i in range(n):
        sumlat += coordinates[i][1]
        sumlon += coordinates[i][0]
    return {'lat': sumlat / n, 'lon': sumlon / n}


def coord_dist(ori, dest, geodist=True):
    """
        Calcul paramétrable de la distance entre deux coordonnées géographique
    """
    res = None
    dlat = math.radians(dest['lat'] - ori['lat'])
    dlon = math.radians(dest['lon'] - ori['lon'])
    if geodist:
        a = math.pow(
            math.sin(dlat / 2.0), 2) + math.cos(
            math.radians(ori['lat'])) * math.cos(
            math.radians(dest['lat'])) * math.pow(
            math.sin(dlon / 2.0), 2)
        res = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    else:
        d = math.sqrt(math.pow(dlat, 2) + math.pow(dlon, 2))
        res = math.tan(d)
    return 1000 * EARTH_RADIUS * res


def axis_dist(ori_lat, ori_lon, dest_lat, dest_lon, geodist=True):
    """
        Calcul de la distance selon la latitude et selon la longitude
    """
    res = None
    dlat = coord_dist({'lat': ori_lat, 'lon': 0.0}, {'lat': dest_lat, 'lon': 0.0})
    dlon = coord_dist({'lat': 0.0, 'lon': ori_lon}, {'lat': 0.0, 'lon': dest_lon})
    return (dlat, dlon)


def n_closest_records(records, coord, n):
    """
        Récupère les N records les plus proches géographiquement de la coordonnée passée en paramètre
    """
    recs = []
    for record in records:
        dist = coord_dist(coord, record['coordinates'])
        recs.append((dist, record))
    # sort records
    sorted_recs = sorted(recs, key=lambda r: r[0])
    # finally return n first records
    return sorted_recs


def closest_record(records, coord):
    """
        Récupère le record le plus proche de la coordonnée géographiquement
    """
    cr = n_closest_records(records, coord, 1)[0]
    return cr


def density_around(records, coord, radius):
    """
        Retourne un tuple contenant la densité, le record le plus proche et sa distance à la coordonnée
    """
    closest = None
    density = 0
    min_dist = 100000000000000000.0 + radius  # meters
    for record in records:
        dist = coord_dist(coord, record['coordinates'])
        if dist < radius:
            density += 1
            if dist < min_dist:
                min_dist = dist
                closest = record
    # finally return record
    return (density, closest, min_dist)


def records_around(records, coord, radius):
    """
        Retourne tous les records compris dans un rayon (radius) autour de coord
    """
    recs = []
    for record in records:
        dist = coord_dist(coord, record['coordinates'])
        if dist < radius:
            recs.append(record)
    # finally return records
    return recs


def reduce_precision_QCGR(grid, precision, determinist=True):
    """
        Fonction de réduction de la granularité de la grille
    """
    print('[algorithm.py]> reducing grid precision using QCGR algorithm...')
    grid_len = len(grid)
    removed_idx = []
    # calcul des points à supprimer
    for i in range(grid_len):
        print_progress(i, grid_len)
        if i not in removed_idx:
            o = {'lon': grid[i][0], 'lat': grid[i][1]}
            for j in range(grid_len):
                if j not in removed_idx:
                    if i != j:
                        p = {'lon': grid[j][0], 'lat': grid[j][1]}
                        if coord_dist(o, p) < precision:
                            removed_idx.append(j)
    # suppression des points en trop
    kept = []
    for i in range(grid_len):
        if i not in removed_idx:
            kept.append(grid[i])
    # retour du ratio
    ratio = float(len(removed_idx)) / grid_len
    print('[algorithm.py]> done !')
    # retour de la grille, du ratio de reduction et du nombre de points enlevés et du total
    return (kept, ratio, len(removed_idx), grid_len)


def reduce_precision_FGR(grid, precision, determinist=True):
    """
        Fonction de réduction de la granularité de la grille
    """
    # constantes de paramètrage
    MIN_LON = 4.681  # degrees
    MIN_LAT = 45.55  # degrees
    # algo
    print('[algorithm.py]> reducing grid precision using FGR algorithm...')
    grid_len = len(grid)
    removed = 0
    matrix = {}
    for i in range(grid_len):
        # calcul de l'index du point à insérer
        dlat, dlon = axis_dist(MIN_LAT, MIN_LON, grid[i][1], grid[i][0])
        lat_idx = int(math.floor(dlat) / precision)
        lon_idx = int(math.floor(dlon) / precision)
        key = '%s-%s' % (lat_idx, lon_idx)
        # insertion du point dans le dico
        # - verif existence clé
        if key in matrix.keys():
            removed += 1
        else:
            matrix[key] = grid[i]
    # calcul du ratio
    ratio = float(removed) / grid_len
    print('[algorithm.py]> done !')
    # retour de la grille, du ratio de reduction et du nombre de points enlevés et du total
    return (list(matrix.values()), ratio, removed, grid_len)


def avg_geo_delta(grid):
    """
        TODO : doc
    """
    print('[algorithm.py]> computing grid stats...')
    dlat = []
    dlon = []
    grid_len = len(grid)
    for i in range(grid_len):
        print_progress(i, grid_len)
        for j in grid:
            dlat.append(abs(grid[i][0] - j[0]))
            dlon.append(abs(grid[i][1] - j[1]))
    print('[algorithm.py]> done !')
    return (sum(dlat) / len(dlat), sum(dlon) / len(dlon))


def avg_heatmap(heatmap_name, criterias_coef, GRID_SET):
    """
        TODO : doc
    """
    # print(heatmap_name)
    coef_tot = sum(criterias_coef.values())
    # la heatmap qui sera retournee
    avg_map = {}
    avg_map['heatmap'] = load_heatmap_grid(heatmap_name)
    avg_map['center'] = isobarycenter(avg_map['heatmap'])
    avg_map['zoom'] = 14
    # tableau des notes moyennes
    notes = [0 for i in avg_map['heatmap']]
    nomcriteres = [k for k, v in criterias_coef.items() if v != 0]

    for criteria in nomcriteres:
        # print(criteria)
        loaded_heatmap = load_heatmap(heatmap_name + GRID_SET, criteria)
        if loaded_heatmap is None:
            continue
        for idx, val in enumerate(loaded_heatmap['heatmap']):
            notes[idx] = notes[idx] + val[2] * criterias_coef[criteria] / coef_tot
        # pour enlever le json de la memoire
        # del loaded_heatmap

    for idx, val in enumerate(notes):
        avg_map['heatmap'][idx] = [round(avg_map['heatmap'][idx][0], 5), round(avg_map['heatmap'][idx][1], 5), round(notes[idx], 2)]
    return avg_map


def satisfaction(note, coef):
    """calcul la satisfation en fonction d'une note et d'un coef"""
    satisfaction = (note * coef / 100) ** (coef / 10)
    satisfaction = ((satisfaction * 10) - 5) * coef
    return satisfaction * 2 #retourne une satisfation ou insatisfaction
