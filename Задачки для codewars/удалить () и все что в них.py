from re import sub


def remove_parentheses(s):
    return sub(r'\([^)]*\)', '', s)


print(remove_parentheses("fd(a(fdadfasdfwqerfd)df"))
