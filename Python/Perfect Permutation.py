# 	233A - Perfect Permutation
if __name__ == '__main__' :
    number = int(input())
    lst = []
    if number % 2 is not 0:
        print(-1)
    else:
        for x in range(1,number+1):
            lst.append(x)
        for x in range(1,number,2):
            var = lst[x]
            lst[x] = lst[x-1]
            lst[x-1] = var
        print(' '.join(str(x) for x in lst))
        
   
        
    
