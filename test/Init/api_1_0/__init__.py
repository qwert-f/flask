
from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)
# 循环导包。导致必须在后面导入
from . import demo
