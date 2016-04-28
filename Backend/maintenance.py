#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------- IMPORTS

#
#   Définit une fonction permettant de récupérer les dépendances
#
from api.dependencies import update_dependencies
#
#   Définit des fonction de pre-processing des données géolocalisée brutes du Grand Lyon
#
from api.maintenance.database.process import process_file, process_all_files
#
#   Définit des fonction de séparation des données après la phase de preprocessing
#
from api.maintenance.database.splitter import split_on_key, split_all
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
from api.maintenance.heatmap.heatmap_creator import gen_heatmap, gen_all_heatmaps

import sys, os

# ----------------------- FUNCTIONS

def assert_args(min_size, msg):
    if len(sys.argv) < min_size:
        print('[maintenance.py]> ' + msg)
        exit()

# ----------------------- SCRIPT

print('[maintenance.py]> working from "%s"' %os.getcwd())

# vérification des paramètres
assert_args(2, 'usage : ./maintenance.py <command> [<options>]')
# récupération de la commande
command = sys.argv[1]
# traitement de la commande
if command == 'help':
    print('[maintenance.py]> Help yourself !')
elif command == 'preview_raw':
    assert_args(3, 'missing filename after preview_raw')
    preview_raw(sys.argv[2])
elif command == 'preview_psd':
    assert_args(3, 'missing filename after preview_psd')
    preview_psd(sys.argv[2])
elif command == 'update_dependencies':
    update_dependencies()
else:
    print('[maintenance.py]> unknown command !')
    exit()

print('[maintenance.py]> done !')

