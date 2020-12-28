from flask import Blueprint

ac = Blueprint('ac', __name__)


@ac.route('/login')
def login():
    return 'login'


@ac.route('/logout')
def logout():
    return 'logout'
