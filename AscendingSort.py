"""AscendingSort"""
def num():
    """add list"""
    mylist_ = []
    for _ in range(5):
        var_ = int(input())
        mylist_.append(var_)
        mylist_.sort()
    for j in range(5):
        print(mylist_[j])

num()
