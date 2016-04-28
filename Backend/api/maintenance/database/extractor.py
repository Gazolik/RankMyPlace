#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------------ IMPORTS

from ...fs.fs import list_database_psd, load_database_psd, dump_database_psd 

# ------------------------------------ FUNCTIONS

def extract_coords():
    # retrieve files
    files = list_database_psd()
    # extract coords for each object
    for f in files:
        print('[extractor.py]> extracting coords from %s...' % f, end='')
        data = load_database_psd(f)
        out_coords = []
        for obj in data:
            out_coords.append(obj['coordinates'])
        # write output
        dump_database_psd(f+'_coord', out_coords)
        print('done !')
    

