"""
a simple app to report any python function's runtime
"""
import logging
import time
from datetime import datetime as dt

logging.basicConfig(level=logging.DEBUG)

# TODO: add verbose, debug modes


def test_say_stuff(words, time_to_sleep=0):
    if time_to_sleep:
        time.sleep(time_to_sleep)

    print(words)


def time_it(fn, *args, **kwargs):
    start_time = dt.now()

    print(f"{fn.__name__} started at {start_time}")

    fn(*args, **kwargs)
    end_time = dt.now()

    print(f"{fn.__name__} ended at {start_time}")

    print(f"{fn.__name__} took {(end_time - start_time)} to run")


time_it(test_say_stuff, "yo there dude hows it going?", time_to_sleep=2)

