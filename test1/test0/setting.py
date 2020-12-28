class baseConfig(object):
    DEBUG = True
    SECRET_KEY = 'test05'


class productionConfig():
    DEBUG = False


class DEV():
    pass


class TEST():
    pass
