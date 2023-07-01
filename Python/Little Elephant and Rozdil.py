#	205A - Little Elephant and Rozdil
if __name__ == '__main__' :
    n = int(input())
    lst = list(map(int,input().split()))
    min = min(lst)
    if lst.count(min) == 1 :
        print(lst.index(min) + 1)
    else :
        print('Still Rozdil')