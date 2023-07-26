# 337A - Puzzles
if __name__ == '__main__' :
    n, m  = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    lst.sort()
    mini = 9999999999
    for a in range(m-n+1) :
        mini= min(mini,lst[a+n-1]-lst[a])
    print(mini)