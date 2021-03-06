#!/usr/bin/python3
# -!- encoding:utf8 -!-

from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_static


def profiles_handler(path, data, api_params):
    """
        Handler called on /profiles route
        Return all predefined profiles and their coefs
    """
    return Response(api_params).serialized({'profiles': load_static('profiles')})
