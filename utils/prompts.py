from pyfiglet import Figlet

render = Figlet(font='slant')

HOME = f"""
{render.renderText("Library Management System")}

1. Sign Up
2. Sign In
3. Exit

Enter your choice: """

ADMIN_MENU = f"""
{render.renderText('ADMIN')}

------------------Admin Menu------------------

1. Add Librarian
2. List Users
3. Remove User
4. Exit

Enter your choice: """

VISITOR_MENU = f"""
{render.renderText('USER')}

------------------Visitor Menu------------------
1. Query Book
2. List books by rating
3. Sort books by price
4. Group by genre
5. Issue Book
6. Check Issued Books
7. Check Dues
8. Return Book
9. Exit

Enter your choice: """

LIBRARIAN_MENU = f"""
{render.renderText('LIBRARIAN')}

------------------Librarian Menu------------------
        
1. Add a Book
2. List Books
3. Remove a Book
4. Exit

Enter your choice: """
