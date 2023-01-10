from lib import app,db
from model import db_model as table
@app.route('/')
def hello_world():
    
    return 'Hello World!'
