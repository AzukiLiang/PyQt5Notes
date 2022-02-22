# coding=utf-8
import time


def print_odds():
    start_time = time.time()
    for i in range(100):
        if i % 2 == 1:
            print(i)
    end_time = time.time()
    print("It takes {} s to find all the odds".format(end_time - start_time))


if __name__ == '__main__':
    print_odds()
