# Acinonyx

Asinoyx is a package which can simplify your multiprocessing implementation, also you 
can easily watch the progress of multiprocessing execution.

## Usage

A simple sample:

```python
import time
from random import random
from acinonyx import run

def log(val):
    time.sleep(random())
    return val

values = range(100)
print(run(log, values))
```

It will run with `cpu_count` processes and print progress bar, output is below:

```python
1%|█       | 1/100 [00:01<00:40,  2.29it/s]
26%|██       | 26/100 [00:01<00:32,  21.29it/s]
100%|██████████| 100/100 [00:03<00:00, 26.86it/s]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

Also you can use multiple args:

```python
import time
from random import random
from acinonyx import run

def add(a, b):
    time.sleep(random())
    return a + b

if __name__ == '__main__':
    values = [(i, i) for i in range(100)]
    print(run(add, values))
```

Also you can use it in other scenario such as web spider:

```python
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
    for result in irun(fetch, range(10), ordered=False):
        print(result)
```

## Trouble Shooting

### NSPlaceholderDate initialize error

```shell script
objc[67206]: +[__NSPlaceholderDate initialize] may have been in progress in another thread when fork() was called
```

Try to set env before execute script:
 
```shell script
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```