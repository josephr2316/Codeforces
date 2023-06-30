# 	450A - Jzzhu and Children
if __name__== '__main__' :
    n,m = input().split()
    lst = [int(x) for x in input().split()]
    max = 0
    position = 0
    x = 0
    for element in lst:
        x += 1
        if element >= max :
            max = element
            position = x
    print(position)
