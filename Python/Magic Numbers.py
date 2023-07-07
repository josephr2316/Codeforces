# 320A - Magic Numbers
if __name__ == '__main__' :
    n = input()
    i = 0
    magic = ''

    while i < len(n) :
        if  n[i:i+3] != '144' :
            if  n[i:i+2] != '14' :
                if n[1] == '1':
                    magic+= '1'
            else :
                magic += '14'
                i+= 1
        else:
            i += 2
            magic += '144'
        i+= 1
    if len(n) == len(magic) :
        print('YES')
    else :
        print('NO')