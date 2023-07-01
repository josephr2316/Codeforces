# 	450A - Jzzhu and Children
if __name__== '__main__' :
    n,m = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    position = 0
    x = 0
    y = 0
    is_max = False
    while x < n :
        if lst[y] != 0 :
            if lst[y] - m <= 0 :
                lst[y] = 0
                x += 1
            else :
                lst[y] = lst[y] - m
                is_max = True
                position = y
        y += 1 
        if y == n :
            y = 0
    if not(is_max):
        print(n)
    else :
        print(position+1)
   
