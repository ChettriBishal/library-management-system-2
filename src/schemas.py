from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)  # never return the user's password
    role = fields.Str(required=True)


class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)


class BookSchema(Schema):
    name = fields.Str(required=True)
    author = fields.Str(required=True)
    price = fields.Float(required=True)
    rating = fields.Int(required=True)
    genre = fields.Str(required=True)
