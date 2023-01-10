from lib import app,db
from controller import admin, index, api
from model import *
 
if __name__ == '__main__':
    # app.run()
    print(app.url_map)
    db.create_all()

    app.run()