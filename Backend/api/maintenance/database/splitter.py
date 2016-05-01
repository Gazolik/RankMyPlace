#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------------ IMPORTS

from ...fs.fs import load_database_pre_psd
from ...fs.fs import dump_database_psd

# ------------------------------------ CONFIGURATION

INPUTS = {
    'point_interet_touristique_psd': {
        'prefix': 'pit_',
        'split_key': 'type'
    },
    'lieux_edifices_psd': {
        'prefix': 'le_',
        'split_key': 'theme'
    }
}

# ------------------------------------ FUNCTIONS


def split_on_key(basename, prefix, split_key):
    """
        TODO : doc
    """
    # load data from psd
    data = load_database_pre_psd(basename)
    # sort objects using split_key
    out_dict = {}
    for obj in data:
        # retrieve split_val
        split_val = obj['data'][split_key]
        # insert a new key and list in dict if missing
        if split_val not in out_dict.keys():
            out_dict[split_val] = []
        # add object to list for given split_val
        out_dict[split_val].append(obj)
    # for each split_val dump objlist in file
    for split_val, objlist in out_dict.keys():
        filename = prefix + split_val.replace(' ', '_').lower()
        dump_database_psd(filename, objlist)


def split_all():
    """
        TODO : doc
    """
    for basename, spec in INPUTS.items():
        split_on_key(basename, spec['prefix'], spec['split_key'])
