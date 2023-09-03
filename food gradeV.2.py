'''chick'''
def main(count, time):
    '''w'''
    if time == 24:
        return count
    if 50 <= float(input()) <= 70:
        return main(count + 1, time + 1)
    else:
        return main(count, time + 1)
print(main(0, 0))
