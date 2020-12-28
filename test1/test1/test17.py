from flask import Flask

app = Flask(__name__)


@app.before_request
def before():
    print('before')
    return "before"  # before返回后，不会执行视图函数


@app.before_request
def befores():
    print('befores')


@app.after_request
def after(request):
    print('after')
    return request


@app.after_request
def afters(request):
    print('afters')
    return request


@app.route("/index", methods=["POST", "GET"])
def index():
    print('index')
    return "index"


@app.route("/test", methods=["POST", "GET"])
def test():
    print('test')
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
