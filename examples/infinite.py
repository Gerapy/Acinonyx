import time
from random import random
from acinonyx import run


def log(val):
    time.sleep(random())
    return val


def data():
    count = 0
    while True:
        yield count
        count += 1


if __name__ == '__main__':
    run(log, data())
