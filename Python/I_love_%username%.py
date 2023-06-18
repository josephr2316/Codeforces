#   155A - I_love_\%username\%
if __name__ == '__main__' :
    cases = int(input())
    lst = [int(x) for x in input().split()]
    val_max = lst[0]
    val_min= lst[0]
    amazing = 0
    del lst[0]
    for number in lst :
        if number > val_max :
            val_max = number
            amazing += 1
        if number < val_min :
            val_min = number
            amazing += 1
    print(amazing)
