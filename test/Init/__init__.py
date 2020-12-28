from config import config_map
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()    # 数据库
# 创建redis连接对象
redis_store = None

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.WARNING)
# 创建日志记录器，指明日志保存路径，每个日志文件大小，保存日志文件上限个数
file_log_handler = RotatingFileHandler("logs/log",
                                       maxBytes=1024*1024*100,
                                       backupCount=10)
# 创建日志记录的格式
formatter = logging.Formatter(
    '%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象(falsk app使用的)添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    '''
    创建flask的应用对象
    :param config_name: str 配置模式的名称 ("develop", "product")
    :return:'''
    app = Flask(__name__)
    # 根据配置模式的名字获取配置参数
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    #  使用app初始化db
    db.init_app(app)
    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(
        host=config_class.REDIS_HOST,
        port=config_class.REDIS_PORT,
        password='redis1')
    # 利用flsak_session,将session数据保存到redis中
    Session(app)
    # 为flask补充csrf防护
    CSRFProtect(app)
    # 注册蓝图
    from Init import api_1_0    # 循环导包，导致需要在用之前才导包
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    return app
