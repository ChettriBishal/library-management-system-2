from controllers.authentication import Authentication
from controllers.user import Admin

auth = Authentication("temp123", "Snow123", "visitor")
auth.login()

auth2 = Authentication("lib345", "Lib345", "librarian")
auth2.login()

admin1 = Admin("anything", "admin")
admin1.remove_user("lib345")
admin1.list_users()





from controllers.book import Book
from controllers.user import Librarian

# n1 = Book("Imitation Game", "Alan Turing", "450", "8", "biography")
# # n1.add_book()
# n1.show_book_details()
lib1 = Librarian("hawre", "hare121", "librarian")
book = lib1.query_book("Permanent Record")
book = Book(*book[0])
book.show_book_details()
