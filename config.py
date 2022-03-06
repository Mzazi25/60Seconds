import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:mzazi25@localhost/watchlist'

class ProdConfig(Config):
    pass



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:Mzazi25@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

