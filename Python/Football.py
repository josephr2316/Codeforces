#   43A - Football
if __name__ == '__main__' :
    n = int(input())
    lst = []
    for i in range(n) :
        lst.append(input())
    max = 0
    winner = ''
    for m in lst :
        if max < lst.count(m) :
            max = lst.count(m)
            winner = m
    print(winner)