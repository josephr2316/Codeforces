# 151A - Soft Drinking
lst = list(map(int, input().split()))
kl = lst[1] * lst[2]
toast = kl // lst[6]
cd = lst[3] * lst[4]
toasts = lst[5] // lst[7]
result = min(toast,cd,toasts) // lst[0]
print(result)
