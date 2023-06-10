# 	1399A - Remove Smallest
if __name__ == '__main__':
    cases = int(input())
    for x in range (cases):
        m = int(input())
        lst = [int(x) for x in input().split()]
        lst.sort()
        new_list = []
        x = 0
        while(len(lst) > 1):
            if abs(lst[x]-lst[x+1]) <= 1:
                del lst[x]
            else:
                print('NO')
                break;
        if len(lst) is 1:
            print('YES')


