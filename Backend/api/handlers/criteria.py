#!/usr/bin/python3
# -!- encoding:utf8 -!-

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_static


def criterias_handler(path, data, api_params):
    database_datas = load_static('criteres')
    group_list = []
    groups = database_datas['groupes']
    for data in groups.keys() :
        group = groups[data]
        criterias = group['membres']
        criterias_list = [{'code':k,'name':criterias[k]['realname'], 'description':criterias[k]['description']} for k in criterias.keys()]
        group_list.append({'name':group['name'], 'description':group['description'], 'membres':criterias_list, 'ordre':group['ordre']})
   
    return Response(api_params).serialized({'groupes':group_list})