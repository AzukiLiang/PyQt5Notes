# coding=utf-8
import time
from functools import wraps


def count_time_wrapper(func):
    """
    This is a function which can decorate func
    :param func: a function  need to be improved
    :return: improved_func
    """

    @wraps(func)
    def improved_func():
        """
        This is a function which can record how long func runs
        :return: None
        """
        start_time = time.time()
        func()
        end_time = time.time()
        print("It takes {} s to find all the odds".format(end_time - start_time))

    return improved_func


@count_time_wrapper
def print_odds():
    """
    This is a function which can print odds among 1-100
    :return: None
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    print_odds()
    print(print_odds.__name__)
    print(print_odds.__doc__)
    print(hasattr(print_odds, '__call__'))