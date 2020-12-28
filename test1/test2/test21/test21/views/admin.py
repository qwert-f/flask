from flask import Blueprint

ad = Blueprint('ad', __name__, url_prefix='/admin')  # 类似路由分发


@ad.route('/home')
def home():
    return 'home'


@ad.before_request
def fname():
    print("before_request")


@ad.route('/index')
def index():
    return 'index'
