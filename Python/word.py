# 59A - Word
word = input()
count_uppter = 0
count_lower = 0
for character in word:
    if 'A' <= character <= 'Z':
        count_uppter += 1
    else:
        count_lower += 1
if count_lower == count_uppter:
    print(word.lower())
else:
    if count_uppter < count_lower:
        print(word.lower())
    else:
        print(word.upper())
