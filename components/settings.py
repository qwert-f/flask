from datetime import timedelta
from redis import Redis
# import redis
# 方法1.2
import pymysql
from dbutils.pooled_db import PooledDB


class Config(object):
    DEBUG = True
    # DEBUG = False
    # TESTING = False
    SECRET_KEY = 'sincos'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)  # 失效时间
    SESSION_REFRESH_EACH_REQUEST = True  # 每次请求都刷新
    # DATABASE_URI = 'sqlite://memory:'
    # 将session设置为redis版本的
    SESSION_TYPE = 'redis'
    PYMYSQL_POOL = PooledDB(  # 方法1.2
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
        maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
        maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。
        # PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
        # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。

        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
        setsession=[],  # 开始会话前执行的命令列表。
        # 如：["set datestyle to ...", "set time zone ..."]
        ping=0,
        # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never,
        # 1 = default = whenever it is requested,
        # 2 = when a cursor is created,
        # 4 = when a query is executed, 7 = always
        host='127.0.0.1',
        port=3306,
        user='root',
        password='sql1',
        database='daily',
        charset='utf8'
    )
    # SESSION_REDIS = Redis(host='127.0.0.1', port='6379', password='redis1')
    # PYMYSQL_HOST = '127.0.0.1'


class ProductionConfig(Config):
    # DATDATABASE_URI = 'mysql://root@localhost:3306/components'
    pass


class DevelopmentConfig(Config):
    # DEBUG = True
    SESSION_REDIS = Redis(
        host='127.0.0.1', port='6379', password='redis1')


class TestingConfig(Config):
    # TESTING = True
    pass
