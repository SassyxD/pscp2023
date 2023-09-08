"""PickThem"""
def pick():
    """Them"""
    import json
    num_even = 0
    num = json.loads(input())
    for i in num:
        if i % 2 == 0:
            print(i)
            num_even = 1
    if num_even == 0:
        print("Nope")
pick()
