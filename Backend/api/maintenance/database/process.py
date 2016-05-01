#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------------------- IMPORTS

from ...fs.fs import load_database_raw
from ...fs.fs import dump_database_pre_psd
from ...algorithm.algorithm import isobarycenter

import json

# ----------------------------------- CONFIGURATION

INPUTS = {
    'TCL': [
        'nom', 'desserte', 'bool:escalator', 'bool:pmr', 'bool:ascenseur'
    ],
    'velov': [
        'name', 'address', 'address2', 'pole', 'int:bike_stands'
    ],
    'bruit': ['float:value'],
    'lieux_edifices': [
        'nom', 'theme', 'soustheme'
    ],
    'point_interet_touristique': [
        'type', 'type_detail', 'nom',
        'adresse', 'int:codepostal',
        'commune', 'telephone', 'email',
        'facebook', 'siteweb', 'producteur',
        'tarifsmin', 'tarifsmax', 'tarifsenclair'
    ]
}

# ------------------------------------ FUNCTIONS


def coords(record):
    """
        Extraction des coordonnées du record
    """
    if record['geometry']['type'] == 'Point':
        return {
            'lat': record['geometry']['coordinates'][1],
            'lon': record['geometry']['coordinates'][0]
        }
    elif record['geometry']['type'] == 'Polygon':
        return isobarycenter(record['geometry']['coordinates'][0])
    else:
        return {'lat': 0.0, 'lon': 0.0}


def data(record, props):
    """
        Extraction des propriétés du record
    """
    properties = {}
    for prop in props:
        if ':' in prop:
            t = prop.split(':')[0]
            p = prop.split(':')[1]
            if t == 'bool':
                properties[p] = (record['properties'][p] == 't')
            elif t == 'int':
                properties[p] = int(record['properties'][p])
            elif t == 'float':
                properties[p] = float(record['properties'][p])
            else:
                properties[p] = record['properties'][p]
        else:
            properties[prop] = record['properties'][prop]
    return properties


def obj(record, props):
    """
        Création d'un objet normalisé à partir du record
    """
    return {
        'coordinates': coords(record),
        'data': data(record, props)
    }


def process_data(basename, props):
    """
        Execute le processus de traitement sur un fichier donné
    """
    try:
        print('[process.py]> processing %s...' % basename, end='')
        # read file
        data = load_database_raw(basename)
        out_data = []
        # fill out_data
        for record in data['features']:
            out_data.append(obj(record, props))
        # output
        dump_database_pre_psd(basename + '_psd', out_data)
        print('done.')
    except Exception as e:
        print('failed ! An error occured, details below :')
        raise e


def process_file(basename):
    """
        TODO : doc
    """
    if basename in INPUTS.keys():
        process_data(basename, INPUTS[basename])
    else:
        print('[process.py]> unknown input file, aborting. Bye !')


def process_all_files():
    """
        TODO : doc
    """
    print('[process.py]> processing all data files.')
    for basename in INPUTS.keys():
        process_data(basename, INPUTS[basename])
    print('[process.py]> all files processed. Bye.')
