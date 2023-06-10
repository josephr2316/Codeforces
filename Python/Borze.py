#   32B - Borze
if __name__ == '__main__':
    word = input()
    size = len(word)
    word = word.replace("--",'2')
    word = word.replace("-.",'1')
    word = word.replace(".",'0')
    print(word)



