from flask import Flask, g

app = Flask(__name__)
# arg = 'i'


@app.before_request
def sd():
    arg = 123
    bf(arg)


def bf(arg):
    # global arg
    g.x = arg
    return arg


@app.route("/index", methods=["POST", "GET"])
def index():
    g.x = 123
    return "index"


@app.route("/test", methods=["POST", "GET"])
def test():
    # 在index路由中声明g.x，请求结束，就销毁了无法在test路由中调用
    # 使用before_request声明，可全局调用
    print(g.x)
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
'''
from functools import partial


def fname(arg):
    print(arg)


new_func = partial(fname)
new_func(1234)'''
