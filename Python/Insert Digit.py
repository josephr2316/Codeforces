# 	1811A - Insert Digit
if __name__ == '__main__' :
    cases = int(input())
    for x in range(cases):
        lst = list(map(int,input().split()))
        word = input()
        is_bigger = False
        x = 0
        for m in word:
            if int(m) < lst[1]  and not is_bigger:
                print(str(lst[1]),end="")
                print(m,end="")
                is_bigger = True
            else :
                print(m,end="")
                x += 1
        if not(is_bigger) :
            print(str(lst[1]))
        else:
            print()

                
            


            
