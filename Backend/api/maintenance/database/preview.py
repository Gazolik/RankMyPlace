#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------ IMPORTS

from ...fs.fs import load_database_raw
from ...fs.fs import load_database_psd
import json

# ------------------------------ FUNCTIONS


def display(data):
    """
        Affiche une structure JSON correctement indentée
    """
    print('Record count : %s' % len(data))
    print(json.dumps(data[0], sort_keys=False, indent=4))


def preview_raw(basename):
    """
        TODO : doc
    """
    data = load_database_raw(basename)
    display(data['features'])


def preview_psd(basename):
    """
        TODO : doc
    """
    data = load_database_psd(basename)
    display(data)
