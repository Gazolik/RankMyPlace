
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
HEATMAP_STREETS = HEATMAP + '/' + STREETS + '.json'
HEATMAP_GRIDS = HEATMAP + '/grids'
HEATMAP_PSD = HEATMAP + '/psd'
HEATMAP_MAPS = HEATMAP + '/maps'

# ---------------------------------------- LIST FUNCTIONS


def basify(files, remove):
    """
        TODO : doc
    """
    kept = []
    # remove all non needed files
    for i in range(len(files)):
        if remove in files[i]:
            kept.append(files[i].replace(remove, ''))
    return kept


def list_static():
    """
        Retourne une liste des fichiers statiques
    """
    return basify(os.listdir(STATIC), '.json')


def list_heatmap_grids():
    """
        TODO : doc
    """
    return basify(os.listdir(HEATMAP_GRIDS), '_grid.json')


def list_heatmap_psd():
    """
        TODO : doc
    """
    return basify(os.listdir(HEATMAP_PSD), '_psd.json')


def list_heatmap_streets():
    """
        TODO : doc
    """
    return HEATMAP_STREETS


def list_database_raw():
    """
        TODO : doc
    """
    return basify(os.listdir(DATABASE_RAW), '.json')


def list_database_pre_psd():
    """
        TODO : doc
    """
    return basify(os.listdir(DATABASE_PRE_PSD), '.json')


def list_database_psd():
    """
        TODO : doc
    """
    return basify(os.listdir(DATABASE_PSD), '_psd.json')


def list_database_coord():
    """
        TODO : doc
    """
    return basify(os.listdir(DATABASE_COORD), '_coord.json')

# ---------------------------------------- LOAD FUNCTIONS


def json_load(path, basename):
    """
        TODO : doc
    """
    data = None
    try:
        with open(path + '/' + basename + '.json', 'r', encoding=ENCODING) as f:
            data = json.load(f)
    except IOError as e:
        print('[fs.json_load]> File cannot be opened : %s' % e)
    finally:
        return data


def load_static(basename):
    """
        TODO : doc
    """
    return json_load(STATIC, basename)


def load_heatmap_grid(basename):
    """
        TODO : doc
    """
    return json_load(HEATMAP_GRIDS, basename + '_grid')


def load_heatmap_psd(basename):
    """
        TODO : doc
    """
    return json_load(HEATMAP_PSD, basename + '_psd')


def load_heatmap_streets():
    """
        TODO : doc
    """
    return json_load(HEATMAP, STREETS)


def load_heatmap(grid_basename, criteria_name):
    """
        TODO : doc
    """
    return json_load(HEATMAP_MAPS, grid_basename + '_' + criteria_name + '_map')


def load_database_raw(basename):
    """
        TODO : doc
    """
    return json_load(DATABASE_RAW, basename)


def load_database_pre_psd(basename):
    """
        TODO : doc
    """
    return json_load(DATABASE_PRE_PSD, basename)


def load_database_psd(basename):
    """
        TODO : doc
    """
    return json_load(DATABASE_PSD, basename + '_psd')


def load_data(basename, idx):
    """
        TODO : doc
    """
    data_list = json_load(DATABASE_DATA, basename + '_dat')
    return data_list[idx]

# ---------------------------------------- DUMP FUNCTIONS


def json_dump(filepath_no_ext, data, indent=None):
    """
        TODO : doc
    """
    try:
        with open(filepath_no_ext + '.json', 'w') as f:
            f.write(json.dumps(data, sort_keys=False, indent=indent))
    except IOError as e:
        print('[fs.json_dump] Error while writing file %s'.format(e))


def dump_static(basename, data, indent=None):
    """
        TODO : doc
    """
    json_dump(STATIC + '/' + basename, data, indent)


def dump_heatmap_grid(commune, coordinates, indent=None):
    """
        TODO : doc
    """
    basename = re.sub('[^\w\.]', '', commune).lower()
    if len(basename) == 0:
        basename = 'unnamed'
    filepath = HEATMAP_GRIDS + '/' + basename + '_grid'
    json_dump(filepath, coordinates, indent)


def dump_heatmap_psd(commune, data, indent=None):
    """
        TODO : doc
    """
    basename = re.sub('[^\w\.]', '', commune).lower()
    if len(basename) == 0:
        basename = 'unnamed'
    filepath = HEATMAP_PSD + '/' + basename + '_psd'
    json_dump(filepath, data, indent)


def dump_heatmap(grid_basename, criteria_name, heatmap, indent=None):
    """
        Génère un fichier de heatmap pour le critere donné et la grille donnée
    """
    filepath = HEATMAP_MAPS + '/' + grid_basename + '_' + criteria_name + '_map'
    json_dump(filepath, {'criteria': criteria_name, 'heatmap': heatmap}, indent)


def dump_database_pre_psd(basename, data, indent=None):
    """
        TODO : doc
    """
    return json_dump(DATABASE_PRE_PSD + '/' + basename, data, indent)


def dump_database_psd(basename, data, indent=None):
    """
        TODO : doc
    """
    return json_dump(DATABASE_PSD + '/' + basename, data, indent)
