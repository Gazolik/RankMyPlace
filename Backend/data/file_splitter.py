#!/usr/bin/python3
# -!- encoding:utf8 -!-

# --------------- IMPORTS
import sys, json

# ------------------------------------ FUNCTIONS

#
#   Lecture du fichier d'entrée
#
def load_data(filename):
    with open(filename, 'r') as f:
        content = f.read()
        f.close()
        data = json.loads(content)
    return data

#
#   Ecriture du fichier de sortie normalisé
#
def dump_json(filename, data):
    processed_file = 'processed/' + filename + '_psd.json'
    with open(processed_file.lower(), 'w') as out:
        out.write(json.dumps(data, sort_keys=False))
        out.close()

# ----------------------------------- MAIN SCRIPT
data = load_data('processed\point_interet_touristique_psd.json')

type_dic = {}

for element in data:
    #print(element)
    typ = element['data']['type']
    #print(typ)
    if not typ in type_dic.keys():
        type_dic[typ] = []
    # Ajout de l'élément dans le tableau correspondant au type
    type_dic[typ].append(element)

print(type_dic.keys())

# écriture des fichiers de sortie
for typ in type_dic.keys():
    dump_json('pit_' + typ, type_dic[typ])
