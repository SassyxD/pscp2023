"""Dataspike"""
def loop(i, num_y=None):
    """asd"""
    if i <= 8:
        num_x = int(input())
        if i == 1:
            num_y = num_x
        num_y = compare(num_y, num_x)
        loop(i+1, num_y)
    else:
        print(num_y)
        
def compare(num_y, num_x):
    """sdf"""
    if num_y < num_x:
        return num_x
    return num_y

loop(1)
