"""Ejudge"""
def main():
    """frame"""
    text = input()
    line(text)
    print("*"+text+"*")
    line(text)

def line(num):
    """lines"""
    print("*"*(len(num)+2))

main()
