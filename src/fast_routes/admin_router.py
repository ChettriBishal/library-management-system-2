from .fast_schemas import UserSchema
from controllers.authentication import Authentication

from controllers.user import Admin

from fastapi import APIRouter, HTTPException, status

admin_route = APIRouter()

# blp = Blueprint("Admin", __name__, description="Operation performed via admin")


@admin_route.get('/admin/users', status_code=status.HTTP_200_OK)
async def list_users():
    admin_obj = Admin()
    return admin_obj.get_users(), 200


@admin_route.delete('/user/{user_name}', status_code=status.HTTP_200_OK)
def remove_user(user_name: str):
    admin_obj = Admin()
    user_removed = admin_obj.remove_user(user_name)
    if user_removed:
        return {"message": f"{user_name} removed"}, 200


@admin_route.post('/admin/register/librarian', status_code=status.HTTP_201_CREATED)
def register_librarian(user_data: UserSchema):
    user_data = user_data.model_dump()
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    signed_up = auth.signup()
    if signed_up:
        return {"message": f"Librarian {user_data['username']} registered, uuid {signed_up}"}
    else:
        raise HTTPException(409, detail="Username already exists!")
