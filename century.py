"""Ejudge"""
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        year = input().split()
        if year[0:3] == "B.E.":
            year[1] = int(year[1])-543
        elif year[0:3] == "A.D.":
            year[1] = int(year[1])
        else:
            year = "Error"
        if year == "Error" or year[1] < 0:
            print("ERROR")
        elif year[1]/100 > year[1]//100:
            print((year[1]//100)+1)
        else:
            print(int(year[1]//100))
main()
