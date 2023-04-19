from flask import Blueprint, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.modules.members.v1.schemas import MemberSchema
from app.modules.models import Transaction, Member, User
from .schemas import *

transaction_bp = Blueprint('transactions', __name__)
api = Api(transaction_bp)

class Transactions(Resource):
    def post(self, user_id):
        data = request.get_json()

        user = User.simple_filter(external_id=user_id)
        if not user:
            return {
                'message': 'User Invalid'
            }
        
        data['user_id'] = user.id
        member_schema = MemberSchema(only=('user_id', 'group_id')).load(data)
        member = Member.simple_filter(**member_schema) # type: ignore
        if not member:
            return {
                'message': 'Parameters are not valid'
            }, 400
        
        data = TransactionSchema().load(data)
        transaction = Transaction(**data)
        transaction.save()
        return {
            'message': 'Request Success',
            'data': TransactionSchema().dump(transaction)
        }

    def get(self, user_id):
        user = User.simple_filter(external_id=user_id)
        if not user:
            return {
                'message': 'User Invalid'
            }
        
        data = request.args.to_dict()
        data[user_id] = user.id
        
        member_schema = MemberSchema(only=('user_id', 'group_id')).load(data)
        member = Member.simple_filter(**member_schema) # type: ignore
        if not member:
            return {
                'message': 'Parameters are not valid'
            }, 400
        
        transactions = Transaction.simple_filter_all(group_id=data['group_id'])

        return {
            'message': f'{str(len(transactions))} founds for this group',
            'data': TransactionSchema().dump(transactions, many=True)
        }

    def put(self):
        pass

api.add_resource(Transactions, '/api/v1/<user_id>/transaction')