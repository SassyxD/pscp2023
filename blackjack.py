"""qasda"""
def main():
    """asdasd"""
    card_list = []
    num = int(input())
    total = 0
    number = 0
    count = 0
    for _ in range(num):
        card = input()
        if card == "J":
            number = 10
        elif card == "Q":
            number = 10
        elif card == "K":
            number = 10
        elif card == "A":
            number = 11
            count += 1
        else:
            number = int(card)
        card_list.append(number)
    total = sum(card_list)
    for _ in range(count):
        if total > 21:
            total -= 10
    print(total)
main()
