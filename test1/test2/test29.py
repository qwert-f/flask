from flask import Flask, session
# from flask_session import RedisSessionInterface
from flask_session import Session
# from flask.ext.session import Session在新的flask中已不支持这种方式
from redis import Redis

app = Flask(__name__)
app.secret_key = 'sincos'

'''
默认是下面的这个session在cookie中
from flask_session import SecureCookieSessionInterface
app.session_interface = SecureCookieSessionInterface()
代码中将session保存到redis中
'''
# 方法一
# app.session_interface = RedisSessionInterface(
#     redis=Redis(host='127.0.0.1', port='6379', password='redis1'),
#     # 前缀
#     key_prefix='flask'
# )
# 方法二
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(
    host='127.0.0.1', port='6379', password='redis1')
Session(app)


@app.route("/test", methods=["POST", "GET"])
def test():
    session['k1'] = 123
    return "test"


@app.route("/index", methods=["POST", "GET"])
def index():
    v = session['k1']
    print(v)
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
