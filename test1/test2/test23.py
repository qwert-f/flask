from threading import local, Thread, get_ident
import time

# 内置local实现
obj = local()


def task(arg):
    # 执行后的值全部是一样的
    # global obj
    # obj = arg
    # 线程中执行时，为每一个线程开辟空间存储其值
    obj.value = arg
    time.sleep(2)
    # print(obj)
    print(obj.value)
    print(get_ident())


for i in range(10):
    t = Thread(target=task, args=(i, ))
    t.start()
# threading.local：为每一个线程开辟一块空间进行数据存储（并且线程之间是相互独立的）
