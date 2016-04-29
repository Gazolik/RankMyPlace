#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------- IMPORTS

from ...fs.fs import load_heatmap_grid, dump_heatmap, list_heatmap_grids, dump_heatmap_grid
from ...criteria.gen_criteria import rank
from ...criteria.criterias import criterias_dict
from ...algorithm.algorithm import reduce_precision, avg_geo_delta
from ...printer.printer import print_progress

# ---------------- FUNCTIONS

#
#   Génère une heatmap à partir d'une grille et d'un critère
#
def gen_heatmap(grid_basename, criteria) :
    print('[heatmap_creator.py]> generating %s heatmap for criteria %s...' % (grid_basename, criteria['name']))
    # read input file
    points = load_heatmap_grid(grid_basename)
    # iterate on points
    heatmap=[]
    points_len = len(points)
    for i in range(points_len):
        print_progress(i, points_len)
        spec={
            'criteria' : criteria,
            'coordinates' : {'lat':points[i][1],'lon':points[i][0]} # rappel lon est la plus petite valeur pour Lyon : aux alentours de 4
        }
        mark, obj = rank(spec)
        points[i].append(mark)
        heatmap.append(points[i])
    print('[heatmap_creator.py]> generating %s heatmap for criteria %s...done !' % (grid_basename, criteria['name']))
    print('[heatmap_creator.py]> writing %s heatmap file...' % grid_basename, end='')
    # write output file
    dump_heatmap(grid_basename, criteria['name'], heatmap)
    print('done !')

#
#   Génère toutes les heatmaps pour toutes les grilles et tous les critères
#
def gen_all_heatmaps():
    grids = list_heatmap_grids()
    for grid in grids :
        for key, criteria in criterias_dict.items():
            gen_heatmap(grid, criteria)

#
#   Calcul de réduction de précision d'une grille
#
def reduce_grid(grid_basename, precision):
    grid = load_heatmap_grid(grid_basename)
    print('[heatmap_creator.py]> cruching %s...' % grid_basename)
    ratio, removed, total = reduce_precision(grid, precision)
    print('[heatmap_creator.py]> cruching %s...done !' % grid_basename)
    print('[heatmap_creator.py]> reduction ratio is %.2f%% for grid %s. Details : removed = %s, total = %s' % (ratio*100, grid_basename, removed, total))
    dump_heatmap_grid(grid_basename + '_red_%s' % int(precision), grid)
#
#
#
def reduce_all(precision):
    grid_basenames = list_heatmap_grids()
    for grid_basename in grid_basenames:
        reduce_grid(grid_basename, precision)
#
#
#
def avg_grid(gridname):
    grid = load_heatmap_grid(gridname)
    moylat, moylon = avg_geo_delta(grid)
    print('[heatmap_creator.py]> for grid: %s, avg lat=%s, avg lon=%s...' % (gridname, moylat, moylon))


