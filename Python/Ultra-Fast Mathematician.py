# 61A - Ultra-Fast Mathematician
if __name__ == '__main__':
    list_a = list(input())
    list_b = list(input())
    word = ''
    for x in range(len(list_a)):
        if list_a[x] == list_b[x]:
            word += '0'
        else:
            word += '1'
    print(word)
