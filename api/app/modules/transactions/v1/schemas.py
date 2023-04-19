from marshmallow import EXCLUDE, Schema, fields

class TransactionSchema(Schema):
    class Meta:
        additional = ('id','type','value','category_id','currency_id','group_id', 'date')
        unknown = EXCLUDE
        ordered = True