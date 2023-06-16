cases = int(input()) 
for n in range(cases): 
    size = int(input()) 
    key = input()
    val = key[0]
    word = ''
    x = 1
    while x < size:
        if key[x] is val:
            word += val
            if x + 1 < size:
                val = key[x+1]
            x +=2
        else:
            x +=1
    print(word)



