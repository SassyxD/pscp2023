"""Ejudge"""
import math
def main(days):
    """ChaChaCha"""
    # i = 0
    # for _ in range(1, num+1):
    #     hour = float(input())
    #     if _  <= num:
    #         i += hour
    #     else:
    #         print("%.2f" %(i*8720))
    
    #total money
    money = 0
    #check days
    if days > 31:
        return
    else:
        #loop for amount of days
        for _ in range(int(days)):
            hours = float(input())
            #check hours can't be > 24
            if hours > 24:
                return
            #total money calculate
            else:
                money += math.ceil(hours) * 8720
    print(int(money))
main(float(input()))
