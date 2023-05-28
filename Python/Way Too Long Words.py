	# 71A - Way Too Long Words

n = int(input())

for i in range(n):
    word = input()
    if len(word) > 10:
        size = len(word)
        new_word = word[0] + str((size-2)) + word[size-1]
        print(new_word)
    else:
        print(word)