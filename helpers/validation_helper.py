import re


def validate_username(username):
    pattern = '[A-Za-z1-9_]+'
    matcher = re.fullmatch(pattern, username)
    return matcher


def validate_password(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    matcher = re.fullmatch(pattern, password)
    return matcher
