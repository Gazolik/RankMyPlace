#!/usr/bin/python3
# -!- encoding:utf8 -!-

# --------------------------- FUNCTIONS


def print_over(msg):
    """
        TODO : doc
    """
    print(msg + '\r', end='')


def print_progress(num, total, prefix='working...'):
    """
        TODO : doc
    """
    print_over(prefix + '%.2f%%' % (float(num) / total * 100))
