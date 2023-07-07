#   34B - Sale
if __name__ == '__main__':
    n,m = input().split()
    lst = [int(x) for x in input().split()]
    lst.sort()
    sum_max = 0
    for t in range(int(m)) : 
        if lst[t] <= 0 :
            sum_max += abs(lst[t])
    print(sum_max)