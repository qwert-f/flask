from flask import Blueprint

ur = Blueprint('ur', __name__)


@ur.route('/info')
def info():
    return 'info'
