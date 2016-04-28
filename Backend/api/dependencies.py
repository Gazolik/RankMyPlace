#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------------- IMPORTS

import os
from subprocess import call

# ----------------------------- FUNCTIONS
#
#   TODO : doc
#
def git_clone(url):
    print('[dependencies.py]> retrieving %s...' % url.split('/')[-1])
    call(['git','clone',url])
    print('[dependencies.py]> done !')
#
#   TODO : doc
#
def rem_dep(dep):
    print('[dependencies.py]> removing old dependency for %s...' % dep, end='')
    path = './'+dep
    if os.path.isdir(path):
            call(['rm','-rf',path])
    print('done !')
#
#   TODO : doc
#
def update_dependencies():
    # move in api dir
    os.chdir('api')
    try:
        # remove old dependencies if needed
        rem_dep('py_geo')
        rem_dep('py_rest')
        # cloning deps
        git_clone('https://github.com/pdautry/py_geo.git')
        git_clone('https://github.com/pdautry/py_rest.git')
    except Exception as e:
        print('[dependencies.py]> an error occured : %s' % e)
    finally:
        # get out of api dir
        os.chdir('..')
    



