#!/usr/bin/python3
# -!- encoding:utf8 -!-

# --------------- IMPORTS
import sys, json

# ----------------------------------- CONFIGURATION

INPUTS = {
    'TCL.json':['nom','desserte','bool:escalator','bool:pmr','bool:ascenseur'],
    'velov.json':['name','address','address2','pole','int:bike_stands'],   
    'bruit.json':['float:value'],
	'lieux_edifices.json':['nom','theme','soustheme'],
    'point_interet_touristique.json':['type','type_detail','nom','adresse','int:codepostal','commune','telephone','email','facebook','siteweb','producteur','tarifsmin','tarifsmax','tarifsenclair']
}

# ------------------------------------ FUNCTIONS

#
#   Lecture du fichier d'entrée
#
def load_data(filename):
    with open('origin/'+filename, 'r') as f:
        content = f.read()
        f.close()
        data = json.loads(content)
    return data

#
#   Ecriture du fichier de sortie normalisé
#
def dump_json(filename, data):
    parts = filename.split('/')[-1].split('.')
    del parts[-1]
    processed_file = 'processed/' + '.'.join(parts) + '_psd.json'
    with open(processed_file.lower(), 'w') as out:
        out.write(json.dumps(data, sort_keys=False))
        out.close()

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
def process_data(filename, props):
    try:
        print('> processing %s...' % filename, end='')
        # read file
        data = load_data(filename)
        out_data = []
        # fill out_data
        for record in data['features']:
            out_data.append(obj(record, props))
        # output
        dump_json(filename, out_data)
        print('done.')
    except Exception as e:
        print('failed ! An error occured, details below :')
        raise e

# ----------------------------------- MAIN SCRIPT

if len(sys.argv) > 1:
    if sys.argv[1] in INPUTS.keys():
        process_data(sys.argv[1], INPUTS[sys.argv[1]])
    else:
        print('> unknown input file, aborting. Bye !')
else:
    print('> processing all data files.')
    for fname in INPUTS.keys():
        process_data(fname, INPUTS[fname])        
    print('> all files processed. Bye.')


