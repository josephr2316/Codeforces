# 	69A - Young Physicist
n = int(input())
x = 0
y = 0
z = 0

for i in range(n):
    list_p = list(map(int,input().split(" ")))
    x += list_p[0]
    y += list_p[1]
    z += list_p[2]
if (x is 0  and y is 0 and z is 0):
    print("YES")
else:
    print("NO")



