"""ValidVar"""
def valid():
    """ValidVar"""
    number = int(input())
    sensitive = "if else elif while for True False continue break\
return is in and or from as pass not def None"
    check = sensitive.split(" ")
    for _ in range(1, number+1):
        txt = input()
        if txt.isidentifier(check) == True:
            if txt in check:
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
    

valid()