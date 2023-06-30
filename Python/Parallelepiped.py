# 	224A - Parallelepiped
import math
if __name__ == '__main__' :
    a, b, c = [int (x) for x in input().split()]
    at = math.sqrt(a*b/c)
    bt = math.sqrt(b*c/a)
    ct = math.sqrt(c*a/b)
    sum = 4 * (at + bt + ct) 
    print(int(sum))