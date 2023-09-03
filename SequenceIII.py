"""Ejudge"""
def main():
    """wertyuiop"""
    num = int(input())
    for i in range(2, num+2):
        rnd = i
        for j in range(2, num+2):
            j = j
            if rnd < i:
                print(i, end=" ")
            else:
                print(rnd, end=" ")
            rnd += 1
        print()
main()
