# 34A - Reconnaissance 2
if __name__ == "__main__" :
    size = int(input())
    man_list = [int(x) for x in input().split()]
    index_a = size
    index_b = 1
    min = abs(man_list[0]-man_list[size-1])
    for n in range(size-1) :
        result = abs(man_list[n] - man_list[n+1])
        if result < min :
            min = result
            index_a = n + 1
            index_b = n + 2
    print(f"{index_a} {index_b}")