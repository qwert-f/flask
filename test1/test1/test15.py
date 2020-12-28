from flask import Flask, session
'''
1.请求刚刚到达
ctx = RequestContext(...)
    - request
    - session = None
ctx.push()
    - ctx.session = SecureCookieSessionInterface.open_session
2.视图函数
3.请求结果
SecureCookieSessionInterface.save_session()
'''
app = Flask(__name__)
app.secret_key = 'test05'


@app.route("/index", methods=["POST", "GET"])
def index():
    # 去ctx中获取session
    session['a1'] = 123
    return "none"


@app.route("/test", methods=["POST", "GET"])
def test():
    print(session['a1'])
    return "none"


if __name__ == '__main__':
    app.run(debug=True)

    # 1.请求一旦到来
    # app.___call__
    # app.wsgi_app
    # app.open_session
