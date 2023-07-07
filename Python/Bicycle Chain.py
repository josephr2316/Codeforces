#	215A - Bicycle Chain
if __name__ == '__main__':
    n, a, m ,b = int(input()), [int(x) for x in input().split()], int(input()), [int(y) for y in input().split()]
    max, times = 0, 0
    for x in range(n) :
        for y in range(m): 
            if b[y]/a[x] > max and b[y]/a[x]==b[y]//a[x] : times = 0; max = b[y]//a[x]
            if b[y]/a[x] == max and b[y]/a[x]==b[y]//a[x]: times+=1
    print(times)



