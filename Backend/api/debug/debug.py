import time



DEBUG = True


def watch_time(func):
    def wrapper(*args):
        time_beg = time.time()
        ret = func(*args)
        time_end = time.time()
        print('%s function took %0.3f ms' % (func.func_name, (time_end - time_beg)*1000.0))
        return ret
    if DEGUB:
        return wrapper
    else:
        return func
