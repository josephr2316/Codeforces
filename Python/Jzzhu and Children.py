# 	450A - Jzzhu and Children
import math
if __name__== '__main__' :
    n,m = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    position = 0
    max = 0
    i = 1
    for number in lst :
        if math.ceil(number/m) >= max :
            max = math.ceil(number/m)
            position = i
        i += 1
    print(position)

