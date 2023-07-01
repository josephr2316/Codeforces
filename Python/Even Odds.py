# 	318A - Even Odds
if __name__ == '__main__' :
    n, position = [int(x) for x in input().split()]
    lst_even = []
    list_odd = []
    for x in range(1,n+1) :
        if x % 2 == 0 :
            lst_even.append(x)
        else :
            list_odd.append(x)
    lst = list_odd + lst_even
    print(lst[position-1])
