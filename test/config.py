import redis


class Config(object):
    '''配置信息'''
    SECRET_KEY = 'logicout'
    '''数据库'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:sql1@127.0.0.1:3306/Daily'
    SQLALCHEMY_TRACK_MODIFICATION = True
    '''redis'''
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,
                                      port=REDIS_PORT,
                                      password='redis1')
    SESSION_USE_SIGNER = True   # 对cokie中session_id进行隐藏
    PERMANENT_SESSION_LIFEIME = 86400   # SEssion数据有效期，单位秒


class DevelopmentConfig(Config):
    '''开发模式配置信息'''
    DEBUG = True


class ProductionConfig(Config):
    '''生产环境配置信息'''
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
