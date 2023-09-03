'''Ejudge'''
def main():
    '''Bigframe'''
    text1 = (input().rstrip())
    text2 = (input().rstrip())
    text3 = (input().rstrip())
    text4 = (input().rstrip())
    text5 = (input().rstrip())
    outer = max(len(text1), len(text2), len(text3), len(text4), len(text5))
    print("**"+("*"*outer)+"**")
    print("* "+text1+" "*((outer)-len(text1))+" *")
    print("* "+text2+" "*((outer)-len(text2))+" *")
    print("* "+text3+" "*((outer)-len(text3))+" *")
    print("* "+text4+" "*((outer)-len(text4))+" *")
    print("* "+text5+" "*((outer)-len(text5))+" *")
    print("**"+("*"*outer)+"**")
main()
