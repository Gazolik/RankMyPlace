#!/usr/bin/python3
# -!- encoding:utf8 -!-

import sys, json

# ------------------------------------ SCRIPT PRE-CONDITION
if len(sys.argv) < 2:
    print('usage : ./process.py <json_origin_file>')
    exit()

# ------------------------------------ FUNCTIONS
def load_data(filename):
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        f.close()
        data = json.loads(content)
    return data

def dump_json(filename, data):
    parts = filename.split('.')
    del parts[-1]
    processed_file = 'processed/' + '.'.join(parts) + '.json'
    with open(processed_file, 'w') as out:
        out.write(json.dumps(data, sort_keys=False))
        out.close()

# ----------------------------------- MAIN SCRIPT

# input & params
data = load_data(sys.argv[1])
out_data = {}


# y a du boulot !

# output
dump_json(sys.argv[1], out_data)
