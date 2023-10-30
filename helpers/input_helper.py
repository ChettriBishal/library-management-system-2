import maskpass
from utils.uuid_generator import generate_uuid
from controllers.book import Book
from helpers.validation_helper import validate_password, validate_username

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
    return Book(book_id, name, author, rating, price, genre)


def get_visitor_details(user_role="visitor"):
    while True:
        username = input("Enter username: ")
        if validate_username(username):
            break
        else:
            print("Please enter a valid username")
    while True:
        password = maskpass.advpass(f"Enter password for {username}: ")
        if validate_password(password):
            user = (username, password, user_role)
            return user
        else:
            print("Please enter a stronger password!")


def get_book_query():
    name = input("Enter the name of the book you're searching for: ")
    return name
