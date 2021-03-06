from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        print('我实例化啦')
        self.logfile = logfile

    def __call__(self, func):
        print("我call啦")
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass


# class B:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = 3
#         self.myfunc1(1, 2, 3)
#
#     @logit()
#     def myfunc1(self, a, b, c):
#         print(self, a, b, c)
#
#
# aaa = B()

# @logit('out2.log')
# def myfunc1(a):
#     return a


# b = myfunc1(1)
# print(b)
# c = myfunc1(2)
