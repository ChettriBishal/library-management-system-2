from jose import jwt
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv


class AccessToken:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = "HS256"

    def create_access_token(self, username: str, expires_delta=timedelta(minutes=20)):
        encode = {'sub': username}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, self.SECRET_KEY, self.ALGORITHM)
