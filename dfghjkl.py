"""Inflation"""
def main(price, year):
    """Inflation"""
    for _ in range(year):
        price = price+(price*(3.81/100))
    print("%.2f" %price)
main(float(input()), int(input()))
