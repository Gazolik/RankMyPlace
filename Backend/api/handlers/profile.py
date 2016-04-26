#!/usr/bin/python3
# -!- encoding:utf8 -!-

import urllib.parse
import json

from ..py_rest.pyrest.rest_server.rest_api.response import Response

VERSION = 'profile v1.0'

def profiles_handler(path, data, api_params):
    msg = urllib.parse.unquote_plus(path.split('/')[-1])
    with open('../../profile/profiles.json') as f:
            data = json.load(f)
    print(data)
    return Response(api_params).serialized(data)
