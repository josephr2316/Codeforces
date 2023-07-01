# 	1108B - Divisors of Two Integers
if __name__ == '__main__' :
    size = int(input())
    lst = [int(x) for x in input().split()]
    x = max(lst)
    
    lst.remove(x)
    lst.sort(reverse=True)
    for m in lst :
        if x % m != 0 :
            print(f"{x} {m}")
            break;
        elif x == m :
            print(f"{x} {m}")
            break;
        elif x % m == 0 and lst.count(m) > 1 :
            print(f"{x} {m}")
            break;
        elif m == 1 :
            print(f"{x} {m}")
            break;
