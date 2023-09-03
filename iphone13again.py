"""Ejudge"""
def main():
    """iPhone 13 Again"""
    model = input()
    size = input()
    price = 0
    if model == "iPhone 13 mini":
        price += 25900
    elif model == "iPhone 13":
        price += 29900
    elif model == "iPhone 13 Pro":
        price += 38900
    elif model == "iPhone 13 Pro Max":
        price += 42900
    else:
        model = True
    if size == "128 GB":
        price += 0
    elif size == "256 GB":
        price += 4000
    elif size == "512 GB":
        price += 12000
    elif size == "1 TB" and (model == "iPhone 13 Pro" or model == "iPhone 13 Pro Max"):
        price += 20000
    else:
        price = True
    if price == True or model == True:
        print("Not Available")
    else:
        print(price)
main()
