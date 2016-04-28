#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------------------- IMPORTS

from ...fs.fs import load_database_raw, dump_database_pre_psd

import json

# ----------------------------------- CONFIGURATION

INPUTS = {
    'TCL':[
        'nom','desserte','bool:escalator','bool:pmr','bool:ascenseur'
    ],
    'velov':[
        'name','address','address2','pole','int:bike_stands'
    ],   
    'bruit':['float:value'],
	'lieux_edifices':[
        'nom','theme','soustheme'
    ],
    'point_interet_touristique':[
        'type','type_detail','nom',
        'adresse','int:codepostal',
        'commune','telephone','email',
        'facebook','siteweb','producteur',
        'tarifsmin','tarifsmax','tarifsenclair'
    ]
}

# ------------------------------------ FUNCTIONS
#
#   Approximation du barycentre car coordonnées géographiques
#
def isobarycenter(coordinates):
    n = len(coordinates)
    sumlat = 0.0
    sumlon = 0.0
    for i in range(n):
        sumlat += coordinates[i][1]
        sumlon += coordinates[i][0]
    return { 'lat':sumlat/n, 'lon':sumlon/n }
#
#   Extraction des coordonnées du record
#
def coords(record):
    if record['geometry']['type'] == 'Point':
        return {
                'lat':record['geometry']['coordinates'][1],
                'lon':record['geometry']['coordinates'][0]
            }
    elif record['geometry']['type'] == 'Polygon':
        return isobarycenter(record['geometry']['coordinates'][0])
    else:
        return { 'lat':0.0, 'lon':0.0 }
#
#   Extraction des propriétés du record
#
def data(record, props):
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
#
#   Création d'un objet normalisé à partir du record
#
def obj(record, props):
    return {
        'coordinates' : coords(record),
        'data' : data(record, props)
    }
#
#   Execute le processus de traitement sur un fichier donné
#
def process_data(basename, props):
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
#
#   TODO : doc
#
def process_file(basename):
    if basename in INPUTS.keys():
        process_data(basename, INPUTS[basename])
    else:
        print('[process.py]> unknown input file, aborting. Bye !')
#
#   TODO : doc
#
def process_all_files():
    print('[process.py]> processing all data files.')
    for basename in INPUTS.keys():
        process_data(basename, INPUTS[basename])        
    print('[process.py]> all files processed. Bye.')

    


