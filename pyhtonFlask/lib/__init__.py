from flask import Flask
from setting import config_dict
from flask_wtf import Form
from flask_wtf.file import FileField
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap
import os
from .func import *


app = Flask(__name__)

config_name = os.getenv('CONFIG_NAME', 'test')
app.config.from_object(config_dict[config_name])

bootstrap = Bootstrap(app)

moment = Moment()
moment.init_app(app)

db = SQLAlchemy(app)

form = Form()

class PhotoForm(Form):
    photo = FileField('Your photo')


