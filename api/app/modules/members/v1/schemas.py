from marshmallow import EXCLUDE, Schema, fields

class GroupSchema(Schema):
    members = fields.List(fields.Nested(lambda: UserSchema(only=('id', 'fullname'))))
    class Meta:
        additional = ('id', 'description', 'name')
        unknown = EXCLUDE
        ordered = True

class UserSchema(Schema):
    id = fields.Str(load_only=True) 
    external_id = fields.Str(data_key='id', dump_only=True)
    email = fields.Email(required=True)
    social_id = fields.Str(load_only=True)
    social_type = fields.Str(load_only=True)
    activated = fields.Str(load_only=True)
    fullname = fields.Str()
    picture = fields.Str()
    last_login = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    password = fields.Str(load_only=True, required=True)
    groups = fields.Nested(GroupSchema, many=True, exclude=('members',))

class MemberSchema(Schema):
    user = fields.Nested(UserSchema, only=('fullname', 'last_login'))
    group = fields.Nested(GroupSchema, exclude=('members','id'))

    class Meta:
        additional = ('id','user_id','group_id', 'active')
        unknown = EXCLUDE
        ordered = True

