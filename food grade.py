"""FoodGrade"""
def main(i, countchicken):
    """asdasd"""
    amountChic = float(input())
    if i > 0 and i <=24:
        if 50 >= amountChic and amountChic <= 70:
            countchicken += 1
    else:
        return
    main(i-1, countchicken)
def check():
    countnaja = 0
    main(24, countnaja)
    print(countnaja)
check()
