"""Ejudge"""
def main():
    """Sequence VIII"""
    row = int(input())
    for i in range(0, row):
        num = 1
        for j in range(i+1, row):
            print("  ", end=" ")
        for j in range(0, i+1):
            j = j
            print("%02d" %num, end=" ")
            num += 1
        print("\r")
main()
