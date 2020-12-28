from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'userlogin'
USER_DICT = {
    '1': {"name": "sin ", "age": "18"},
    '2': {"name": "cos ", "age": "18"},
    '3': {"name": "tan ", "age": "18"},
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'alex' and pwd == '1234':
        session['user_info'] = user  # cookie中查看
        return redirect('/index')   # 重定向
    else:
        return render_template('login.html', msg="用户名或密码错误")
        # return render_template('login.html', **{'msg':"用户名或密码错误"})


@app.route("/detail")
def index():
    user_info = session.get("user_info")
    if not user_info:
        return redirect("/login")
    uid = request.args.get('uid')
    info = USER_DICT.get(uid)
    return render_template('detail.html', info=info)


@app.route("/index")
def detail():
    user_info = session.get("user_info")
    if not user_info:
        return redirect("/login")
    return render_template('index.html', user_dict=USER_DICT)


@app.route('/logout')
def logout():
    del session["user_info"]
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
