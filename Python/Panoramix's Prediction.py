# 	80A - Panoramix's Prediction
def prime_number(number):
    if number == 1 or number == 0 :
        return False
    for x in range(2,number):
        if number % x == 0:
            return False
    return True



if __name__ == '__main__':
    lst = [int(x) for x in input().split(" ")]
    prime_lst = []
    for m in range(lst[0],lst[1] + 1):
        if prime_number(m):
            prime_lst.append(m)
    if len(prime_lst)> 1 and prime_lst[1] == lst[1] :
        print('YES')
    else:
        print('NO')