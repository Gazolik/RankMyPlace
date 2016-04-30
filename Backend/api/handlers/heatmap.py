#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------------- IMPORTS

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_heatmap, list_database_psd, list_heatmap_grids,load_static
from ..algorithm.algorithm import avg_heatmap, isobarycenter
import json

# ---------------------------------- CONFIGURATION

GRID_SET = '_red_100_fgr'

# ---------------------------------- HANDLERS
#
#
#
def heatmap_base_handler(path, data, api_params):

    data = [v for k,v in load_static('areas').items()]
    print(data)
    return Response(api_params).serialized({'data':data})
#
# Calcul une heatmap d'un critere
#
def heatmap_grid_handler(path, data, api_params):
    data = {}
    parts = path.split('/')
    if len(parts) == 4: # on attend ['','heatmap','<grid_name>','<criteria_name>']
        grid_basename = parts[2]
        criteria_name = parts[3]
        data['heatmap'] = load_heatmap(grid_basename+GRID_SET, criteria_name)['heatmap']
        data['zoom'] = 14
        data['center'] = isobarycenter(data['heatmap'])
    return Response(api_params).serialized(data)


#
# Calcul une heatmap de plusieurs criteres
#
def avg_heatmap_grid_handler(path, data, api_params):
    #extraction des criteres utiles
    d = json.loads(data['data'][0])
    criteres = d['criteres']
    nomcriteres = [k for k,v in criteres.items() if v != 0]
    parts = path.split('/')
    avg_map = avg_heatmap(parts[2], criteres, GRID_SET)
    return Response(api_params).serialized(avg_map)




