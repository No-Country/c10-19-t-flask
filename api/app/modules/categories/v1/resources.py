from flask import Blueprint, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.modules.models import Category
from .schemas import CategorySchema

categories_bp = Blueprint('categories', __name__)
api = Api(categories_bp)

category_schema = CategorySchema()

class Categories(Resource):
    def get(self, member_id):
        category = Category()
        categories = category.get_all()
        return {
            'message': str(len(categories))+' categories founds for this member',
            'data': category_schema.dump(categories, many=True)
        }
    
    def post(self, member_id):
        data = request.get_json()
        data['member_id'] = member_id
        data = category_schema.load(data)
        category = Category(data)
        category.save()
        return {
            'message': 'Category added',
            'data': category_schema.dump(category)
        }
    
api.add_resource(Categories, '/api/v1/categories', endpoint='categories')