import os
from datetime import datetime
from src.models.database import insert_item
from src.config import sql_query
from src.utils.logs import Log


class BookIssue:
    log_obj = Log(os.path.basename(__file__))

    def __init__(self, issue_id, username, book_id, issue_date, due_date,
                 date_returned):
        (self.issue_id, self.username, self.book_id, self.issue_date,
         self.due_date, self.date_returned
         ) = issue_id, username, book_id, issue_date, due_date, date_returned

    @property
    def get_issue_details(self):
        return (self.issue_id, self.username, self.book_id, self.issue_date,
                self.due_date, self.date_returned)

    def show_issue_details(self):
        print("------------------")
        print(f"""
        Issue Id: {self.issue_id}
        Book Id: {self.book_id}
        Issue Date: {self.issue_date}
        Due Date: {self.due_date}
        """)

    def add_book(self, bookname):
        insert_item(sql_query.ISSUE_BOOK_QUERY, self.get_issue_details)
        print(f"{bookname} is successfully issued!!")
        self.log_obj.logger.info(f"{bookname} added into database")

    def get_dues(self):
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        current_date = datetime.now()
        dues = 0
        if current_date > due_date:
            delta = current_date - due_date
            days = delta.days
            dues = days * 3

        return dues
