from .fast_schemas import UserSchema
from controllers.authentication import Authentication

from controllers.user import Admin

from fastapi import APIRouter, HTTPException, status, Depends

from .auth import get_current_user
from typing import Annotated

admin_route = APIRouter(
    tags=['Admin Methods']
)

# blp = Blueprint("Admin", __name__, description="Operation performed via admin")

user_dependency = Annotated[dict, Depends(get_current_user)]


@admin_route.get('/admin/users', status_code=status.HTTP_200_OK)
async def list_users(user: user_dependency):
    if user is None:
        raise HTTPException(401, "Authentication Failed")
    admin_obj = Admin()
    return admin_obj.get_users(), 200


@admin_route.delete('/user/{user_name}', status_code=status.HTTP_200_OK)
def remove_user(user: user_dependency, user_name: str):
    if user is None:
        raise HTTPException(401, "Authentication Failed")

    admin_obj = Admin()
    user_removed = admin_obj.remove_user(user_name)
    if user_removed:
        return {"message": f"{user_name} removed"}, 200


@admin_route.post('/admin/register/librarian', status_code=status.HTTP_201_CREATED)
def register_librarian(user: user_dependency, user_data: UserSchema):
    if user is None:
        raise HTTPException(401, "Authentication Failed")
    if user.get('role') != 'admin':
        raise HTTPException(401, "Unauthorized to perform this action")

    user_data = user_data.model_dump()
    auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
    signed_up = auth.signup()
    if signed_up:
        return {"message": f"Librarian {user_data['username']} registered, uuid {signed_up}"}
    else:
        raise HTTPException(409, detail="Username already exists!")
