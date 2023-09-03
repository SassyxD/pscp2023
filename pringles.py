"""Ejudge"""
def main():
    """ghjkl"""
    count = 0
    total = 0
    num = int(input())
    if num == 1:
        print(1)
    else:
        while total != num:
            total = len(str(num))+1
            count += 1
        print(total)
main()