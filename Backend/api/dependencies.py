#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ----------------------------- IMPORTS

import os
from subprocess import call

# ----------------------------- FUNCTIONS


def git_clone(url):
    """
        TODO : doc
    """
    print('[dependencies.py]> retrieving %s...' % url.split('/')[-1])
    call(['git', 'clone', url])
    print('[dependencies.py]> done !')


def rem_dep(dep):
    """
        TODO : doc
    """
    print('[dependencies.py]> removing old dependency for %s...' % dep, end='')
    path = './' + dep
    if os.path.isdir(path):
            call(['rm', '-rf', path])
    print('done !')


def update_dependencies():
    """
        TODO : doc
    """
    # move in api dir
    os.chdir('api')
    try:
        rem_dep('py_rest')
        git_clone('https://github.com/pdautry/py_rest.git')
    except Exception as e:
        print('[dependencies.py]> an error occured : %s' % e)
    finally:
        # get out of api dir
        os.chdir('..')
