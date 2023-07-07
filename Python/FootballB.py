#	96A - Football
string = input()
max = 0
count = 1
for i in range(len(string)-1) :
    if string[i] == string[i+1] :
        count += 1
        if max < count :
            max = count
    else : count = 1
if max >= 7 : print('YES')
else : print('NO')