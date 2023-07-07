#   199A - Hexadecimal's theorem
memo = [-1 for x in range(100)]

def fib(n) :
    if n == 0 :
        memo[n] = 0
    if n == 1 :
        memo[n] = 1
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

if __name__ == '__main__' :
    n = int(input())
    fib(n)
    is_fibo = False
    for x in range(0,n) :
        for y in range(0,n) :
            z = n - (memo[x] + memo[y])
            
            if z >= 0  :
                print(f"{memo[x]} {memo[y]} {z}")
            print( "I'm too stupid to solve this problem")

    