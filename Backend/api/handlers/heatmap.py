#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------------- IMPORTS

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_heatmap
from ..fs.fs import list_database_psd
from ..fs.fs import list_heatmap_grids
from ..fs.fs import load_static
from ..algorithm.algorithm import avg_heatmap
from ..algorithm.algorithm import isobarycenter
import json

# ---------------------------------- CONFIGURATION

GRID_SET = '_red_100_fgr'

# ---------------------------------- HANDLERS


def heatmap_base_handler(path, data, api_params):
    """
        Handler called on /heatmap route
        Return lists of available heatmap zone
    """
    data = [v for k, v in load_static('areas').items()]
    return Response(api_params).serialized({'data': data})


def heatmap_grid_handler(path, data, api_params):
    """
        Handler called on /heatmap route for one criteria and one zone 
    """
    data = {}
    parts = path.split('/')
    if len(parts) == 4:  # extract zone and criteria from route url ['','heatmap','<grid_name>','<criteria_name>']
        grid_basename = parts[2]
        criteria_name = parts[3]
        data['heatmap'] = load_heatmap(grid_basename + GRID_SET, criteria_name)['heatmap']
        data['zoom'] = 14
        data['center'] = isobarycenter(data['heatmap'])
    return Response(api_params).serialized(data)


def avg_heatmap_grid_handler(path, data, api_params):
    """
        Handler called on /heatmap route for one zone and all criterias
    """
    # usefull criterias extract
    d = json.loads(data['data'][0])
    criterias = d['criteres']
    parts = path.split('/')
    avg_map = avg_heatmap(parts[2], criterias, GRID_SET)
    return Response(api_params).serialized(avg_map)
