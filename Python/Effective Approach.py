# 227B - Effective Approach
if __name__ == '__main__' :
    size = int(input())
    lst_array = [int(x) for x in input().split()]
    lst = [0 for i in range(size+1)]
    query_size = int(input())
    lst_querries = [int(x) for x in input().split()]
    Vasya = 0
    Petya = 0
    for y in range(size) :
        lst[lst_array[y]] = y
    for query in lst_querries :
        index = lst[query]
        Vasya +=  index + 1
        Petya += size - index
    print(f'{Vasya} {Petya}')
