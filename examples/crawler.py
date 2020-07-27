import requests
from random import random
import time
from acinonyx import irun


def fetch():
    delay = random()
    url = 'https://httpbin.org/uuid'
    time.sleep(delay)
    return requests.get(url).json().get('uuid')


if __name__ == '__main__':
    for result in irun(fetch, range(100), ordered=False):
        print(result)
