"""dfghjkl"""
def main(line):
    """XII"""
    for i in range(-line + 1, line, 1):
        for j in range(-line + 1, line, 1):
            print("%02d" %(line - abs(abs(i)-abs(j))), end=" ")
        print()
main(int(input()))
