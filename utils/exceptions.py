class UserDoesNotExist(Exception):
    """
    Exception raised when someone tries to operate on user which doesn't exist
    """

    def __init__(self, username):
        self.username = username
        self.message = f"User with username `{username}` doesn't exist!!"
        super().__init__(self.message)


class BookDoesNotExist(Exception):
    """
    Exception raised when someone tries to operate on book which doesn't exist
    """

    def __init__(self, bookname):
        self.bookname = bookname
        self.message = f"Book `{bookname}` doesn't exist!!!"
        super().__init__(self.message)
