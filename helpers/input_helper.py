import os
import stdiomask
from collections import namedtuple
from utils.uuid_generator import generate_uuid
from controllers.book import Book
from controllers.user import Visitor


def get_book_details():
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    price = float(input("Enter the price of the book: "))
    rating = int(input("Enter the rating of the book (1-10): "))
    if rating < 1 or rating > 10:
        print("Enter a valid rating!")
        return get_book_details()
    genre = input("Enter the genre of the book: ")

    book_id = generate_uuid()
    return Book(book_id, name, author, price, rating, genre)


def get_user_details(user_role="visitor"):
    username = input("Enter username: ")
    password = stdiomask.getpass(prompt=f"Enter password for {username}: ", mask="*")
    user = Visitor(username, password, user_role)
    return user

def get_book_query():
    name = input("Enter the name of the book you're searching for: ")

