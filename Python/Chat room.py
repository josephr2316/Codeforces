# 	58A - Chat room
if __name__ == '__main__' :
    s = input()
    word = 'hello'
    x = 0
    for m in s :
        if m == word[x] :
            x += 1
        if x == 5 : break
    if x == 5 :
        print('YES')
    else : print('NO')