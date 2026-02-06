class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flask:flask123@127.0.0.1:3306/testing"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



