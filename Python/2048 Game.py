# 	1221A - 2048 Game
if __name__ == '__main__' :
    cases = int(input())
    for x in range(cases) :
        n = int(input())
        lst = [int(x) for x in input().split()]
        set_a = set(lst)
        dict = {}
        for x in range(1,2049)  :
            dict[x] = 0
        is_possbile = False
        for i in set_a :
            value = lst.count(i)
            if value>= 2 and i <2048:
                dict[i] =  value
            elif i<=2048:
                dict[i] = value
        for m in range(1,2049) :
            if m == 2048 :
                if dict[m] > 0 :
                    is_possbile = True
            else :
                if dict[m] != 0 and dict[m]>=2:
                    dict[m+m] += dict[m]/2   
        if is_possbile : print('YES')
        else : print ('NO')
            

