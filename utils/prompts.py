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
1. Add Librarian
2. List Users
3. Remove User
4. Exit

Enter your choice: """

USER_MENU = f"""
{render.renderText('USER')}
1. List Books
2. Query Book
3. Sort books by rating
4. Sort books by price
5. Group by genre
6. Issue Book
7. Check Issued Books
8. Check Dues
9. Return Book
10. Exit

Enter your choice: """

LIBRARIAN_MENU = f"""
{render.renderText('LIBRARIAN')}

------------------Librarian Menu------------------
        
1. Add a Book
2. List Books
3. Remove a Book
4. Exit

Enter your choice: """
