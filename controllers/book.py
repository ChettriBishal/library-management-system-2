from models.database import insert_item
from utils.sql_query import ADD_BOOK


class Book:
    def __init__(self, book_id, name, author, price, rating, genre):
        (
            self.book_id,
            self.name,
            self.author,
            self.price,
            self.rating,
            self.genre
        ) = book_id, name, author, price, rating, genre

    @property
    def get_book_details(self):
        return (self.book_id,
                self.name,
                self.author,
                self.price,
                self.rating,
                self.genre)

    def show_book_details(self):
        print("------------------")
        print(f"""
        Name: {self.name}
        Author: {self.author}
        Price: {self.price}
        Rating: {self.rating}
        Genre: {self.genre}
        
        """)

    def add_book(self):
        insert_item(ADD_BOOK, self.get_book_details)
        print(f"{self.name} is inserted!!")

    def remove_book(self):
        pass

