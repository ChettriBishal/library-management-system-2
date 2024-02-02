from fastapi import APIRouter, Body, HTTPException, status
from controllers.authentication import Authentication
from utils.access_token import AccessToken
from fast_routes.fast_schemas import Token

user_route = APIRouter(tags=['User routes for authentication'])


@user_route.post('/login', status_code=status.HTTP_200_OK, response_model=Token)
async def login_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    print(user_data)
    logged_in = auth.login()
    if logged_in:
        access_token_object = AccessToken()
        token = access_token_object.create_access_token(user_data['username'], user_data['role'])  # create jwt token
        return {"access_token": token, "token_type": 'bearer'}
    else:
        raise HTTPException(404, detail="User not found")


@user_route.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    signed_up = auth.signup()
    if signed_up:
        return {"message": f"{user_data['username']} signed up, uuid {signed_up}"}
    else:
        raise HTTPException(422, detail="Check the user inputs")
