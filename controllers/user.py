from controllers.authentication import Authentication
from models.database import get_many_items, get_item, remove_item

from utils import sql_query
from utils.exceptions import UserDoesNotExist
from controllers.book import Book

from helpers.input_helper import get_book_details


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def user_details(self):
        return f"Username: {self.username} | Role: {self.role}"

    def query_book(self, name):
        response = get_many_items(sql_query.GET_BOOK_BY_NAME, (name,))
        return response

    def sort_books_by_rating(self):
        books = get_many_items(sql_query.GET_BOOKS_BY_RATING, None)
        books = [Book(*book) for book in books]
        for book in books:
            book.show_book_details()

    def sort_books_by_price(self) -> None:
        books = get_many_items(sql_query.GET_BOOKS_BY_PRICE, None)
        books = [Book(*book) for book in books]
        for book in books:
            book.show_book_details()

    def group_books_by_genre(self, genre):
        books = get_many_items(sql_query.GET_BOOKS_BY_PRICE, (genre,))
        if books is not None:
            books = [Book(*book) for book in books]
            for book in books:
                book.show_book_details()
        else:
            print(f"Null entries for genre `{genre}`")


class Admin(User):
    def register_librarian(self, username, password, user_role="librarian"):
        new_librarian = Authentication(username, password, user_role)
        new_librarian.signup()
        print("-----------------------------")
        print(f"Librarian with username `{username}` registered successfully!")

    def list_users(self):
        response = get_many_items(sql_query.GET_ALL_USERS, None)
        users = [User(*user) for user in response]
        for user in users:
            print(user.user_details())

    def remove_user(self, username):
        check_user = get_item(sql_query.GET_USER_BY_USERNAME, (username,))
        try:
            if check_user is None:
                raise UserDoesNotExist(username)
            remove_item(sql_query.REMOVE_USER, (username,))
            print(f"{username} successfully removed!!!")
        except UserDoesNotExist as user_error:
            print(user_error)


class Librarian(User):
    def add_book(self):
        book_info = get_book_details()
        book_info.add_book()

    def remove_book(self, name):
        book_to_remove = get_item(sql_query.GET_BOOK_BY_NAME, (name,))
        if book_to_remove is None:
            return False
        book_obj = Book(*book_to_remove)
        book_obj.remove_book()
        return True


class Visitor(User):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)
