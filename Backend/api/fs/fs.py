
import json
import os
import re

# /!\
#   Toutes les méthodes supposent que le script appelant (main) est à la racine du Backend/
# /!\

# ---------------------------------------- CONFIGURATION

# file encoding for reading
ENCODING = 'latin-1'
# roots
STATIC = './static'
DATA = './data'
# database
DATABASE = DATA + '/database'
DATABASE_RAW = DATABASE + '/raw'
DATABASE_PRE_PSD = DATABASE + '/pre_psd'
DATABASE_PSD = DATABASE + '/psd'
DATABASE_COORD = DATABASE + '/psd'
# heatmap
HEATMAP = DATA + '/heatmap'
STREETS = 'streets'
HEATMAP_STREETS = HEATMAP + '/'+ STREETS +'.json'
HEATMAP_PSD = HEATMAP + '/psd'
HEATMAP_MAPS = HEATMAP + '/maps'


# ---------------------------------------- LIST FUNCTIONS
#
#   TODO : doc
#
def basify(files, remove):
    kept = []
    #remove all non needed files
    for i in range(len(files)):
        if remove in files[i]:
            kept.append(files[i].replace(remove,''))
    return kept

#
#   Retourne une liste des fichiers statiques
#
def list_static():
    return basify(os.listdir(STATIC), '.json')
#
#   Retourne une liste des fichiers de type grille
#
def list_heatmap_grids():
    return basify(os.listdir(HEATMAP_PSD),'_grid.json')

#
#   Retourne une liste des fichiers de type psd
#
def list_heatmap_psd():
    return basify(os.listdir(HEATMAP_PSD), '_psd.json')
#
#   TODO : doc
#
def list_heatmap_streets():
    return HEATMAP_STREETS
#
#   TODO : doc
#
def list_database_raw():
    return basify(os.listdir(DATABASE_RAW), '.json')
#
#   TODO : doc
#
def list_database_pre_psd():
    return basify(os.listdir(DATABASE_PRE_PSD), '.json')
#
#   TODO : doc
#
def list_database_psd():
    return basify(os.listdir(DATABASE_PSD), '_psd.json')

#
#    TODO:doc
#
def list_database_coord():
    return basify(os.listdir(DATABASE_COORD), '_coord.json')
#
# ---------------------------------------- LOAD FUNCTIONS
#
#   TODO : doc
#
def json_load(path, basename):
    data = None
    try :
        with open(path + '/' + basename + '.json', 'r', encoding=ENCODING) as f:
            data = json.load(f)
    except Exception as e :
        print('[fs.json_load] File cannot be opened : %s' % e)
    finally :
        return data
#
#   TODO : doc
#
def load_static(basename):
    return json_load(STATIC, basename)
#
#   TODO : doc
#
def load_heatmap_grid(basename):
    return json_load(HEATMAP_PSD, basename + '_grid')
#
#   TODO : doc
#
def load_heatmap_psd(basename):
    return json_load(HEATMAP_PSD, basename + '_psd')
#
#   TODO : doc
#
def load_heatmap_streets():
    return json_load(HEATMAP, STREETS)
#
#   TODO : doc
#
def load_database_raw(basename):
    return json_load(DATABASE_RAW, basename)
#
#   TODO : doc
#
def load_database_pre_psd(basename):
    return json_load(DATABASE_PRE_PSD, basename)
#
#   TODO : doc
#
def load_database_psd(basename):
    return json_load(DATABASE_PSD, basename+'_psd')

#
# TODO:doc
#
def load_data(basename, idx):
    data_list = json_load(DATABASE_DATA, basename+'_dat')
    return data_list[idx]
#
# ---------------------------------------- DUMP FUNCTIONS
#
#   TODO : doc
#
def json_dump(filepath_no_ext, data):
    try :
        with open(filepath_no_ext + '.json', 'w') as f:
            f.write(json.dumps(data, sort_keys=False))
    except Exception as e :
        print('[fs.json_dump] Error while writing file %s'.format(e))
#
#   TODO : doc
#
def dump_static(basename, data):
    json_dump(STATIC + '/' + basename, data)
#
#   TODO : doc
#
def dump_heatmap_grid(commune, coordinates):
    basename = re.sub('[^\w\.]','',commune).lower()
    if len(basename) == 0:
        basename = 'unnamed'
    filepath = HEATMAP_PSD + '/' + basename + '_grid'
    json_dump(filepath, coordinates)
#
#   TODO : doc
#
def dump_heatmap_psd(commune, data):
    basename = re.sub('[^\w\.]','',commune).lower()
    if len(basename) == 0:
        basename = 'unnamed'
    filepath = HEATMAP_PSD + '/' + basename + '_psd'
    json_dump(filepath, data)
#
#   Génère un fichier de heatmap pour le critere donné et la grille donnée
#
def dump_heatmap(grid_basename, criteria_name, heatmap):
    filepath = HEATMAP_MAPS + '/' + grid_basename + '_' + criteria_name + '_heatmap'
    json_dump(filepath, { 'criteria' : criteria_name, 'heatmap' : heatmap })
#
#   TODO : doc
#
def dump_database_pre_psd(basename, data):
    return json_dump(DATABASE_PRE_PSD + '/' + basename, data)
#
#   TODO : doc
#
def dump_database_psd(basename, data):
    return json_dump(DATABASE_PSD + '/' + basename, data)



