from fastapi import APIRouter, HTTPException, Query
from controllers.user import User

book_route = APIRouter(tags=['Routes for books'])


@book_route.get('/books')
async def get_books(filter: str = Query(None, description='Filter books by price or rating'),
    genre: str = Query(None, description='Filter books by genre'),
    bookname: str = Query(None, description='Search for a specific book by name')
):
    print(f"Filter = {filter}")

    user_data_access = User()
    if filter:
        if filter == 'price':
            return user_data_access.sort_books_by_price()
        elif filter == 'rating':
            return user_data_access.sort_books_by_rating()
        raise HTTPException(404, detail='Book not found')
    elif genre:
        return user_data_access.group_books_by_genre(genre)
    elif bookname:
        return user_data_access.query_book(bookname)
