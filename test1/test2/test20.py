from flask import Flask

app = Flask(__name__)
app.secret_key = 'sincos'


@app.route("/index", methods=["POST", "GET"])
def index():
    return "index"


class test(object):
    def __init__(self, old_wsgi_app):
        # 服务端启动时，自动执行
        self.old.wsgi_app = old_wsgi_app

    def __call__(self, *args, **kwargs):
        # 每次有用户请求时
        print('before')
        obj = self.wsgi_app(*args, **kwargs)
        print('after')
        return obj


if __name__ == '__main__':
    # app.wsgi_app = lamda x, y: x+y
    app.wsgi_app = test(app.wsgi_app)
    app.run(debug=True)
# 中间件，使用较少，请求时可以使用，但是一般都是用的request之类的
