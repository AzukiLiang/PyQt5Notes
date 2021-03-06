# coding=utf-8
import time
from functools import wraps


class Logit:
    """
    This is a class decorator for counting time
    """
    def __init__(self, func, logfile='out.log'):
        print("我实例化啦")
        self.func = func
        self.logfile = logfile

    def __call__(self, *args, **kwargs):
        print("我已经被装饰好啦")
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 起始时间
        self.func(*args, **kwargs)  # 执行函数
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 结束时间
        print("Logging: func:{} runs from {} to {}".format(self.func.__name__, start_time, end_time))
        print('在{}中写入日志'.format(self.logfile))


class CountTimeWrapper:
    """
    This is a class decorator for counting time
    """
    def __init__(self, func):
        print("我实例化啦")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("我已经被装饰好啦")
        start_time = time.time()
        self.func(*args, **kwargs)
        end_time = time.time()
        print("It takes {} s to find all the odds".format(end_time - start_time))

@Logit
# @CountTimeWrapper
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
    print_odds.func(5)
    print(print_odds.__class__)
    print(print_odds.__doc__)
    # print(print_odds.__name__)
    # print(print_odds.__doc__)
    # print(hasattr(print_odds, '__call__'))

    # print_odds = CountTimeWrapper(print_odds)
    # # countTimeWrapper.func(5)
    # print_odds(5)
    # print_odds(5)
