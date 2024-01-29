from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, status
from controllers.authentication import Authentication
from jose import jwt

auth_route = APIRouter()

SECRET_KEY = "thisisnotasecretanymoreisit"

@auth_route.post('/login', status_code=status.HTTP_200_OK)
async def login_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    logged_in = auth.login()
    if logged_in:
        return {"message": f"{user_data['username']} has logged in!"}
    else:
        raise HTTPException(404, detail="User not found")


def authenticate_user(username: str, password: str, role: str):
    auth = Authentication(username, password, role)
    logged_in = auth.login()
    if logged_in:
        return True
    else:
        return False


@auth_route.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, 'visitor')
    if not user:
        return {"message": "Failed Authentication"}
    return {"message": "Successful Authentication"}

