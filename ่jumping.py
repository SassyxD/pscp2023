def jumping(num):
    if num <= 4:
        print_output(num)
        num += 1
        jumping(num)

def print_output(num):
    if num <= 3:
        print(f'Output {num}')
        num += 1
        print_output(num)
    else:
        print(f'Output {num}')


jumping(1)
