#!/usr/bin/python3
# -!- encoding:utf8 -!-

from subprocess import call

def git_clone(url):
    call(['git','clone',url])

def cmd(args):
    call(args)

git_clone('https://github.com/pdautry/py_geo.git')
git_clone('https://github.com/pdautry/py_rest.git')


