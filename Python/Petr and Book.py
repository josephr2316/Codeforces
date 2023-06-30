# 	139A - Petr and Book
if __name__ == '__main__':
    pages = int(input())
    pages_week = [int(x) for x in input().split()]
    sum = 0
    x = 0
    while sum < pages :
       x %= 7
       sum += pages_week[x]
       x += 1
    print(x)

