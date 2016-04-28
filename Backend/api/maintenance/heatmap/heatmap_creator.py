#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------- IMPORTS

from ...fs.fs import load_heatmap_grid, dump_heatmap, list_heatmap_grids
from ...criteria.criterias import criterias_dict

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
        spec['criteria'] = criteria
        spec['coordinates'] = {'lat':p[1],'lon':p[0]} # rappel lon est la plus petite valeur pour Lyon : aux alentours de 4
        mark = rank(spec)
        heatmap.append([p, mark])
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
        for key, criteria in criterias_dict :
            gen_heatmap(grid, criteria)


