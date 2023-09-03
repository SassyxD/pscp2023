"""Ejudge"""
def main(text):
    """Future"""
    if str.isdigit(text) == True:
        print("Number")
    elif str.isupper(text) == True:
        print("Uppercase")
    elif str.islower(text) == True:
        print("Lowercase")
    elif str.istitle(text) == True:
        print("Title")
    elif str.isspace(text) == True:
        print("Space")
    else:
        print("Other")
main(input())
