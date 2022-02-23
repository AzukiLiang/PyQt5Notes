# coding=utf-8
import time
from functools import wraps


class Logit:
    """
    This is a class decorator for counting time
    """

    def __init__(self, logfile='out.log'):
        print("我实例化啦")
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def log_wrapper(*args, **kwargs):
            print("我已经被装饰好啦")
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 起始时间
            func(*args, **kwargs)  # 执行函数
            end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 结束时间
            print("Logging: func:{} runs from {} to {}".format(func.__name__, start_time, end_time))
            print('在{}中写入日志'.format(self.logfile))

        return log_wrapper


class CountTimeWrapper:
    """
    This is a class decorator for counting time
    """

    def __init__(self):
        print("我实例化啦")

    def __call__(self, func):
        @wraps(func)
        def count_time_wrapper(*args, **kwargs):
            print("我已经被装饰好啦")
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print("It takes {} s to find all the odds".format(end_time - start_time))

        return count_time_wrapper


@Logit('a.log')
@CountTimeWrapper()
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
