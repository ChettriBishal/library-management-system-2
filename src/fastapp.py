from fast_routes.user_router import user_route
from fast_routes.admin_router import admin_route
from fast_routes.librarian_router import lib_route
from fast_routes.book_router import book_route


from fastapi import FastAPI

app = FastAPI()

app.include_router(user_route)
app.include_router(admin_route)
app.include_router(lib_route)
app.include_router(book_route)



