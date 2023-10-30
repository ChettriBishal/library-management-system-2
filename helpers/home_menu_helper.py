import maskpass

from utils import prompts, sql_query
from controllers.authentication import Authentication
from helpers import input_helper
from models.database import get_item
from controllers.user import Admin, Visitor, Librarian
from controllers.book_issue import BookIssue

from utils.exceptions import UserDoesNotExist
from models.database import get_many_items


def home():
    while True:
        choice = input(prompts.HOME)
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            exit(0)
        else:
            print("Enter a valid choice!")


def signup():
    print("---------------SIGN UP---------------")
    visitor_info = input_helper.get_visitor_details()
    visitor = Authentication(*visitor_info)
    visitor.signup()


def login():
    print("---------------SIGN IN---------------")
    username = input("Enter the username: ")
    password = maskpass.advpass(f"Enter the password for `{username}: ")
    role = get_item(sql_query.GET_USER_ROLE, (username,))
    try:
        if role is None:
            raise UserDoesNotExist(username)
    except UserDoesNotExist as user_error:
        print(user_error)

    role = role[0]
    user = Authentication(username, password, role)
    if user.login() is None:
        print("Wrong password! Please try again")
        return

    if role == 'admin':
        admin = Admin(username, password, role)
        admin_menu(admin)
    elif role == 'visitor':
        visitor = Visitor(username, password, role)
        visitor_menu(visitor)
    elif role == 'librarian':
        librarian = Librarian(username,password,role)
        librarian_menu(librarian)


def admin_menu(admin):
    while True:
        choice = input(prompts.ADMIN_MENU)
        if choice == '1':
            username = input("Enter the username: ")
            password = maskpass.advpass(f"Enter the password for {username}: ")
            admin.register_librarian(username, password)
        elif choice == '2':
            admin.list_users()
        elif choice == '3':
            username = input("Enter the username to remove: ")
            admin.remove_user(username)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


def visitor_menu(visitor):
    while True:
        choice = input(prompts.VISITOR_MENU)

        if choice == '1':
            bookname = input("\nEnter the name of the book to query: ")
            response = visitor.query_book(bookname)
            if response is None:
                print(f"No book with name {bookname} found!")
            else:
                book_cnt = get_item(sql_query.NO_OF_BOOKS_OF_SAME_NAME,(bookname,))
                print(f"Number of copies of `{bookname}`: {book_cnt[0]}")

        elif choice == '2':
            visitor.sort_books_by_rating()

        elif choice == '3':
            visitor.sort_books_by_price()

        elif choice == '4':
            genre = input("\nEnter the genre whose books you want to see: ")
            visitor.group_books_by_genre(genre)

        elif choice == '5':
            bookname = input("\nEnter the name of the book to issue: ")
            visitor.issue_book(bookname)

        elif choice == '6':
            books = visitor.books_issued()
            if books is None:
                print(f"{visitor.username} has not issued any books yet!")
            else:
                books = [BookIssue(*book) for book in books]
                for book in books:
                    book.show_issue_details()

        elif choice == '7':
            records = get_many_items(sql_query.BOOK_ISSUED, (visitor.username,))
            books = [BookIssue(*book) for book in records]
            if records:
                print(f"\nBooks issued by user `{visitor.username}`")
                for book in books:
                    print(f"Dues for {book.book_id} -> `{book.get_dues()}`")
                    print("--------------------")

        elif choice == '8':
            book_id = input("\nEnter the book id to return: ")
            bookname = get_item(sql_query.BOOK_NAME,(book_id,))
            check = visitor.return_book(book_id)
            if check:
                print(f"Book `{bookname[0]}` returned successfully!")
            else:
                print(f"`{visitor.username}` has not issued this book!")

        elif choice == '9':
            break

        else:
            print("Invalid choice!")


def librarian_menu(librarian):
    while True:
        choice = input(prompts.LIBRARIAN_MENU)
        if choice == '1':
            librarian.add_book()
        elif choice == '2':
            librarian.sort_books_by_rating()
        elif choice == '3':
            name = input("Enter the name of the book to remove: ")
            librarian.remove_book(name)
        elif choice == '4':
            break
        else:
            print("Invalid Choice!")

