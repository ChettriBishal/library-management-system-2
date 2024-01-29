from fastapi import APIRouter, Body, HTTPException
from controllers.authentication import Authentication

user_route = APIRouter(tags=['User routes for authentication'])


@user_route.post('/login')
async def login_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    logged_in = auth.login()
    if logged_in:
        return {"message": f"{user_data['username']} has logged in!"}
    else:
        raise HTTPException(404, detail="User not found")


@user_route.post('/signup')
async def signup_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    signed_up = auth.signup()
    if signed_up:
        return {"message": f"{user_data['username']} signed up, uuid {signed_up}"}
    else:
        raise HTTPException(422, detail="Check the user inputs")



