# 275A - Lights Out
if __name__ == '__main__' : 
    lst = list()
    for x in range(3) :
        lst.append([int(x) % 2 for x in input().split()])
    print(lst)
    for x in range(3) :
        for y in range(3) :
            if lst[x][y] is 0 :
                lst[x][y] = 1
            else :
                lst[x][y] = 0
            if x - 1 >= 0 :
                if lst[x-1][y] is 0 :
                    lst[x-1][y] = 1
                else :
                    lst[x-1][y] = 0
            if x + 1 < 3 :
                if lst[x+1][y] is 0 :
                    lst[x+1][y] = 1
                else :
                    lst[x+1][y] = 0
            
            if y - 1 >= 0 :
                if lst[x][y-1] is 0 :
                    lst[x][y-1] = 1
                else :
                    lst[x][y-1] = 0
            if y + 1 < 3:
                if lst[x][y+1] is 0 :
                    lst[x][y+1] = 1
                else :
                    lst[x][y+1] = 0
    for x in range(3) :
        for y in range(3) :
            print(lst[x][y],end='')
        print()
