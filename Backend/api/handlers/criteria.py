#!/usr/bin/python3
# -!- encoding:utf8 -!-

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_static


def criterias_handler(path, data, api_params):
    """
        TODO : doc
    """
    criteres = load_static('criteres')
    name_list = []
    for k in criteres.keys():
        criteria = {'code': k,
                'name': criteres[k]['realname'],
                'groupe': criteres[k]['group'],
                'description': criteres[k]['description'],
                'type': criteres[k]['type'] }
        if criteres[k]['type'] == 'distance_based':
            criteria['dist'] = [criteres[k]['params']['min_dist'],criteres[k]['params']['max_dist']]
            criteria['dens'] = []
        elif criteres[k]['type'] == 'density_based':
            criteria['dist'] = []
            criteria['dens']=[criteres[k]['params']['min_density'],criteres[k]['params']['max_density']]

        elif criteres[k]['type'] == 'dist_dens_based':
            criteria['dist'] = [criteres[k]['params']['min_dist'],criteres[k]['params']['max_dist']]
            criteria['dens'] = [criteres[k]['params']['min_density'],criteres[k]['params']['max_density']]

        else:
            criteres[k]['dist'] = []
            criteres[k]['dens'] = []
        name_list.append(criteria)
    return Response(api_params).serialized({'criteres': name_list})
