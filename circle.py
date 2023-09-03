"""asdasd"""
import math

"""asdasd"""
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

"""asdasd"""
def check_overlap(x1, y1, r1, x2, y2, r2):
    distance_between_devices = distance(x1, y1, x2, y2)
    
    if distance_between_devices <= r1 + r2:
        return True
    else:
        return False

"""asdasd"""
def main():
    # Input
    x_mine = float(input())  # X-coordinate of your device
    y_mine = float(input())  # Y-coordinate of your device
    r_mine = float(input())  # Radius of your mosquito repellent device

    x_friend = float(input())  # X-coordinate of your friend's device
    y_friend = float(input())  # Y-coordinate of your friend's device
    r_friend = float(input())  # Radius of your friend's mosquito repellent device

    # Check for overlap
    if check_overlap(x_mine, y_mine, r_mine, x_friend, y_friend, r_friend):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
