"""
    API 文件,用于前后分离的项目,如小程序,APP,WEB前后分离的项目
"""

from lib import app
from flask_restful import Api,Resource

api = Api(app)

class IndexView(Resource):
    def get(self):
        return {"username":"donghao"}
    def put(self):
        return {"mode": 'PUT'}
    def post(self):
        return {"mode": 'post'}
    def delete(self):
        return {"mode": 'delete'}
api.add_resource(IndexView,'/api/index')