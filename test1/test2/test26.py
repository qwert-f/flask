from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'sincos'


@app.route("/index", methods=["POST", "GET"])
def index():
    print(request)  # LocalProxy.__str__
    # LocalProxy.__getattr__(key='method');ctx中request,再去request中获取method
    request.method
    # LocalProxy.__getattr__(key='args');ctx中request,再去request中获取args
    request.args
    # LocalProxy.__getitem__(key=k1, value=123);ctx中session,再去session中设置k1的值
    session['k1'] = 123
    # LocalProxy.__getitem__(key='k1');ctx中session,再去session中获取k1对应的值
    session['k1']
    return "index"


if __name__ == '__main__':
    app.__call__
    app.wsgi_app
    app.run(debug=True)
# flask中有两个localstack和local对象，但是可以有多个进程或协程，均是由这两个进行操作的
# localstack创建local
'''
falsk两种上下文
    1.RequestContext 请求上下文
        Request 请求的对象，封装了Http请求(environ)的内容
        Session 根据请求中的cookie，重新载入该访问者相关的会话信息。
    2.AppContext 程序上下文
        g 处理请求时用作临时存储的对象。每次请求都会重设这个变量
        current_app 当前激活程序的程序实例
'''
