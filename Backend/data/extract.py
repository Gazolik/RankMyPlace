#!/usr/bin/python3
# -!- encoding:utf8 -!-

import sys, json

if len(sys.argv) < 2:
    print('usage : ./extract.py <json_file>')
    exit()

with open(sys.argv[1], 'r') as f:
    content = f.read()
    obj = json.loads(content)
    print(json.dumps(obj['features'][0], sort_keys=False, indent=4))

