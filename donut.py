"""donut"""
def main():
    """Process"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    free_donuts = (d // (b+c)) * c
    additional_donuts = (d // (b+c)) * b
    total_cost = (additional_donuts + free_donuts) * a
    print(total_cost, d + additional_donuts)
main()