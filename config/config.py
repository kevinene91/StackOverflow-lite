import os 

class Config(object): 
    DEBUG = False 
    CSRF_ENABLED = True 
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/stackoverflow.db'

class DevelopmentConfig(Config):
    Debug = True


class TestingConfig(Config): 
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True 

class StagingConfig(Config): 
    DEBUG = True

class ProductionConfig(Config):

    DEBUG = False 
    TESTING = False


app_config = {
    'development': DevelopmentConfig, 
    'testing': TestingConfig, 
    'staging': StagingConfig, 
    'production': ProductionConfig,
}