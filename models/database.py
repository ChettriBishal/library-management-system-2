import sqlite3
from helpers.path_helper import USER_DB


class DBConnection:
    def __init__(self):
        self.connection = None
        self.host = USER_DB
        self.cursor = None

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {exc_tb}")
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


def get_item(query, data):
    with DBConnection() as cursor:
        try:
            response = cursor.execute(query, data).fetchone()
        except sqlite3.Error as error:
            print(error)
        return response


def get_many_items(query, data):
    with DBConnection() as cursor:
        try:
            if data:
                response = cursor.execute(query, data).fetchall()
            else:
                response = cursor.execute(query).fetchall()
        except sqlite3.Error as error:
            print(error)
        return response


def insert_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
        except sqlite3.Error as error:
            print(error)


def remove_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
        except sqlite3.Error as error:
            print(error)


def update_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
        except sqlite3.Error as error:
            print(error)


def execute_query(query):
    with DBConnection() as cursor:
        try:
            cursor.execute(query)
        except sqlite3.Error as error:
            print(error)
