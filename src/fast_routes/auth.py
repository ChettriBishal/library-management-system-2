import os
from datetime import timedelta

from fastapi import APIRouter, Depends, status, Form
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, status
from controllers.authentication import Authentication
from utils.access_token import AccessToken
from fast_routes.fast_schemas import Token
from dotenv import load_dotenv
from jose import jwt, JWTError

auth_route = APIRouter(
    prefix='/auth',
    tags=['auth']
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


# @auth_route.post('/login', status_code=status.HTTP_200_OK)
# async def login_user(user_data=Body()):
#     auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
#     logged_in = auth.login()
#     if logged_in:
#         access_token_object = AccessToken()
#         token = access_token_object.create_access_token(user_data['username'])  # create jwt token
#         return {"access_token": token, "token_type": 'bearer'}
#     else:
#         raise HTTPException(404, detail="User not found")


def authenticate_user(username: str, password: str, role: str):
    auth = Authentication(username, password, role)
    logged_in = auth.login()
    if logged_in:
        return True
    else:
        return False


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        load_dotenv()
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        username: str = payload.get('sub')
        role: str = payload.get('role')
        if username is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

        return {'username': username, 'role': role}
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')


# @auth_route.post("/login", response_model=Token)
# async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#                                  role: str = Form(...)):
#     user = authenticate_user(form_data.username, form_data.password, role)
#     if not user:
#         return {"message": "Failed Authentication"}
#     access_token_obj = AccessToken()
#     token = access_token_obj.create_access_token(form_data.username, role, timedelta(minutes=20))
#
#     return {"access_token": token, "token_type": "bearer"}


@auth_route.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, 'admin')
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
    access_token_obj = AccessToken()
    token = access_token_obj.create_access_token(form_data.username, 'admin')

    return {'access_token': token, 'token_type': 'bearer'}
