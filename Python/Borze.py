#   32B - Borze
if __name__ == '__main__':
    word = input()
    size = len(word)
    # word = word.replace("--",'2')
    # word = word.replace("-.",'1')
    # word = word.replace(".",'0')
    x = 0;
    new_word = ''
    while x < size :
        if word[x] is '.':
            new_word += '0'
            x +=1
        elif x < size -1 and word[x] + word[x+1] == "-." :
            new_word += '1'
            x+=2
        elif x < size -1 and word[x] + word[x+1] == "--" :
            new_word += '2'
            x+=2
    print(new_word)



