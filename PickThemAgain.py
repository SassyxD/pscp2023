"""PickThemAgain"""
def sameagain():
    """think"""
    word = input().split()
    mylist_ = []
    for i in word:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            mylist_.append(int(i))

    if mylist_ == []:
        print("Nope")
    for j in mylist_[::-1]:
        print(j)
sameagain()
