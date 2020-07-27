import unittest
import time
from random import random
from acinonyx import run


def log(val):
    """
    print val
    :param val:
    :return:
    """
    time.sleep(random())
    return val


def add(a, b):
    """
    get sum of a and b
    :param a:
    :param b:
    :return:
    """
    time.sleep(random())
    return a + b


class TestCase(unittest.TestCase):
    """
    Test acinonyx
    """
    def test_single_arg(self):
        """
        test single arg
        :return:
        """
        items = range(0, 100)
        result = run(log, items)
        self.assertEqual(len(result), len(items))
    
    def test_multi_args(self):
        """
        test multi args
        :return:
        """
        items = [(i, i) for i in range(0, 100)]
        result = run(add, items)
        self.assertEqual(len(result), len(items))


if __name__ == '__main__':
    unittest.main()
