from models.database import get_many_items, get_item, remove_item
from utils.sql_query import GET_BOOK_BY_NAME
class BookCollection:

    def query_book(self,name):
        response = get_item(GET_BOOK_BY_NAME,(name,))