import os
from models.database import insert_item, remove_item
from config.sql_query import ADD_BOOK, REMOVE_BOOK_BY_ID, REMOVE_BOOK_BY_NAME
from utils.logs import Log
from utils.uuid_generator import generate_uuid


class Book:
    log_obj = Log(os.path.basename(__file__))

    def __init__(self, name, author, rating, price, genre):
        (self.book_id, self.name, self.author, self.price, self.rating,
         self.genre) = generate_uuid(), name, author, price, rating, genre

    @property
    def get_book_details(self):
        return (self.book_id, self.name, self.author, self.rating, self.price,
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
        print(f"{self.name} is added successfully!!")
        self.log_obj.logger.info(f"{self.name} is added into database")
        return True

    def remove_book(self):
        remove_item(REMOVE_BOOK_BY_ID, (self.book_id, ))
        print(f"A copy of {self.name} is removed successfully!!")
        self.log_obj.logger.info(f"{self.name} is removed from database")

    def remove_book_by_name(self):
        remove_item(REMOVE_BOOK_BY_NAME, (self.name, ))
        print(f"A copy of {self.name} is removed successfully!!")
        self.log_obj.logger.info(f"{self.name} is removed from database")
