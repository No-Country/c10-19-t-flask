from flask import Blueprint, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.modules.models import User, Group, Member
from .schemas import GroupSchema, MemberSchema

members_bp = Blueprint('members', __name__)
api = Api(members_bp)

class Groups(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if not user:
            return {
                'message': 'user id is not valid'
            }, 400
        
        return {
            'message': str(len(user.groups))+' groups founds for this user',
            'data': GroupSchema(exclude=('members',)).dump(user.groups, many=True)
        }
    
    def post(self, user_id):
        user = User.get_by_id(user_id)
        if not user:
            return {
                'message': 'user id is not valid'
            }, 400
        
        data = request.get_json()
        data_format = GroupSchema().dump(data)
        group = Group(**data_format)
        group.save()
        member_group = Member(group_id=group.id, user_id=user.id)
        member_group.save()

        return {
            'message': 'Group created',
            'data': GroupSchema().dump(group)
        }

class GroupResource(Resource):
    def get(self, user_id,  group_id):
        user = User.simple_filter(external_id=user_id)
        if not user:
            return {
                'message': 'User Invalid'
            }
        
        member = Member.simple_filter(user_id=user.id, group_id=group_id)
        if not member:
            return {
                'message': 'Parameters are not valid'
            }, 400
        
        members = Member.simple_filter_all(group_id=group_id)
        return {
            'message': 'Request Success',
            'data': MemberSchema(only=('user',)).dump(members, many=True)
        }
    
    def post(self, user_id, group_id):
        user = User.simple_filter(external_id=user_id)
        if not user:
            return {
                'message': 'User Invalid'
            }
        
        member = Member.simple_filter(user_id=user.id, group_id=group_id)
        if not member:
            return {
                'message': 'Parameters are not valid'
            }, 400
        
        data = request.get_json()
        user_invited = User.find_by_email(data.get('email', None))
        if not user_invited:
            return {
                'message': 'User Invited is not valid'
            }
        member = Member.simple_filter(user_id=user_invited.id, group_id=group_id)
        if member:
            return {
                'message': 'Invited user already exist in group'
            }, 400
        data_format = MemberSchema().dump({'user_id': user_invited.id, 'group_id': group_id, 'active': True})
        member_group = Member(**data_format)
        member_group.save()
        return {
            'message': 'succes',
            'data': MemberSchema(only=('id','user')).dump(Member.simple_filter_all(group_id=group_id), many=True)
        }

api.add_resource(Groups, '/v1/<user_id>/groups') # Crea nuevo grupo para determinado usuario
api.add_resource(GroupResource, '/v1/<user_id>/group/<group_id>/members') # Consulta los miembros de un grupo determinado o agrega miembros al grupo