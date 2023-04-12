from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str() 
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