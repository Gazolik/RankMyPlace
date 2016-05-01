import time

DEBUG = True


def watch_time(func):
    """
        TODO : doc
    """
    def wrapper(*args):
        time_beg = time.time()
        ret = func(*args)
        time_end = time.time()
        print('[debug.watch_time] > %s function took %0.3f ms' % (func.__name__, (time_end - time_beg) * 1000.0))
        return ret
    if DEBUG:
        return wrapper
    else:
        return func
