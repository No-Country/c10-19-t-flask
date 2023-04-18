from marshmallow import EXCLUDE, Schema, fields

class GroupSchema(Schema):
    members = fields.List(fields.Nested(lambda: UserSchema(only=('id', 'fullname'))))
    class Meta:
        additional = ('id', 'description', 'name')
        unknown = EXCLUDE
        ordered = True

class UserSchema(Schema):
    id = fields.Str() 
    external_id = fields.Str()
    email = fields.Email()
    social_id = fields.Str()
    social_type = fields.Str()
    activated = fields.Str()
    fullname = fields.Str()
    email = fields.Str()
    picture = fields.Str()
    last_login = fields.DateTime()
    created_at = fields.DateTime()
    password = fields.Str(load_only=True)
    groups = fields.Nested(GroupSchema, many=True)

class MemberSchema(Schema):
    user = fields.Nested(UserSchema, only=('fullname', 'last_login'))
    group = fields.Nested(GroupSchema, exclude=('members','id'))

    class Meta:
        additional = ('id','user_id','group_id', 'active')
        unknown = EXCLUDE
        ordered = True

