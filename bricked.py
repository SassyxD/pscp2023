"""dugfhiodufg"""
def main(small, big, goal):
    """asd"""
    if big*5 + small < goal or big%5 > small:
        print("-1")
    else:
        if big*5 >= goal:
            print(goal%5)
        else:
            print(goal-(big*5))
main(int(input()), int(input()), int(input()))
