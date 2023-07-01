# 	318A - Even Odds
import math
if __name__ == '__main__' :
    n, position = [int(x) for x in input().split()]
    if position <= math.ceil(n/2) :
        print(position * 2 - 1)
    else :
        print((position - math.ceil(n/2)) * 2)
