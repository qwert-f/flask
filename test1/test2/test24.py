from threading import get_ident, Thread
import time
# 自定义字典实现
storage = {}


def set(k, v):
    ident = get_ident()
    if ident in storage:
        storage[ident][k] = v
    else:
        storage[ident] = {k: v}


def get(k):
    ident = get_ident()
    return storage[ident][k]


def task(arg):
    set('val', arg)
    # 实现输出所有的i值
    time.sleep(1)
    v = get('val')
    print(v)


for i in range(10):
    t = Thread(target=task, args=(i, ))
    t.start()
# 基于函数实现
