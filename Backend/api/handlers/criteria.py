#!/usr/bin/python3
# -!- encoding:utf8 -!-

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_static

def criterias_handler(path, data, api_params):
    criteres = load_static('criteres')
    name_list = [{'code':k,'name':criteres[k]['realname'], 'groupe':criteres[k]['group'], 'description':criteres[k]['description']} for k in criteres.keys()]
    return Response(api_params).serialized({"criteres":name_list})