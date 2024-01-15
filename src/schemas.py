from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)  # never return the user's password
    role = fields.Str(required=True)


class BookSchema(Schema):
    book_id = fields.Str(required=True)
    name = fields.Str(required=True)
    author = fields.Str(required=True)
    price = fields.Float(required=True)
    rating = fields.Int(required=True)
    genre = fields.Str(required=True)
