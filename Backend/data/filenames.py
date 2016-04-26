import json

from os import listdir
from os.path import isfile, join

def filenames() :
        files = [{"name" : "", "code" : f[:-5]} for f in listdir('database') if isfile(join('database', f))]
        with open('../static/criteres.json', 'w') as f :
                f.write(json.dumps(files))

filenames()
