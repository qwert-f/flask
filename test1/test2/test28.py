
class test(object):
    def __init__(self):
        self.__age = 14


obj = test()
v = obj._test__age
print(v)
# 面向对象私有字段
'''
Local对象作用
    --Local源码， threading.local相似，但又不同
    --Local是基于greenlet获取唯一标识，粒度更细
LocalStack对象作用
    --对Local对象中的数据进行操作
    --将local对象中的数据维护成一个栈
        Local = {
            1231:{stack:[ctx, ]}
        }
上下文管理
    --请求上下文：request/session
    --APP上下文：app/g
什么是g
获取session/g/current_app/request
'''
