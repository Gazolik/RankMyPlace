#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------- IMPORTS

#
#   Définit une fonction permettant de récupérer les dépendances
#
from api.dependencies import update_dependencies
#
#
#
from api.fs.fs import list_static, list_heatmap_grids, list_heatmap_psd, list_database_raw, list_database_pre_psd, list_database_psd
#
#   Définit des fonction de pre-processing des données géolocalisée brutes du Grand Lyon
#
from api.maintenance.database.process import process_file, process_all_files
#
#   Définit des fonction de séparation des données après la phase de preprocessing
#
from api.maintenance.database.splitter import split_on_key, split_all
#
#   Définit des fonction de séparation des données pour extraires les coordonnées
#
from api.maintenance.database.extractor import extract_coords
#
#   Définit des fonctions de visualisation d'extrait de données des fichiers de données
#
from api.maintenance.database.preview import preview_raw, preview_psd
#
#   Définit des fonctions pour la récupération des données et de construction de la grille à partir de ces dernières
#
from api.maintenance.heatmap.process_streets import update_streets_data, download_streets_data, process_streets
#
#   Définit des fonctions permettant de visualiser les données de la grille
#
from api.maintenance.heatmap.drawer import draw_map_part, draw_map
#
#   Définit des fonctions permettant de construire des cartes de chaleur à partir de la grille et des critères
#
<<<<<<< HEAD
from api.maintenance.heatmap.heatmap_creator import gen_heatmap, gen_all_heatmaps, reduce_grid, reduce_all
=======
from api.maintenance.heatmap.heatmap_creator import gen_heatmap, gen_all_heatmaps, avg_grid
#
>>>>>>> 1ea20ed3ee7f940bdd79c1d8e82d80e346a44a04
#
#
from api.criteria.criterias import criterias_dict

import sys, os

# ----------------------- FUNCTIONS

def abort(msg):
    print('[maintenance.py]> ' + msg)
    print('-----------------------------\n[maintenance.py]> aborted !')
    exit()

def assert_args(min_size, msg):
    if len(sys.argv) < min_size:
        abort(msg)

# ------------------------- COMMANDS FUNCTIONS

def cmd_help():
    print('[maintenance.py]> Help yourself !')

def cmd_list(category):
    files = []
    if category == 'static':
        files = list_static()
    elif category == 'heatmap_grids':
        files = list_heatmap_grids()
    elif category == 'heatmap_psd':
        files = list_heatmap_psd()
    elif category == 'database_raw':
        files = list_database_raw()
    elif category == 'database_pre_psd':
        files = list_database_pre_psd()
    elif category == 'database_psd':
        files = list_database_psd()
    else:
        abort('[maintenance.py]> unknown category to list, type "help list" to get a list of categories.')
    # print file list
    print('Listing %s files for %s :\n  +    ' % (len(files), category) + '\n  +    '.join(files))

# ----------------------- SCRIPT

print('[maintenance.py]> working from "%s"\n-----------------------------' %os.getcwd())

# vérification des paramètres
assert_args(2, 'usage : ./maintenance.py <command> [<options>]')
# récupération de la commande
command = sys.argv[1]
# traitement de la commande
if command == 'help':
    cmd_help()
elif command == 'list':
    assert_args(3, 'missing category after list')
    cmd_list(sys.argv[2])
elif command == 'preview_raw':
    assert_args(3, 'missing filename after preview_raw')
    preview_raw(sys.argv[2])
elif command == 'preview_psd':
    assert_args(3, 'missing filename after preview_psd')
    preview_psd(sys.argv[2])
elif command == 'update_dependencies':
    update_dependencies()
elif command == 'gen_heatmap':
    assert_args(3, 'missing grid_basename after gen_heatmap')
    gen_heatmap(sys.argv[2],criterias_dict['le_deplacement'])
elif command == 'gen_all_heatmaps':
    gen_all_heatmaps()
elif command == 'reduce_grid':
    assert_args(4, 'missing grid_basename or/and precision after reduce_grid')
    reduce_grid(sys.argv[2], int(sys.argv[3]))
elif command == 'reduce_all':
    assert_args(3, 'missing precision after reduce_all')
    reduce_all(int(sys.argv[2]))
elif command == 'process_streets':
    process_streets()
elif command == 'process_all_files':
    process_all_files()
elif command == 'extract_coords':
    extract_coords()
elif command == 'draw_map_part':
    assert_args(3, 'missing grid_basename after draw_map_part')
    draw_map_part(sys.argv[2])
elif command == 'draw_map':
    draw_map()
elif command == 'avg_grid':
    assert_args(3, 'missing gridname after avg_coord')
    avg_grid(sys.argv[2])
else:
    abort('[maintenance.py]> unknown command !')

print('-----------------------------\n[maintenance.py]> done !')


