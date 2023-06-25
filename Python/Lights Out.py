# 275A - Lights Out
if __name__ == '__main__' : 
    lst = list()
    for x in range(3) :
        lst.append([int(x) % 2 for x in input().split()])
    matrix = [[1]*3 for _ in range(3)]
    for x in range(3) :
        for y in range(3) :
            if lst[x][y] is 1 :
                matrix[x][y] ^= 1
                if x - 1 >= 0 :
                    matrix[x-1][y] ^= 1
                if x + 1 < 3 :
                    matrix[x+1][y] ^= 1                
                if y - 1 >= 0 :
                    matrix[x][y-1] ^= 1
                if y + 1 < 3:
                    matrix[x][y+1] ^= 1
    for x in range(3) :
        for y in range(3) :
            print(matrix[x][y],end='')
        print()
