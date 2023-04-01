import time
import logging
from functools import wraps

def retry(max_tries = 3, delay_seconds = 1):
    '''Takes in a max_tries, delay_seconds and retry function'''
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry

def memoize(func):
    '''Takes in a function, using basic memoization with the map inside'''
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

def timing_decorator(func):
    '''Takes in a function, using basic timing library to show the time function get's to complete'''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper


def log_execution(func, log_level=logging.INFO):
    '''Log function using logging module and log_level setting'''
    logging.basicConfig(level=log_level)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result
    return wrapper
