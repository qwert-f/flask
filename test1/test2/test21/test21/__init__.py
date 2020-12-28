from .views import account
from .views import user
from .views import admin
from flask import Flask
app = Flask(__name__)

app.register_blueprint(account.ac)
app.register_blueprint(admin.ad)
app.register_blueprint(user.ur)
