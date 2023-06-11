#	144A - Arrival of the General
if __name__ == '__main__' : 
    n = int(input())
    lst = [int(x) for x in input().split()]
    max_number = max(lst)
    min_number = min(lst)
    pos_max = lst.index(max_number)
    pos_min = (n - 1)  - lst[::-1].index(min_number)
    if pos_max > pos_min : 
        pos_min = (n - 1) - pos_min
        print (pos_max + pos_min - 1)
    else :
        pos_min = (n - 1) - pos_min
        print(pos_max + pos_min)
