"""asda"""
def c0unt_digits_l3ngth():
    """asdasd"""
    number = int(input())
    c0unt = 0
    temp_number = abs(number)
    if temp_number == 0:
        c0unt = 1
    else:
        while temp_number:
            c0unt += 1
            temp_number //= 10

    print(c0unt)
    return c0unt

c0unt_digits_l3ngth()
