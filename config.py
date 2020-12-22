from decouple import config

class Config:
    SECRET_KEY = '°l/_out\nfsddsdfdsf{¿091=badfg'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1:5432/agrosechura'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://remcrnwmxlvnpw:c4b0269e77924721ef4ae160a972279331a9972382109d544a7ab8986388f048@ec2-34-238-26-109.compute-1.amazonaws.com:5432/dckonl1hua8af1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

#postgres://remcrnwmxlvnpw:c4b0269e77924721ef4ae160a972279331a9972382109d544a7ab8986388f048@ec2-34-238-26-109.compute-1.amazonaws.com:5432/dckonl1hua8af1
