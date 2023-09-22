class Config(object):
    DEBUG = False
    TESTING =False

    SECRET_KEY = "dsfsfs"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    Testing = True

    SESSION_COOKIE_SECURE = False
