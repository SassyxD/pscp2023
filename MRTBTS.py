"""Ejudge"""
def main(day, age, height):
    """BTSMRT"""
    if age < 14 and height < 90:
        print("FREE")
    elif age >= 60 and day == "Senior Day":
        print("FREE")
    elif age < 14 and height <= 140 and day == "Children Day":
        print("FREE")
    else:
        print("PAY")
main(str(input()), float(input()), float(input()))
