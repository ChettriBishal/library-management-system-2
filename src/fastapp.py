from fast_routes.user_router import user_route
from fast_routes.admin_router import admin_route
from fast_routes.librarian_router import lib_route
from fast_routes.book_router import book_route
from fast_routes.auth import auth_route

from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()

app = FastAPI()

app.include_router(user_route)
app.include_router(admin_route)
app.include_router(lib_route)
app.include_router(book_route)
app.include_router(auth_route)


@app.get("/")
async def server_status():
    return {"message": "Server is running"}
