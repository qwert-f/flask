from flask import Flask
from .views import account
from .views import home
from flask_session import Session
# from components.utils.pools import init_pool


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)
    Session(app)
    # init_pool(app)
    return app
