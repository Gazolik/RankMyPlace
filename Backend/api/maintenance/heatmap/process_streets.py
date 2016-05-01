#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------- IMPORTS

from subprocess import call
from ...fs.fs import list_heatmap_streets
from ...fs.fs import load_heatmap_streets
from ...fs.fs import dump_heatmap_grid
from ...fs.fs import dump_heatmap_psd
from ...printer.printer import print_progress

# ---------------------------- CONFIGURATION

baseurl = 'https://download.data.grandlyon.com/wfs/grandlyon'
params = {
    'SERVICE': 'WFS',
    'VERSION': '2.0.0',
    'outputformat': 'GEOJSON',
    'maxfeatures': '1000000000',
    'request': 'GetFeature',
    'typename': 'adr_voie_lieu.adraxevoie',
    'SRSNAME': 'urn:ogc:def:crs:EPSG::4171'
}

# ---------------------------- FUNCTIONS


def download_streets_data():
    """
        Récupère les données des rues en utilisant l'api du Grand Lyon
    """
    # build url
    url = baseurl + '?'
    for key, value in params.items():
        url += key + '=' + value + '&'
    url = url[:-1]
    # call wget
    print('[process_streets.py]> retrieving data...')
    call(['wget', '-O', list_heatmap_streets(), url])
    print('[data_processor.py]> done !')


def split_on_commune(data):
    """
        Création d'un dictionnaire indexé sur les communes pour les rues
    """
    # split data structure using 'nomcommune' field
    streets = data['features']
    communes = {}
    total = len(streets)
    i = 0
    print('[process_streets.py]> processing %s streets...' % total)
    for street in streets:
        i += 1
        if i % 100 == 0:
            print_progress(i, total)
        commune = street['properties']['nomcommune']
        if commune not in communes.keys():
            communes[commune] = []
        # add street to commune
        communes[commune].append({
            'nom': street['properties']['nom'],
            'coordinates': street['geometry']['coordinates']
        })
    print('[process_streets.py]> done !')
    return communes


def create_files(communes):
    """
        Génération des fichiers de sortie (psd, grille)
    """
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


def process_streets():
    """
        Découpage intégral du fichier streets.json en fichiers par commune
    """
    # load streets data
    streets = load_heatmap_streets()
    # split on communes
    communes = split_on_commune(streets)
    # create output files
    create_files(communes)


def update_streets_data():
    """
        Télécharge et lance le traitement des données
    """
    # download data
    download_streets_data()
    # process data
    process_streets()
