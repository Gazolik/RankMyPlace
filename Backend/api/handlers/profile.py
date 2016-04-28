#!/usr/bin/python3
# -!- encoding:utf8 -!-

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_static

def profiles_handler(path, data, api_params):
    return Response(api_params).serialized(load_static('profiles'))
