from marshmallow import EXCLUDE, Schema, fields

class TransactionSchema(Schema):
    class Meta:
        additional = ('id','type','value','category_id','currency_id','member_id')
        unknown = EXCLUDE
        ordered = True