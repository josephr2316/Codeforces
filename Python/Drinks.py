# 200B - Drinks
if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    sum_list = sum(lst)
    result =  sum_list / n
    print(f'{result:.12f}')
