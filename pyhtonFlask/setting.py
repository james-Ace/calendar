import logging
import os
class BaseConfig(object): 
 
    DEBUG = True
    SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    WTF_CSRF_SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"

    SQLALCHEMY_DATABASE_URI = "mysql://username:password@192.168.1.89:3306/app_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://:password@192.168.1.89:6379/0"
    LEVEL_NAME = logging.DEBUG
 
class DevelopConfig(BaseConfig):
    SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    WTF_CSRF_SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    
 
class TestConfig(BaseConfig):
 
    TESTING = True
    SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    WTF_CSRF_SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:881301@127.0.0.1:3306/test"

 
class ProductConfig(BaseConfig):
 
    DEBUG = False
    SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    WTF_CSRF_SECRET_KEY = "abcejame@345ofdfds./dfewef?$fdsjkl*7DFsf0IEd9034&"
    LEVEL_NAME = logging.ERROR
 
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql://username:password@**.***.*.**:3306/app_db")
 
config_dict = {
 
    "develop": DevelopConfig,
 
    "product": ProductConfig,
 
    "test": TestConfig
 
}