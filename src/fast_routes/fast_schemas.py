import re
from pydantic import BaseModel, Field, field_validator
pwd_regexp = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"


class UserSchema(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: str = Field(min_length=4)

    @classmethod
    @field_validator("password")
    def regex_match(cls, p: str) -> str:
        re_for_pw: re.Pattern[str] = re.compile(pwd_regexp)
        if not re_for_pw.match(p):
            raise ValueError("invalid password")
        return p


class UserRegisterSchema(UserSchema):
    email: str = Field()


class BookNameSchema(BaseModel):
    name: str


class BookSchema(BaseModel):
    name: str
    author: str
    price: float
    rating: int = Field(gt=-1, lt=11)
    genre: str
