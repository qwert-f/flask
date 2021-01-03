# class A(object):
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(object):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(D.__mro__)
# # 面向对象相关
# # __mro__找到当前类寻找属性的顺序
#
#
# class Foo(object):
#     CTY = 'bj'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         pass
#
#
# print(Foo.CTY)
# print(Foo.func)
# print(Foo.__dict__)
#
# # 创建类的两种方式
#
#
# class test(object):
#     X = 'x'
#
#     def func(self, x):
#         return x+1
#
#
# test1 = type('test1', (object), {'X': 'x', 'func': lambda self, x: x+1})


# 默认当前类由type类创建
# 类由type创建，通过metaclass可以指定当前类由那一个type创建
class MyType(type):
    def __init__(self, *args, **kwargs):
        print("before")
        super(MyType, self).__init__(*args, **kwargs)
        print("after")


class F(object, metaclass=MyType):
    # class F(object, metaclass=type):
    CTY = 'sh'

    def Ff(self, x):
        return x+1


# 类的继承
# 类的基类中指定了metaclass,那么当前类也是由metaclass指定的类来创建
class Ba(F):
    pass


def meta():
    return MyType('base', (object,), {})


class As(meta()):
    pass
