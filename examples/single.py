import time
from random import random
from acinonyx import run


def log(val):
    time.sleep(random())
    return val


if __name__ == '__main__':
    values = range(100)
    print(run(log, values))
