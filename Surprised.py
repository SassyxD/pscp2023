"""Ejudge"""
def main():
    """SurprisingVote"""
    sumscore = float(input())
    mscore = float(input())
    tmpscore = 0
    if mscore*2 < sumscore:
        tmpscore = sumscore - mscore*2
    if mscore - tmpscore > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
