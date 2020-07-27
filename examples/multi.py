import time
from random import random
from acinonyx import run


def add(a, b):
    time.sleep(random())
    return a + b


if __name__ == '__main__':
    values = [(i, i) for i in range(100)]
    print(run(add, values))
