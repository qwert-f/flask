from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ajfhhafhh'


@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')
    return "login"


@app.route("/index", methods=["POST", "GET"])
def index():
    print('index')
    return "index"


@app.route("/login", methods=["POST", "GET"])
def login():
    return "login"


if __name__ == '__main__':
    app.run(debug=True)

'''
404界面定制
@app.errorhandler(404)
def page_not_found(error):
    return 'pass'
常见装饰器可以自行百度
@app.before_first_request
'''
