from flask import Blueprint, render_template, request, session, redirect
# from uuid import uuid4
from ..utils.sql import SQLHelper

account = Blueprint('account', __name__)


@account.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    # 连接数据库--->查询--->关闭数据库
    obj = SQLHelper.fetch_one(
        "select id,name from users where name=%s and pwd=%s", [user, pwd, ])
    if obj:
        # if user == 'ama' and pwd == '1234':
        # uid = str(uuid4())
        session.permanent = True    # redis默认设置了为true
        # session['user_info'] = {'id': uid, 'name': user}
        session['user_info'] = {'id': obj['id'], 'name': user}
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误！')
