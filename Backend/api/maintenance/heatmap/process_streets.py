#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------- IMPORTS

from subprocess import call
from ...fs.fs import list_heatmap_streets, load_heatmap_streets, dump_heatmap_grid, dump_heatmap_psd
from ...printer.printer import print_progress

# ---------------------------- CONFIGURATION

baseurl = 'https://download.data.grandlyon.com/wfs/grandlyon'
params = {
    'SERVICE':'WFS',
    'VERSION':'2.0.0',
    'outputformat':'GEOJSON',
    'maxfeatures':'1000000000',
    'request':'GetFeature',
    'typename':'adr_voie_lieu.adraxevoie',
    'SRSNAME':'urn:ogc:def:crs:EPSG::4171'
}

# ---------------------------- FUNCTIONS

#
#   Récupère les données des rues en utilisant l'api du Grand Lyon
#
def download_streets_data():
    # build url
    url = baseurl + '?'
    for key, value in params.items():
        url += key + '=' + value + '&'
    url = url[:-1]
    # call wget
    print('[process_streets.py]> retrieving data...')
    call(['wget', '-O', list_heatmap_streets(), url])
    print('[data_processor.py]> done !')

#
#   Création d'un dictionnaire indexé sur les communes pour les rues
#
def split_on_commune(data):
    # split data structure using 'nomcommune' field
    streets = data['features']
    communes = {}
    total = len(streets)
    i = 0
    print('[process_streets.py]> processing %s streets...' % total)
    for street in streets:
        i += 1
        if i % 100 == 0:
            print_progress(i, total, '[process_streets.py]> progress ')
        commune = street['properties']['nomcommune']
        if not commune in communes.keys():
            communes[commune] = []
        # add street to commune
        communes[commune].append({
            'nom':street['properties']['nom'],
            'coordinates':street['geometry']['coordinates']
        })
    print('[process_streets.py]> done !')
    return communes

#
#   Génération des fichiers de sortie (psd, grille)
#
def create_files(communes):
    # creating ouput files
    for commune, data in communes.items():
        print('[process_streets.py]> writing psd file for %s...' % commune, end='')
        dump_heatmap_psd(commune, data)
        print('done !')
        print('[process_streets.py]> writing grid file for %s...' % commune, end='')
        coordinates = []
        for elem in data:
            coordinates += elem['coordinates']
        dump_heatmap_grid(commune, coordinates)
        print('done !')

#
#   Découpage intégral du fichier streets.json en fichiers par commune
#
def process_streets():
    # load streets data
    streets = load_heatmap_streets()
    # split on communes
    communes = split_on_commune(streets)
    # create output files
    create_files(communes)

#
#   Télécharge et lance le traitement des données
#
def update_streets_data():
    # download data
    download_streets_data()
    # process data
    process_streets()

