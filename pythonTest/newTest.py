class demoClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


class Singleton(object):

    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象

        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


if __name__ == '__main__':
    # example1
    test1 = demoClass("abc")
    test2 = demoClass("xyz")
    print(test1.number, test1.instances_created)
    print(test2.number, test2.instances_created)

    # example2
    obj1 = Singleton()
    obj2 = Singleton()
    obj1.attr1 = 'value1'
    print(obj1.attr1, obj2.attr1)
    print(obj1 is obj2)
