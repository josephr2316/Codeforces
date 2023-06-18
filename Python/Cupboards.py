#	248A - Cupboards
def calculate_minimun(lst,m,size):
    count_z = 0
    count_one = 0
    for x in range(size) :
        if lst[x][m] == 0 :
            count_z += 1
        else :
            count_one += 1
    return min(count_one,count_z)

if __name__ == '__main__' :
    cases = int(input())
    lst = list()
    for x in range(cases) :
        lst.append([int(x) for x in input().split()])
    result = calculate_minimun(lst,0,cases) + calculate_minimun(lst,1,cases)
    print(result)
