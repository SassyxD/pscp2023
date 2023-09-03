"""ertyuio"""
def main(num):
    '''GHJKL;'''
    count = 0
    total = 0
    if num == 1:
        print("1")
    else:
        while count != num:
            count += 1
            total += len(str(count))
            total += 1
        print(total)
main(int(input()))
