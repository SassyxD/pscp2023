"""Triangle"""
def main():
    """Process"""
    side_a = abs(float(input()))
    side_b = abs(float(input()))
    side_c = abs(float(input()))
    if abs(side_a**2 + side_b**2 - side_c**2) <= 0.01 or \
        abs(side_a**2 + side_c**2 - side_b**2) <= 0.01 \
        or abs(side_c**2 + side_b**2 - side_a**2) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
