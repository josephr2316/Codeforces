# 148A - Insomnia cure
if __name__ == '__main__' :
    k, l, m, n, d = int(input()), int(input()), int(input()), int(input()),int(input())
    val = 0
    for x in range(1,d+1):
        if x % k == 0 or x % l == 0 or x % m == 0 or x % n == 0:
            val+= 1
    print(val)