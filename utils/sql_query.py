GET_USER_BY_USERNAME = f"""
SELECT * FROM users WHERE username = ?
"""

ADD_USER = """
INSERT INTO users VALUES(?,?,?,?)
"""

SELECT_ROLE = """
SELECT role FROM users WHERE username = ?
"""

GET_PASSWORD = f"""
SELECT password FROM users WHERE username = ?
"""

GET_ALL_USERS = """
SELECT username, role FROM users
"""

REMOVE_USER = """
DELETE FROM users WHERE username = ?
"""


GET_USER = """
SELECT * FROM users WHERE username=?
"""

GET_USER_ROLE = """
SELECT role FROM users WHERE username=?
"""

ADD_BOOK = """
INSERT INTO books VALUES(?,?,?,?,?,?)
"""

REMOVE_BOOK_BY_ID = """
DELETE FROM books WHERE book_id = ?
"""

CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS users(user_id text primary key, username text,password text, role text)
"""

CREATE_BOOK_TABLE = f"""
CREATE TABLE IF NOT EXISTS books
(book_id text primary key, name text NOT NULL,
author text NOT NULL, rating int NOT NULL,price real NOT NULL, quantity int NOT NULL, genre text)
"""

GET_BOOK_BY_NAME = "SELECT * FROM books WHERE name=?"

NO_OF_BOOKS_OF_SAME_NAME = """
    SELECT COUNT(*) as book_count
    FROM books
    WHERE name = ?
"""

GET_BOOKS_BY_RATING = """
SELECT * FROM books ORDER BY rating DESC
"""

GET_BOOKS_BY_PRICE = """
SELECT * FROM books ORDER BY price ASC
"""

GROUP_BOOKS_BY_GENRE = """
SELECT name, author, price, rating FROM books WHERE genre=?
"""


CREATE_BOOK_ISSUE_TABLE = f"""CREATE TABLE IF NOT EXISTS books_issue(
            issue_id TEXT PRIMARY KEY, 
            username TEXT,  -- Added username column
            book_id TEXT, 
            issue_date DATE NOT NULL, 
            due_date DATE NOT NULL, 
            date_returned DATE, 
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (username) REFERENCES users (username)  -- Added foreign key for user_id
        )"""

ISSUE_BOOK_QUERY = """
INSERT INTO books_issue (issue_id, username, book_id, issue_date, due_date, date_returned)
VALUES (?, ?, ?, ?, ?, ?)
"""

BOOK_ISSUED = """
SELECT books.name, books.author, books_issue.issue_date, books_issue.due_date, books_issue.date_returned
FROM books_issue
INNER JOIN books ON books_issue.book_id = books.book_id
WHERE books_issue.username = ?
"""

ISSUE_ID = """
SELECT books_issue.issue_id
FROM books_issue
INNER JOIN books ON books_issue.book_id = books.book_id
WHERE books_issue.username = ?
AND books.name = ?
"""

BOOK_RETURN = """
DELETE FROM books_issue WHERE issue_id = ?
"""


