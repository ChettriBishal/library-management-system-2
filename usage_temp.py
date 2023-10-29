from controllers.authentication import Authentication
from controllers.user import Admin

auth = Authentication("temp123", "Snow123", "visitor")
auth.login()

auth2 = Authentication("lib345","Lib345","librarian")
auth2.login()

admin1 = Admin("anything","admin")
admin1.remove_user("lib345")
admin1.list_users()
