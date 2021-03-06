#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------- IMPORTS

from ...fs.fs import load_heatmap_grid
from ...fs.fs import dump_heatmap
from ...fs.fs import list_heatmap_psd
from ...fs.fs import list_heatmap_grids
from ...fs.fs import dump_heatmap_grid
from ...fs.fs import list_database_psd
from ...criteria.gen_criteria import rank
from ...criteria.criterias import criterias_dict
from ...algorithm.algorithm import reduce_precision_QCGR
from ...algorithm.algorithm import reduce_precision_FGR
from ...algorithm.algorithm import avg_geo_delta
from ...printer.printer import print_progress

# ---------------- FUNCTIONS


def gen_heatmap(grid_basename, criteria):
    """
        Génère une heatmap à partir d'une grille et d'un critère
    """
    print('[heatmap_creator.py]> generating %s heatmap for criteria %s...' % (grid_basename, criteria['name']))
    # read input file
    points = load_heatmap_grid(grid_basename)
    # iterate on points
    heatmap = []
    points_len = len(points)
    for i in range(points_len):
        print_progress(i, points_len)
        lat = points[i][1]
        lon = points[i][0]
        spec = {
            'criteria': criteria,
            # rappel lon est la plus petite valeur pour Lyon : aux alentours de 4
            'coordinates': {'lat': lat, 'lon': lon}
        }
        mark, ul1, ul2 = rank(spec)
        heatmap.append([round(lon, 5), round(lat, 5), round(mark, 2)])
    #
    print('[heatmap_creator.py]> done !')
    print('[heatmap_creator.py]> writing %s heatmap file...' % grid_basename, end='')
    # write output file
    dump_heatmap(grid_basename, criteria['name'], heatmap)
    print('done !')


def gen_all_heatmaps():
    """
        Génère toutes les heatmaps pour toutes les grilles et tous les critères
    """
    grids = list_heatmap_grids()
    for grid in grids:
        for key, criteria in criterias_dict.items():
            gen_heatmap(grid, criteria)


def reduced_grid_name(grid_basename, precision, method=None):
    """
        TODO : doc
    """
    method_name = 'fgr'
    if method == 'QCGR':
        method_name = 'qcgr'
    return grid_basename + '_red_%s_%s' % (int(precision), method_name)


def reduce_grid(grid_basename, precision, method=None):
    """
        Calcul de réduction de précision d'une grille
    """
    grid = load_heatmap_grid(grid_basename)
    print('[heatmap_creator.py]> cruching %s...' % grid_basename)
    #
    if method == 'QCGR':
        red_grid, ratio, removed, total = reduce_precision_QCGR(grid, precision)
    else:
        red_grid, ratio, removed, total = reduce_precision_FGR(grid, precision)
    #
    print('[heatmap_creator.py]> done !')
    print('[heatmap_creator.py]> reduction ratio is %.2f%% for grid %s. Details : removed = %s, total = %s' % (ratio * 100, grid_basename, removed, total))
    dump_heatmap_grid(reduced_grid_name(grid_basename, precision, method), red_grid)


def reduce_all(precision, method=''):
    """
        TODO : doc
    """
    grid_basenames = list_heatmap_grids()
    for grid_basename in grid_basenames:
        reduce_grid(grid_basename, precision, method)


def avg_grid(gridname):
    """
        TODO : doc
    """
    grid = load_heatmap_grid(gridname)
    moylat, moylon = avg_geo_delta(grid)
    print('[heatmap_creator.py]> for grid: %s, avg lat=%s, avg lon=%s...' % (gridname, moylat, moylon))


def gen_script(precision, method='QCGR'):
    """
        TODO : doc
    """
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
    # create script
    script = """#!/bin/bash
# -!- encoding:utf8 -!-
#
echo "[BASH]> starting grid crunching."
#
%s
#
echo "[BASH]> grid crunching done."
echo "[BASH]> starting heatmap generation."
#
""" % '\n'.join(reduce_cmds)
    # add heatmap commands
    heatmap_cmds_len = len(heatmap_cmds)
    for i in range(heatmap_cmds_len):
        script += heatmap_cmds[i] + '; '
        script += 'echo "[BASH]> overall progress : %s/%s"\n' % (i + 1, heatmap_cmds_len)
    # add script end
    script += """#
echo "[BASH]> heatmap generation done."
#
    """
    # write script file
    with open(script_name, 'w') as f:
        f.write(script)
    # print message
    print('[heatmap_creator.py]> %s generation done !' % script_name)
