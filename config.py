from decouple import config

class Config:
    SECRET_KEY = '°l/_out\nfsddsdfdsf{¿091=badfg'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1:5432/agrosechura'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///../app-guias.sqlite3'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/agrosechura'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

