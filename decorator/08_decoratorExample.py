# coding=utf-8
import time
from functools import wraps


def logit(logfile='out.log'):
    print("我只执行了一次")

    def log_wrapper(func):
        @wraps(func)
        def improved_func(*args, **kwargs):
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 起始时间
            func(*args, **kwargs)  # 执行函数
            end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 结束时间
            print("Logging: func:{} runs from {} to {}".format(func.__name__, start_time, end_time))
            print('在{}中写入日志'.format(logfile))

        return improved_func

    return log_wrapper


def count_time_wrapper(func):
    """
    This is a function which can decorate func
    :param func: a function  need to be improved
    :return: improved_func
    """

    @wraps(func)
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


@logit('new_out.log')
@count_time_wrapper
def print_odds(lim=10000):
    """
    This is a function which can print odds among 1-lim
    :return: None
    """
    for i in range(lim):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    print_odds(5)
    print_odds(5)
    # print(print_odds.__name__)
    # print(print_odds.__doc__)
    # print(hasattr(print_odds, '__call__'))
