from models.database import execute_query
from utils import sql_query


def create_book_table() -> None:
    execute_query(sql_query.CREATE_BOOK_TABLE)


def create_user_table() -> None:
    execute_query(sql_query.CREATE_USER_TABLE)


def create_book_issue_table() -> None:
    execute_query(sql_query.CREATE_USER_TABLE)


def init_all() -> None:
    create_book_table()
    create_user_table()
    create_book_issue_table()
