"""rtyuiop"""
def main(num):
    """ghjkl"""
    sum_total = sum(int(i) for i in str(num))
    sum_mod = sum_total*10
    sum_total += sum_mod
    if sum_total >= 10000 :
        print(str(sum_total).zfill(4))
    elif sum_total <= 1000:
        print(sum_total + 1000)
main(int(input()))
    