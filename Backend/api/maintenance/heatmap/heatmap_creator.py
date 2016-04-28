#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------- IMPORTS

from ...fs.fs import load_heatmap_grid, dump_heatmap, list_heatmap_grids, json_dump
from ...criteria.gen_criteria import rank
from ...criteria.criterias import criterias_dict
<<<<<<< HEAD
from ...algorithm.algorithm import reduce_precision

=======
from ...algorithm.algorithm import avg_geo_delta
>>>>>>> 1ea20ed3ee7f940bdd79c1d8e82d80e346a44a04
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
    for p in points:
        spec={
            'criteria' : criteria,
            'coordinates' : {'lat':p[1],'lon':p[0]} # rappel lon est la plus petite valeur pour Lyon : aux alentours de 4
        }
        mark, obj = rank(spec)
        p.append(mark)
        heatmap.append(p)
    print('[heatmap_creator.py]> done !')
    print('[heatmap_creator.py]> writing %s heatmap file...' % grid_basename)
    # write output file
    dump_heatmap(grid_basename, criteria['name'], heatmap)
    print('[heatmap_creator.py]> done !')

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
    ratio, removed, total = reduce_precision(grid, precision)
    print('[heatmap_creator.py]> reduction ratio is %.2f%% for grid %s. Details : removed = %s, total = %s' % (ratio*100, grid_basename, removed, total))
    return grid
#
#
#
def reduce_all(precision):
    files = list_heatmap_grids()
    for f in files:
        json_dump('./data/heatmap/psd/' + f + '_red_%s_grid' % int(precision), reduce_grid(f, precision))
#
#
#
def avg_grid(gridname):
    grid = load_heatmap_grid(gridname)
    moylat, moylon = avg_geo_delta(grid)
    print('[heatmap_creator.py]> for grid: %s, avg lat=%s, avg lon=%s...' %(gridname, moylat, moylon))


