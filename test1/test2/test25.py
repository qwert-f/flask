from threading import get_ident, Thread
# import time


class test(object):
    def __init__(self):
        # 循环调用，导致出错
        # self.storage = {}
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return self.storage[ident][k]


obj = test()
obja = test()


def task(arg):
    obj.val = arg
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i, ))
    t.start()

# class test(object):
#     # 静态字段用类直接可以调用，包含构造方法时用self
#     storage = {}
#
#     def __setattr__(self, k, v):
#         ident = get_ident()
#         if ident in test.storage:
#             test.storage[ident][k] = v
#         else:
#             test.storage[ident] = {k: v}
#
#     def __getattr__(self, k):
#         ident = get_ident()
#         return test.storage[ident][k]
#
#
# obj = test()
#
#
# def task(arg):
#     obj.val = arg
#     print(obj.val)
#
#
# for i in range(10):
#     t = Thread(target=task, args=(i, ))
#     t.start()

# class test(object):
#     # 静态字段用类直接可以调用，包含构造方法时用self
#     storage = {}
#
#     def set(self, k, v):
#         ident = get_ident()
#         if ident in test.storage:
#             test.storage[ident][k] = v
#         else:
#             test.storage[ident] = {k: v}
#
#     def get(self, k):
#         ident = get_ident()
#         return test.storage[ident][k]
#
#
# obj = test()
#
#
# def task(arg):
#     obj.set('val', arg)
#     time.sleep(1)
#     v = obj.get('val')
#     print(v)
#
#
# for i in range(10):
#     t = Thread(target=task, args=(i, ))
#     t.start()
