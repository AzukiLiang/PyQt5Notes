# coding=utf-8
import time


def count_time_wrapper(func):
    """
    This is a function which can decorate func
    :param func: a function  need to be improved
    :return: improved_func
    """

    def improved_func(*args, **kwargs):
        """
        This is a function which can record how long func runs
        :return: None
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("It takes {} s to find all the odds".format(end_time - start_time))

    return improved_func


def print_odds(lim=100):
    """
    This is a function which can print odds among 1-100
    :return: None
    """
    for i in range(lim):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    print_odds_addedCountTime = count_time_wrapper(print_odds)
    print_odds_addedCountTime(1000)
    print(print_odds_addedCountTime.__name__)
    print(print_odds_addedCountTime.__doc__)
