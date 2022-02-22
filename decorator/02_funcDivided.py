# coding=utf-8
import time


def count_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("It takes {} s to find all the odds".format(end_time - start_time))


def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    count_time(print_odds)
    print(print_odds.__name__)
