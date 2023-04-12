from marshmallow import EXCLUDE, Schema, fields

class CategorySchema(Schema):
    class Meta:
        fields = ('id', 'icons', 'name')
        unknown = EXCLUDE
        ordered = True