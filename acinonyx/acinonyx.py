from functools import partial
from multiprocessing import Pool, cpu_count, freeze_support
from types import GeneratorType
from tqdm import tqdm
from acinonyx.utils import is_windows
from inspect import signature


def close(pool):
    """
    close pool
    :param pool:
    :return:
    """
    pool.close()
    pool.join()


def process(args, func):
    """
    execute function by args and function
    :param args: args of function
    :param func: function
    :return:
    """
    if not isinstance(args, (list, tuple)):
        args = [args]
    
    # check args
    sig = signature(func)
    params_length = len(sig.parameters)
    
    # call function
    if params_length == 0:
        return func()
    return func(*args)


def irun(func, iterable, total=None, processes=None, ordered=True):
    """
    run func with iterable using multiprocessing
    :param func: main function
    :param iterable: iterable data
    :param total: you must specify total is iterable is generator
    :param processes: number of processes
    :param ordered: keep order
    :return:
    """
    if is_windows():
        freeze_support()
    
    # set processes
    if not processes:
        processes = cpu_count()
    pool = Pool(processes=processes)
    
    # set total
    if total is None:
        total = None if isinstance(iterable, GeneratorType) else len(iterable)
    
    # call processor
    processor = pool.imap if ordered else pool.imap_unordered
    yield from tqdm(processor(partial(process, func=func), iterable), total=total)
    
    close(pool)


def run(func, iterable, total=None, processes=None, ordered=True):
    """
    run generator with same args
    :param func: main function
    :param iterable: iterable data
    :param total: you must specify total is iterable is generator
    :param processes: number of processes
    :param ordered: keep order
    :return:
    """
    return list(irun(func, iterable, total, processes, ordered))
