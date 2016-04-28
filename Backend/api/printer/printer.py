#!/usr/bin/python3
# -!- encoding:utf8 -!-

# --------------------------- FUNCTIONS

def print_over(msg):
    print(msg + '\r', end='')

def print_progress(num, total, prefix=''):
    print_over(prefix + '%.2f%%' % (float(num)/total*100))
    