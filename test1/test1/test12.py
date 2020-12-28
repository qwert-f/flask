from flask import Flask, views
import functools

app = Flask(__name__)

# FBV


def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return inner


@app.route("/test", methods=["POST", "GET"])
@wapper
def test():
    return "none"


# CBV


class IndexView(views.View):
    metmethods = ['GET']
    decdecorators = [wapper, ]

    def disdispatch_request(self):
        print("Index")
        return 'Index!'


app.add_url_rule('/index', view_func=IndexView(name='index'))


class Login(views.MethodView):
    methods = ['POST', 'GET']
    # 如果需要在CBV中加装饰器的话,括号里就是装饰器的内存地址，可以传多个
    decorators = [wapper, ]

    def get(self):
        print('get 请求')
        return 'login get'

    def post(self):
        print('post 请求')
        return 'login post'


app.add_url_rule('/login', view_func=Login.as_view(name='login'))


if __name__ == '__main__':
    app.run(debug=True)
