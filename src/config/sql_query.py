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
SELECT username, password, role FROM users
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
REMOVE_BOOK_BY_NAME = """
DELETE FROM books WHERE name = ?
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
SELECT * FROM books WHERE genre=?
"""

GET_UNISSUED_BOOKS_BY_NAME = """
SELECT books.book_id
FROM books
LEFT JOIN books_issue ON books.book_id = books_issue.book_id
WHERE books.name = ? AND books_issue.book_id IS NULL;
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

BOOK_NAME = """
SELECT name FROM books WHERE book_id = ?
"""

BOOK_ISSUED = """
SELECT * FROM books_issue
WHERE username = ?
"""

ISSUE_ID = """
SELECT issue_id FROM books_issue 
WHERE book_id = ?
"""

BOOK_RETURN = """
DELETE FROM books_issue WHERE issue_id = ?
"""
