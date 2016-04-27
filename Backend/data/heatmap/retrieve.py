#!/usr/bin/python3
# -!- encoding:utf8 -!-

from subprocess import call

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

# build url
url = baseurl + '?'
for key, value in params.items():
    url += key + '=' + value + '&'

# url & output_file
url = url[:-1]
output_file = 'streets.json'

# call wget
print('> retrieving data...')
call(['wget','-O',output_file,url])
print('> done !')

