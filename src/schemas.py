from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp("[A-Za-z1-9_]+"))
    password = fields.Str(required=True, load_only=True, validate=validate.Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?["
                                                                                  "0-9])(?=.*?[#?!@$%^&*-]).{8,"
                                                                                  "}$"))  # never return the user's
    # password
    role = fields.Str(required=True, validate=validate.Regexp("^[a-zA-Z]+$"))


class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True, validate=validate.Regexp("^[a-zA-Z][a-zA-Z0-9]+\@[a-zA-Z]+\.(in|net|com)"))


class BookNameSchema(Schema):
    name = fields.Str(required=True)


class BookSchema(Schema):
    name = fields.Str(required=True)
    author = fields.Str(required=True)
    price = fields.Float(required=True)
    rating = fields.Int(required=True)
    genre = fields.Str(required=True)
