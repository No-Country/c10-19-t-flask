from flask import Blueprint, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.modules.models import User, Group, Member

members_bp = Blueprint('members', __name__)
api = Api(members_bp)

class Groups(Resource):
    pass

class Members(Resource):
    pass

api.add_resource(Groups, 'api/v1/<user_id>/groups') # Crea nuevo grupo para determinado usuario
api.add_resource(Members, 'api/v1/<group_id>/members') # Consulta los miembros de un grupo determinado o agrega miembros al grupo