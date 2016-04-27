#!/usr/bin/python3
# -!- encoding:utf8 -!-

import json

data = {}
with open('streets.json', 'r') as f:
    data = json.load(f)

features = data['features']

# processing data structure splitting on comcommune

communes = {}
total = len(features)
i = 0
print('> processing %s streets...')
for feature in features:
    i += 1
    if i % 100 == 0:
        print('> progress %s/%s' % (i, total))
    commune = feature['properties']['nomcommune']
    if not commune in communes.keys():
        communes[commune] = []
    # add street to commune
    communes[commune].append({
        'nom':feature['properties']['nom'],
        'coordinates':feature['geometry']['coordinates']
    })
print('> done !')

# creating ouput files
for key, value in communes.items():
    filename = key.replace(' ','_')
    filename = filename.lower()
    if len(filename) == 0:
        filename = 'unamed'
    full_file = 'psd/' + filename + '_psd.json'
    print('> writing %s...' % full_file, end='')
    with open(full_file, 'w') as f:
        f.write(json.dumps(value))
    print('done !')
    coord_file = 'psd/' + filename + '_grid.json'
    print('> writing %s...' % coord_file, end='')
    coordinates = []
    for v in value:
        coordinates += v['coordinates']
    with open(coord_file, 'w') as f:
        f.write(json.dumps(coordinates))
    print('> done !')



