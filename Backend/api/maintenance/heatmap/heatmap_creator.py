#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------- IMPORTS

from ...fs.fs import load_heatmap_grid, dump_heatmap, list_heatmap_psd, list_heatmap_grids, dump_heatmap_grid, list_database_psd
from ...criteria.gen_criteria import rank
from ...criteria.criterias import criterias_dict
from ...algorithm.algorithm import reduce_precision_QCGR, reduce_precision_FGR, avg_geo_delta
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
        lat = points[i][1]
        lon = points[i][0]
        spec={
            'criteria' : criteria,
            'coordinates' : { 'lat':lat, 'lon':lon } # rappel lon est la plus petite valeur pour Lyon : aux alentours de 4
        }
        mark, ul1, ul2 = rank(spec)
        heatmap.append([round(lon,5), round(lat,5), round(mark,2)])

    print('[heatmap_creator.py]> done !')
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
#
#
def reduced_grid_name(grid_basename, precision, method=None):
    method_name = 'fgr'
    if method == 'QCGR':
        method_name = 'qcgr'
    return grid_basename + '_red_%s_%s' % (int(precision), method_name)
#
#   Calcul de réduction de précision d'une grille
#
def reduce_grid(grid_basename, precision, method=None):
    grid = load_heatmap_grid(grid_basename)
    print('[heatmap_creator.py]> cruching %s...' % grid_basename)
    #
    if method == 'QCGR':
        red_grid, ratio, removed, total = reduce_precision_QCGR(grid, precision)
    else:
        red_grid, ratio, removed, total = reduce_precision_FGR(grid, precision)
    #
    print('[heatmap_creator.py]> done !')
    print('[heatmap_creator.py]> reduction ratio is %.2f%% for grid %s. Details : removed = %s, total = %s' % (ratio*100, grid_basename, removed, total))
    dump_heatmap_grid(reduced_grid_name(grid_basename, precision, method), red_grid)
#
#
#
def reduce_all(precision, method=''):
    grid_basenames = list_heatmap_grids()
    for grid_basename in grid_basenames:
        reduce_grid(grid_basename, precision, method)
#
#
#
def avg_grid(gridname):
    grid = load_heatmap_grid(gridname)
    moylat, moylon = avg_geo_delta(grid)
    print('[heatmap_creator.py]> for grid: %s, avg lat=%s, avg lon=%s...' % (gridname, moylat, moylon))
#
#
#
def gen_script(precision, method='QCGR'):
    # initialize command lists
    reduce_cmds = []
    heatmap_cmds = []
    script_name = 'heatmap_%s_%s_gen.sh' % (precision, method)
    # list base grids
    initial_psd = list_heatmap_psd()
    # list criterias files
    criterias = list_database_psd()
    # for each base grid
    for initial_grid in initial_psd:
        # create and add reduce equivalent command
        reduce_cmds.append('./maintenance.py heatmap reduce %s %s %s' % (initial_grid, int(precision), method))
        # initialize new grid name
        grid_name = reduced_grid_name(initial_grid, precision, method)
        # for each criteria
        for criteria in criterias:
            # create and add heatmap generation command
            heatmap_cmds.append('./maintenance.py heatmap gen %s %s' % (grid_name, criteria))
    # write script file
    with open(script_name, 'w') as f:
        f.write("""#!/bin/bash
# -!- encoding:utf8 -!-
#
echo "[BASH]> starting grid crunching."
#
%s
#
echo "[BASH]> grid crunching done."
echo "[BASH]> starting heatmap generation."
#
%s
#
echo "[BASH]> heatmap generation done."
#
""" % ('\n'.join(reduce_cmds), '\n'.join(heatmap_cmds)))
    # print message
    print('[heatmap_creator.py]> %s generation done !' % script_name)
