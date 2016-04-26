from os import listdir
from os.path import isfile, join

def create_files() :
    filenames = [f[:-5] for f in listdir('../data/database')if isfile(join('../data/database', f))]
    for name in filenames :
        with open('./criteria/'+name+'.py', 'w') as fichier :
            fichier.write('from .gen_criteria import gen_criteria\nclass %s(gen_criteria): \n     def rank(self) : \n       pass'%name)

create_files()
