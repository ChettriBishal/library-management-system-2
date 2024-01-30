from fastapi import APIRouter, HTTPException, status, Depends
from .fast_schemas import BookSchema, BookNameSchema
from controllers.book import Book
from controllers.user import Librarian
from .auth import get_current_user
from typing import Annotated

lib_route = APIRouter(tags=['Routes for librarian'])

user_dependency = Annotated[dict, Depends(get_current_user)]


@lib_route.post('/librarian/books', status_code=status.HTTP_201_CREATED)
def add_new_book(user: user_dependency, book_data: BookSchema):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    book_data = book_data.model_dump()
    book_obj = Book(book_data['name'], book_data['author'], book_data['rating'], book_data['price'],
                    book_data['genre'])
    book_added = book_obj.add_book()
    if book_added:
        return {"message": f"Book added {book_obj.name}"}, 200
    else:
        raise HTTPException(400, detail=f"Something went wrong")


@lib_route.delete('/books', status_code=status.HTTP_200_OK)
def remove_book(user: user_dependency, book_name: BookNameSchema):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    book_name = book_name.model_dump()
    book_name = book_name['name']
    status = Librarian().remove_book(book_name)
    if status:
        return {"message": f"Book {book_name} is removed"}, 200
    else:
        raise HTTPException(404, detail=f"Book with name {book_name} not found!")
