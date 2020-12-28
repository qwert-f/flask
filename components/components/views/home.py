from flask import Blueprint, render_template
# , session

home = Blueprint('home', __name__)


@home.route("/index", methods=["POST", "GET"])
def index():
    # user_info = session['user_info']
    # print(user_info)
    # session['user_info'] = {'k1': 3, 'k2': 2}
    # user_info = session['user_info']
    # print(user_info)
    # session['user_info']['k1'] = 1234
    # 若不加下面的这test中的user_info的值并未改变，当整体被修改时modified为true,局部修改时modified为false
    # settings中SESSION_REFRESH_EACH_REQUEST设置后可不设置下面的
    # session['modified'] = True
    return render_template('home.html')


@home.route("/test", methods=["POST", "GET"])
def test():
    # user_info = session['user_info']
    # print(user_info)
    return "test"
