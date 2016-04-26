#!/usr/bin/python3
# -!- encoding:utf8 -!-

from subprocess import call

def git_clone(url):
    print('> retrieving %s...' % url.split('/')[-1])
    call(['git','clone',url])
    print('done !')

def cmd(args):
    call(args)

print('> removing all dependencies...', end='')
cmd(['rm','-rf','py_geo/','py_rest/'])
print('done !')
git_clone('https://github.com/pdautry/py_geo.git')
git_clone('https://github.com/pdautry/py_rest.git')


