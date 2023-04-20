from marshmallow import EXCLUDE, Schema, fields

from app.modules.members.v1.schemas import UserSchema


class TransactionSchema(Schema):
    user = fields.Nested(UserSchema, only=('external_id', "fullname"))
    class Meta:
        additional = ('id','type','value','category_id','currency_id','group_id', 'date', 'user_id')
        unknown = EXCLUDE
        ordered = True