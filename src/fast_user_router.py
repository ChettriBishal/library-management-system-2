from fastapi import FastAPI, Body
from controllers.authentication import Authentication

app = FastAPI()


@app.post('/login')
async def login_user(user_data=Body()):
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    logged_in = auth.login()
    if logged_in:
        return {"message": f"{user_data['username']} has logged in!"}
    return {"message": f"{user_data['username']} not found!"}
