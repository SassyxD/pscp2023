"""Backward"""
def back():
    """Backward"""
    mylist = []
    while True:
        word = input()
        if word == "NULL":
            break
        mylist.append(word)
    for i in range(1, len(mylist)+1):
        print(mylist[-i])

back()
