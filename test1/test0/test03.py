import functools

# 装饰器


def wapper(func):
    @functools.wraps(func)  # 让装饰器函数保持原名，不会在反向生成时，多个都为inner导致报错
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


'''
执行wapper函数，并将被装饰的函数当做参数，wapper(index)
将第一步的返回值，重新赋值给，新index = wapper(旧index)
'''


@wapper
def index(a):
    return a


@wapper
def order(a1):
    return a1


v = index(4)
print(v)
print(index.__name__)   # 没有装饰前函数名叫index
print(order.__name__)
