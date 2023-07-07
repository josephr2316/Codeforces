# 320A - Magic Numbers
if __name__ == '__main__' :
    n = input()
    i = 0
    magic = True

    while i < len(n) :
        if i + 3 <= len(n) and n[i:i+3] == '144'   :
            i += 3
        elif i+2<= len(n) and n[i:i+2] == '14':
            i += 2
        elif n[i] == '1' :
           i += 1
        else :
            magic = False
            break
    if magic : print('YES')
    else : print('NO')