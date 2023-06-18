# 116A - Tram
if __name__ == '__main__' :
    cases = int(input())
    max = 0
    c = 0
    for x in range(cases) :
        lst = [int(x) for x in input().split()]
        a, b = lst
        c += b-a
        if  c > max :
            max = c
    print(max)
