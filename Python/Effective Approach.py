# 227B - Effective Approach
if __name__ == '__main__' :
    size = int(input())
    lst_array = [int(x) for x in input().split()]
    query_size = int(input())
    lst_querries = [int(x) for x in input().split()]
    Vasya = 0
    Petya = 0
    for query in lst_querries :
        index = lst_array.index(query)
        Vasya +=  index + 1
        Petya += size - index
    print(f'{Vasya} {Petya}')
