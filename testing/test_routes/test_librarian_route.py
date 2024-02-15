from fastapi.testclient import TestClient
from src.fast_routes.librarian_router import lib_route, get_current_user
from src.models.database import DBConnection
from src.schemas import BookSchema
from src.fastapp import app

client = TestClient(lib_route)


def mock_get_current_user():
    return "edward"


app.dependency_overrides[get_current_user] = mock_get_current_user




# def test_add_new_book_success():
#     # Mock user and book data
#     user_token = "mock_user_token"
#     book_data = {
#         "name": "Test Book",
#         "author": "Test Author",
#         "rating": 4.5,
#         "price": 29.99,
#         "genre": "Fiction",
#     }
#
#     # Perform the request
#     response = client.post(
#         "/librarian/books",
#         json=book_data,
#         headers={"Authorization": f"Bearer {user_token}"},
#     )
#
#     assert response.status_code == 201
#     assert response.json() == {"message": "Book added Test Book"}

#
# def test_add_new_book_unauthorized():
#     # No user token provided
#     book_data = {
#         "name": "Test Book",
#         "author": "Test Author",
#         "rating": 4.5,
#         "price": 29.99,
#         "genre": "Fiction",
#     }
#
#     # Perform the request without authorization header
#     response = client.post("/librarian/books", json=book_data)
#
#     assert response.status_code == 401
#     assert response.json() == {"detail": "Authentication failed"}
#
#
# def test_add_new_book_failure(monkeypatch):
#     user_token = "mock_user_token"
#     book_data = {
#         "name": "Test Book",
#         "author": "Test Author",
#         "rating": 4.5,
#         "price": 29.99,
#         "genre": "Fiction",
#     }
#
#     class MockBook:
#         @staticmethod
#         def add_book():
#             return False
#
#     # client.dependency_overrides[BookSchema] = MockBook
#     # monkeypatch.setattr(BookSchema, return_value=)
#     monkeypatch.setattr(BookSchema, "model_dump", MockBook.model_dump)
#
#     response = client.post(
#         "/librarian/books",
#         json=book_data,
#         headers={"Authorization": f"Bearer {user_token}"},
#     )
#
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Something went wrong"}
