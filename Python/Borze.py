word = input()
size = len(word)
new_word = []
result = ''
if word[0] is '.':
    result += '0'
    for x in range(1,size,2):
        if x == size-1:
            new_word.append(word[x])
        else:
            new_word.append(word[x]+word[x+1])
else:
    for x in range(0,size,2):
        if x == size-1:
            new_word.append(word[x])
        else:
            new_word.append(word[x]+word[x+1])
for val in  new_word:
    if val == '.':
        result += '0'
    elif val == '-.':
        result += '1'
    elif val == '--':
        result += '2'   
print(result)



