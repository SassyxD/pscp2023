"""asdasd"""
def print_traffic_sign(number_01, numbber_02):
    """asdasdasd"""
    for i in range(numbber_02):
        if i < numbber_02 // 2 + 1:
            spaces = " " * (numbber_02 // 2 - i)
            stars = "*" * number_01
        else:
            spaces = " " * (i - numbber_02 // 2)
            stars = "*" * number_01
        print(spaces + stars)
print_traffic_sign(int(input()), int(input()))
