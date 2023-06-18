# 	231A - Team
if __name__ == '__main__' :
    cases = int(input())
    solutions = 0
    for x in range(cases) :
        lst = list(map(int,input().split()))
        numbers_one = lst.count(1)
        if numbers_one >= 2 :
            solutions += 1
    print(solutions)
