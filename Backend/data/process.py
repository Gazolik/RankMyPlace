#!/usr/bin/python3
# -!- encoding:utf8 -!-

import sys, json

# ------------------------------------ SCRIPT PRE-CONDITION
if len(sys.argv) < 2:
    print('usage : ./process.py <json_origin_file>')
    exit()

# ------------------------------------ FUNCTIONS
def load_data(filename):
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        f.close()
        data = json.loads(content)
    return data

def dump_json(filename, data):
    parts = filename.split('/')[-1].split('.')
    del parts[-1]
    processed_file = 'processed/' + '.'.join(parts) + '_psd.json'
    with open(processed_file.lower(), 'w') as out:
        out.write(json.dumps(data, sort_keys=False))
        out.close()

# ----------------------------------- MAIN SCRIPT

# input & params
data = load_data(sys.argv[1])
out_data = []


for record in data['features']:
    out_data.append({
# main loop for TCL file
#             'coordinates' : {
#                 'lat':record['geometry']['coordinates'][0],
#                 'lon':record['geometry']['coordinates'][1]
#             },
#             'data' : {
#                 'nom':record['properties']['nom'],
#                 'desserte':record['properties']['desserte'],
#                 'escalator':(record['properties']['escalator'] == 't'),
#                 'pmr':(record['properties']['pmr'] == 't'),
#                 'ascenseur':(record['properties']['ascenseur'] == 't')
#             }
#
# main loop for velov
            'coordinates' : {
                'lat':record['geometry']['coordinates'][0],
                'lon':record['geometry']['coordinates'][1]
            },
            'data' : {
                'name':record['properties']['name'],
                'address':record['properties']['address'],
                'address2':record['properties']['address2'],
                'pole':record['properties']['pole'],
                'bike_stands':record['properties']['bike_stands'],
            }
         })

# main loop for vlov

# output
dump_json(sys.argv[1], out_data)
