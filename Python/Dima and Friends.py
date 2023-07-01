# 272A - Dima and Friends
if __name__ == '__main__' :
    n = int(input())
    lst = [int(x) for x in input().split()]
    sum = sum(lst)
    ways = 0
    for i in range(1,6) :
        if (sum + i) % (n + 1) != 1 :
            ways += 1
    print(ways)

