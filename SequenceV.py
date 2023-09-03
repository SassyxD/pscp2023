"""Ejudge"""
def main():
    """Sequence V"""
    num = int(input())
    for i in range(0, num):
        if i % 7 == 0 and i != 0:
            print()
        print(num, end=" ")
        num -= 1
main()
