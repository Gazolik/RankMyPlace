#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------ IMPORTS

from ...fs.fs import load_database_raw, load_database_psd
import json

# ------------------------------ FUNCTIONS
#
#   Affiche une structure JSON correctement indentée
#
def display(data):
    print('Record count : %s' % len(data))
    print(json.dumps(data[0], sort_keys=False, indent=4))
#
#   TODO : doc
#
def preview_raw(basename):
    data = load_database_raw(basename)
    display(data['features'])
#
#   TODO : doc
#
def preview_psd(basename):
    data = load_database_psd(basename)
    display(data)


